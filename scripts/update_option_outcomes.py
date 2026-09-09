#!/usr/bin/env python3
"""Idempotently populate matured option outcomes from immutable bar snapshots."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 5, 10, 20, 30)
STATUSES = {"PENDING", "OBSERVED", "MISSING_SOURCE_DATA", "UPDATE_FAILED", "NOT_APPLICABLE"}


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


def weekday_maturity(signal_day: date, horizon: int) -> date:
    current = signal_day
    for _ in range(horizon):
        current += timedelta(days=1)
        while current.weekday() >= 5:
            current += timedelta(days=1)
    return current


def session_dates(snapshot: dict[str, Any]) -> list[str]:
    explicit = snapshot.get("trading_dates") or snapshot.get("market_sessions")
    if explicit:
        return sorted(str(item.get("date") if isinstance(item, dict) else item)[:10] for item in explicit)
    dates = set()
    for bars in snapshot.get("equity_bars", {}).values():
        dates.update(str(bar["date"])[:10] for bar in bars if bar.get("date"))
    return sorted(dates)


def observation_day(signal_date: str, horizon: int, dates: list[str]) -> str:
    later = [day for day in dates if day > signal_date]
    if len(later) >= horizon:
        return later[horizon - 1]
    parsed = parse_day(signal_date)
    return weekday_maturity(parsed, horizon).isoformat() if parsed else ""


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
    equity = bars_by_date(snapshot.get("equity_bars", {}).get(symbol, []))
    spy = bars_by_date(snapshot.get("equity_bars", {}).get("SPY", []))
    qqq = bars_by_date(snapshot.get("equity_bars", {}).get("QQQ", []))
    option_id = row.get("option_id") or row.get("instrument_id") or snapshot.get("option_id_lookup", {}).get(str(row.get("option_setup_id")))
    option = bars_by_date(snapshot.get("option_bars", {}).get(str(option_id), []))
    entry_underlying = numeric(row.get("underlying_price_at_entry") or row.get("entry_underlying_price")) or numeric(equity.get(signal_date, {}).get("close"))
    entry_option = numeric(row.get("entry_option_mid") or row.get("entry_midpoint") or row.get("entry_premium") or row.get("entry_mark"))
    spy_entry, qqq_entry = numeric(spy.get(signal_date, {}).get("close")), numeric(qqq.get(signal_date, {}).get("close"))

    for horizon in HORIZONS:
        prefix = f"forward_{horizon}d"
        maturity = observation_day(signal_date, horizon, dates)
        maturity_day = parse_day(maturity)
        status_key, meta_key = f"{prefix}_status", f"{prefix}_observation"
        old_status = row.get(status_key)
        if maturity_day is None or maturity_day > snapshot_as_of:
            status, reason = "PENDING", "horizon_not_mature_as_of_source_snapshot"
        else:
            try:
                underlying_ret = pct_return(entry_underlying, equity.get(maturity, {}).get("close"))
                option_ret = pct_return(entry_option, option.get(maturity, {}).get("close"))
                spy_ret = pct_return(spy_entry, spy.get(maturity, {}).get("close"))
                qqq_ret = pct_return(qqq_entry, qqq.get(maturity, {}).get("close"))
                missing = [name for name, value in (("underlying_close_or_entry", underlying_ret), ("option_close_or_entry", option_ret), ("spy_close_or_entry", spy_ret)) if value is None]
                if missing:
                    status, reason = "MISSING_SOURCE_DATA", ",".join(missing)
                else:
                    status, reason = "OBSERVED", None
                    pairs = [(f"underlying_forward_{horizon}d_return", underlying_ret), (f"option_forward_{horizon}d_return", option_ret), (f"underlying_forward_vs_spy_{horizon}d", round(underlying_ret-spy_ret, 6)), (f"forward_{horizon}d_underlying_return", underlying_ret), (f"forward_{horizon}d_option_return", option_ret), (f"forward_{horizon}d_vs_spy", round(underlying_ret-spy_ret, 6))]
                    if qqq_ret is not None:
                        pairs += [(f"underlying_forward_vs_qqq_{horizon}d", round(underlying_ret-qqq_ret, 6)), (f"forward_{horizon}d_vs_qqq", round(underlying_ret-qqq_ret, 6))]
                    window = [day for day in dates if signal_date < day <= maturity]
                    for asset, entry, bars in (("underlying", entry_underlying, equity), ("option", entry_option, option)):
                        highs = [pct_return(entry, bars.get(day, {}).get("high")) for day in window]
                        lows = [pct_return(entry, bars.get(day, {}).get("low")) for day in window]
                        pairs += [(f"{asset}_mfe_{horizon}d", max(v for v in highs if v is not None) if any(v is not None for v in highs) else None), (f"{asset}_mae_{horizon}d", min(v for v in lows if v is not None) if any(v is not None for v in lows) else None)]
                    for key, value in pairs:
                        changed |= assign(row, key, value, allow_correction)
            except Exception as exc:  # persisted diagnostic boundary
                status, reason = "UPDATE_FAILED", f"{type(exc).__name__}: {exc}"
        if old_status == "OBSERVED" and not allow_correction:
            status, reason = "OBSERVED", None
        if row.get(status_key) != status:
            row[status_key], changed = status, True
        old_meta = row.get(meta_key) or {}
        meta = {"maturity_date": maturity, "status": status, "observed_at": old_meta.get("observed_at") if status == "OBSERVED" and old_meta.get("observed_at") and not allow_correction else (observed_at if status == "OBSERVED" else None), "source": old_meta.get("source") if status == "OBSERVED" and old_meta.get("source") and not allow_correction else (source if status == "OBSERVED" else None), "source_as_of": str(snapshot.get("as_of") or observed_at), "reason": reason}
        if old_meta != meta:
            row[meta_key], changed = meta, True
        if status in {"MISSING_SOURCE_DATA", "UPDATE_FAILED"}:
            issues.append({"horizon": f"{horizon}D", "maturity_date": maturity, "current_status": status, "reason": reason})
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
    overdue = sum(v for k, v in counts.items() if k.endswith(("MISSING_SOURCE_DATA", "UPDATE_FAILED")))
    health = {"canonical_outcome_records": canonical_count, "horizons": {f"{h}D": {"expected": counts[f"{h}D_OBSERVED"]+counts[f"{h}D_MISSING_SOURCE_DATA"]+counts[f"{h}D_UPDATE_FAILED"], "observed": counts[f"{h}D_OBSERVED"], "pending": counts[f"{h}D_PENDING"]} for h in HORIZONS}, "overdue_outcome_windows": overdue, "update_failures": sum(v for k, v in counts.items() if k.endswith("UPDATE_FAILED")), "status": "DEGRADED" if overdue else "HEALTHY"}
    return {"outcome_health": health, "records_updated_this_run": changed_rows, "issues": failures}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--paths", nargs="*", type=Path)
    parser.add_argument("--allow-correction", action="store_true")
    parser.add_argument("--correction-reason")
    parser.add_argument("--as-of", type=date.fromisoformat, help="Evaluate maturity through this date even when the source snapshot is older.")
    args = parser.parse_args()
    if args.allow_correction and not args.correction_reason:
        parser.error("--allow-correction requires --correction-reason")
    snapshot_path = args.snapshot if args.snapshot.is_absolute() else ROOT / args.snapshot
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    if args.as_of:
        snapshot["evaluation_as_of"] = args.as_of.isoformat()
    paths = args.paths or list((ROOT / "data/option_signal_outcomes").glob("*.jsonl"))
    paths = [path if path.is_absolute() else ROOT / path for path in paths]
    report = update_files(paths, snapshot, allow_correction=args.allow_correction, correction_reason=args.correction_reason)
    report["snapshot"] = str(snapshot_path.relative_to(ROOT)) if snapshot_path.is_relative_to(ROOT) else str(snapshot_path)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
