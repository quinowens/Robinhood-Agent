# Private Data Policy

This repository is private by default.

The project may contain account-adjacent research artifacts, including masked account identifiers, portfolio snapshots, scanner outputs, rejected-candidate memory, research logs, and run manifests. These files are useful for reproducibility, but they are not suitable for a public repository without review and sanitization.

## Sensitive Material

Do not commit:

- Robinhood credentials, tokens, cookies, MFA material, OAuth responses, or session exports.
- Full account numbers, routing numbers, tax IDs, Social Security numbers, or personal identity documents.
- `.env` files or local configuration containing secrets.
- Screenshots or exports that expose balances, full account identifiers, addresses, emails, phone numbers, or authentication state.

Permitted in this private repository:

- Masked account identifiers, such as last-four references.
- Research-only scanner outputs and candidate rankings.
- Generated daily logs, raw scanner snapshots, research records, manifests, and state files when they do not contain secrets.
- Portfolio exposure summaries needed for reproducible research decisions.

## Public Release Rule

Before making this repository public or sharing it broadly:

1. Remove or sanitize `data/`, `research_logs/`, `state/`, and `backtests/`.
2. Run `make scan-sensitive`.
3. Run `make validate`.
4. Review the full diff manually.
5. Prefer a fresh public-safe repository over changing this repository's visibility.

## Daily Handling

- Keep live order activity out of generated research logs unless explicitly needed for audit.
- Use masked account references only.
- Never paste authentication responses into markdown, JSON, or logs.
- Treat all generated Robinhood artifacts as private even when they contain only public ticker data.
