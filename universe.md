# Trading Universe

## Purpose

This file defines how the agent builds, ranks, and maintains the approved trading universe.

The Current Universe is the source of truth for what the Portfolio Manager Agent may consider for new entries.

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

The goal is to identify strong candidates before trade selection, not to trade every interesting stock.

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
| Earnings within 5 trading days | Retain tier; set `eligibility: blocked_by_earnings` |
| Extreme one-day move | Retain tier; set `eligibility: blocked_by_extension` until follow-through review |
| Weak market regime | Retain tier; set `eligibility: blocked_by_market_regime` |
| Temporary trend damage | Retain tier or Watchlist; set a review date |
| Portfolio constraint | Retain tier; Portfolio Manager blocks entry |

Each block requires a reason and `eligible_after` or `next_review_date`.

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
| Tier 1 | Score 85+; data completeness 90%+; constructive 200-day trend | Yes unless temporarily blocked | 15% |
| Tier 2 | Score 75-84; data completeness 80%+ | Yes unless temporarily blocked; user approval required | 10% |
| Watchlist | Interesting but not approved for entry | No | n/a |
| Reject | Failed filter or weak score | No | n/a |

Initial construction targets:

- Tier 1: 8-12 names.
- Tier 2: 12-20 names.
- Watchlist: no more than 30 names.
- No more than 30% of Tier 1 from one sector.
- No more than 50% of Tier 1 and Tier 2 combined from one theme.

These are universe construction controls, not portfolio allocation targets. If too few names qualify, leave unused capacity rather than lowering standards.

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

Mid-month additions should be rare.

A candidate may be added mid-month only if:

- It passes all Permanent Membership Rejection Filters.
- It has an exceptional catalyst or breakout.
- The Research Agent score is 90+.
- The Portfolio Manager Agent confirms risk capacity.
- The user explicitly approves the exception.
- The exception is logged.

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

Tier 2 names may be reviewed by the Portfolio Manager Agent only after user approval and only when temporary blocks, earnings windows, sizing, and order-quality checks pass:

| Symbol | Research Score | Data Completeness | Eligibility |
| --- | ---: | ---: | --- |
| GOOGL | 82 | 93% | Eligible for PM review |
| AMZN | 82 | 93% | Blocked by extension until 2026-08-07 |
| MSFT | 81 | 93% | Blocked by extension until 2026-08-07 |
| NVDA | 80 | 92% | Eligible for PM review; monitor earnings |
| META | 78 | 91% | Blocked by extension until 2026-08-07 |
| CRWD | 77 | 87% | Eligible for PM review; monitor earnings |
| PANW | 76 | 86% | Eligible for PM review; monitor earnings |
| AVGO | 76 | 86% | Eligible for PM review; monitor earnings |

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

The Current Universe governs underlying equity eligibility.

An option contract may only be researched or proposed if its underlying is approved by the universe process or explicitly approved by the user for a one-off review.

Options are not added to the Current Universe. They are handled through `options_strategy.md`.


---

## Dynamic Pipeline Relationship

The universe is no longer expected to begin from a static watchlist. Scanner outputs from `scanner_engine.md` and `pipeline_config.md` feed the Research Agent.

Conservative v1.7 rule: scanner candidates are **research candidates only** until the monthly Current Universe is officially populated. They may be analyzed, scored, and used for proposal-only dry runs, but they are not approved for live orders.

A scanner candidate can become a mid-month exception only with explicit user approval, documented rationale, and exception logging. Without that approval, the Portfolio Manager must treat it as outside the approved universe.

The monthly universe refresh should use dynamic scanner results as one input, alongside fundamentals, historical trend, earnings timing, and market regime.
