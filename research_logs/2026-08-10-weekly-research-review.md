# Weekly Research Review - 2026-08-10

Review period: 2026-08-03 through 2026-08-07  
Automation: Robinhood Agent Weekly Options Research Review  
Mode: Research-only / proposal-only / shadow-trading  
Strategy version reviewed: v2.0.1 options-primary  
Execution status: No live orders placed, modified, canceled, reviewed, or approved.

## Executive Summary

The weekly result is one shadow-only qualified options setup and no live trade. `NVDA` was the only candidate that reached full v2.0 options-primary research. It passed underlying research, directional classification, options suitability, and contract-quality review, but failed account fit because the selected one-contract long call required $977.50 of premium risk against a $100 account.

Run health improved through the week but remained degraded overall. All five daily scanner runs resolved and ran the three configured scanners. The main degradation pattern was incomplete full-row scanner persistence from large connector responses, restricted/missing `RUT` and `DJI` index coverage, intermittent null financial rows, and, on 2026-08-07, missing fresh equity-historical tool availability. Earlier daily runs mostly stopped at underlying/NO TRADE review; the 2026-08-07 run was the first full v2.0.1 options-primary run with chain, instrument, quote, setup, shadow-trade, and option-outcome records.

No Tier 1 names are approved. Current Universe remains populated from the official 2026-08-03 catch-up refresh with eight Tier 2 names: `GOOGL`, `AMZN`, `MSFT`, `NVDA`, `META`, `CRWD`, `PANW`, and `AVGO`. Daily evidence does not authorize a Current Universe rewrite.

## Weekly Run Health

| Date | Status | Scanner coverage | Decision candidates | Completeness | Options step health |
| --- | --- | --- | ---: | ---: | --- |
| 2026-08-03 | complete | 3/3 scanners, 889 total matches | 11 | 90% | No option-chain work; no finalists advanced |
| 2026-08-04 | degraded | 3/3 scanners, 951 total matches | 32 | 88% | Skipped; no eligible exact options finalist |
| 2026-08-05 | degraded | 3/3 scanners, 722 total matches | 25 terminal counts reported | N/A in manifest | Skipped; no eligible exact options finalist |
| 2026-08-06 | degraded | 3/3 scanners, 809 total matches | 30 | 88% | Skipped; no finalists requiring execution-quality review |
| 2026-08-07 | degraded | 3/3 scanners, 547 total matches | 31 | 86% | Completed scoped v2.0 option research for `NVDA` |

Weekly health classification: degraded, usable for research and validation. No run failed. No run placed, modified, canceled, or submitted a live order.

Recurring missing or degraded fields:

- Full scanner row exports were not preserved for large Momentum and Earnings Risk payloads; visible rows and scanner totals were saved.
- `RUT` quotes were restricted and `DJI` did not resolve through index lookup.
- Null financial rows appeared for names such as `NBIS`, `ZBRA`, `ENTG`, `ARM`, `SPCX`, `DT`, `GFI`, `AEM`, `PAAS`, `TIGO`, `TEAM`, and `HALO` on affected days.
- 2026-08-07 lacked fresh callable equity-historical access, so trend work used prior universe scoring plus live quote/fundamental context.
- The validation summary was stale before this weekly run; it has now been regenerated and includes the 2026-08-07 option setup, shadow trade, and option outcome record.

## Market / Benchmark Context

The week was constructive enough for research but not strong enough to override universe, event, account-fit, or contract-quality rules.

- 2026-08-03: `SPY` and `QQQ` rebounded sharply from prior closes; `SPX` and `NDX` quotes were available.
- 2026-08-04: `SPY` remained above the prior July close; `QQQ` was rebounding but still showed choppy July context.
- 2026-08-05: `SPX` was near 7,743.92 and `NDX` near 29,695.23 in the recorded manifest; `SPY` was slightly positive and `QQQ` slightly negative intraday.
- 2026-08-07: `SPX` 7,759.01 and `NDX` 29,731.0516 were constructive intraday; `SPY` and `QQQ` were both positive versus prior close.

Market-regime conclusion: constructive/mixed research environment. No aggressive live entries; require high-quality Tier 2 evidence and clean account fit.

## Scanner Review

| Scanner | Weekly role | Observed quality |
| --- | --- | --- |
| Momentum Candidates | Primary underlying movement discovery | Best source for liquid, institutionally relevant movement, but heavily event-driven this week. |
| Options Activity Radar | Options context only | Useful when it overlapped `NVDA` and Current Universe names; noisy at the top with microcap, low-price, and high-IV rows. |
| Earnings Risk Radar | Event-risk confirmation | Useful secondary reminder, but direct earnings tools correctly controlled actual block decisions. |

Scanner frequency was not treated as bullish or bearish evidence. It was used only to prioritize research and validation.

Notable recurring or high-attention names:

