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


def first_date_value(row: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = row.get(key)
        if value:
            return str(value)
    return ""


def outcome_by_research_id(outcomes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in outcomes:
        research_id = row.get("research_id")
        if research_id is not None:
            result[str(research_id)] = row
    return result


def is_canonical(row: dict[str, Any]) -> bool:
    value = row.get("is_canonical")
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() not in {"false", "0", "no"}


def canonical_signal_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return rows that represent independent signals for analytics.

    Reruns and repair records are preserved in the raw JSONL files, but they
    must not create extra observations in win rates, returns, or funding stats.
    """
    canonical_rows = [row for row in rows if is_canonical(row)]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    ungrouped: list[dict[str, Any]] = []
    for row in canonical_rows:
        group_id = row.get("signal_group_id")
        if group_id:
            grouped[str(group_id)].append(row)
        else:
            ungrouped.append(row)

    result = list(ungrouped)
    for group_rows in grouped.values():
        result.append(
            sorted(
                group_rows,
                key=lambda row: str(row.get("created_at") or row.get("timestamp") or row.get("entry_snapshot_at") or ""),
            )[0]
        )
    return result


def canonical_setup_ids(rows: list[dict[str, Any]]) -> set[str]:
    return {str(row["option_setup_id"]) for row in rows if row.get("option_setup_id") is not None}


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
    if "tier 2 requires" in text or "approval" in text or "eligible_for_pm_review" in text:
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
    returns = [
        value
        for row in shadow_rows
        if (value := numeric(
            row.get("pnl_pct")
            or row.get("theoretical_option_return")
            or row.get("forward_30d_option_return")
            or row.get("forward_20d_option_return")
            or row.get("forward_10d_option_return")
            or row.get("forward_5d_option_return")
            or row.get("forward_1d_option_return")
        )) is not None
    ]
    r_multiples = [value for row in shadow_rows if (value := numeric(row.get("r_multiple"))) is not None]
    return {
        "count": len(shadow_rows),
        "observed_count": len(returns),
        "closed_count": sum(numeric(row.get("forward_30d_option_return")) is not None for row in shadow_rows),
        "average_pnl_pct": mean(returns),
        "median_pnl_pct": statistics.median(returns) if returns else None,
        "average_r_multiple": mean(r_multiples),
        "positive_rate": (sum(1 for value in returns if value > 0) / len(returns)) if returns else None,
    }


def summarize_funding_requirements(setups: list[dict[str, Any]]) -> dict[str, Any]:
    qualified = [
        row
        for row in setups
        if str(row.get("setup_quality_status") or "").upper() == "QUALIFIED"
    ]
    account_fit_failures = [
        row
        for row in qualified
        if str(row.get("account_fit_status") or "").upper() == "FAIL"
        or str(row.get("final_decision") or "").upper() == "SHADOW_ONLY_QUALIFIED"
    ]
    premiums = [
        value
        for row in qualified
        if (value := numeric(row.get("premium_allocation_dollars") or row.get("max_contractual_loss_dollars"))) is not None
    ]
    failed_premiums = [
        value
        for row in account_fit_failures
        if (value := numeric(row.get("premium_allocation_dollars") or row.get("max_contractual_loss_dollars"))) is not None
    ]
    planned_risks = [
        value
        for row in qualified
        if (value := numeric(row.get("planned_trade_risk_dollars"))) is not None
    ]
    failed_planned_risks = [
        value
        for row in account_fit_failures
        if (value := numeric(row.get("planned_trade_risk_dollars"))) is not None
    ]
    premium_caps = [
        value
        for row in qualified
        if (value := numeric(row.get("max_premium_allocation_pct_account"))) is not None and value > 0
    ]
    planned_risk_caps = [
        value
        for row in qualified
        if (value := numeric(row.get("max_planned_trade_risk_pct_account"))) is not None and value > 0
    ]
    premium_cap = statistics.median(premium_caps) if premium_caps else 0.10
    planned_risk_cap = statistics.median(planned_risk_caps) if planned_risk_caps else 0.01
    median_premium = statistics.median(premiums) if premiums else None
    p75_premium = percentile(premiums, 0.75)
    median_failed_premium = statistics.median(failed_premiums) if failed_premiums else None
    p75_failed_premium = percentile(failed_premiums, 0.75)
    median_planned_risk = statistics.median(planned_risks) if planned_risks else None
    p75_planned_risk = percentile(planned_risks, 0.75)
    median_failed_planned_risk = statistics.median(failed_planned_risks) if failed_planned_risks else None
    p75_failed_planned_risk = percentile(failed_planned_risks, 0.75)

    def required_account_size(amount: float | None, cap: float) -> float | None:
        if amount is None or cap <= 0:
            return None
        return amount / cap

    return {
        "qualified_setup_count": len(qualified),
        "account_fit_failure_count": len(account_fit_failures),
        "account_fit_failure_pct": (len(account_fit_failures) / len(qualified)) if qualified else None,
        "preferred_contract_premium": {
            "median_all_qualified": median_premium,
            "percentile_75_all_qualified": p75_premium,
            "median_account_fit_failures": median_failed_premium,
            "percentile_75_account_fit_failures": p75_failed_premium,
        },
        "planned_trade_risk": {
            "median_all_qualified": median_planned_risk,
            "percentile_75_all_qualified": p75_planned_risk,
            "median_account_fit_failures": median_failed_planned_risk,
            "percentile_75_account_fit_failures": p75_failed_planned_risk,
        },
        "assumed_caps": {
            "premium_allocation_pct_account": premium_cap,
            "planned_trade_risk_pct_account": planned_risk_cap,
        },
        "estimated_account_size_needed": {
            "median_premium_at_premium_cap": required_account_size(median_premium, premium_cap),
            "p75_premium_at_premium_cap": required_account_size(p75_premium, premium_cap),
            "median_failed_premium_at_premium_cap": required_account_size(median_failed_premium, premium_cap),
            "p75_failed_premium_at_premium_cap": required_account_size(p75_failed_premium, premium_cap),
            "median_planned_risk_at_planned_risk_cap": required_account_size(median_planned_risk, planned_risk_cap),
            "p75_planned_risk_at_planned_risk_cap": required_account_size(p75_planned_risk, planned_risk_cap),
            "median_failed_planned_risk_at_planned_risk_cap": required_account_size(median_failed_planned_risk, planned_risk_cap),
            "p75_failed_planned_risk_at_planned_risk_cap": required_account_size(p75_failed_planned_risk, planned_risk_cap),
        },
    }


def bucket_dte(value: Any) -> str:
    dte = numeric(value)
    if dte is None:
        return "missing"
    if dte < 30:
        return "under_30"
    if dte <= 45:
        return "30_45"
    if dte <= 60:
        return "46_60"
    if dte <= 90:
        return "61_90"
    return "over_90"


def bucket_delta(value: Any) -> str:
    delta = numeric(value)
    if delta is None:
        return "missing"
    absolute = abs(delta)
    if absolute < 0.35:
        return "under_035"
    if absolute <= 0.50:
        return "035_050"
    if absolute <= 0.70:
        return "051_070"
    return "over_070"


def summarize_option_setups(setups: list[dict[str, Any]], outcomes: list[dict[str, Any]], shadows: list[dict[str, Any]]) -> dict[str, Any]:
    canonical_setups = canonical_signal_rows(setups)
    canonical_ids = canonical_setup_ids(canonical_setups)
    canonical_outcomes = [
        row
        for row in outcomes
        if row.get("option_setup_id") is None or str(row.get("option_setup_id")) in canonical_ids
    ]
    canonical_shadows = [
        row
        for row in shadows
        if row.get("option_setup_id") is None or str(row.get("option_setup_id")) in canonical_ids
    ]
    outcome_lookup = {str(row.get("option_setup_id")): row for row in canonical_outcomes if row.get("option_setup_id") is not None}
    joined: list[dict[str, Any]] = []
    for row in canonical_setups:
        merged = dict(row)
        outcome = outcome_lookup.get(str(row.get("option_setup_id")), {})
        for key, value in outcome.items():
            if key not in merged or merged[key] is None:
                merged[key] = value
        joined.append(merged)

    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_dte: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_delta: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_score: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_block: dict[str, list[dict[str, Any]]] = defaultdict(list)
    classifications: dict[str, int] = defaultdict(int)
    setup_quality: dict[str, int] = defaultdict(int)
    account_fit: dict[str, int] = defaultdict(int)
    final_decisions: dict[str, int] = defaultdict(int)
    account_fit_failures_by_reason: dict[str, int] = defaultdict(int)
    shadow_conversion: dict[str, int] = defaultdict(int)
    for row in joined:
        by_type[str(row.get("option_type") or "missing")].append(row)
        by_dte[bucket_dte(row.get("dte") or row.get("dte_at_signal"))].append(row)
        by_delta[bucket_delta(row.get("delta"))].append(row)
        by_score[score_bucket(row.get("options_setup_score"))].append(row)
        block = row.get("primary_blocking_rule")
        if block:
            by_block[str(block)].append(row)
        classifications[str(row.get("outcome_classification") or "unobserved")] += 1
        setup_quality[str(row.get("setup_quality_status") or "missing")] += 1
        account_fit[str(row.get("account_fit_status") or "missing")] += 1
        final_decision = str(row.get("final_decision") or row.get("decision") or "missing")
        final_decisions[final_decision] += 1
        if str(row.get("account_fit_status") or "").upper() == "FAIL":
            reasons = row.get("account_fit_reasons") or [row.get("primary_blocking_rule") or "missing"]
            for reason in reasons:
                account_fit_failures_by_reason[str(reason)] += 1
        if str(row.get("setup_quality_status") or "").upper() == "QUALIFIED":
            if str(row.get("account_fit_status") or "").upper() == "PASS":
                shadow_conversion["qualified_account_fit_pass"] += 1
            elif str(row.get("account_fit_status") or "").upper() == "FAIL":
                shadow_conversion["qualified_account_fit_fail"] += 1
            else:
                shadow_conversion["qualified_account_fit_missing"] += 1

    return {
        "setup_records": len(canonical_setups),
        "raw_setup_records": len(setups),
        "noncanonical_setup_records": len(setups) - len(canonical_setups),
        "outcome_records": len(canonical_outcomes),
        "raw_outcome_records": len(outcomes),
        "shadow_trades": summarize_shadow(canonical_shadows),
        "raw_shadow_trade_records": len(shadows),
        "funding_requirements": summarize_funding_requirements(canonical_setups),
        "setup_quality_status": dict(sorted(setup_quality.items())),
        "account_fit_status": dict(sorted(account_fit.items())),
        "final_decisions": dict(sorted(final_decisions.items())),
        "account_fit_failures_by_reason": dict(sorted(account_fit_failures_by_reason.items())),
        "pipeline_conversion": dict(sorted(shadow_conversion.items())),
        "outcome_maturation": {
            f"{horizon}D": {
                "eligible_records": len(canonical_outcomes),
                "observed_option_returns": sum(numeric(row.get(f"option_forward_{horizon}d_return")) is not None for row in canonical_outcomes),
                "observed_underlying_returns": sum(numeric(row.get(f"underlying_forward_{horizon}d_return")) is not None for row in canonical_outcomes),
            }
            for horizon in (1, 5, 10, 20, 30)
        },
        "by_option_type": {key: summarize_group(rows, "option_forward_20d_return") for key, rows in sorted(by_type.items())},
        "by_dte_bucket": {key: summarize_group(rows, "option_forward_20d_return") for key, rows in sorted(by_dte.items())},
        "by_delta_bucket": {key: summarize_group(rows, "option_forward_20d_return") for key, rows in sorted(by_delta.items())},
        "by_options_setup_score_bucket": {key: summarize_group(rows, "option_forward_20d_return") for key, rows in sorted(by_score.items())},
        "by_primary_blocking_rule": {key: summarize_group(rows, "option_forward_20d_return") for key, rows in sorted(by_block.items())},
        "outcome_classifications": dict(sorted(classifications.items())),
    }


def build_report(month: str | None) -> dict[str, Any]:
    research = []
    outcomes = []
    shadow = []
    option_setups = []
    option_outcomes = []
    option_shadow = []
    for path in sorted((ROOT / "data/research_records").glob("*.jsonl")):
        research.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/signal_outcomes").glob("*.jsonl")):
        outcomes.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/shadow_trades").glob("*.jsonl")):
        shadow.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/options_setup_records").glob("*.jsonl")):
        option_setups.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/option_signal_outcomes").glob("*.jsonl")):
        option_outcomes.extend(read_jsonl(path))
    for path in sorted((ROOT / "data/option_shadow_trades").glob("*.jsonl")):
        option_shadow.extend(read_jsonl(path))

    if month:
        research = [row for row in research if str(row.get("date", "")).startswith(month)]
        outcomes = [row for row in outcomes if str(row.get("signal_date", "")).startswith(month)]
        shadow = [row for row in shadow if str(row.get("setup_date", "")).startswith(month)]
        option_setups = [
            row
            for row in option_setups
            if first_date_value(row, ["date", "timestamp", "created_at", "signal_date"]).startswith(month)
        ]
        option_outcomes = [
            row
            for row in option_outcomes
            if first_date_value(row, ["signal_date", "date", "entry_date", "created_at"]).startswith(month)
        ]
        option_shadow = [
            row
            for row in option_shadow
            if first_date_value(row, ["entry_date", "date", "created_at", "entry_snapshot_at"]).startswith(month)
        ]

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
        "options_strategy": summarize_option_setups(option_setups, option_outcomes, option_shadow),
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
