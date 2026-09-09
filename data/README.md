# Structured Data

Version 2.0 stores machine-readable records alongside human-readable reports.

```text
data/
├── run_manifests/          # One JSON manifest per universe or daily run
├── raw_scanner_snapshots/  # Append-only JSONL raw scanner rows
├── research_records/       # Append-only JSONL candidate evaluations
├── signal_outcomes/        # Append-only JSONL forward-return updates
├── shadow_trades/          # Append-only JSONL hypothetical trades
├── options_setup_records/  # Append-only JSONL options setup evaluations
├── option_shadow_trades/   # Append-only JSONL hypothetical options trades
├── option_signal_outcomes/ # Append-only JSONL option/underlying forward outcomes
├── market_regime/          # Market health snapshots
├── validation_reports/     # Monthly evidence summaries
├── scheduled_run_ledger/   # Explicit status for every expected scheduled run
└── integrity_audits/       # Optional persisted weekly cross-record audits
```

Rules:

- Use stable, explicit `run_id`, `research_record_id`, `options_setup_id`, `shadow_trade_id`, and `outcome_record_id` values.
- Preserve raw scanner rows before normalization.
- Never replace unavailable values with estimates; use `null`.
- Do not overwrite completed records or finalized outcome windows. Append corrections with supersession IDs, a correction reason, and an update timestamp.
- A qualified setup is not complete until its research, setup, canonical shadow, canonical outcome, and run-manifest references form one validated chain.
- Use explicit source, scanner-archive, options-data, persistence, decision-data, and pipeline degradation categories; do not collapse them into one ambiguous state.
- A degraded run may write data here but may not replace the last valid Current Universe.
- Do not store credentials, tokens, account secrets, or authentication responses.
- Treat all generated records as private unless they have been manually sanitized.
- Run `make validate` before committing generated record changes.

Use the JSON templates in `templates/` as the record contracts.

Run outcome analysis with:

```bash
python3 scripts/analyze_outcomes.py
python3 scripts/analyze_outcomes.py --month YYYY-MM --output data/validation_reports/YYYY-MM-validation-summary.json
python3 scripts/data_integrity.py --as-of YYYY-MM-DD --output data/integrity_audits/YYYY-MM-DD.json
python3 scripts/migrate_v202_ids.py --dry-run  # preview deterministic legacy-ID backfill
python3 scripts/generate_strategy_diagnostics.py --output data/validation_reports/strategy-diagnostics.json
```

Every canonical option outcome carries an explicit status and observation metadata for 1D, 5D, 10D, 20D, and 30D. `OBSERVED` windows are immutable by default. A mature missing window must be `MISSING_SOURCE_DATA` or `UPDATE_FAILED` with a persisted reason; it must never remain an unexplained null.