- Current Universe Tier 2 repeats: `NVDA`, `GOOGL`, `CRWD`, `PANW`, `AVGO`, `AMZN`, `MSFT`, `META`.
- Watchlist/event repeats: `AMD`, `ANET`, `PLTR`, `COHR`, `CRWV`, `NBIS`, `MU`, `CRDO`, `RKLB`, `AAOI`.
- Post-earnings scanner movers outside Current Universe: `TEAM`, `TWLO`, `HALO`, `ABNB`, `MCHP`, `INSM`, `U`, `TIGO`, `ALAB`, `SNDK`.
- Rejected/noisy options rows: `SURG`, `HTZ`, `MARA`, `TENX`, `ARAY`, `DGNX`, `EGHT`.

## Underlying Queue

Priority queue for the next daily research cycle:

| Priority | Symbols | Reason |
| --- | --- | --- |
| 1 | `NVDA` | Only shadow-qualified setup; needs outcome tracking and fresh pre-earnings reassessment before any future exact review. |
| 2 | `CRWD`, `PANW`, `AVGO` | Bullish Tier 2 candidates on 2026-08-07; options research deferred or blocked by limit/quality/concentration context. |
| 3 | `AMZN`, `MSFT`, `META` | Extension blocks reached review date 2026-08-07; require settled follow-through review before eligibility can change. |
| 4 | `GOOGL` | High score but 2026-08-07 direction was neutral/no edge due weak relative strength. |
| 5 | `CRDO`, `MU`, `COHR`, `PLTR`, `RKLB`, `ANET`, `AMD` | Watchlist names near provisional review interest, but still blocked by watchlist, event, trend, or post-event requirements. |
| 6 | `TEAM`, `TWLO`, `HALO`, `ABNB`, `MCHP` | Strong post-earnings movers outside Current Universe; track opportunity cost, do not promote without full provisional Tier 2 evidence. |

## Directional Thesis Review

Directional classification was explicit only in the 2026-08-07 v2.0.1 records:

| Symbol | Direction | Directional confidence | Options suitability | Weekly interpretation |
| --- | --- | ---: | --- | --- |
| `NVDA` | bullish | 70 | `OPTIONS_RESEARCH` | Qualified for long-call research, then account-fit blocked. |
| `AMZN` | bullish | N/A | `TEMP_BLOCK` | Thesis not actionable while extension block requires settled review. |
| `MSFT` | bullish | N/A | `TEMP_BLOCK` | Same as `AMZN`; no options proposal. |
| `CRWD` | bullish | N/A | `WATCH` | Serious candidate, but options work deferred by shadow-research limit. |
| `PANW` | bullish | N/A | `WATCH` | Bullish but financial-quality caution kept it out of proposal flow. |
| `AVGO` | bullish | N/A | `WATCH` | Bullish but semiconductor/AI infrastructure concentration context limited escalation. |
| `GOOGL`, `META`, outside-universe movers | neutral | N/A | `NO_DIRECTIONAL_EDGE`, `TEMP_BLOCK`, or `WATCH` | Neutral or unsupported direction means no options proposal. |

## Options Setup Review

Only one setup record exists for the week:

| Underlying | Contract | Type | DTE | Delta | Spread | OI / volume | IV | Options score | Completeness | Confidence |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `NVDA` | 2026-09-18 230C | long call | 42 | 0.4649 | 1.53% of midpoint | 30,278 / 2,906 | 0.3888 | 79 | 92 | 75 |

Contract-quality conclusion: qualified for shadow tracking. The contract fit the enabled v2.0 launch scope: single-leg long call, not 0DTE, 42 DTE, mid-delta, tight quoted spread, high open interest, and acceptable liquidity. No puts, covered calls, cash-secured puts, spreads, short options, or cheap substituted contracts were proposed.

## Account-Fit / Shadow-Only Review

The `NVDA` setup was `QUALIFIED` on setup quality and `FAIL` on account fit:

- Account value: $100.
- Cash / buying power: $100.
- Option positions: 0.
- Open option orders: 0.
- Broker options capability: Level 2 confirmed on 2026-08-07 after user app approval.
- Strategy permission: `LONG_CALL` and `LONG_PUT` only.
- One-contract premium allocation: $977.50.
- Maximum contractual loss: $977.50.
- Planned trade risk: $977.50, defaulted to maximum contractual loss.
- Primary account-fit block: `account_risk`.

Final classification: `SHADOW_ONLY_QUALIFIED`. The high-quality unaffordable setup remained in shadow tracking and was not forced into a worse contract.

## Options Outcome Review

Outcome sample is not yet sufficient.

| Metric | Weekly result |
| --- | ---: |
| Option setup records | 1 |
| Option outcome records | 1 |
| Option shadow trades | 1 |
| Closed shadow trades | 0 |
| Outcome classifications | 1 unobserved |
| Call setups | 1 |
| Put setups | 0 |
| DTE bucket | 30-45: 1 |
| Delta bucket | 0.35-0.50: 1 |
| Options setup score bucket | 75-79: 1 |
| Account-fit failures | 1 |

