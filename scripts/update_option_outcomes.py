#!/usr/bin/env python3
"""Populate matured option shadow outcome fields from historical bar snapshots."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 5, 10, 20, 30)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSONL {path}:{line_number}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def numeric(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def close_by_date(bars: list[dict[str, Any]]) -> dict[str, float]:
    return {str(bar["date"]): float(bar["close"]) for bar in bars if bar.get("close") is not None}


def high_low_by_date(bars: list[dict[str, Any]]) -> tuple[dict[str, float], dict[str, float]]:
    highs = {str(bar["date"]): float(bar["high"]) for bar in bars if bar.get("high") is not None}
    lows = {str(bar["date"]): float(bar["low"]) for bar in bars if bar.get("low") is not None}
    return highs, lows


def trading_dates(snapshot: dict[str, Any]) -> list[str]:
    dates = set()
    for bars in snapshot["equity_bars"].values():
        dates.update(str(bar["date"]) for bar in bars)
    return sorted(dates)


def target_date(signal_date: str, horizon: int, dates: list[str]) -> str | None:
    if signal_date not in dates:
        return None
    index = dates.index(signal_date) + horizon
    if index >= len(dates):
        return None
    return dates[index]


def pct_return(entry: float | None, exit_value: float | None) -> float | None:
    if entry in (None, 0) or exit_value is None:
        return None
    return round((exit_value / entry) - 1, 6)


def max_observed(values: list[float | None]) -> float | None:
    observed = [value for value in values if value is not None]
    return max(observed) if observed else None


def min_observed(values: list[float | None]) -> float | None:
    observed = [value for value in values if value is not None]
    return min(observed) if observed else None


def classify(row: dict[str, Any]) -> str:
    one_day = numeric(row.get("option_forward_1d_return") or row.get("forward_1d_option_return"))
    five_day = numeric(row.get("option_forward_5d_return") or row.get("forward_5d_option_return"))
    if five_day is None and one_day is None:
        return str(row.get("outcome_classification") or row.get("outcome_class") or "INSUFFICIENT_DATA")
    reference = five_day if five_day is not None else one_day
    if reference is None:
        return "INSUFFICIENT_DATA"
    if reference > 0:
        return "THESIS_RIGHT_CONTRACT_RIGHT"
    return "THESIS_WRONG_OR_CONTRACT_POOR_PENDING_REVIEW"


def update_row(row: dict[str, Any], snapshot: dict[str, Any], dates: list[str]) -> bool:
    signal_date = str(row.get("signal_date") or row.get("date") or "")
    underlying = str(row.get("underlying") or "")
    if not signal_date or not underlying:
        return False

    equity_bars = snapshot["equity_bars"].get(underlying)
    spy_bars = snapshot["equity_bars"].get("SPY")
    qqq_bars = snapshot["equity_bars"].get("QQQ")
    if not equity_bars or not spy_bars or not qqq_bars:
        return False

    option_id = row.get("option_id") or row.get("instrument_id")
    if not option_id:
        option_id = snapshot.get("option_id_lookup", {}).get(str(row.get("option_setup_id")))
    option_bars = snapshot.get("option_bars", {}).get(str(option_id))
    if not option_bars:
        return False

    equity_close = close_by_date(equity_bars)
    spy_close = close_by_date(spy_bars)
    qqq_close = close_by_date(qqq_bars)
    option_close = close_by_date(option_bars)

    entry_underlying = numeric(row.get("underlying_price_at_entry"))
    notes: list[str] = list(row.get("outcome_update_notes") or [])
    if entry_underlying is None:
        entry_underlying = equity_close.get(signal_date)
        if entry_underlying is not None and "underlying_price_at_entry_missing_used_signal_close" not in notes:
            notes.append("underlying_price_at_entry_missing_used_signal_close")

    entry_option = numeric(row.get("entry_option_mid") or row.get("entry_midpoint") or row.get("entry_premium") or row.get("entry_mark"))
    spy_entry = spy_close.get(signal_date)
    qqq_entry = qqq_close.get(signal_date)
    changed = False

    for horizon in HORIZONS:
        date = target_date(signal_date, horizon, dates)
        if date is None:
            continue
        underlying_ret = pct_return(entry_underlying, equity_close.get(date))
        option_ret = pct_return(entry_option, option_close.get(date))
        spy_ret = pct_return(spy_entry, spy_close.get(date))
        qqq_ret = pct_return(qqq_entry, qqq_close.get(date))

        for key, value in [
            (f"underlying_forward_{horizon}d_return", underlying_ret),
            (f"option_forward_{horizon}d_return", option_ret),
        ]:
            if value is not None and key in row and row.get(key) is None:
                row[key] = value
                changed = True

        if underlying_ret is not None and spy_ret is not None:
            key = f"underlying_forward_vs_spy_{horizon}d"
            if key in row and row.get(key) is None:
                row[key] = round(underlying_ret - spy_ret, 6)
                changed = True

        if underlying_ret is not None and qqq_ret is not None:
            key = f"underlying_forward_vs_qqq_{horizon}d"
            if key in row and row.get(key) is None:
                row[key] = round(underlying_ret - qqq_ret, 6)
                changed = True

        # Shadow-trade files use a parallel naming convention.
        for key, value in [
            (f"forward_{horizon}d_underlying_return", underlying_ret),
            (f"forward_{horizon}d_option_return", option_ret),
        ]:
            if value is not None and key in row and row.get(key) is None:
                row[key] = value
                changed = True
        if underlying_ret is not None and spy_ret is not None:
            key = f"forward_{horizon}d_vs_spy"
            if key in row and row.get(key) is None:
                row[key] = round(underlying_ret - spy_ret, 6)
                changed = True
        if underlying_ret is not None and qqq_ret is not None:
            key = f"forward_{horizon}d_vs_qqq"
            if key in row and row.get(key) is None:
                row[key] = round(underlying_ret - qqq_ret, 6)
                changed = True

    if target_date(signal_date, 20, dates) is not None:
        end = target_date(signal_date, 20, dates)
        if end is not None:
            window = [date for date in dates if signal_date < date <= end]
            option_high, option_low = high_low_by_date(option_bars)
            equity_high, equity_low = high_low_by_date(equity_bars)
            option_mfe = max_observed([pct_return(entry_option, option_high.get(date)) for date in window])
            option_mae = min_observed([pct_return(entry_option, option_low.get(date)) for date in window])
            underlying_mfe = max_observed([pct_return(entry_underlying, equity_high.get(date)) for date in window])
            underlying_mae = min_observed([pct_return(entry_underlying, equity_low.get(date)) for date in window])
            for key, value in [
                ("option_mfe_20d", option_mfe),
                ("option_mae_20d", option_mae),
                ("underlying_mfe_20d", underlying_mfe),
                ("underlying_mae_20d", underlying_mae),
            ]:
                if value is not None and row.get(key) is None:
                    row[key] = value
                    changed = True

    if notes:
        row["outcome_update_notes"] = notes
    if changed:
        as_of = snapshot.get("as_of") or datetime.now(timezone.utc).isoformat()
        row["last_updated_at"] = as_of
        classification = classify(row)
        if "outcome_classification" in row:
            row["outcome_classification"] = classification
        if "outcome_class" in row:
            row["outcome_class"] = classification
    return changed


def update_files(paths: list[Path], snapshot: dict[str, Any]) -> int:
    dates = trading_dates(snapshot)
    changed_rows = 0
    for path in paths:
        rows = read_jsonl(path)
        changed = False
        for row in rows:
            if update_row(row, snapshot, dates):
                changed_rows += 1
                changed = True
        if changed:
            write_jsonl(path, rows)
    return changed_rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--paths", nargs="*", type=Path)
    args = parser.parse_args()

    snapshot_path = args.snapshot if args.snapshot.is_absolute() else ROOT / args.snapshot
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    paths = args.paths or list((ROOT / "data/option_signal_outcomes").glob("*.jsonl")) + list(
        (ROOT / "data/option_shadow_trades").glob("*.jsonl")
    )
    paths = [path if path.is_absolute() else ROOT / path for path in paths]
    changed = update_files(paths, snapshot)
    print(f"Updated {changed} outcome rows from {snapshot_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
