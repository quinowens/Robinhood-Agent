#!/usr/bin/env python3
"""Cross-artifact integrity and outcome-maturation audits for v2.0.2."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

from historical_resolver import trading_day


ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 5, 10, 20, 30)
QUALIFIED_DECISIONS = {"SHADOW_ONLY_QUALIFIED", "PM_PROPOSAL", "QUALIFIED"}
LEDGER_STATUSES = {
    "COMPLETED", "COMPLETED_DEGRADED", "SKIPPED_NON_TRADING_DAY",
    "SKIPPED_SCHEDULE", "FAILED", "MISSING",
}


def canonical(row: dict[str, Any]) -> bool:
    return row.get("canonical", row.get("is_canonical", True)) is not False


def load_jsonl(directory: str) -> list[tuple[Path, int, dict[str, Any]]]:
    result = []
    for path in sorted((ROOT / directory).glob("*.jsonl")):
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if line.strip():
                    result.append((path, line_number, json.loads(line)))
    return result


def load_json(directory: str) -> list[tuple[Path, dict[str, Any]]]:
    return [(path, json.loads(path.read_text(encoding="utf-8"))) for path in sorted((ROOT / directory).glob("*.json"))]


def record_id(row: dict[str, Any], kind: str) -> str | None:
    candidates = {
        "research": ("research_record_id", "research_id"),
        "setup": ("options_setup_id", "option_setup_id"),
        "shadow": ("shadow_trade_id", "option_shadow_trade_id"),
        "outcome": ("outcome_record_id", "option_signal_outcome_id", "outcome_id"),
    }[kind]
    return next((str(row[key]) for key in candidates if row.get(key)), None)


def index(rows: Iterable[tuple[Path, int, dict[str, Any]]], kind: str) -> tuple[dict[str, list[dict[str, Any]]], list[str]]:
    by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    missing = []
    for path, line, row in rows:
        rid = record_id(row, kind)
        if rid:
            by_id[rid].append(row)
        else:
            missing.append(f"{path.relative_to(ROOT)}:{line}")
    return by_id, missing


def parse_day(value: Any) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def matured_day(signal_day: date, horizon: int) -> date:
    return trading_day(signal_day, horizon)


def audit(as_of: date | None = None) -> dict[str, Any]:
    as_of = as_of or date.today()
    research_rows = load_jsonl("data/research_records")
    setup_rows = load_jsonl("data/options_setup_records")
    shadow_rows = load_jsonl("data/option_shadow_trades")
    outcome_rows = load_jsonl("data/option_signal_outcomes")
    manifests = load_json("data/run_manifests")

    research, missing_research_ids = index(research_rows, "research")
    setups, missing_setup_ids = index(setup_rows, "setup")
    shadows, missing_shadow_ids = index(shadow_rows, "shadow")
    outcomes, missing_outcome_ids = index(outcome_rows, "outcome")
    manifest_by_run = {str(row.get("run_id")): row for _, row in manifests if row.get("run_id")}

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    qualified = []
    complete = 0
    referenced_shadow: set[str] = set()
    referenced_outcome: set[str] = set()

    def issue(target: list, code: str, **details: Any) -> None:
        target.append({"code": code, **details})

    for kind, records in (("RESEARCH", research), ("SETUP", setups), ("SHADOW", shadows), ("OUTCOME", outcomes)):
        for rid, rows in records.items():
            canonical_count = sum(canonical(row) for row in rows)
            if canonical_count > 1:
                issue(errors, f"DUPLICATE_CANONICAL_{kind}_ID", record_id=rid, count=canonical_count)

    for setup_id, records in setups.items():
        canon = [row for row in records if canonical(row)]
        for setup in canon:
            decision = str(setup.get("final_decision") or setup.get("decision") or "").upper()
            is_qualified = decision in QUALIFIED_DECISIONS or str(setup.get("setup_quality_status") or "").upper() == "QUALIFIED"
            if not is_qualified:
                continue
            qualified.append(setup)
            missing = []
            research_id = str(setup.get("research_record_id") or setup.get("research_id") or "")
            shadow_id = str(setup.get("shadow_trade_id") or setup.get("option_shadow_trade_id") or "")
            outcome_id = str(setup.get("outcome_record_id") or setup.get("option_signal_outcome_id") or "")
            run_id = str(setup.get("run_id") or "")
            if not research_id or research_id not in research:
                missing.append("underlying_research_record")
            matching_shadows = [r for r in shadows.get(shadow_id, []) if canonical(r)] if shadow_id else []
            if len(matching_shadows) != 1 or matching_shadows[0].get("option_setup_id") != setup_id:
                missing.append("option_shadow_trade")
            else:
                referenced_shadow.add(shadow_id)
            matching_outcomes = [r for r in outcomes.get(outcome_id, []) if canonical(r)] if outcome_id else []
            if len(matching_outcomes) != 1 or matching_outcomes[0].get("option_setup_id") != setup_id:
                missing.append("option_signal_outcome")
            else:
                referenced_outcome.add(outcome_id)
            manifest = manifest_by_run.get(run_id)
            if not manifest:
                missing.append("run_manifest")
            elif setup_id not in set(manifest.get("artifact_ids", {}).get("options_setup_ids", [])):
                issue(warnings, "MANIFEST_MISSING_ARTIFACT_REFERENCE", run_id=run_id, options_setup_id=setup_id)
            if missing:
                issue(errors, "INCOMPLETE_QUALIFIED_CHAIN", options_setup_id=setup_id, run_id=run_id, missing=missing)
            else:
                complete += 1

    for shadow_id, records in shadows.items():
        for row in records:
            if canonical(row) and shadow_id not in referenced_shadow:
                issue(errors, "ORPHANED_SHADOW_TRADE", shadow_trade_id=shadow_id, options_setup_id=row.get("option_setup_id"))
    for outcome_id, records in outcomes.items():
        for row in records:
            if canonical(row) and outcome_id not in referenced_outcome:
                issue(errors, "ORPHANED_OUTCOME", outcome_record_id=outcome_id, options_setup_id=row.get("option_setup_id"))

    overdue = Counter()
    expected = Counter()
    observed = Counter()
    update_failures = 0
    for _, _, row in outcome_rows:
        if not canonical(row):
            continue
        signal_day = parse_day(row.get("signal_date"))
        if not signal_day:
            continue
        for horizon in HORIZONS:
            key = f"option_forward_{horizon}d_return"
            maturity = matured_day(signal_day, horizon)
            status = str(row.get(f"forward_{horizon}d_status") or "PENDING")
            value = row.get(key)
            if maturity <= as_of:
                expected[horizon] += 1
            if value is not None:
                observed[horizon] += 1
            if status == "OBSERVED" and value is None:
                issue(errors, "OBSERVED_STATUS_WITHOUT_VALUE", outcome_record_id=record_id(row, "outcome"), symbol=row.get("underlying"), signal_date=signal_day.isoformat(), horizon=f"{horizon}D", maturity_date=maturity.isoformat(), current_status=status, reason="status is OBSERVED but option return is null")
            if maturity > as_of and value is None:
                continue
            if maturity <= as_of and value is None:
                overdue[horizon] += 1
                if status == "UPDATE_FAILED":
                    update_failures += 1
                observation = row.get(f"forward_{horizon}d_observation") or {}
                issue(warnings, "MATURED_OBSERVATION_MISSING", outcome_record_id=record_id(row, "outcome"), symbol=row.get("underlying"), signal_date=signal_day.isoformat(), horizon=f"{horizon}D", maturity_date=maturity.isoformat(), current_status=status, reason=observation.get("reason") or "updater has not persisted a source-data failure reason")

    unaccounted = 0
    legacy_ledger_rows = 0
    for path, ledger in load_json("data/scheduled_run_ledger"):
        for entry in ledger.get("entries", []):
            raw_status = str(entry.get("status") or "").upper()
            if raw_status not in LEDGER_STATUSES:
                legacy_ledger_rows += 1
            if entry.get("expected", entry.get("expected_session")) and raw_status in {"", "MISSING", "MISSING_RUN_RECORD", "PARTIAL_STRUCTURED_RECORD"}:
                unaccounted += 1

    for location in missing_research_ids + missing_setup_ids + missing_shadow_ids + missing_outcome_ids:
        issue(warnings, "MISSING_EXPLICIT_RECORD_ID", location=location, migration="run scripts/migrate_v202_ids.py")
    if legacy_ledger_rows:
        issue(warnings, "LEGACY_LEDGER_FORMAT_GRANDFATHERED", count=legacy_ledger_rows, reason="pre-v2.0.2 status vocabulary retained as intentional migration history")

    outcome_health = {
        "canonical_outcome_records": sum(canonical(row) for _, _, row in outcome_rows),
        "horizons": {f"{h}D": {"expected": expected[h], "observed": observed[h]} for h in HORIZONS},
        "overdue_outcome_windows": sum(overdue.values()),
        "update_failures": update_failures,
        "status": "DEGRADED" if sum(overdue.values()) else "HEALTHY",
    }

    return {
        "schema_version": "2.0.2",
        "as_of": as_of.isoformat(),
        "status": "FAIL" if errors else ("PASS_WITH_WARNINGS" if warnings else "PASS"),
        "qualified_setups": len(qualified),
        "complete_qualified_chains": complete,
        "orphaned_shadow_records": sum(e["code"] == "ORPHANED_SHADOW_TRADE" for e in errors),
        "orphaned_outcome_records": sum(e["code"] == "ORPHANED_OUTCOME" for e in errors),
        "overdue_outcome_observations": sum(overdue.values()),
        "overdue_by_window": {f"{horizon}D": overdue[horizon] for horizon in HORIZONS},
        "outcome_health": outcome_health,
        "unaccounted_scheduled_runs": unaccounted,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of", type=date.fromisoformat)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args()
    report = audit(args.as_of)
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        path = args.output if args.output.is_absolute() else ROOT / args.output
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(text, end="")
    return int(report["status"] == "FAIL" or (args.strict_warnings and report["warnings"]))


if __name__ == "__main__":
    raise SystemExit(main())
