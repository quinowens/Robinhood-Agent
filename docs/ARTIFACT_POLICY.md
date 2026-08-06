# Artifact Policy

This project separates durable source-of-truth files from generated research artifacts.

## Source Of Truth

These files define the system and should stay under version control:

- `system_prompt.md`
- `tool_policy.md`
- `pipeline_config.md`
- `scanner_engine.md`
- `research_agent.md`
- `portfolio_manager_agent.md`
- `universe.md`
- `performance_metrics.md`
- `strategy.md`
- `options_strategy.md`
- `templates/`
- `README.md`
- `PRIVATE_DATA.md`
- `docs/`
- `scripts/`
- `Makefile`

## Persistent State

These files are tracked while the repository is private because they are part of the agent's memory:

- `state/current_universe.json`
- `state/open_theses.json`
- `state/rejected_candidates.json`

State changes should be small and intentional. Daily scanner runs may update `state/rejected_candidates.json` only for obvious repeated rejects supported by current and prior evidence. Daily runs must not update `state/current_universe.json`.

## Generated Research Artifacts

These directories are currently tracked for reproducibility:

- `research_logs/`
- `data/run_manifests/`
- `data/raw_scanner_snapshots/`
- `data/research_records/`
- `data/signal_outcomes/`
- `backtests/`

If these artifacts become too noisy, switch them to local archival by adding the generated paths to `.gitignore` and keeping only `.gitkeep` placeholders plus periodic sanitized summaries.

## Commit Guidance

Use focused commits:

- Daily run: `Add daily scanner dry run for YYYY-MM-DD`
- State change: `Update rejected candidate memory`
- Rule change: `Tighten earnings block rules`
- Tooling change: `Add repository validation checks`

Avoid bundling unrelated strategy, state, and generated-output changes in the same commit unless they are part of one run.
