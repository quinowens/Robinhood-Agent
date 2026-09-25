#!/usr/bin/env python3
"""Mark pre-component-status option outcomes without changing economic data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HORIZONS = (1, 5, 10, 20, 30)
COMPONENTS = ("underlying", "option", "spy", "qqq")
LEGACY_COMPONENT_SCHEMA_VERSION = "pre-v2.0.2-component-status"
CURRENT_NULLABLE_FIELDS = ("terminal_state", "terminal_value", "valuation_method")


def has_complete_component_schema(row: dict[str, Any]) -> bool:
    return all(
        f"forward_{horizon}d_{component}_status" in row
        for horizon in HORIZONS
        for component in COMPONENTS
    ) and all(
        isinstance(row.get(f"forward_{horizon}d_observation"), dict)
        and "target_observation_date" in row[f"forward_{horizon}d_observation"]
        and "component_resolutions" in row[f"forward_{horizon}d_observation"]
        for horizon in HORIZONS
    )


def migrate_row(row: dict[str, Any]) -> bool:
    if has_complete_component_schema(row):
        changed = False
        for field in CURRENT_NULLABLE_FIELDS:
            if field not in row:
                row[field] = None
                changed = True
        return changed
    if row.get("legacy_component_schema") is True and row.get("component_schema_version") == LEGACY_COMPONENT_SCHEMA_VERSION:
        return False
    row["legacy_component_schema"] = True
    row["component_schema_version"] = LEGACY_COMPONENT_SCHEMA_VERSION
    return True


def migrate(paths: list[Path], *, dry_run: bool = False) -> dict[str, Any]:
    files_updated = 0
    records_updated = 0
    for path in paths:
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        changed = sum(1 for row in rows if migrate_row(row))
        if not changed:
            continue
        files_updated += 1
        records_updated += changed
        if not dry_run:
            path.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")
    return {"dry_run": dry_run, "files_updated": files_updated, "records_updated": records_updated}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    paths = args.paths or sorted((ROOT / "data/option_signal_outcomes").glob("*.jsonl"))
    paths = [path if path.is_absolute() else ROOT / path for path in paths]
    print(json.dumps(migrate(paths, dry_run=args.dry_run), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
