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

## Path Compatibility

The project directory was renamed from `Robinhood-Agent-v1.6` to `Robinhood-Agent`. Existing app automation metadata may still reference the old cwd, so a local compatibility symlink points:

```text
/Users/quinowens/Desktop/Robinhood-Agent-v1.6 -> /Users/quinowens/Desktop/Robinhood-Agent
```

Do not remove that symlink unless the Codex app automation project path is updated.
