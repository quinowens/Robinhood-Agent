# Approved Underlying Universe

## Purpose

This file defines how the agent builds, ranks, and maintains the approved underlying universe.

The Current Universe is the source of truth for which equities are high enough quality to serve as option underlyings.

The agent should **not** rely on an old manually created watchlist. Legacy watchlists may be used for tool testing only.

---

## Universe Philosophy

The universe should be:

- Dynamic
- Liquid
- High quality
- Institutionally relevant
- Momentum-aware
- Broad enough to avoid tunnel vision
- Narrow enough for disciplined execution

The goal is to identify strong underlyings before options selection, not to trade every interesting stock or contract.

---

## Seed Universe

The monthly refresh may source candidates from:

- S&P 500
- Nasdaq 100
- Russell 1000 growth names
- AI / semiconductor leaders
- Cloud / software leaders
- Cybersecurity leaders
- Data center and infrastructure names
- Defense technology names
- Financial technology names
- Healthcare innovation names
- High-quality ETFs such as `SPY`, `QQQ`, or sector ETFs when appropriate
- Live scanner results, if they pass all Permanent Membership Rejection Filters

The seed universe should typically contain 100-500 candidates when tool access permits.

---

## Filter Hierarchy

### Permanent Membership Rejection Filters

A stock is rejected from universe membership before scoring if it fails any permanent rule:

| Filter | Requirement |
| --- | --- |
| Asset type | Common stock or approved ETF only |
| Tradability | Active and regular-hours tradable |
| Exclusions | No penny stocks, OTC, crypto, leveraged ETFs, inverse ETFs |
| Liquidity floor | Must have structurally sufficient average dollar volume for safe entry and exit |
| Critical data | Reject if tradability, price, or risk data is missing |

### Temporary Entry Blocks

Temporary conditions affect entry eligibility, not universe membership:

| Condition | Treatment |
| --- | --- |
| Earnings within 3-5 trading days | Retain tier; set `eligibility: blocked_by_earnings` |
| Completed earnings event | Re-evaluate after the first complete trading session; do not impose an automatic long cooldown |
| Extreme one-day move | Retain tier; set `eligibility: blocked_by_extension` only until structure/risk review confirms or rejects follow-through |
| Weak market regime | Retain tier; set `eligibility: blocked_by_market_regime` |
| Temporary trend damage | Retain tier or Watchlist; set a review date |
| Portfolio constraint | Retain tier; Portfolio Manager blocks entry |

Each block requires a reason and `eligible_after` or `next_review_date`.

### Post-Earnings Recheck

Before earnings, no new entry is allowed inside the blackout window.

After earnings, the candidate may become eligible after the first complete trading session if all of the following are true:

- Direct earnings result and next earnings date are recorded.
- The gap or one-day move is not excessive relative to recent volatility.
- Volume confirms institutional participation.
- Price holds the earnings move without immediate reversal.
- Entry, stop, and target still provide acceptable risk/reward.
- Market health and correlation-cluster checks pass.

If these cannot be verified, keep the temporary block and set `next_review_date`. Do not keep a candidate blocked solely because an earnings-related move occurred.

### Canonical Eligibility State

Use one canonical state progression:

```text
watchlist -> eligible -> temporarily_blocked -> proposed -> approved -> ordered
```

Implementation values:

| State | Meaning |
| --- | --- |
| `watchlist` | Research-only; not entry eligible |
| `eligible` | Tier 1, Tier 2, or provisional Tier 2 candidate may be reviewed by the Portfolio Manager |
| `blocked_by_earnings` | Temporarily blocked by pre-earnings or unsettled post-earnings risk |
| `blocked_by_extension` | Temporarily blocked by an unconfirmed extreme move |
| `blocked_by_market_regime` | Temporarily blocked by market health |
| `blocked_by_trend` | Temporarily blocked by damaged price/RS structure |
| `blocked_by_portfolio` | Temporarily blocked by account, exposure, or sizing constraints |
| `proposed` | Portfolio Manager produced an exact proposal; no order placed |
| `approved` | User approved exact order terms |
| `ordered` | Order was submitted and must be verified through order history |

Do not use `eligible_for_pm_review`. That concept is represented by `eligibility: eligible` plus a valid tier.

### Scoring / Penalty Filters

These factors reduce research score, data completeness, or decision confidence, but do not automatically reject a candidate by themselves:

| Factor | Preferred Rule |
| --- | --- |
| Market cap | Greater than $10B |
| Liquidity quality | Average dollar volume preferred; average daily volume greater than 2M shares is a secondary reference |
| Fractional eligibility | Preferred for small accounts |
| Trend | Price above 200-day SMA |
| Relative strength | Outperforming `SPY` over 30-60 sessions |
| Fundamentals | Complete and improving fundamentals preferred |

