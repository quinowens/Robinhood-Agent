#!/usr/bin/env python3
"""Idempotently populate matured option outcomes from immutable bar snapshots."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from historical_resolver import (
    NON_RETRYABLE_STATUSES,
    get_historical_benchmark_close,
    get_historical_option_close,
    get_historical_underlying_close,
    resolve_option_id,
    signal_trading_date,
    trading_day,
)

ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 5, 10, 20, 30)
STATUSES = {"PENDING", "OBSERVED", "MISSING_SOURCE_DATA", "UPDATE_FAILED", "NOT_APPLICABLE", "RETRYABLE_SOURCE_ERROR", "PERMANENTLY_UNAVAILABLE"}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"Invalid JSONL {path}:{line_number}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")


def numeric(value: Any) -> float | None:
    try:
        return None if value is None or value == "" else float(value)
    except (TypeError, ValueError):
        return None


def parse_day(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value)[:10]) if value else None
    except ValueError:
        return None


def session_dates(snapshot: dict[str, Any]) -> list[str]:
    explicit = snapshot.get("trading_dates") or snapshot.get("market_sessions")
    if explicit:
        return sorted(str(item.get("date") if isinstance(item, dict) else item)[:10] for item in explicit)
    dates = set()
    for bars in snapshot.get("equity_bars", {}).values():
        dates.update(str(bar["date"])[:10] for bar in bars if bar.get("date"))
    return sorted(dates)


def observation_day(signal_date: str, horizon: int, dates: list[str]) -> str:
    parsed = parse_day(signal_date)
    return trading_day(parsed, horizon).isoformat() if parsed else ""


def observation_day_from_session(signal_session: date, horizon: int) -> str:
    return trading_day(signal_session, horizon).isoformat()


def bars_by_date(bars: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(bar.get("date"))[:10]: bar for bar in bars if bar.get("date")}


def pct_return(entry: float | None, exit_value: Any) -> float | None:
    exit_number = numeric(exit_value)
    if entry in (None, 0) or exit_number is None:
        return None
    return round((exit_number / entry) - 1, 6)


def record_id(row: dict[str, Any]) -> str:
    return str(row.get("outcome_record_id") or row.get("option_signal_outcome_id") or row.get("outcome_id") or row.get("option_setup_id") or "UNKNOWN")


def existing_return(row: dict[str, Any], asset: str, horizon: int) -> float | None:
    return numeric(row.get(f"{asset}_forward_{horizon}d_return", row.get(f"forward_{horizon}d_{asset}_return")))


def assign(row: dict[str, Any], key: str, value: Any, allow_correction: bool) -> bool:
    if value is None:
        return False
    if row.get(key) is None or (allow_correction and row.get(key) != value):
        row[key] = value
        return True
    return False


def direction_won(row: dict[str, Any], value: float) -> bool:
    bearish = str(row.get("directional_thesis") or "").lower() == "bearish" or str(row.get("option_type") or "").lower() == "put"
    return value < 0 if bearish else value > 0


def classify(row: dict[str, Any], horizon: int) -> str:
    underlying = existing_return(row, "underlying", horizon)
    option = existing_return(row, "option", horizon)
    if underlying is None or option is None:
        return "INCONCLUSIVE"
    return f"UNDERLYING_{'WIN' if direction_won(row, underlying) else 'LOSS'}_OPTION_{'WIN' if option > 0 else 'LOSS'}"


def update_row(row: dict[str, Any], snapshot: dict[str, Any], dates: list[str], *, allow_correction: bool = False, correction_reason: str | None = None) -> tuple[bool, list[dict[str, Any]]]:
    changed, issues = False, []
    signal_date = str(row.get("signal_date") or row.get("entry_date") or row.get("date") or "")[:10]
    signal_day = parse_day(signal_date)
    symbol = str(row.get("underlying") or row.get("symbol") or "")
    snapshot_as_of = parse_day(snapshot.get("evaluation_as_of") or snapshot.get("as_of")) or date.today()
    observed_at = str(snapshot.get("captured_at") or snapshot.get("as_of") or datetime.now(timezone.utc).isoformat())
    source = str(snapshot.get("source") or snapshot.get("source_id") or "historical_bar_snapshot")
    if not signal_day or not symbol:
        return False, [{"reason": "missing_signal_date_or_symbol"}]
    signal_session = signal_trading_date(signal_day, row.get("entry_snapshot_at") or row.get("timestamp"))
    signal_session_text = signal_session.isoformat()
    equity = bars_by_date(snapshot.get("equity_bars", {}).get(symbol, []))
    spy = bars_by_date(snapshot.get("equity_bars", {}).get("SPY", []))
    qqq = bars_by_date(snapshot.get("equity_bars", {}).get("QQQ", []))
    option_id = row.get("option_id") or row.get("instrument_id") or snapshot.get("option_id_lookup", {}).get(str(row.get("option_setup_id")))
    option = bars_by_date(snapshot.get("option_bars", {}).get(str(option_id), []))
    entry_underlying = numeric(row.get("underlying_price_at_entry") or row.get("entry_underlying_price")) or numeric(equity.get(signal_session_text, {}).get("close"))
    entry_option = numeric(row.get("entry_option_mid") or row.get("entry_midpoint") or row.get("entry_premium") or row.get("entry_mark"))
    spy_entry, qqq_entry = numeric(spy.get(signal_session_text, {}).get("close")), numeric(qqq.get(signal_session_text, {}).get("close"))

    for horizon in HORIZONS:
        prefix = f"forward_{horizon}d"
        maturity = observation_day_from_session(signal_session, horizon)
        maturity_day = parse_day(maturity)
        status_key, meta_key = f"{prefix}_status", f"{prefix}_observation"
        old_status = row.get(status_key)
        if old_status == "OBSERVED" and not allow_correction:
            status, reason = "OBSERVED", None
            resolutions = (row.get(meta_key) or {}).get("component_resolutions", {})
            component_observed = {
                "underlying": existing_return(row, "underlying", horizon) is not None,
                "option": existing_return(row, "option", horizon) is not None,
                "spy": row.get(f"underlying_forward_vs_spy_{horizon}d") is not None,
                "qqq": row.get(f"underlying_forward_vs_qqq_{horizon}d") is not None,
            }
            for component, is_observed in component_observed.items():
                key = f"{prefix}_{component}_status"
                desired = "OBSERVED" if is_observed else (row.get(key) or "PENDING")
                if row.get(key) != desired:
                    row[key], changed = desired, True
        elif maturity_day is None or maturity_day > snapshot_as_of:
            status, reason = "PENDING", "horizon_not_mature_as_of_source_snapshot"
            resolutions = {}
            for component in ("underlying", "option", "spy", "qqq"):
                key = f"{prefix}_{component}_status"
                if row.get(key) != "PENDING":
                    row[key], changed = "PENDING", True
        else:
            try:
                resolutions = {
                    "underlying": get_historical_underlying_close(snapshot, symbol, maturity_day, as_of=snapshot_as_of),
                    "option": get_historical_option_close(snapshot, row, maturity_day, as_of=snapshot_as_of),
                    "spy": get_historical_benchmark_close(snapshot, "SPY", maturity_day, as_of=snapshot_as_of),
                    "qqq": get_historical_benchmark_close(snapshot, "QQQ", maturity_day, as_of=snapshot_as_of),
                }
                returns = {
                    "underlying": pct_return(entry_underlying, resolutions["underlying"].get("price")),
                    "option": pct_return(entry_option, resolutions["option"].get("price")),
                    "spy": pct_return(spy_entry, resolutions["spy"].get("price")),
                    "qqq": pct_return(qqq_entry, resolutions["qqq"].get("price")),
                }
                pairs = [(f"underlying_forward_{horizon}d_return", returns["underlying"]), (f"option_forward_{horizon}d_return", returns["option"]), (f"forward_{horizon}d_underlying_return", returns["underlying"]), (f"forward_{horizon}d_option_return", returns["option"])]
                if returns["underlying"] is not None and returns["spy"] is not None:
                    pairs += [(f"underlying_forward_vs_spy_{horizon}d", round(returns["underlying"]-returns["spy"],6)), (f"forward_{horizon}d_vs_spy", round(returns["underlying"]-returns["spy"],6))]
                if returns["underlying"] is not None and returns["qqq"] is not None:
                    pairs += [(f"underlying_forward_vs_qqq_{horizon}d", round(returns["underlying"]-returns["qqq"],6)), (f"forward_{horizon}d_vs_qqq", round(returns["underlying"]-returns["qqq"],6))]
                window = [day for day in dates if signal_session_text < day <= str(resolutions["option"].get("resolved_trading_date") or maturity)]
                for asset, entry, bars in (("underlying", entry_underlying, equity), ("option", entry_option, option)):
                    highs = [pct_return(entry, bars.get(day, {}).get("high")) for day in window]
                    lows = [pct_return(entry, bars.get(day, {}).get("low")) for day in window]
                    pairs += [(f"{asset}_mfe_{horizon}d", max((v for v in highs if v is not None),default=None)), (f"{asset}_mae_{horizon}d", min((v for v in lows if v is not None),default=None))]
                for key, value in pairs: changed |= assign(row,key,value,allow_correction)
                for component, resolution in resolutions.items():
                    component_status = "OBSERVED" if resolution["status"] == "FOUND" and returns[component] is not None else resolution["status"]
                    key=f"{prefix}_{component}_status"
                    if row.get(key) != component_status: row[key],changed=component_status,True
                missing = [component for component in ("underlying","option","spy") if returns[component] is None]
                permanent_statuses=NON_RETRYABLE_STATUSES
                if not missing: status,reason="OBSERVED",None
                elif any(resolutions[c]["status"] in permanent_statuses for c in missing): status,reason="PERMANENTLY_UNAVAILABLE",",".join(f"{c}:{resolutions[c]['status']}" for c in missing)
                else: status,reason="RETRYABLE_SOURCE_ERROR",",".join(f"{c}:{resolutions[c]['status']}" for c in missing)
                if resolutions["option"].get("terminal_state"):
                    for key in ("terminal_state","terminal_value","valuation_method"):
                        changed |= assign(row,key,resolutions["option"].get(key),allow_correction)
                    changed |= assign(row,"expired_worthless",resolutions["option"].get("terminal_state")=="EXPIRED_OTM",allow_correction)
            except Exception as exc:  # persisted diagnostic boundary
                status, reason, resolutions = "RETRYABLE_SOURCE_ERROR", f"{type(exc).__name__}: {exc}", {}
        if row.get(status_key) != status:
            row[status_key], changed = status, True
        old_meta = row.get(meta_key) or {}
        retryable=status in {"RETRYABLE_SOURCE_ERROR","MISSING_SOURCE_DATA","UPDATE_FAILED"}
        prior_attempts=int(old_meta.get("attempt_count") or 0)
        should_attempt=maturity_day is not None and maturity_day <= snapshot_as_of and old_status != "OBSERVED"
        meta = {"maturity_date": maturity, "target_observation_date": maturity, "signal_trading_session": signal_session_text, "status": status, "observed_at": old_meta.get("observed_at") if status == "OBSERVED" and old_meta.get("observed_at") and not allow_correction else (observed_at if status == "OBSERVED" else None), "source": old_meta.get("source") if status == "OBSERVED" and old_meta.get("source") and not allow_correction else (source if status == "OBSERVED" else None), "source_as_of": str(snapshot.get("as_of") or observed_at), "reason": reason, "attempt_count": prior_attempts + int(should_attempt), "last_attempt_at": observed_at if should_attempt else old_meta.get("last_attempt_at"), "last_error": reason, "retryable": retryable, "next_retry_eligible_at": observed_at if retryable else None, "component_resolutions": resolutions if maturity_day is not None and maturity_day <= snapshot_as_of else {}}
        if old_meta != meta:
            row[meta_key], changed = meta, True
        if status in {"MISSING_SOURCE_DATA", "UPDATE_FAILED", "RETRYABLE_SOURCE_ERROR", "PERMANENTLY_UNAVAILABLE"}:
            missing_components=[name for name,value in (meta.get("component_resolutions") or {}).items() if value.get("status") != "FOUND"]
            issues.append({"horizon": f"{horizon}D", "target_observation_date": maturity, "current_status": status, "missing_component": missing_components, "attempted_source": source, "reason": reason, "retryable": retryable, "contract": row.get("contract") or f"{symbol} {row.get('expiration')} {row.get('strike')}{str(row.get('option_type') or '')[:1].upper()}"})
        bucket = classify(row, horizon)
        if row.get(f"outcome_classification_{horizon}d") != bucket:
            row[f"outcome_classification_{horizon}d"], changed = bucket, True
    observed = [h for h in HORIZONS if row.get(f"forward_{h}d_status") == "OBSERVED"]
    latest = classify(row, max(observed)) if observed else "INCONCLUSIVE"
    if row.get("outcome_classification") != latest:
        row["outcome_classification"], changed = latest, True
    if allow_correction:
        row["correction_reason"] = correction_reason
    if changed:
        row["last_updated_at"] = observed_at
    return changed, issues


def update_files(paths: list[Path], snapshot: dict[str, Any], *, allow_correction: bool = False, correction_reason: str | None = None) -> dict[str, Any]:
    dates, counts, failures = session_dates(snapshot), Counter(), []
    canonical_count = changed_rows = 0
    for path in paths:
        rows, file_changed = read_jsonl(path), False
        for row in rows:
            if row.get("canonical", row.get("is_canonical", True)) is False:
                continue
            canonical_count += 1
            changed, issues = update_row(row, snapshot, dates, allow_correction=allow_correction, correction_reason=correction_reason)
            changed_rows += int(changed); file_changed |= changed
            for horizon in HORIZONS:
                counts[f"{horizon}D_{row.get(f'forward_{horizon}d_status', 'PENDING')}"] += 1
            failures += [{"record_id": record_id(row), "symbol": row.get("underlying"), "signal_date": row.get("signal_date"), "path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path), **issue} for issue in issues]
        if file_changed:
            write_jsonl(path, rows)
    failure_suffixes=("MISSING_SOURCE_DATA","UPDATE_FAILED","RETRYABLE_SOURCE_ERROR","PERMANENTLY_UNAVAILABLE")
    overdue = sum(v for k, v in counts.items() if k.endswith(failure_suffixes))
    health = {"canonical_outcome_records": canonical_count, "horizons": {f"{h}D": {"expected": counts[f"{h}D_OBSERVED"]+sum(counts[f"{h}D_{s}"] for s in failure_suffixes), "observed": counts[f"{h}D_OBSERVED"], "pending": counts[f"{h}D_PENDING"]} for h in HORIZONS}, "overdue_outcome_windows": overdue, "update_failures": sum(v for k,v in counts.items() if k.endswith(("UPDATE_FAILED","RETRYABLE_SOURCE_ERROR"))), "status": "DEGRADED" if overdue else "HEALTHY"}
    component_counts=Counter()
    for path in paths:
        for row in read_jsonl(path):
            if row.get("canonical",row.get("is_canonical",True)) is False: continue
            for h in HORIZONS:
                for component in ("underlying","option","spy","qqq"):
                    status=row.get(f"forward_{h}d_{component}_status")
                    if status: component_counts[f"{component}:{status}"]+=1
    retrieval_health={"mature_observations_expected":sum(v["expected"] for v in health["horizons"].values()),"successfully_resolved":sum(v["observed"] for v in health["horizons"].values()),"pending":sum(v["pending"] for v in health["horizons"].values()),"retryable_failures":sum(v for k,v in counts.items() if k.endswith(("RETRYABLE_SOURCE_ERROR","UPDATE_FAILED"))),"permanently_unavailable":sum(v for k,v in counts.items() if k.endswith("PERMANENTLY_UNAVAILABLE")),"component_retrieval":{component:{"found":component_counts[f"{component}:OBSERVED"],"attempted":sum(v for k,v in component_counts.items() if k.startswith(component+":") and not k.endswith(("PENDING","NOT_YET_MATURE"))),"success_rate":round(component_counts[f"{component}:OBSERVED"]/sum(v for k,v in component_counts.items() if k.startswith(component+":") and not k.endswith(("PENDING","NOT_YET_MATURE"))),6) if sum(v for k,v in component_counts.items() if k.startswith(component+":") and not k.endswith(("PENDING","NOT_YET_MATURE"))) else None} for component in ("underlying","option","spy","qqq")}}
    return {"outcome_health": health, "outcome_retrieval_health":retrieval_health, "records_updated_this_run": changed_rows, "issues": failures}


def merge_snapshots(snapshots: list[dict[str, Any]]) -> dict[str, Any]:
    """Merge append-only provider captures; later captures win for the same session."""
    merged: dict[str, Any] = {"equity_bars": {}, "option_bars": {}, "option_id_lookup": {}, "option_contracts": {}, "option_quotes": {}, "option_quote_checkpoints": {}, "capabilities": {}}
    for snapshot in sorted(snapshots, key=lambda item: str(item.get("as_of") or "")):
        merged["as_of"] = snapshot.get("as_of") or merged.get("as_of")
        merged.setdefault("sources", []).append(snapshot.get("source") or snapshot.get("source_id") or "historical_bar_snapshot")
        for key in ("option_id_lookup", "option_contracts"):
            merged[key].update(snapshot.get(key, {}))
        merged["capabilities"].update(snapshot.get("capabilities", {}))
        checkpoint_date = str(snapshot.get("checkpoint_date") or snapshot.get("quote_date") or snapshot.get("as_of") or "")[:10]
        for option_id, quote in (snapshot.get("option_quotes") or {}).items():
            merged["option_quotes"][option_id] = quote
            if checkpoint_date:
                merged["option_quote_checkpoints"].setdefault(checkpoint_date, {})[option_id] = quote
        for checkpoint_day, quotes in (snapshot.get("option_quote_checkpoints") or {}).items():
            merged["option_quote_checkpoints"].setdefault(str(checkpoint_day)[:10], {}).update(quotes)
        results = ((snapshot.get("data") or {}).get("results") or snapshot.get("results") or [])
        if checkpoint_date and results:
            target = merged["option_quote_checkpoints"].setdefault(checkpoint_date, {})
            for item in results:
                quote = item.get("quote") if isinstance(item, dict) else None
                option_id = str(quote.get("instrument_id")) if quote and quote.get("instrument_id") else ""
                if option_id:
                    target[option_id] = {"quote": quote, "close": item.get("close")}
        for group in ("equity_bars", "option_bars"):
            for instrument, bars in snapshot.get(group, {}).items():
                by_day = {str(bar.get("date"))[:10]: bar for bar in merged[group].get(instrument, [])}
                by_day.update({str(bar.get("date"))[:10]: bar for bar in bars if bar.get("date")})
                merged[group][instrument] = [by_day[day] for day in sorted(by_day)]
    merged["source"] = "; ".join(dict.fromkeys(merged.pop("sources", [])))
    return merged


def default_snapshot_paths() -> list[Path]:
    return sorted((ROOT / "data/outcome_update_snapshots").glob("*.json"))


def find_record(paths: list[Path], wanted: str) -> tuple[Path, dict[str, Any]] | None:
    for path in paths:
        for row in read_jsonl(path):
            if record_id(row) == wanted or str(row.get("option_signal_outcome_id") or "") == wanted:
                return path, row
    return None


def repository_option_id_lookup() -> dict[str, str]:
    lookup: dict[str, str] = {}
    for directory in ("data/options_setup_records", "data/option_shadow_trades", "data/option_signal_outcomes"):
        for path in sorted((ROOT / directory).glob("*.jsonl")):
            for row in read_jsonl(path):
                option_id = row.get("option_id") or row.get("instrument_id")
                if not option_id:
                    continue
                for key in ("option_setup_id", "options_setup_id", "outcome_record_id", "option_signal_outcome_id", "option_shadow_trade_id", "shadow_trade_id"):
                    if row.get(key):
                        lookup[str(row[key])] = str(option_id)
    return lookup


def due_option_checkpoints(paths: list[Path], as_of: date, option_id_lookup: dict[str, str] | None = None) -> list[dict[str, Any]]:
    due: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    option_id_lookup = option_id_lookup or {}
    for path in paths:
        for row in read_jsonl(path):
            if row.get("canonical", row.get("is_canonical", True)) is False:
                continue
            signal_text = str(row.get("signal_date") or row.get("entry_date") or row.get("date") or "")[:10]
            signal_day = parse_day(signal_text)
            if signal_day is None:
                continue
            signal_session = signal_trading_date(signal_day, row.get("entry_snapshot_at") or row.get("timestamp"))
            option_id = (
                row.get("option_id")
                or row.get("instrument_id")
                or option_id_lookup.get(str(row.get("option_setup_id")))
                or option_id_lookup.get(record_id(row))
                or option_id_lookup.get(str(row.get("option_shadow_trade_id") or row.get("shadow_trade_id") or ""))
                or resolve_option_id({}, row)
            )
            if not option_id:
                continue
            for horizon in HORIZONS:
                target = trading_day(signal_session, horizon)
                if target != as_of:
                    continue
                if row.get(f"option_forward_{horizon}d_return") is not None:
                    continue
                if row.get(f"forward_{horizon}d_option_status") == "OBSERVED":
                    continue
                key = (option_id, f"{horizon}D")
                if key in seen:
                    continue
                seen.add(key)
                due.append({
                    "record_id": record_id(row),
                    "path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                    "underlying": row.get("underlying") or row.get("symbol"),
                    "option_id": option_id,
                    "horizon": f"{horizon}D",
                    "signal_date": signal_text,
                    "signal_trading_session": signal_session.isoformat(),
                    "target_observation_date": target.isoformat(),
                    "entry_option_mid": row.get("entry_option_mid") or row.get("entry_midpoint") or row.get("entry_premium"),
                    "contract": row.get("contract") or f"{row.get('underlying')} {row.get('expiration')} {row.get('strike')}{str(row.get('option_type') or '')[:1].upper()}",
                })
    return due


def debug_record(row: dict[str, Any], snapshot: dict[str, Any], horizon: int, *, path: Path | None = None, verbose: bool = False) -> dict[str, Any]:
    signal_text = str(row.get("signal_date") or row.get("entry_date") or row.get("date") or "")[:10]
    signal_day = parse_day(signal_text)
    if signal_day is None:
        raise SystemExit(f"Record {record_id(row)} has no parseable signal date")
    signal_session = signal_trading_date(signal_day, row.get("entry_snapshot_at") or row.get("timestamp"))
    target = trading_day(signal_session, horizon)
    as_of = parse_day(snapshot.get("evaluation_as_of") or snapshot.get("as_of")) or date.today()
    symbol = str(row.get("underlying") or row.get("symbol") or "")
    trace = {
        "record_id": record_id(row),
        "path": str(path.relative_to(ROOT)) if path and path.is_relative_to(ROOT) else (str(path) if path else None),
        "horizon": f"{horizon}D",
        "signal": {
            "signal_date": signal_text,
            "entry_snapshot_at": row.get("entry_snapshot_at"),
            "signal_trading_session": signal_session.isoformat(),
            "target_observation_date": target.isoformat(),
        },
        "underlying": get_historical_underlying_close(snapshot, symbol, target, as_of=as_of),
        "option": get_historical_option_close(snapshot, row, target, as_of=as_of),
        "benchmark": {
            "SPY": get_historical_benchmark_close(snapshot, "SPY", target, as_of=as_of),
            "QQQ": get_historical_benchmark_close(snapshot, "QQQ", target, as_of=as_of),
        },
    }
    print(f"SIGNAL record_id={trace['record_id']} signal_date={signal_text} entry_snapshot_at={row.get('entry_snapshot_at')} session={signal_session.isoformat()}")
    print(f"HORIZON horizon={horizon}D target_observation_date={target.isoformat()} source_as_of={snapshot.get('as_of')}")
    print(f"UNDERLYING symbol={symbol} status={trace['underlying']['status']} price={trace['underlying'].get('price')} reason={trace['underlying'].get('root_cause')}")
    option = trace["option"]
    print(f"OPTION option_id={option.get('instrument_id')} status={option['status']} price={option.get('price')} reason={option.get('root_cause')}")
    for benchmark, result in trace["benchmark"].items():
        print(f"BENCHMARK symbol={benchmark} status={result['status']} price={result.get('price')} reason={result.get('root_cause')}")
    if verbose:
        print(json.dumps(trace, indent=2, sort_keys=True))
    return trace


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", action="append", type=Path, help="Repeat to merge multiple append-only history captures.")
    parser.add_argument("--paths", nargs="*", type=Path)
    parser.add_argument("--debug-record", help="Print a component-level historical retrieval trace for one outcome record without writing files.")
    parser.add_argument("--horizon", default="1D", help="Debug horizon such as 1D, 5D, 10D, 20D, or 30D.")
    parser.add_argument("--list-due-option-checkpoints", action="store_true", help="List option contracts whose prospective checkpoint quote is due on --as-of.")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--allow-correction", action="store_true")
    parser.add_argument("--correction-reason")
    parser.add_argument("--as-of", type=date.fromisoformat, help="Evaluate maturity through this date even when the source snapshot is older.")
    args = parser.parse_args()
    if args.allow_correction and not args.correction_reason:
        parser.error("--allow-correction requires --correction-reason")
    if not args.snapshot and not args.debug_record and not args.list_due_option_checkpoints:
        parser.error("--snapshot is required unless --debug-record is used")
    snapshot_paths = [path if path.is_absolute() else ROOT / path for path in (args.snapshot or default_snapshot_paths())]
    if not snapshot_paths and not args.list_due_option_checkpoints:
        parser.error("No outcome-update snapshots found")
    snapshot = merge_snapshots([json.loads(path.read_text(encoding="utf-8")) for path in snapshot_paths]) if snapshot_paths else {}
    if args.as_of:
        snapshot["evaluation_as_of"] = args.as_of.isoformat()
    paths = args.paths or list((ROOT / "data/option_signal_outcomes").glob("*.jsonl"))
    paths = [path if path.is_absolute() else ROOT / path for path in paths]
    snapshot.setdefault("option_id_lookup", {}).update(repository_option_id_lookup())
    if args.list_due_option_checkpoints:
        checkpoint_day = args.as_of or date.today()
        option_id_lookup = repository_option_id_lookup()
        payload = {
            "checkpoint_date": checkpoint_day.isoformat(),
            "source": "prospective_option_checkpoint_request",
            "count": 0,
            "option_ids": [],
            "due": due_option_checkpoints(paths, checkpoint_day, option_id_lookup),
            "capture_instruction": "Call get_option_quotes for option_ids, save the raw response with checkpoint_date/source, then rerun update_option_outcomes.py with that quote snapshot.",
        }
        payload["option_ids"] = sorted({item["option_id"] for item in payload["due"]})
        payload["count"] = len(payload["option_ids"])
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    if args.debug_record:
        horizon_text = str(args.horizon).upper().removesuffix("D")
        try:
            horizon = int(horizon_text)
        except ValueError as exc:
            raise SystemExit(f"Invalid --horizon {args.horizon!r}") from exc
        found = find_record(paths, args.debug_record)
        if not found:
            raise SystemExit(f"Outcome record not found: {args.debug_record}")
        debug_record(found[1], snapshot, horizon, path=found[0], verbose=args.verbose)
        return 0
    report = update_files(paths, snapshot, allow_correction=args.allow_correction, correction_reason=args.correction_reason)
    report["snapshots"] = [str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path) for path in snapshot_paths]
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
