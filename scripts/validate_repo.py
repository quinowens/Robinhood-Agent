#!/usr/bin/env python3
"""Repository validation checks for the Robinhood Agent project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "PRIVATE_DATA.md",
    "tool_policy.md",
    "system_prompt.md",
    "pipeline_config.md",
    "scanner_engine.md",
    "research_agent.md",
    "portfolio_manager_agent.md",
    "universe.md",
    "performance_metrics.md",
    "strategy.md",
    "options_strategy.md",
    "state/current_universe.json",
    "state/open_theses.json",
    "state/rejected_candidates.json",
    "templates/daily_research_log.md",
    "templates/raw_scanner_snapshot.json",
    "templates/research_record.json",
    "templates/signal_outcome.json",
    "templates/shadow_trade.json",
    "templates/options_setup_record.json",
    "templates/option_shadow_trade.json",
    "templates/option_signal_outcome.json",
    "templates/market_regime_snapshot.json",
    "templates/universe_run_manifest.json",
    "docs/VALIDATION_RELEASE.md",
]

REQUIRED_DIRS = [
    "data/options_setup_records",
    "data/option_shadow_trades",
    "data/option_signal_outcomes",
]

DAILY_LOG_REQUIRED_SECTIONS = [
    "## Executive Decision",
    "## Market",
    "## Scanner Summary",
    "## Run Health",
    "## Blocked",
    "## Portfolio Manager",
]

STRICT_DAILY_LOG_START = "2026-08-03"

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|password|token|access[_-]?key|refresh[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"),
    re.compile(r"(?i)authorization\s*[:=]\s*['\"]?bearer\s+[A-Za-z0-9_./+=-]{16,}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", "dist", "build", "coverage"}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonl", ".py", ".yml", ".yaml", ".toml", ".ini", ".cfg", ".env", ".example", ""}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_required_files(errors: list[str]) -> None:
    for file_name in REQUIRED_FILES:
        if not (ROOT / file_name).is_file():
            fail(errors, f"missing required file: {file_name}")
    for dir_name in REQUIRED_DIRS:
        if not (ROOT / dir_name).is_dir():
            fail(errors, f"missing required directory: {dir_name}")


def read_text_file(file_name: str) -> str:
    return (ROOT / file_name).read_text(encoding="utf-8")


def check_v2_options_invariants(errors: list[str]) -> None:
    core = "\n".join(
        read_text_file(file_name)
        for file_name in [
            "README.md",
            "system_prompt.md",
            "strategy.md",
            "options_strategy.md",
            "pipeline_config.md",
            "portfolio_manager_agent.md",
            "performance_metrics.md",
        ]
    )
    lower = core.lower()
    required_phrases = [
        "version 2.0",
        "options-primary",
        "long calls",
        "long puts",
        "underlying thesis score",
        "options setup score",
        "options data completeness",
        "options decision confidence",
        "exact reviewed order",
        "no autonomous",
        "0dte",
        "naked short calls",
        "naked short puts",
    ]
    for phrase in required_phrases:
        if phrase not in lower:
            fail(errors, f"missing v2.0 invariant phrase: {phrase}")

    if "current universe" not in lower or "underlying" not in lower:
        fail(errors, "Current Universe / underlying relationship is not documented")

    pipeline = read_text_file("pipeline_config.md")
    for step in [
        "classify_directional_thesis",
        "evaluate_options_suitability",
        "pull_option_chains_for_qualified_finalists",
        "rank_option_contracts",
        "calculate_options_setup_score",
        "evaluate_account_fit",
        "record_option_shadow_trade_when_qualified",
        "schedule_option_outcome_tracking",
    ]:
        if step not in pipeline:
            fail(errors, f"missing options pipeline step: {step}")

    options_setup = json.loads(read_text_file("templates/options_setup_record.json"))
    for field in [
        "underlying_research_score",
        "options_setup_score",
        "options_data_completeness",
        "options_decision_confidence",
        "account_fit_status",
        "primary_blocking_rule",
    ]:
        if field not in options_setup:
            fail(errors, f"options setup template missing field: {field}")

    universe = json.loads(read_text_file("state/current_universe.json"))
    for contract_key in ["expiration", "strike", "option_type", "contract"]:
        if contract_key in universe:
            fail(errors, f"Current Universe must not store option contracts: {contract_key}")


def check_json(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("state/*.json")):
        parse_json_file(path, errors)
    for path in sorted(ROOT.glob("data/run_manifests/*.json")):
        parse_json_file(path, errors)
    for path in sorted(ROOT.glob("data/market_regime/*.json")):
        parse_json_file(path, errors)
    for path in sorted(ROOT.glob("data/validation_reports/*.json")):
        parse_json_file(path, errors)
    for path in sorted(ROOT.glob("backtests/*.json")):
        parse_json_file(path, errors)


def parse_json_file(path: Path, errors: list[str]) -> None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except Exception as exc:  # noqa: BLE001
        fail(errors, f"invalid JSON: {rel(path)}: {exc}")


def check_jsonl(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("data/**/*.jsonl")):
        try:
            with path.open("r", encoding="utf-8") as handle:
                for line_number, line in enumerate(handle, 1):
                    if line.strip():
                        json.loads(line)
        except Exception as exc:  # noqa: BLE001
            fail(errors, f"invalid JSONL: {rel(path)}:{line_number}: {exc}")


def check_daily_logs(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("research_logs/*daily-scanner-dry-run.md")):
        text = path.read_text(encoding="utf-8")
        log_date = path.name[:10]
        if log_date >= STRICT_DAILY_LOG_START:
            missing = [section for section in DAILY_LOG_REQUIRED_SECTIONS if section not in text]
            if missing:
                fail(errors, f"daily log missing sections: {rel(path)}: {', '.join(missing)}")
        if "No orders" not in text and "NO TRADE" not in text:
            fail(errors, f"daily log missing no-order / NO TRADE statement: {rel(path)}")


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in {"Makefile", ".gitignore"}:
            paths.append(path)
    return paths


def check_sensitive_strings(errors: list[str]) -> None:
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    fail(errors, f"possible secret: {rel(path)}:{line_number}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-sensitive-only", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []

    if args.scan_sensitive_only:
        check_sensitive_strings(errors)
    else:
        check_required_files(errors)
        check_json(errors)
        check_jsonl(errors)
        check_daily_logs(errors)
        check_v2_options_invariants(errors)
        check_sensitive_strings(errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