Permanent membership rejection filters happen before scoring. Penalty filters affect score, data completeness, decision confidence, and tier placement.

---

## Composite Ranking Formula

When data is available, score each eligible candidate from 0-100.

| Component | Weight |
| --- | ---: |
| 6-month price momentum, excluding latest 5 sessions | 20% |
| 3-month price momentum | 10% |
| Relative strength vs `SPY` | 20% |
| Trend quality | 15% |
| Volume / institutional participation | 10% |
| Earnings or revenue quality | 10% |
| Sector strength | 5% |
| Volatility / risk quality | 5% |
| Narrative durability | 5% |

Missing data must be marked as `N/A`. Do not fabricate values.

Measurable factors should be normalized across the eligible refresh population using percentile ranks or capped z-scores. Extreme observations must be winsorized so one outlier cannot dominate the total score. Persist every component score, its raw input, and the final score.

Track three separate measures:

- `research_score`: candidate attractiveness from 0-100.
- `data_completeness`: percentage of required inputs available.
- `decision_confidence`: confidence that the assigned classification is correct.

---

## Tier Definitions

| Tier | Role | Entry Eligibility | Position Cap |
| --- | --- | --- | ---: |
| Tier 1 | Score 85+; data completeness 90%+; constructive 200-day trend | Eligible as option underlying unless temporarily blocked | 15% equity-equivalent cap |
| Tier 2 | Score 75-84; data completeness 80%+ | Eligible as option underlying unless temporarily blocked | 10% equity-equivalent cap |
| Provisional Tier 2 | Daily-run candidate meeting Tier 2 standards until next refresh | Eligible as option underlying unless temporarily blocked | 10% equity-equivalent cap |
| Watchlist | Interesting but not approved for live-quality option proposal | No | n/a |
| Reject | Failed filter or weak score | No | n/a |

Initial construction targets:

- Tier 1: 8-12 names.
- Tier 2: 12-20 names.
- Watchlist: no more than 30 names.
- No more than 30% of Tier 1 from one sector.
- No more than 50% of Tier 1 and Tier 2 combined from one theme.

These are universe construction controls, not portfolio allocation targets. If too few names qualify, leave unused capacity rather than lowering standards.

### Threshold Calibration Audit

Do not lower Tier 1 or Tier 2 thresholds just to create activity. An empty Tier 1 is valid.

However, if multiple official monthly refreshes show the best qualified candidates clustering below the Tier 1 threshold, run a calibration audit before changing rules:

- Record the score distribution, including 90th, 95th, and 99th percentiles.
- Compare fixed thresholds against percentile-based thresholds.
- Measure forward returns and alpha by score bucket.
- Check whether the 85+ Tier 1 threshold is genuinely predictive or simply unreachable.
- Propose any threshold change only with evidence in `data/validation_reports/` and a changelog entry.

A possible future Tier 1 definition may combine percentile rank and absolute quality, such as top-decile qualified candidates plus minimum score, completeness, confidence, and trend requirements. Do not adopt this without validation evidence.

Every official universe refresh manifest must include score distribution fields: highest score, 95th percentile, 90th percentile, median, Tier 1 count, Tier 2 count, and any calibration warning. After three refreshes with the highest score below 85 or the 95th percentile below 85, flag Tier 1 threshold calibration for review.

---

## Monthly Universe Refresh

Run the refresh on the first weekend after the final trading day of each month.

Steps:

1. Run read-only authentication and data-access preflight checks.
2. Create a run manifest with a unique `run_id`, version, timestamps, expected fields, and benchmark dates.
3. Build a 300-500 name seed universe from the S&P 500, Nasdaq 100, available large/mid-cap growth sources, unique monthly Momentum candidates, recurring research candidates, and prior universe members.
4. Deduplicate candidates and preserve all seed-source tags.
5. Persist raw input data before transformation.
6. Pull available fundamentals, quotes, historicals, tradability, and earnings data.
7. Apply Permanent Membership Rejection Filters.
8. Calculate and normalize component scores across the eligible population.
9. Rank candidates and assign tiers subject to data-completeness and concentration rules.
10. Apply Temporary Entry Blocks without removing qualified members.
11. Verify the run-completeness gate in `pipeline_config.md`.
12. Archive the prior universe in `backtests/YYYY-MM-universe.md`.
13. Publish the new Current Universe only when the completeness gate passes.
14. Add a summary to `changelog.md` only if behavior changed.

---

## Mid-Month Exceptions

Mid-month additions should be controlled, but not impossible.

