# Changelog

## 2026-08-06

- Added private data handling policy for account-adjacent research artifacts.
- Added repository validation tooling and Make targets.
- Added artifact tracking, contribution, and branch-protection guidance.
- Clarified that generated Robinhood research records are private by default.
- Added v1.9 validation-release guidance focused on shadow portfolios, score-bucket performance, scanner-source alpha, and rule opportunity cost.
- Added market-health and shadow-trade templates plus outcome analysis tooling.
- Added Portfolio Manager correlation-cluster checks for hidden AI/mega-cap concentration.
- Replaced `eligible_for_pm_review` with canonical `eligibility: eligible` state.
- Changed Tier 2 approval sequencing so Portfolio Manager proposals do not require prior user approval; exact live orders still require approval.
- Added provisional Tier 2 daily promotion path for scanner candidates that meet Tier 2 standards before the next monthly refresh.
- Changed post-earnings blocks from fixed cooldowns to settled-session evidence reviews.
- Added 5/10/20-day NO TRADE opportunity-cost tracking by block reason.
- Added score-distribution threshold calibration reporting for universe refreshes.
- Added primary-vs-secondary blocking-rule attribution so opportunity-cost analysis does not double-count stacked rules.

## Version 1.8 — Expanded Robinhood Tool Integration

- Added `tool_policy.md` mapping all currently documented Robinhood Agentic Trading tools to read-only research, account writes, simulations, live orders, and cancellations.
- Added dynamic scan discovery with `get_scans` and filter-spec validation before scanner changes.
- Added direct financials, earnings results/calendar, index context, technical cross-checks, and optional Level 2 execution-quality checks.
- Added realized P&L, trade history, and tax-lot checks to portfolio review.
- Added batching, freshness, ambiguous-order, post-action verification, and explicit approval rules.
- Preserved proposal-only defaults and did not modify any live Robinhood watchlist, scanner, or order.

## v1.7 - Measurable Universe and Signal Validation

- Separated permanent universe-membership rejection from temporary entry eligibility.
- Changed earnings blackout from a universe rejection to a temporary entry block.
- Added a reproducible scoring model with separate 126-session and 63-session momentum factors.
- Required cross-population normalization, outlier winsorization, and persisted component scores.
- Split attractiveness, data completeness, and decision confidence into separate measures.
- Added Tier 1, Tier 2, Watchlist, sector, and theme construction limits.
- Added a 90% refresh-completeness gate and protection against overwriting the last valid universe with a degraded run.
- Added preflight, manifest, retry, restart, and raw-input retention requirements.
- Limited Options Activity to qualified secondary confirmation and no more than a 3-point decision-confidence boost.
- Added structured templates for run manifests, raw scanner snapshots, research records, and signal outcomes.
- Added fixed-horizon outcome tracking for promoted, watched, and rejected candidates.
- Added shadow-portfolio and explicit daily-zero reporting requirements.
- Migrated `state/current_universe.json` to the v1.7 metadata structure without populating or approving any names.
- Did not modify any saved Robinhood scanner or execution permission.

## v1.6 - Dynamic Scanner Pipeline

- Added `pipeline_config.md`.
- Upgraded the Scanner Engine from single-scan support to multi-scanner dynamic discovery.
- Documented active Robinhood scanner IDs:
  - Momentum Candidates: `26cdeb14-da13-493f-b0c6-783468971a16`
  - Options Activity Radar: `7068db65-2a47-470c-bde9-94d66f36b806`
  - Earnings Risk Radar: `737924f1-e94f-4ad4-ba98-6c12fcaafaa9`
- Added scanner deduplication, source tagging, and routing rules.
- Added scanner pipeline metrics to performance tracking.
- Added `templates/daily_research_log.md` for consistent scanner dry-run reports.
- Added `research_logs/` for live scanner dry runs and research reports.
- Added `state/` placeholders for current universe, open theses, and rejected candidates.
- Updated Research Agent and System Prompt to treat scanners as research inputs only.
- Reinforced that scanner hits are not trade signals.

---

## Version 1.0
Date: June 2026

### Initial Release

Created foundational AI trading system.

Features:

- Long-equity focus
- Momentum-based framework
- Trend-following methodology
- Sector rotation philosophy
- Capital preservation mandate
- Risk management controls
- Daily review process

---

## Version 1.1
Date: June 2026

### Additions

- Fixed version alignment across core files.
- Added objective market environment definitions.
- Added explicit position sizing math.
- Clarified that 1% risk means maximum loss if stop is hit, not 1% allocation.
- Added tier-specific position caps.
- Added account drawdown circuit breakers.
- Added earnings risk rules.
- Added kill switch behavior.

---

## Version 1.2
Date: June 2026

### Additions

- Added `performance_metrics.md`.
- Added trade log schema.
- Added R-multiple tracking.
- Added opportunity capture tracking.
- Added benchmark tracking using `SPY` and `QQQ`.
- Added alpha calculations vs benchmarks.
- Added monthly review template.
- Added risk-reduction triggers.
- Added rule-change governance.

---

## Version 1.3
Date: June 2026

### Additions

- Added `universe.md`.
- Replaced hard-coded watchlist with monthly dynamic universe selection.
- Added Mandatory Rejection Filters and Scoring / Penalty Filters for market cap, volume, trend, relative strength, earnings trend, and earnings blackout.
- Added composite ranking formula.
- Added Tier 1 / Tier 2 / Watchlist structure.
- Added monthly universe refresh process.
- Added mid-month exception rules.
- Added held-position rules for demoted or dropped stocks.

---

## Version 1.4
Date: June 2026

### Major Architecture Update

Replaced the single-agent watchlist model with a **two-agent research and portfolio management model**.

### Additions

- Added `research_agent.md`.
- Added `portfolio_manager_agent.md`.
- Clarified that old manual watchlists are stale and not sources of truth.
- Expanded the seed universe beyond the old WST watchlist.
- Added broad universe categories including S&P 500, Nasdaq 100, Russell 1000 growth, AI, semiconductors, software, cybersecurity, data centers, defense technology, fintech, healthcare innovation, and ETFs.
- Added Research Agent scoring model.
- Added Portfolio Manager Agent trade proposal framework.
- Added small-account mode for accounts below $1,000.
- Added separate research quality metrics.
- Added research log schema.
- Updated trade log schema to allow fractional shares when supported.
- Updated system prompt to default to proposal-only mode.

### System Behavior Changes

- The Research Agent finds and ranks opportunities.
- The Portfolio Manager Agent decides whether a ranked idea fits the portfolio.
- No stock becomes tradable simply because it appears on an old watchlist.
- Current Universe remains empty until an official broad refresh is completed.
- Temporary testing universe may be used for dry runs only.

---

## Current Repository Structure

```text
Robinhood-Agent/
├── README.md
├── system_prompt.md
├── research_agent.md
├── portfolio_manager_agent.md
├── strategy.md
├── universe.md
├── scanner_engine.md
├── pipeline_config.md
├── performance_metrics.md
├── changelog.md
├── templates/
├── research_logs/
├── state/
└── backtests/
```

---

## Roadmap

### v1.8

- Market regime scoring
- VIX filters
- Breadth filters
- Objective market health score

### v1.9

- Sector rotation model
- Correlation checks
- Sector exposure optimizer

### v2.0

- Persistent state file
- Trade log automation
- Research log automation
- Paper-trading workflow
- Automated monthly universe refresh
