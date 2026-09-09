#!/usr/bin/env python3
"""Generate research-only strategy diagnostics from canonical setup outcomes."""
from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 5, 10, 20, 30)


def load_jsonl(directory: str) -> list[dict[str, Any]]:
    rows = []
    for path in sorted((ROOT / directory).glob("*.jsonl")):
        rows.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    return rows


def number(value: Any) -> float | None:
    try:
        return None if value is None or value == "" else float(value)
    except (TypeError, ValueError):
        return None


def canonical(row: dict[str, Any]) -> bool:
    return row.get("canonical", row.get("is_canonical", True)) is not False


def median(rows: list[dict[str, Any]], field: str) -> float | None:
    values = [value for row in rows if (value := number(row.get(field))) is not None]
    return round(statistics.median(values), 6) if values else None


def directional_win(row: dict[str, Any], value: float) -> bool:
    bearish = str(row.get("directional_thesis") or "").lower() == "bearish" or str(row.get("option_type") or "").lower() == "put"
    return value < 0 if bearish else value > 0


def horizon_metrics(rows: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    observed = [row for row in rows if row.get(f"forward_{horizon}d_status") == "OBSERVED" or (number(row.get(f"underlying_forward_{horizon}d_return")) is not None and number(row.get(f"option_forward_{horizon}d_return")) is not None)]
    option_values = [number(row.get(f"option_forward_{horizon}d_return")) for row in observed]
    underlying_values = [number(row.get(f"underlying_forward_{horizon}d_return")) for row in observed]
    option_values = [value for value in option_values if value is not None]
    underlying_pairs = [(row, value) for row in observed if (value := number(row.get(f"underlying_forward_{horizon}d_return"))) is not None]
    return {
        "mature_sample": len(observed),
        "option_win_rate": round(sum(value > 0 for value in option_values) / len(option_values), 6) if option_values else None,
        "underlying_win_rate": round(sum(directional_win(row, value) for row, value in underlying_pairs) / len(underlying_pairs), 6) if underlying_pairs else None,
        "median_option_return": median(observed, f"option_forward_{horizon}d_return"),
        "median_underlying_return": median(observed, f"underlying_forward_{horizon}d_return"),
        "median_spy_excess_return": median(observed, f"underlying_forward_vs_spy_{horizon}d"),
        "median_qqq_excess_return": median(observed, f"underlying_forward_vs_qqq_{horizon}d"),
        "median_option_mfe": median(observed, f"option_mfe_{horizon}d"),
        "median_option_mae": median(observed, f"option_mae_{horizon}d"),
        "median_underlying_mfe": median(observed, f"underlying_mfe_{horizon}d"),
        "median_underlying_mae": median(observed, f"underlying_mae_{horizon}d"),
        "classifications": dict(sorted(Counter(str(row.get(f"outcome_classification_{horizon}d") or "INCONCLUSIVE") for row in observed).items())),
    }


def score_bucket(value: Any) -> str:
    score = number(value)
    if score is None: return "missing"
    if score < 70: return "<70"
    if score < 75: return "70-74"
    if score < 80: return "75-79"
    if score < 85: return "80-84"
    return "85+"


def range_bucket(value: Any, cuts: tuple[float, ...], labels: tuple[str, ...]) -> str:
    numeric = number(value)
    if numeric is None: return "missing"
    for cut, label in zip(cuts, labels):
        if numeric < cut: return label
    return labels[-1]


def group_report(rows: list[dict[str, Any]], getter: Callable[[dict[str, Any]], str]) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows: groups[getter(row)].append(row)
    return {name: {"count": len(group), "horizons": {f"{h}D": horizon_metrics(group, h) for h in HORIZONS}} for name, group in sorted(groups.items())}


def blocked_category(row: dict[str, Any]) -> str:
    text = " ".join(str(row.get(key) or "") for key in ("primary_blocking_rule", "blocked_reason", "entry_eligibility", "pipeline_status")).lower()
    if "outside" in text or "universe" in text: return "outside-universe blocked"
    if "earning" in text: return "earnings blocked"
    if "extension" in text or "extended" in text: return "extension blocked"
    if "account" in text or "premium_risk" in text: return "account-risk blocked"
    if "directional" in text: return "insufficient_directional_edge"
    if "suitability" in text: return "insufficient_options_suitability"
    return "other blocked"


def underlying_only_metrics(rows: list[dict[str, Any]], horizon: int) -> dict[str, Any]:
    field = f"forward_{horizon}d_return"
    values = [value for row in rows if (value := number(row.get(field))) is not None]
    return {"count": len(rows), "observed_count": len(values), "median_underlying_return": round(statistics.median(values), 6) if values else None, "win_rate": round(sum(value > 0 for value in values)/len(values), 6) if values else None, "median_spy_excess_return": median(rows, f"forward_vs_spy_{horizon}d")}


def build_report() -> dict[str, Any]:
    setups = [row for row in load_jsonl("data/options_setup_records") if canonical(row)]
    outcomes = [row for row in load_jsonl("data/option_signal_outcomes") if canonical(row)]
    research = [row for row in load_jsonl("data/research_records") if canonical(row)]
    signal_outcomes = load_jsonl("data/signal_outcomes")
    signal_outcome_by_research = {str(row.get("research_record_id") or row.get("research_id")): row for row in signal_outcomes}
    for row in research:
        for key, value in signal_outcome_by_research.get(str(row.get("research_record_id") or row.get("research_id")), {}).items():
            if row.get(key) is None:
                row[key] = value
    manifests = [json.loads(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "data/run_manifests").glob("*.json"))]
    regime_by_run = {str(row.get("run_id")): str(row.get("market_regime") or row.get("regime") or row.get("market_context", {}).get("regime") or "missing") for row in manifests}
    for row in research:
        row.setdefault("market_regime", regime_by_run.get(str(row.get("run_id")), "missing"))
    research_by_id = {str(row.get("research_record_id") or row.get("research_id")): row for row in research}
    outcome_by_setup = {str(row.get("option_setup_id")): row for row in outcomes}
    qualified = []
    for setup in setups:
        quality = str(setup.get("setup_quality_status") or "").upper()
        if not (quality.startswith("QUALIFIED") or str(setup.get("final_decision") or "").upper() == "SHADOW_ONLY_QUALIFIED"):
            continue
        merged = dict(research_by_id.get(str(setup.get("research_record_id") or setup.get("research_id")), {}))
        merged.update(setup)
        merged.update(outcome_by_setup.get(str(setup.get("option_setup_id") or setup.get("options_setup_id")), {}))
        merged.setdefault("market_regime", regime_by_run.get(str(setup.get("run_id")), "missing"))
        qualified.append(merged)

    dimensions = {
        "setup_score_bucket": lambda r: score_bucket(r.get("options_setup_score")),
        "underlying_score_bucket": lambda r: score_bucket(r.get("underlying_research_score") or r.get("research_score")),
        "call_vs_put": lambda r: str(r.get("option_type") or "missing").lower(),
        "underlying_ticker": lambda r: str(r.get("underlying") or "missing"),
        "sector": lambda r: str(r.get("sector") or "missing"),
        "dte_bucket": lambda r: range_bucket(r.get("dte_at_signal") or r.get("dte"), (30,46,61,91), ("<30","30-45","46-60","61-90","91+")),
        "delta_bucket": lambda r: range_bucket(abs(number(r.get("entry_delta") or r.get("delta")) or -1), (.35,.51,.71), ("<0.35","0.35-0.50","0.51-0.70",">0.70")),
        "iv_bucket": lambda r: range_bucket(r.get("entry_implied_volatility") or r.get("implied_volatility"), (.25,.40,.60), ("<25%","25-39%","40-59%","60%+")),
        "scanner_source": lambda r: str((r.get("scanner_sources") or [r.get("scanner_source") or "missing"])[0]),
        "market_regime": lambda r: str(r.get("market_regime") or r.get("regime") or "missing"),
        "account_fit_status": lambda r: str(r.get("account_fit_status") or "missing"),
        "approved_universe_status": lambda r: str(r.get("approved_universe_status") or r.get("underlying_eligibility") or "missing"),
    }
    regime_bias: dict[str, Counter[str]] = defaultdict(Counter)
    for row in research:
        regime = str(row.get("market_regime") or row.get("regime") or "missing")
        thesis = str(row.get("directional_thesis") or row.get("thesis_direction") or "neutral").lower()
        regime_bias[regime][f"{thesis}_theses" if thesis in {"bullish","neutral","bearish"} else "neutral_theses"] += 1
        if thesis == "bearish" and blocked_category(row) != "other blocked": regime_bias[regime]["rejected_bearish_candidates"] += 1
    for row in qualified:
        regime = str(row.get("market_regime") or row.get("regime") or "missing")
        regime_bias[regime][f"qualified_{str(row.get('option_type') or 'missing').lower()}s"] += 1
    for counts in regime_bias.values():
        for key in ("bullish_theses", "neutral_theses", "bearish_theses", "qualified_calls", "qualified_puts", "rejected_bearish_candidates"):
            counts.setdefault(key, 0)

    blocked: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in research:
        category = blocked_category(row)
        if category != "other blocked": blocked[category].append(row)
    comparison = {"qualified setups": {f"{h}D": horizon_metrics(qualified, h) for h in HORIZONS}}
    comparison.update({category: {f"{h}D": underlying_only_metrics(rows, h) for h in HORIZONS} for category, rows in sorted(blocked.items())})
    return {
        "report_type": "STRATEGY_DIAGNOSTICS_RESEARCH_ONLY", "generated_at": datetime.now(timezone.utc).isoformat(),
        "strategy_changes_applied": False, "total_qualified_setups": len(qualified),
        "overall_by_horizon": {f"{h}D": horizon_metrics(qualified, h) for h in HORIZONS},
        "breakdowns": {name: group_report(qualified, getter) for name, getter in dimensions.items()},
        "score_discrimination": group_report(qualified, dimensions["setup_score_bucket"]),
        "direction_and_option_bias_by_market_regime": {key: dict(sorted(value.items())) for key, value in sorted(regime_bias.items())},
        "rejection_opportunity_cost": comparison,
        "interpretation_guardrail": "Descriptive diagnostics only; no threshold optimization or automatic strategy changes.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path); args = parser.parse_args()
    report = build_report(); payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        path = args.output if args.output.is_absolute() else ROOT / args.output
        path.parent.mkdir(parents=True, exist_ok=True); path.write_text(payload, encoding="utf-8"); print(f"Wrote {path}")
    else: print(payload, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
