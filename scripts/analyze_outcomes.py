#!/usr/bin/env python3
"""Summarize validation evidence from research outcomes and shadow trades."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSONL {path}:{line_number}: {exc}") from exc
    return rows


def numeric(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def score_bucket(score: Any) -> str:
    value = numeric(score)
    if value is None:
        return "missing"
    lower = int(value // 5) * 5
    upper = lower + 4
    return f"{lower:02d}-{upper:02d}"


def mean(values: list[float]) -> float | None:
    return statistics.fmean(values) if values else None


def percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * pct
    lower = int(rank)
    upper = min(lower + 1, len(ordered) - 1)
    weight = rank - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def summarize_group(rows: list[dict[str, Any]], field: str) -> dict[str, Any]:
    values = [value for row in rows if (value := numeric(row.get(field))) is not None]
    return {
        "count": len(rows),
        "observed_count": len(values),
        "average": mean(values),
        "median": statistics.median(values) if values else None,
    }


def outcome_by_research_id(outcomes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in outcomes:
        research_id = row.get("research_id")
        if research_id is not None:
            result[str(research_id)] = row
    return result


def joined_research_rows(research: list[dict[str, Any]], outcomes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    outcome_lookup = outcome_by_research_id(outcomes)
    joined: list[dict[str, Any]] = []
    for row in research:
        merged = dict(row)
        outcome = outcome_lookup.get(str(row.get("research_id")), {})
        for key, value in outcome.items():
            merged.setdefault(key, value)
        joined.append(merged)
    return joined


def summarize_score_buckets(rows: list[dict[str, Any]]) -> dict[str, Any]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[score_bucket(row.get("research_score"))].append(row)
    return {
        bucket: {
            "forward_30d_return": summarize_group(bucket_rows, "forward_30d_return"),
            "forward_vs_spy_30d": summarize_group(bucket_rows, "forward_vs_spy_30d"),
            "forward_vs_qqq_30d": summarize_group(bucket_rows, "forward_vs_qqq_30d"),
        }
        for bucket, bucket_rows in sorted(buckets.items())
    }


def summarize_score_distribution(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scores = [score for row in rows if (score := numeric(row.get("research_score"))) is not None]
    tier_1_threshold = 85
    tier_2_threshold = 75
    highest = max(scores) if scores else None
    p95 = percentile(scores, 0.95)
    p90 = percentile(scores, 0.90)
    warning = None
    if scores and highest is not None and highest < tier_1_threshold:
        warning = "highest_score_below_tier_1_threshold"
    return {
        "scored_count": len(scores),
        "highest": highest,
        "percentile_95": p95,
        "percentile_90": p90,
        "median": statistics.median(scores) if scores else None,
        "tier_1_threshold": tier_1_threshold,
        "tier_2_threshold": tier_2_threshold,
        "tier_1_count": sum(1 for score in scores if score >= tier_1_threshold),
        "tier_2_count": sum(1 for score in scores if tier_2_threshold <= score < tier_1_threshold),
        "calibration_warning": warning,
    }


def summarize_scanners(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scanners: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        for scanner in row.get("scanner_sources") or ["missing"]:
            scanners[str(scanner)].append(row)
    return {
        scanner: {
            "forward_30d_return": summarize_group(scanner_rows, "forward_30d_return"),
            "forward_vs_spy_30d": summarize_group(scanner_rows, "forward_vs_spy_30d"),
        }
        for scanner, scanner_rows in sorted(scanners.items())
    }


def summarize_options_lift(rows: list[dict[str, Any]]) -> dict[str, Any]:
    confirmed: list[dict[str, Any]] = []
    unconfirmed: list[dict[str, Any]] = []
    for row in rows:
        signals = row.get("scanner_signals") or {}
        if signals.get("momentum"):
            if signals.get("options_activity"):
                confirmed.append(row)
            else:
                unconfirmed.append(row)
    confirmed_avg = summarize_group(confirmed, "forward_vs_spy_30d")
    unconfirmed_avg = summarize_group(unconfirmed, "forward_vs_spy_30d")
    lift = None
    if confirmed_avg["average"] is not None and unconfirmed_avg["average"] is not None:
        lift = confirmed_avg["average"] - unconfirmed_avg["average"]
    return {
        "confirmed_momentum": confirmed_avg,
        "unconfirmed_momentum": unconfirmed_avg,
        "alpha_lift": lift,
    }


def infer_primary_blocking_rule(row: dict[str, Any]) -> str:
    explicit = row.get("primary_blocking_rule")
    if explicit:
        return str(explicit)
    text = " ".join(
        str(value or "")
        for value in [
            row.get("blocked_reason"),
            row.get("entry_eligibility"),
            row.get("pipeline_status"),
            row.get("eligibility"),
        ]
    ).lower()
    if any(term in text for term in ["penny", "microcap", "otc", "tradability", "unsupported", "critical data"]):
        return "permanent_rejection_filter"
    if "earning" in text or "report" in text:
        return "blocked_by_earnings"
    if any(term in text for term in ["buying power", "account", "kill", "drawdown", "open order"]):
        return "blocked_by_account_risk"
    if any(term in text for term in ["correlation", "concentration", "exposure"]):
        return "blocked_by_concentration"
    if "market" in text and "regime" in text:
        return "blocked_by_market_regime"
    if any(term in text for term in ["trend", "relative strength", "rs "]):
        return "blocked_by_trend"
    if "extension" in text or "extended" in text:
        return "blocked_by_extension"
    if "watchlist" in text or "outside" in text:
        return "watchlist_or_outside_universe"
    if "tier 2 requires" in text or "approval" in text:
        return "legacy_tier_2_approval_deadlock"
    if any(term in text for term in ["score", "confidence", "completeness", "threshold"]):
        return "insufficient_score_or_confidence"
    return str(row.get("blocked_reason") or row.get("entry_eligibility") or row.get("pipeline_status") or "missing")


def summarize_blocked_candidates(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        status = str(row.get("pipeline_status") or row.get("eligibility") or "")
        reason = infer_primary_blocking_rule(row)
        if "block" in status or "reject" in status or reason not in {"eligible", "missing", None}:
            groups[str(reason)].append(row)
    return {
        reason: {
            "forward_5d_return": summarize_group(group_rows, "forward_5d_return"),
            "forward_10d_return": summarize_group(group_rows, "forward_10d_return"),
            "forward_20d_return": summarize_group(group_rows, "forward_20d_return"),
            "forward_vs_spy_20d": summarize_group(group_rows, "forward_vs_spy_20d"),
            "mfe_20d": summarize_group(group_rows, "max_favorable_excursion_20d"),
            "mae_20d": summarize_group(group_rows, "max_adverse_excursion_20d"),
        }
        for reason, group_rows in sorted(groups.items())
    }


def summarize_shadow(shadow_rows: list[dict[str, Any]]) -> dict[str, Any]:
    returns = [value for row in shadow_rows if (value := numeric(row.get("pnl_pct"))) is not None]
    r_multiples = [value for row in shadow_rows if (value := numeric(row.get("r_multiple"))) is not None]
    return {
        "count": len(shadow_rows),
        "closed_count": len(returns),
        "average_pnl_pct": mean(returns),
        "median_pnl_pct": statistics.median(returns) if returns else None,
        "average_r_multiple": mean(r_multiples),
        "positive_rate": (sum(1 for value in returns if value > 0) / len(returns)) if returns else None,
    }


def build_report(month: str | None) -> dict[str, Any]:
    research = []
    outcomes = []
    shadow = []
    for path in sorted((ROOT / "data/research_records").glob("*.jsonl")):
        research.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/signal_outcomes").glob("*.jsonl")):
        outcomes.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/shadow_trades").glob("*.jsonl")):
        shadow.extend(read_jsonl(path))

    if month:
        research = [row for row in research if str(row.get("date", "")).startswith(month)]
        outcomes = [row for row in outcomes if str(row.get("signal_date", "")).startswith(month)]
        shadow = [row for row in shadow if str(row.get("setup_date", "")).startswith(month)]

    joined = joined_research_rows(research, outcomes)
    observed_30d = sum(1 for row in joined if numeric(row.get("forward_30d_return")) is not None)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "month_filter": month,
        "sample_health": {
            "research_records": len(research),
            "signal_outcomes": len(outcomes),
            "joined_records": len(joined),
            "observed_30d_outcomes": observed_30d,
            "conclusion_quality": "directional" if observed_30d < 20 else "usable",
        },
        "score_distribution": summarize_score_distribution(joined),
        "score_buckets": summarize_score_buckets(joined),
        "scanner_sources": summarize_scanners(joined),
        "options_confirmation_lift": summarize_options_lift(joined),
        "blocked_candidate_opportunity_cost": summarize_blocked_candidates(joined),
        "shadow_portfolio": summarize_shadow(shadow),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", help="Optional YYYY-MM filter.")
    parser.add_argument("--output", help="Optional JSON output path.")
    args = parser.parse_args()

    report = build_report(args.month)
    text = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = ROOT / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {output_path}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
