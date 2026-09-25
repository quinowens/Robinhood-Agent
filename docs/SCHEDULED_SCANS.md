# Scheduled Scans

The Codex app owns the actual cron schedules. This file documents the expected v2.0 behavior for the active Robinhood Agent automations.

All scheduled scans run in research-only / proposal-only / shadow-trading mode. They may generate hypothetical options proposals and shadow records, but they may not place, modify, cancel, or submit live orders.

## Daily

Automation ID: `robinhood-agent-daily-scanner-dry-run`

Name: Robinhood Agent Daily Options Scanner Dry Run

Cadence: weekdays at the existing scheduled time.

Purpose:

- Run saved scanners as underlying discovery inputs.
- Resolve scanner names/IDs before `run_scan`.
- Preserve raw scanner rows before normalization.
- Enrich surviving underlyings progressively.
- Classify directional thesis and options suitability.
- Pull option-chain data only for qualified finalists.
- Rank long-call / long-put contracts.
- Record options setup, option shadow, and option outcome tracking where applicable.
- For every setup where option setup quality passes but account fit fails, classify `SHADOW_ONLY_QUALIFIED` and add the exact frozen contract to the Options Shadow Portfolio.
- Keep `WATCH` separate from `SHADOW_ONLY_QUALIFIED`; do not add merely interesting stocks to the shadow portfolio.
- Report primary and secondary blocking rules.
- Mature newly eligible 1D/5D/10D/20D/30D outcomes, preserve finalized values, and report any eligible value that could not be populated.
- Close the run only after the qualified-setup persistence chain passes; otherwise record `DEGRADED_PERSISTENCE`.
- Write a scheduled-run ledger entry even for failure, intentional schedule skips, and non-trading days.
- Emit the full `OUTCOME_HEALTH` expected/observed counts and mark the run degraded whenever overdue windows are non-zero.
- Emit `OUTCOME_RETRIEVAL_HEALTH` with expected, resolved, retryable, permanent, and per-component success rates; retry eligible matured component failures automatically.
- After the market session, run `python3 scripts/update_option_outcomes.py --list-due-option-checkpoints --as-of YYYY-MM-DD` before outcome maturation.
- When the due manifest contains option IDs, call `get_option_quotes` for exactly those IDs, preserve the complete raw response in `data/option_quote_checkpoints/YYYY-MM-DD-option-quotes.json` with `source: robinhood_option_quote_checkpoint` and the exact `checkpoint_date`, then run `scripts/update_option_outcomes.py` with the checkpoint and available equity-history snapshots.
- If no option checkpoints are due, record a zero-count checkpoint decision and continue. If quotes are due but capture or persistence fails, mark the run degraded and retain the due manifest/error; never substitute a later quote for the missed target session.
- Run aggregate outcome analytics and repository validation only after the checkpoint snapshot has been ingested.

## Weekly

Automation ID: `robinhood-agent-weekly-research-review`

Name: Robinhood Agent Weekly Options Research Review

Cadence: Sunday at the existing scheduled time.

Purpose:

- Consolidate daily scanner outputs and v2.0 option records.
- Review recurring underlyings, provisional Tier 2 candidates, and expiring temporary blocks.
- Evaluate directional thesis quality, options suitability, contract-selection quality, and account-fit misses.
- Review option shadow outcomes by call/put, DTE, delta, spread, IV/premium, scanner source, and market regime where sample size allows.
- Review 1/5/10/20/30-day option and underlying performance for every `SHADOW_ONLY_QUALIFIED` setup, including stop/target flags and thesis-right versus contract-right classification.
- Summarize account-fit failures and preferred-contract premium distribution to estimate realistic account funding needs.
- Keep primary blocking-rule attribution separate from secondary diagnostics.
- Run the structured integrity audit, list exceptions by stable ID and source date, and visibly fail/degrade the weekly integrity section for broken canonical chains.
- Account for every expected daily run using `COMPLETED`, `COMPLETED_DEGRADED`, `SKIPPED_NON_TRADING_DAY`, `SKIPPED_SCHEDULE`, `FAILED`, or `MISSING`.
- Generate the research-only strategy diagnostic report, including score discrimination, option-versus-underlying classifications, directional bias by regime, and rejection opportunity cost.
- Before weekly aggregation, perform the same due-option-checkpoint discovery, live quote capture, dated snapshot persistence, and outcome update sequence for any horizons maturing on the weekly run date. Report any missed weekday checkpoints from the run ledger; do not backfill them with current quotes.
- Run outcome analysis and integrity validation only after that sequence completes.

