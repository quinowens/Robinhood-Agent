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
    "state/account_capabilities.json",
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
        "version 2.0.1",
        "options-primary",
        "long calls",
        "long puts",
        "broker capability",
        "strategy permission",
        "underlying thesis score",
        "options setup score",
        "options data completeness",
        "options decision confidence",
        "setup_quality_status",
        "account_fit_status",
        "final_decision",
        "premium_allocation_dollars",
        "options shadow portfolio",
        "shadow_only_qualified",
        "frozen",
        "max_contractual_loss_dollars",
        "planned_trade_risk_dollars",
        "exact reviewed order",
        "no autonomous",
        "0dte",
        "naked short calls",
        "naked short puts",
    ]
    for phrase in required_phrases:
        if phrase not in lower:
            fail(errors, f"missing v2.0 invariant phrase: {phrase}")

    forbidden_phrases = [
        "exact-order approval requirements",
        "before producing any options proposal, confirm",
    ]
    for phrase in forbidden_phrases:
        if phrase in lower:
            fail(errors, f"deprecated v2.0.1 phrase remains: {phrase}")

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
        "signal_group_id",
        "supersedes_setup_id",
        "is_canonical",
        "underlying_research_score",
        "options_setup_score",
        "options_data_completeness",
        "options_decision_confidence",
        "setup_quality_status",
        "account_fit_status",
        "account_fit_reasons",
        "premium_allocation_dollars",
        "premium_allocation_pct_account",
        "max_contractual_loss_dollars",
        "max_contractual_loss_pct_account",
        "planned_trade_risk_dollars",
        "planned_trade_risk_pct_account",
        "account_snapshot_id",
        "account_snapshot_as_of",
        "final_decision",
        "primary_blocking_rule",
        "shadow_tracking_required",
        "shadow_tracking_reason",
        "frozen_entry_snapshot_required",
        "option_shadow_trade_id",
        "option_signal_outcome_id",
    ]:
        if field not in options_setup:
            fail(errors, f"options setup template missing field: {field}")

    option_shadow = json.loads(read_text_file("templates/option_shadow_trade.json"))
    for field in [
        "signal_group_id",
        "supersedes_setup_id",
        "is_canonical",
        "shadow_portfolio",
        "shadow_reason",
        "freeze_rule",
        "entry_snapshot_at",
        "entry_midpoint",
        "entry_open_interest",
        "entry_volume",
        "entry_breakeven",
        "forward_1d_option_return",
        "forward_30d_option_return",
        "forward_1d_underlying_return",
        "forward_30d_underlying_return",
        "forward_30d_vs_spy",
        "forward_30d_vs_qqq",
        "planned_stop_triggered",
        "planned_target_hit",
        "thesis_validity_status",
        "expired_worthless",
        "directional_thesis_result",
        "contract_selection_result",
        "option_vs_underlying_result",
    ]:
        if field not in option_shadow:
            fail(errors, f"option shadow template missing field: {field}")

    option_outcome = json.loads(read_text_file("templates/option_signal_outcome.json"))
    for field in [
        "signal_group_id",
        "supersedes_setup_id",
        "is_canonical",
        "option_shadow_trade_id",
        "shadow_portfolio",
        "entry_snapshot_at",
        "entry_premium",
        "underlying_price_at_entry",
        "underlying_forward_1d_return",
        "option_forward_1d_return",
        "underlying_forward_vs_spy_30d",
        "underlying_forward_vs_qqq_30d",
        "option_mfe_30d",
        "option_mae_30d",
        "planned_stop_triggered",
        "planned_target_hit",
        "thesis_validity_status",
        "expired_worthless",
        "directional_thesis_result",
        "contract_selection_result",
        "option_vs_underlying_result",
    ]:
        if field not in option_outcome:
            fail(errors, f"option outcome template missing field: {field}")

    universe = json.loads(read_text_file("state/current_universe.json"))
    for contract_key in ["expiration", "strike", "option_type", "contract"]:
        if contract_key in universe:
            fail(errors, f"Current Universe must not store option contracts: {contract_key}")

    capabilities = json.loads(read_text_file("state/account_capabilities.json"))
    accounts = capabilities.get("account_capabilities") or []
    if not accounts:
        fail(errors, "account capabilities file has no accounts")
    for account in accounts:
        broker = account.get("broker_options_capabilities") or {}
        strategy = account.get("strategy_options_capabilities") or {}
        enabled = set(strategy.get("enabled_structures") or [])
        if broker.get("options_level") != "level_2":
            fail(errors, "Agentic broker capability must record level_2")
        if not broker.get("buy_calls") or not broker.get("buy_puts"):
            fail(errors, "Agentic broker capability must allow buying calls and puts")
        if broker.get("spreads") is not False:
            fail(errors, "Agentic broker capability must record spreads as unavailable")
        if enabled != {"LONG_CALL", "LONG_PUT"}:
            fail(errors, "strategy enabled options structures must be LONG_CALL and LONG_PUT only")
        for disabled_flag in [
            "covered_calls_enabled",
            "cash_secured_puts_enabled",
            "spreads_enabled",
            "autonomous_live_execution_enabled",
        ]:
            if strategy.get(disabled_flag) is not False:
                fail(errors, f"strategy capability must disable {disabled_flag}")

    check_v201_option_records(errors)
    check_v201_run_manifests(errors)


