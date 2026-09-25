#!/usr/bin/env python3
"""Deterministically add v2.0.2 join IDs without changing economic data."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")


def stable_id(kind: str, path: Path, line_number: int, row: dict[str, Any]) -> str:
    day = str(row.get("signal_date") or row.get("date") or row.get("timestamp") or "unknown")[:10]
    symbol = str(row.get("underlying") or row.get("ticker") or "unknown").upper()
    seed = f"{path.relative_to(ROOT)}:{line_number}:{day}:{symbol}"
    digest = hashlib.sha256(seed.encode()).hexdigest()[:12]
    return f"legacy-{kind}-{day}-{symbol}-{digest}"


def existing_id(row: dict[str, Any], keys: tuple[str, ...]) -> str | None:
    return next((str(row[key]) for key in keys if row.get(key)), None)


def merge_defaults(target: dict[str, Any], defaults: dict[str, Any]) -> None:
    for key, value in defaults.items():
        if key not in target:
            target[key] = copy.deepcopy(value)
        elif isinstance(value, dict) and isinstance(target.get(key), dict):
            merge_defaults(target[key], value)


def migrate(dry_run: bool = False) -> dict[str, Any]:
    setup_paths = sorted((ROOT / "data/options_setup_records").glob("*.jsonl"))
    shadow_paths = sorted((ROOT / "data/option_shadow_trades").glob("*.jsonl"))
    outcome_paths = sorted((ROOT / "data/option_signal_outcomes").glob("*.jsonl"))
    research_paths = sorted((ROOT / "data/research_records").glob("*.jsonl"))

    research_by_day_symbol: dict[tuple[str, str], str] = {}
    for path in research_paths:
        for line_number, row in enumerate(read_jsonl(path), 1):
            day = str(row.get("signal_date") or row.get("date") or row.get("timestamp") or "")[:10]
            symbol = str(row.get("underlying") or row.get("ticker") or "").upper()
            rid = existing_id(row, ("research_record_id", "research_id")) or stable_id("research", path, line_number, row)
            if day and symbol:
                research_by_day_symbol[(day, symbol)] = rid

    shadow_by_setup: dict[str, str] = {}
    for path in shadow_paths:
        for line_number, row in enumerate(read_jsonl(path), 1):
            setup_id = row.get("option_setup_id")
            rid = existing_id(row, ("shadow_trade_id", "option_shadow_trade_id")) or stable_id("shadow", path, line_number, row)
            if setup_id and row.get("is_canonical", True) is not False:
                shadow_by_setup[str(setup_id)] = rid

    outcome_by_setup: dict[str, str] = {}
    for path in outcome_paths:
        for line_number, row in enumerate(read_jsonl(path), 1):
            setup_id = row.get("option_setup_id")
            rid = existing_id(row, ("outcome_record_id", "option_signal_outcome_id", "outcome_id")) or stable_id("outcome", path, line_number, row)
            if setup_id and row.get("is_canonical", True) is not False:
                outcome_by_setup[str(setup_id)] = rid

    outcome_template = json.loads((ROOT / "templates/option_signal_outcome.json").read_text(encoding="utf-8"))
    counts = {"research": 0, "setups": 0, "shadows": 0, "outcomes": 0, "manifests": 0}

    def update_paths(paths: list[Path], kind: str) -> None:
        for path in paths:
            rows = read_jsonl(path)
            changed = False
            for line_number, row in enumerate(rows, 1):
                before = dict(row)
                if kind == "research":
                    row.setdefault("research_record_id", existing_id(row, ("research_id",)) or stable_id("research", path, line_number, row))
                elif kind == "setup":
                    setup_id = existing_id(row, ("options_setup_id", "option_setup_id")) or stable_id("setup", path, line_number, row)
                    row.setdefault("options_setup_id", setup_id)
                    day = str(row.get("signal_date") or row.get("date") or row.get("timestamp") or row.get("created_at") or "")[:10]
                    symbol = str(row.get("underlying") or row.get("ticker") or "").upper()
                    migrated_research_id = research_by_day_symbol.get((day, symbol))
                    if migrated_research_id:
                        row["research_record_id"] = migrated_research_id
                    elif row.get("research_id"):
                        row.setdefault("research_record_id", row["research_id"])
                    if setup_id in shadow_by_setup:
                        row.setdefault("shadow_trade_id", shadow_by_setup[setup_id])
                    if setup_id in outcome_by_setup:
                        row.setdefault("outcome_record_id", outcome_by_setup[setup_id])
                elif kind == "shadow":
                    row.setdefault("shadow_trade_id", existing_id(row, ("option_shadow_trade_id",)) or stable_id("shadow", path, line_number, row))
                elif kind == "outcome":
                    row.setdefault("outcome_record_id", existing_id(row, ("option_signal_outcome_id", "outcome_id")) or stable_id("outcome", path, line_number, row))
                    if str(row.get("strategy_version") or "") >= "2.0.2":
                        merge_defaults(row, outcome_template)
                row.setdefault("legacy_schema", str(row.get("strategy_version") or "") < "2.0.2")
                row.setdefault("id_migration_version", "2.0.2")
                if row != before:
                    counts[kind + "s" if kind != "research" else "research"] += 1
                    changed = True
            if changed and not dry_run:
                write_jsonl(path, rows)

    update_paths(research_paths, "research")
    update_paths(shadow_paths, "shadow")
    update_paths(outcome_paths, "outcome")
    update_paths(setup_paths, "setup")
    # Manifest references are bookkeeping, not economic observations, and can
    # be deterministically reconstructed from each setup's run_id.
    setup_ids_by_run: dict[str, list[str]] = {}
    for path in setup_paths:
        for row in read_jsonl(path):
            setup_id = row.get("option_setup_id") or row.get("options_setup_id")
            if row.get("run_id") and setup_id:
                setup_ids_by_run.setdefault(str(row["run_id"]), []).append(str(setup_id))
    for path in sorted((ROOT / "data/run_manifests").glob("*.json")):
        manifest = json.loads(path.read_text(encoding="utf-8"))
        run_id = str(manifest.get("run_id") or "")
        expected = sorted(set(setup_ids_by_run.get(run_id, [])))
        if not expected:
            continue
        artifact_ids = manifest.setdefault("artifact_ids", {})
        current = sorted(set(str(value) for value in artifact_ids.get("options_setup_ids", [])))
        merged = sorted(set(current + expected))
        if merged != current:
            artifact_ids["options_setup_ids"] = merged
            manifest.setdefault("migration_warnings", []).append("options_setup_ids deterministically backfilled by migrate_v202_ids.py")
            counts["manifests"] += 1
            if not dry_run:
                path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {"dry_run": dry_run, "updated_records": counts}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(json.dumps(migrate(args.dry_run), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