## Run Completion Contract

Writing a Markdown report is not proof of completion. Each v2.0.2 manifest records artifact IDs, decision integrity, persistence integrity, and zero or more degradation categories. Scanner archival shortfalls are non-decision-critical when candidate evaluation is complete; missing decision quotes, required scoring data, or canonical persistence artifacts are decision-critical.

Scheduled processing runs due-checkpoint discovery, same-session live option quote capture, snapshot persistence, and outcome maturation before aggregate analytics, then runs the persistence audit. `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE` is a valid permanent component status and does not fail repository validation. A scheduled run is degraded when a quote was due that session but could not be captured or persisted; it must not replace the missed checkpoint with a later quote.

## Monthly

Automation ID: `robinhood-agent-monthly-universe-review`

Name: Robinhood Agent Monthly Underlying and Options Review

Cadence: first Saturday of each month at the existing scheduled time.

Purpose:

- Complete the official Approved Underlying Universe refresh when the completeness gate passes.
- Preserve broad seed, scanner raw, run manifest, component-score, and monthly review artifacts.
- Evaluate options strategy evidence separately from underlying universe evidence.
- Calibrate Underlying Thesis Score and Options Setup Score distributions.
- Review option contract-selection rules and account-fit constraints without changing thresholds from small samples.
- Report how many qualified setups failed account fit, the median and 75th percentile preferred-contract premium, and estimated account size needed to participate under the current premium-risk caps.
- Before monthly aggregation, perform the same due-option-checkpoint discovery, live quote capture, dated snapshot persistence, and outcome update sequence for horizons maturing on the monthly run date.
- Audit daily and weekly run ledgers for missed prospective checkpoints, report those gaps separately from permanent historical-source limitations, and never use a current quote as a historical substitute.
- Run monthly outcome analysis, strategy diagnostics, integrity checks, and repository validation only after checkpoint ingestion and outcome maturation.

## Prospective Option Checkpoint Contract

The scheduled sequence is mandatory and ordered:

1. Discover: export the contracts due on the current U.S. trading session with `scripts/update_option_outcomes.py --list-due-option-checkpoints --as-of YYYY-MM-DD`.
2. Capture: when `option_ids` is non-empty, call `get_option_quotes` once for the unique due IDs after the regular session close.
3. Persist: save the unmodified provider payload plus `source: robinhood_option_quote_checkpoint`, `checkpoint_date: YYYY-MM-DD`, and capture timestamp under `data/option_quote_checkpoints/`.
4. Update: pass the saved option checkpoint and available equity-history snapshots to `scripts/update_option_outcomes.py` so all independently resolvable components are recorded.
5. Verify: run outcome analytics and `scripts/validate_repo.py`, and record due/captured/updated/missed counts in the run report and ledger.

Only an exact-date checkpoint may populate a target horizon. Empty due lists are successful no-op captures. Historical horizons that predate this mechanism may remain `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE`; future due horizons must be captured prospectively whenever the quote tool is available.

## Path Compatibility

The project directory was renamed from `Robinhood-Agent-v1.6` to `Robinhood-Agent`. Existing app automation metadata may still reference the old cwd, so a local compatibility symlink points:

```text
/Users/quinowens/Desktop/Robinhood-Agent-v1.6 -> /Users/quinowens/Desktop/Robinhood-Agent
```

Do not remove that symlink unless the Codex app automation project path is updated.