def parse_jsonl_file(path: Path, errors: list[str]) -> list[tuple[int, dict]]:
    rows: list[tuple[int, dict]] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if line.strip():
                    rows.append((line_number, json.loads(line)))
    except Exception as exc:  # noqa: BLE001
        fail(errors, f"invalid JSONL: {rel(path)}:{line_number}: {exc}")
    return rows


def check_v201_option_records(errors: list[str]) -> None:
    setup_template = json.loads(read_text_file("templates/options_setup_record.json"))
    shadow_template = json.loads(read_text_file("templates/option_shadow_trade.json"))
    outcome_template = json.loads(read_text_file("templates/option_signal_outcome.json"))
    canonical_by_group: dict[str, list[str]] = {}

    for path in sorted((ROOT / "data/options_setup_records").glob("*.jsonl")):
        for line_number, row in parse_jsonl_file(path, errors):
            strategy_version = row.get("strategy_version")
            if strategy_version is None or str(strategy_version) < "2.0.1":
                continue
            setup_quality = str(row.get("setup_quality_status") or "").upper()
            account_fit = str(row.get("account_fit_status") or "").upper()
            final_decision = str(row.get("final_decision") or "").upper()
            where = f"{rel(path)}:{line_number}"
            require_template_fields(errors, row, setup_template, "option setup", where)
            require_non_empty_fields(
                errors,
                row,
                ["option_setup_id", "run_id", "research_id", "timestamp", "underlying", "expiration", "final_decision"],
                "option setup",
                where,
            )
            validate_canonical_fields(errors, row, canonical_by_group, where)
            if setup_quality == "QUALIFIED" and account_fit == "FAIL" and final_decision != "SHADOW_ONLY_QUALIFIED":
                fail(errors, f"qualified account-fit failure must be SHADOW_ONLY_QUALIFIED: {where}")
            if setup_quality == "QUALIFIED" and account_fit == "FAIL":
                blocked_eligibility = {"blocked_by_portfolio", "blocked_by_account", "account_risk"}
                if row.get("underlying_eligibility") in blocked_eligibility:
                    fail(errors, f"account fit must not rewrite underlying eligibility: {where}")
            if row.get("option_type") in {"call", "put"} and row.get("side") == "buy":
                premium = row.get("premium_allocation_dollars")
                max_loss = row.get("max_contractual_loss_dollars")
                planned = row.get("planned_trade_risk_dollars")
                if numeric_equal(premium, max_loss) is False:
                    fail(errors, f"long option max contractual loss must equal premium allocation: {where}")
                if numeric_equal(planned, max_loss) is False:
                    fail(errors, f"current long-option planned trade risk must equal max contractual loss: {where}")
                if row.get("planned_trade_risk_source") != "default_max_contractual_loss":
                    fail(errors, f"current long-option planned risk source must be default_max_contractual_loss: {where}")
            if str(row.get("decision") or "").upper() == "QUALIFIED_BUT_NOT_ACCOUNT_FIT":
                fail(errors, f"deprecated decision written in v2.0.1 record: {where}")

    for group_id, locations in canonical_by_group.items():
        if len(locations) > 1:
            fail(errors, f"multiple canonical option setup records for signal_group_id {group_id}: {', '.join(locations)}")

    for path in sorted((ROOT / "data/option_shadow_trades").glob("*.jsonl")):
        for line_number, row in parse_jsonl_file(path, errors):
            strategy_version = row.get("strategy_version")
            if strategy_version is None or str(strategy_version) < "2.0.1":
                continue
            where = f"{rel(path)}:{line_number}"
            require_template_fields(errors, row, shadow_template, "option shadow trade", where)
            require_non_empty_fields(
                errors,
                row,
                ["option_shadow_trade_id", "option_setup_id", "run_id", "underlying", "entry_snapshot_at", "final_decision"],
                "option shadow trade",
                where,
            )
            validate_canonical_fields(errors, row, {}, where)
            if row.get("option_type") in {"call", "put"}:
                if numeric_equal(row.get("planned_trade_risk_dollars"), row.get("max_contractual_loss_dollars")) is False:
                    fail(errors, f"current option shadow planned trade risk must equal max contractual loss: {where}")
                if row.get("planned_trade_risk_source") != "default_max_contractual_loss":
                    fail(errors, f"current option shadow planned risk source must be default_max_contractual_loss: {where}")

    for path in sorted((ROOT / "data/option_signal_outcomes").glob("*.jsonl")):
        for line_number, row in parse_jsonl_file(path, errors):
            strategy_version = row.get("strategy_version")
            if strategy_version is None or str(strategy_version) < "2.0.1":
                continue
            where = f"{rel(path)}:{line_number}"
            require_template_fields(errors, row, outcome_template, "option signal outcome", where)
            require_non_empty_fields(
                errors,
                row,
                ["option_setup_id", "option_shadow_trade_id", "underlying", "signal_date", "entry_snapshot_at", "final_decision"],
                "option signal outcome",
                where,
            )
            validate_canonical_fields(errors, row, {}, where)
            if row.get("option_type") in {"call", "put"}:
                if numeric_equal(row.get("planned_trade_risk_dollars"), row.get("max_contractual_loss_dollars")) is False:
                    fail(errors, f"current option outcome planned trade risk must equal max contractual loss: {where}")
                if row.get("planned_trade_risk_source") != "default_max_contractual_loss":
                    fail(errors, f"current option outcome planned risk source must be default_max_contractual_loss: {where}")