A daily scanner candidate may become `provisional_tier_2` until the next monthly refresh if:

- It passes all Permanent Membership Rejection Filters.
- It meets current Tier 2 standards: research score 75+, data completeness 80%+, and decision confidence 70%+.
- It has complete critical data: tradability, quote, liquidity, earnings timing, historical trend, and benchmark-relative strength.
- It is not blocked by earnings, unconfirmed extension, market regime, trend, or portfolio risk.
- The Portfolio Manager can produce a full proposal with entry, stop, target, position size, reasons for and against, and all account checks.
- The provisional promotion is logged in the run manifest and research record with source scanner tags.

User approval is required before submitting any exact live order, not before producing a Portfolio Manager proposal. A candidate below Tier 2 standards may still be considered as an exceptional one-off only with explicit user approval and documented rationale.

---

## Held Position Rules

If a held stock is demoted or removed during a refresh:

- Do not automatically force-sell.
- Do not add to the position.
- Manage the position under normal exit rules.
- Review whether the original thesis still holds.
- Close the position if trend, relative strength, risk, or thesis breaks.

---

## Current Universe

Status: **Populated by official broad catch-up refresh on 2026-08-03.**

Run ID: `2026-08-03-catch-up-universe-refresh`

The old WST watchlist remains stale and is not the source of truth.

### Tier 1

No Tier 1 names are currently approved. No candidate cleared the 85+ research-score threshold with 90%+ data completeness and sufficient decision confidence during the 2026-08-03 catch-up refresh.

### Tier 2

Tier 2 names may be reviewed by the Portfolio Manager Agent when temporary blocks, earnings windows, sizing, concentration, and order-quality checks pass. User approval is required only before submitting an exact live order:

| Symbol | Research Score | Data Completeness | Eligibility |
| --- | ---: | ---: | --- |
| GOOGL | 82 | 93% | Eligible |
| AMZN | 82 | 93% | Blocked by extension until 2026-08-07 |
| MSFT | 81 | 93% | Blocked by extension until 2026-08-07 |
| NVDA | 80 | 92% | Eligible; monitor earnings |
| META | 78 | 91% | Blocked by extension until 2026-08-07 |
| CRWD | 77 | 87% | Eligible; monitor earnings |
| PANW | 76 | 86% | Eligible; monitor earnings |
| AVGO | 76 | 86% | Eligible; monitor earnings |

### Watchlist

Watchlist names are research-only and are not approved for new entries:

`CRDO`, `MU`, `VRT`, `ORCL`, `PLTR`, `NOW`, `FSLR`, `ANET`, `AMD`, `BA`, `CRWV`, `NBIS`, `SOFI`, `COHR`

Temporary blocks from the 2026-08-03 refresh:

| Symbol | Block | Review |
| --- | --- | --- |
| AMZN | Post-earnings extension | 2026-08-07 |
| MSFT | Post-earnings extension | 2026-08-07 |
| META | Post-earnings extension and EPS-miss follow-through | 2026-08-07 |
| PLTR | Same-day earnings report | 2026-08-06 |
| ANET | Earnings on 2026-08-04 after market close | 2026-08-06 |
| AMD | Earnings on 2026-08-04 after market close | 2026-08-06 |
| CRWV | Upcoming earnings and extension risk | 2026-08-12 |
| NBIS | Upcoming earnings and extension risk | 2026-08-13 |

---

## Temporary Testing Universe

The following names may be used only for tool-call validation, quote testing, historical-data testing, and dry-run demonstrations:

`SPY`, `QQQ`, `AAPL`, `MSFT`, `GOOG`, `META`, `AMZN`, `NVDA`, `AMD`, `TSLA`, `ANET`, `CRDO`, `SOFI`, `APLD`, `ASTS`

These are **not automatically approved for live trading**.

---

## Options Relationship

The Current Universe governs option underlying eligibility.

An option contract may only be researched or proposed if its underlying is approved by the universe process or explicitly approved by the user for a one-off review.

Options contracts are not added to the Current Universe. They are handled through `options_strategy.md` and option setup records.


---

## Dynamic Pipeline Relationship

The universe is no longer expected to begin from a static watchlist. Scanner outputs from `scanner_engine.md` and `pipeline_config.md` feed the Research Agent.

Scanner candidates are **research candidates only** until validated. After the monthly Current Universe is officially populated, a daily scanner candidate can become `provisional_tier_2` through the Mid-Month Exceptions rules above. Without that validation, the Portfolio Manager must treat it as outside the approved universe.

The monthly universe refresh should use dynamic scanner results as one input, alongside fundamentals, historical trend, earnings timing, and market regime.