No thesis-right versus contract-right classification can be made yet because forward 5/10/20/30-day and option MFE/MAE fields are still unobserved.

## Current Universe Review

Current Universe state remains unchanged.

Strengthening or actionable research names:

- `NVDA`: strongest v2.0 evidence; shadow setup opened.
- `CRWD`, `PANW`, `AVGO`: bullish Tier 2 candidates needing fresh options research and event checks.

Needs settled temporary-block review:

- `AMZN`, `MSFT`, `META`: extension blocks had review date 2026-08-07 but were not cleared by weekly evidence.

Watchlist/provisional candidates to monitor:

- `CRDO`, `MU`, `COHR`, `PLTR`, `RKLB`, `ANET`, `AMD`, plus post-earnings movers `TEAM`, `TWLO`, `HALO`, `ABNB`, `MCHP`.

Monthly refresh implication: do not lower standards. The next official refresh should evaluate whether repeated watchlist names near 75 are improving with complete data, but no weekly evidence authorizes a mid-month universe rewrite.

## Primary Blocking-Rule Analysis

Weekly primary blocks from structured records and regenerated validation:

| Primary block | Count | Interpretation |
| --- | ---: | --- |
| `blocked_by_earnings` | 15 | Event risk dominated watchlist and scanner movers. |
| `blocked_by_extension` | 13 | Post-earnings or post-gap follow-through review remains a major filter. |
| `legacy_tier_2_approval_deadlock` | 7 | Older daily records still used legacy Tier 2 approval wording before v2.0.1 cleanup. |
| `outside_current_universe` | 4 | Scanner-only names were correctly blocked from proposal flow. |
| `account_risk` | 1 | `NVDA` setup quality passed but account fit failed. |
| `correlation_cluster_limit` | 1 | `AVGO` held back by semiconductor/AI infrastructure exposure context. |
| `financial_quality_caution` | 1 | `PANW` required more caution before option research. |
| `weak_relative_strength` | 1 | `GOOGL` lacked actionable directional edge on 2026-08-07. |
| `penny_stock_or_microcap` | 2 | Low-quality Options Activity rows rejected. |

Secondary blocks were retained as context only and not double-counted.

## Score And Options Threshold Calibration

Underlying score distribution from available scored records:

| Metric | Value |
| --- | ---: |
| Scored count | 19 |
| Highest | 82 |
| Median | 80 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 85 | 0 |
| Count >= 75 | 19 |

Calibration observation: the highest score remains below the 85 Tier 1 threshold, so the validation file correctly flags `highest_score_below_tier_1_threshold`. This is not enough evidence to lower Tier 1 standards. Keep the threshold unchanged until multiple official refreshes and forward outcomes show the fixed threshold is not predictive or structurally unreachable.

Options setup score distribution:

| Metric | Value |
| --- | ---: |
| Setup count | 1 |
| Highest | 79 |
| Median | 79 |
| 90th percentile | 79 |
| 95th percentile | 79 |
| Count >= 80 | 0 |
| Count >= 75 | 1 |

Options calibration observation: one setup is not a threshold sample. Continue collecting setup and outcome records before changing Options Setup Score thresholds.

## State Decisions

| File / artifact | Decision |
| --- | --- |
| `state/current_universe.json` | Unchanged; weekly evidence does not authorize universe rewrite. |
| `state/open_theses.json` | Unchanged; no live or approved thesis opened. |
| `state/rejected_candidates.json` | Left as produced by daily runs; 2026-08-07 already updated `HTZ` and `MARA`. |
| `state/account_capabilities.json` | Left as produced by 2026-08-07; broker Level 2 is recorded separately from strategy scope. |
| `data/validation_reports/2026-08-validation-summary.json` | Regenerated to include the 2026-08-07 options setup, shadow trade, and outcome record. |

No separate research-agent candidate review file was necessary; the queue and candidate classifications above are sufficient for this weekly review.

## Next Research Actions

1. Update `NVDA` shadow outcome after 5, 10, and 20 trading days; separate underlying thesis result from contract-selection result.
2. Re-run fresh histories and benchmark-relative calculations for `NVDA`, `CRWD`, `PANW`, `AVGO`, `AMZN`, `MSFT`, and `META` when the historical tool is available.
3. Perform settled extension-block review for `AMZN`, `MSFT`, and `META`.
4. Run scoped option-chain work for `CRWD`, `PANW`, and `AVGO` only if earnings windows, directional thesis, and account-fit prerequisites are satisfied.
5. Continue rejecting Options Activity-only low-cap/high-IV rows unless they independently pass universe, tradability, liquidity, fundamentals, trend, and event checks.
6. Track `TEAM`, `TWLO`, `HALO`, `ABNB`, and `MCHP` as outside-universe post-earnings opportunity-cost names, not provisional Tier 2 members.

## Execution Statement

No order review, order placement, order cancellation, scanner modification, watchlist modification, or option exercise was performed during this weekly review.

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