def require_template_fields(
    errors: list[str],
    row: dict,
    template: dict,
    record_name: str,
    where: str,
    prefix: str = "",
) -> None:
    for field, value in template.items():
        key = f"{prefix}{field}" if prefix else field
        if isinstance(value, dict):
            nested = row.get(field)
            if not isinstance(nested, dict):
                fail(errors, f"v2.0.1 {record_name} missing object {field}: {where}")
                continue
            require_template_fields(errors, nested, value, record_name, where, prefix="")
        elif field not in row:
            fail(errors, f"v2.0.1 {record_name} missing {field}: {where}")


def require_non_empty_fields(
    errors: list[str],
    row: dict,
    fields: list[str],
    record_name: str,
    where: str,
) -> None:
    for field in fields:
        if row.get(field) in {None, ""}:
            fail(errors, f"v2.0.1 {record_name} has empty {field}: {where}")


def validate_canonical_fields(
    errors: list[str],
    row: dict,
    canonical_by_group: dict[str, list[str]],
    where: str,
) -> None:
    if "signal_group_id" not in row or not row.get("signal_group_id"):
        fail(errors, f"v2.0.1 option record missing signal_group_id: {where}")
    if "is_canonical" not in row or not isinstance(row.get("is_canonical"), bool):
        fail(errors, f"v2.0.1 option record must set boolean is_canonical: {where}")
    if row.get("is_canonical") is False and not row.get("supersedes_setup_id"):
        fail(errors, f"non-canonical option record must set supersedes_setup_id: {where}")
    group_id = row.get("signal_group_id")
    if row.get("is_canonical") is True and group_id and canonical_by_group is not None:
        canonical_by_group.setdefault(str(group_id), []).append(where)


def check_v201_run_manifests(errors: list[str]) -> None:
    for path in sorted((ROOT / "data/run_manifests").glob("*.json")):
        data = parse_json_file_return(path, errors)
        pipeline_version = data.get("pipeline_version") if data else None
        if not data or pipeline_version is None or str(pipeline_version) < "2.0.1":
            continue
        where = rel(path)
        for field in ["run_trigger", "session_context", "intended_workflow", "started_at", "first_tool_call_at", "last_tool_call_at", "completed_at"]:
            if field not in data:
                fail(errors, f"v2.0.1 run manifest missing {field}: {where}")
        if data.get("status") == "RUNNING" and data.get("completed_at") is not None:
            fail(errors, f"RUNNING manifest must have completed_at null: {where}")
        if data.get("status") != "RUNNING" and not data.get("completed_at"):
            fail(errors, f"completed v2.0.1 manifest must set completed_at: {where}")


def parse_json_file_return(path: Path, errors: list[str]) -> dict | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:  # noqa: BLE001
        fail(errors, f"invalid JSON: {rel(path)}: {exc}")
        return None


def numeric_equal(left: object, right: object, tolerance: float = 0.0001) -> bool | None:
    try:
        return abs(float(left) - float(right)) <= tolerance
    except (TypeError, ValueError):
        return None


def numeric_less(left: object, right: object) -> bool:
    try:
        return float(left) < float(right)
    except (TypeError, ValueError):
        return False


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
