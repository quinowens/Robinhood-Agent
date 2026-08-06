# Structured Data

Version 1.7 stores machine-readable records alongside human-readable reports.

```text
data/
├── run_manifests/          # One JSON manifest per universe or daily run
├── raw_scanner_snapshots/  # Append-only JSONL raw scanner rows
├── research_records/       # Append-only JSONL candidate evaluations
└── signal_outcomes/        # Append-only JSONL forward-return updates
```

Rules:

- Use stable `run_id` and `research_id` values.
- Preserve raw scanner rows before normalization.
- Never replace unavailable values with estimates; use `null`.
- Do not overwrite completed records. Append corrections with an update timestamp.
- A degraded run may write data here but may not replace the last valid Current Universe.
- Do not store credentials, tokens, account secrets, or authentication responses.
- Treat all generated records as private unless they have been manually sanitized.
- Run `make validate` before committing generated record changes.

Use the JSON templates in `templates/` as the record contracts.
