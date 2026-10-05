# Weekly Research Review — 2026-10-04

Review window: 2026-09-28 through 2026-10-02  
Run date: 2026-10-04  
Mode: Research-only / Proposal-only / Shadow-trading  
Strategy: v2.0 options-primary; single-leg long calls and long puts only  
Decision: **NO LIVE TRADE / ONE NEW SHADOW-ONLY QUALIFIED SETUP / STATE UNCHANGED**

## Executive Summary

MRVL was the only new setup to complete the full underlying, direction, contract-quality, and provisional Tier 2 path. The frozen 2026-11-20 250C scored 84, but one contract required $3,275 against $100 of account value and buying power. It was therefore recorded as `SHADOW_ONLY_QUALIFIED`; no cheaper or lower-quality substitute was used.

META and CRWD remained the strongest official Tier 2 research names, but both already had active canonical bullish signal groups, so no duplicate shadow signals were created. PANW and OKTA failed contract execution quality, NBIS failed IV/premium quality, and all remaining serious candidates stayed watch-only, temporarily blocked, stock-thesis-only, or directionally unsupported.

Run health was materially weaker than the research signal. September 28 and 29 completed in degraded mode, September 30 completed with no decision because its scanner evidence was recovered cross-session, October 1 had no run artifact and missed two prospective option checkpoints, and October 2 completed late on October 4 using decision evidence captured for the October 2 post-close session. Thresholds and Current Universe state remain frozen.

## Weekly Run Health

| Target session | Run status | Scanner evidence | v2.0 options steps | Checkpoint result |
| --- | --- | --- | --- | --- |
| 2026-09-28 | `DEGRADED_COMPLETE` | 515 rows; 502 deduplicated symbols; Momentum and Earnings capped | Completed; 2 WATCH setups | 0 due; successful no-op |
| 2026-09-29 | `DEGRADED_COMPLETE` | 504 rows; 486 deduplicated symbols; Momentum and Earnings capped | Completed; 3 setups and 1 new shadow chain | 0 due; successful no-op |
| 2026-09-30 | `DEGRADED_NO_DECISION` | 473 rows; 454 symbols; captured on 2026-10-02 and unusable for the target session | Correctly stopped before new contract selection | 3 due, 3 captured, 3 updated, 0 missed |
| 2026-10-01 | Missing run | No manifest, report, or structured scanner record | Skipped | 2 due, 0 captured, 0 updated, 2 missed |
| 2026-10-02 | `DEGRADED_COMPLETE` (late local completion) | Same-session post-close: Momentum 200/396, Options Activity 74/74, Earnings Risk 41/41 | 10 terminal research records and 3 WATCH option setups | 1 due, 1 captured and ingested, 0 missed |

Weekly health count: 0 fully successful, 4 degraded, and 1 missing target-session run. Three degraded runs produced valid terminal decisions; September 30 correctly produced no decision rather than mix sessions.

The October 2 MSFT checkpoint was captured and ingested on its target session and classified `UNDERLYING_WIN_OPTION_LOSS` at 20D. The local daily run did not finish publishing until October 4, but its scanner, quote, account, and checkpoint decision evidence was preserved from the October 2 session. This is a late-completion weakness, not a missed checkpoint.

Tool/data limitations remained consistent: full reported financial statements, option historical bars, formal breadth/sector participation, and individual trade-history P/L were unavailable in several daily runs; Momentum and Earnings payloads were often capped; only the progressive finalist set received direct enrichment. The weekly integrity audit found no broken canonical chains or orphaned records.

## Prospective Option Checkpoint and Outcome Preflight

The run-date command for 2026-10-04 returned zero due option IDs, a successful no-op. No quote call or checkpoint file was required for the run date.

Weekly target-session audit:

- Due: 6 option checkpoints.
- Captured on target session: 4.
- Ingested/updated: 4.
- Missed prospective checkpoints: 2.
- Missed IDs: AMZN 2026-10-16 265C 30D and NVDA 2026-10-16 225C 20D, both due 2026-10-01.
- The two October 1 misses were not backfilled with later quotes.
- Permanent historical-source limitations remain separate: `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE` is valid and did not fail validation.

Outcome maturation refreshed 12 records from the available immutable snapshots. The integrity audit reports 14 complete qualified chains, 0 errors, 0 orphaned shadow records, 0 orphaned option outcomes, 0 update failures, and 24 matured full-horizon observations still incomplete, primarily because option history is not supported. Repository validation passed with warnings.

## Account and Portfolio Context

The read-only weekly cross-check confirmed the Agentic cash account ending 8691 remains Level 2 with $100 account value, $100 cash, and $100 buying power. It has no equity positions, option positions, or equity/option orders during the review window. Current live premium exposure is $0.

Broker capability does not expand strategy scope. Long calls and long puts remain the only enabled structures; autonomous execution, 0DTE, naked selling, cash-secured puts, covered calls, and multi-leg spreads remain disabled.

## Market and Benchmark Context

The market remained constructive but selective. SPY and QQQ were above their 20-day, 50-day, and 200-day averages with positive 50-day slopes on both the early-week and October 2 snapshots, while breadth remained unavailable. SPY's official closes moved from 771.35 on September 28 to 762.36 on September 30 and recovered to 769.64 on October 2. QQQ moved from 744.50 to 739.71 and then recovered to 749.58. The October 2 Market Health Score was 65 with VIX at 15.31.

The September 30 regime was not reclassified because recovery occurred cross-session. The October 2 regime artifact supports constructive/selective with late-week recovery, not a fully confirmed strong regime. Market context permits selective bullish research but does not override volume, event, contract-quality, or account-fit rules.

## Scanner Review

Momentum Candidates remained useful for underlying movement discovery. NTAP, STM, KLAC, P, TER, and CCL appeared in all four visible scanner captures; CRWD and PANW appeared three times, and watchlist names VRT, ORCL, NBIS, COHR, and LITE also appeared three times. Frequency only prioritized research and did not establish bullish direction.

Options Activity Radar remained context rather than direction. NVDA, AMZN, AAPL, TSLA, SPCX, and NAUT appeared in all four visible captures; current-universe names MSFT, AVGO, AMD, and MU appeared repeatedly. The high-IV and small-cap tail remained noisy, so permanent quality filters were necessary before enrichment.

Earnings Risk Radar continued to identify event windows but included many low-quality names and was capped on three captures. Direct earnings verification remained necessary for serious candidates. The outcome sample is not large or balanced enough to rank scanner sources by predictive quality.

## Weekly Underlying Research Queue

| Priority | Symbol | Weekly evidence | Score / completeness / confidence | Direction | Eligibility / disposition | Next research trigger |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | MRVL | New qualified provisional path; Friday close 272.29 | 82 / 88% / 80% | Bullish | Provisional Tier 2; `SHADOW_ONLY_QUALIFIED` | Continue scheduled outcome checkpoints; consider at governed monthly refresh |
| 2 | CRWD | Strongest recurring official member; existing signal; Friday close 270.04 | 83 / 90% / 82% | Bullish | Tier 2; existing active signal group | Track frozen 250C; do not duplicate signal |
| 3 | META | Highest weekly score; Friday close 728.08 | 84 / 90% / 84% | Bullish on 9/29 | Tier 2; existing active signal group | Reassess after active horizon matures or thesis independently resets |
| 4 | PANW | Recurred three times; Friday close 403.24 | 83 / 89% / 81% | Bullish | Tier 2; WATCH | Require materially tighter spread and adequate OI/volume |
| 5 | OKTA | Strong trend and score; Friday close 211.49 | 82 / 87% / 79% | Bullish | Watchlist; provisional path incomplete | Fresh same-date contract with tighter spread and controlled IV |
| 6 | NBIS | Recurred three times; Friday close 242.81 | 81 / 87% / 79% | Bullish | Watchlist; WATCH | IV/premium and spread must improve before promotion |
| 7 | COHR | Recurred three times; Friday close 337.04 | 79 / 87% / 78% | Bullish | Watchlist; WATCH | Resolve earnings/expiration conflict and liquidity |
| 8 | LITE | Recurred three times; Friday close 1,085.42 | 78 / 86% / 76% | Bullish | Watchlist; research-limit stop | Complete full provisional and contract review |
| 9 | P / RBRK / ZS | Improving directional evidence | 81 / 80 / 78 | Bullish watch | Watchlist; low-volume block | Require participation confirmation, not scanner recurrence alone |
| 10 | TWLO | Strong stock thesis | 80 / 88% / 78% | Bullish | `STOCK_THESIS_ONLY`; earnings/event block | Re-evaluate after verified event window |
| 11 | NVDA / AVGO / AMZN / MSFT | Recurrent current-universe/options context | Mixed | NVDA/MSFT bullish watch; AVGO neutral | No new proposal | Require evidence independent of options activity and duplicate signals |

All ten directly refreshed serious underlyings were active and tradable for the Agentic account. Friday official closes were used only as freshness context; weekend/overnight prints were not treated as new signal sessions.

## Directional Thesis Review

Across the 40 terminal weekly research records, direction was 15 bullish, 3 bullish-watch, and 22 neutral. Nine records reached `OPTIONS_RESEARCH`; the full suitability distribution was 9 `OPTIONS_RESEARCH`, 1 `STOCK_THESIS_ONLY`, 11 `WATCH`, 3 `TEMP_BLOCK`, 15 `NO_DIRECTIONAL_EDGE`, and 1 `REJECT`.

MRVL, CRWD, META, PANW, OKTA, NBIS, and COHR had serious bullish theses. LITE remained bullish but did not complete the full path. P, RBRK, and ZS were bullish-watch because volume did not confirm. TWLO had a bullish stock thesis but no compliant pre-event option expression. NVDA's October 2 underlying read was bullish, but options activity was insufficient to justify new contract research; the earlier NVDA and September 28 META observations were neutral. No bearish thesis qualified, so no long-put proposal was generated.

## Options Setup Review

| Underlying | Contract | DTE / delta | Spread / IV | OI / volume | Setup score | Setup / account result | Primary block |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| META | 2026-11-20 720C | 52 / 0.609 | 2.33% / 43.35% | 1,961 / 309 | 87 | Strong contract; WATCH to avoid duplicate active signal; account fail | Existing active signal group |
| MRVL | 2026-11-20 250C | 52 / 0.640 | 1.53% / 64.17% | 4,697 / 370 | 84 | Qualified; `SHADOW_ONLY_QUALIFIED` | Account-fit premium risk |
| OKTA | 2026-11-20 200C | 53 / 0.574 | 7.86% / 59.18% | 543 / 115 | 74 | WATCH | Option execution quality |
| NBIS | 2026-11-20 230C | 52 / 0.610 | 3.97% / 88.13% | 3,622 / 295 | 72 | WATCH | Option IV/premium risk |
| PANW | 2026-11-06 390C | 39 / 0.556 | 18.21% / 53.52% | 9 / 16 | 62 | WATCH | Option execution quality |
| PANW | 2026-11-06 390C | 35 / 0.624 | 20.12% / 51.37% | 24 / 0 | 62 | WATCH | Option execution quality |
| NBIS | 2026-11-06 250C | 35 / 0.505 | 6.39% / 78.21% | 101 / 46 | 65 | WATCH | Option IV/premium risk |
| COHR | 2026-11-06 320C | 35 / 0.639 | 8.40% / 76.51% | 19 / 7 | 53 | WATCH | Option event risk |

All eight reviewed records were calls in the preferred 30-90 DTE and approximately 0.35-0.70 delta ranges. No put reached contract review. MRVL was the only new setup-quality pass. META's contract quality was stronger numerically, but an active canonical signal prevented duplicate tracking. PANW and OKTA failed execution quality before affordability could matter; NBIS failed long-premium quality; COHR failed event compatibility and liquidity. Repeated PANW and NBIS WATCH records represent new daily observations, not duplicate qualified shadow signals.

## Account-Fit and Shadow-Only Review

Every reviewed contract exceeded the $100 buying power. One-contract premiums ranged from $1,972.50 to $6,000. MRVL's exact frozen premium and maximum contractual loss were $3,275, or 32.75 times account value. The account-fit failure did not rewrite MRVL's underlying score, direction, setup quality, or provisional eligibility.

The correct weekly classifications were 1 new `SHADOW_ONLY_QUALIFIED` setup and 7 WATCH records. There were no `PM_PROPOSAL` records. No qualified setup was replaced by a far-OTM, shorter-DTE, or otherwise inferior cheap contract.

MRVL's first scheduled checkpoint classified `UNDERLYING_WIN_OPTION_WIN`: the underlying gained 0.35% and the option gained 1.01% at 1D. That is one observation, not evidence for threshold changes.

## Options Outcome Review

The canonical qualified sample is 14 setups, all calls and all account-fit failures. There is still no put sample, so bullish and bearish playbooks cannot be compared.

| Horizon | Mature sample | Median underlying return | Median option return | Underlying win rate | Option win rate |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1D | 8 | +0.26% | -1.00% | 62.5% | 50.0% |
| 5D | 8 | -1.17% | -22.85% | 50.0% | 25.0% |
| 10D | 8 | -1.37% | -39.21% | 37.5% | 37.5% |
| 20D | 3 | +1.46% | -21.36% | 66.7% | 0.0% |
| 30D | 4 | +13.94% | -100.00% | 100.0% | 25.0% |

The current latest classification mix is 4 `UNDERLYING_WIN_OPTION_WIN`, 5 `UNDERLYING_WIN_OPTION_LOSS`, 4 `UNDERLYING_LOSS_OPTION_LOSS`, and 1 inconclusive. The most important pattern remains thesis-right/contract-poor at longer horizons: all four 30D underlyings were positive, while only one option was positive. CRWD is a positive counterexample, with option returns of +4.35%, +45.33%, and +41.50% at 1D, 5D, and 10D. Sample sizes remain too small for rule changes.

## Current Universe Review

The official Current Universe is still dated 2026-08-03 and contains temporary-block review dates that expired in August. It should be rebuilt through the governed monthly process rather than patched from this weekly review.

- Strengthening/confirmed research attention: CRWD, META, and PANW; AVGO and NVDA remained recurrent context names but lacked a new weekly directional edge.
- Provisional candidate: MRVL completed the daily provisional Tier 2 path and should be considered in the monthly refresh, not inserted automatically.
- Watchlist candidates deserving full refresh: NBIS, ORCL, COHR, CRDO, and new candidate LITE. VRT's October 2 direct evidence weakened to neutral because price was below its 50-day and 200-day averages.
- Temporary blocks requiring explicit reassessment: AMZN, MSFT, META, PLTR, ANET, AMD, CRWV, and NBIS. Expired dates do not automatically clear the underlying evidence requirement.
- GOOGL's low scanner frequency is not evidence of deterioration; it needs the same governed direct refresh as every other official member.

`state/current_universe.json`, `state/open_theses.json`, and `state/rejected_candidates.json` were not changed.

## Primary Blocking-Rule Analysis

Underlying primary blocks across 40 terminal records, consolidated without secondary-rule double counting:

- Trend/weak-trend: 16.
- Earnings/event risk: 3.
- Low volume/participation: 3.
- Existing active signal group: 3.
- Option execution quality: 3.
- No fresh directional edge: 2.
- Extension: 2.
- Option IV/premium risk: 2.
- Weak relative strength: 1.
- Account-fit premium risk: 1.
- Outside-universe/no provisional promotion: 1.
- Volatility/risk quality: 1.
- Option event risk: 1.
- Options activity alone insufficient: 1.

Options primary blocks across eight canonical weekly setup records were execution quality 3, IV/premium risk 2, existing active signal group 1, account-fit premium risk 1, and event risk 1. Account fit remained secondary for the seven records that did not newly pass setup quality or duplicate controls.

## Score and Threshold Calibration

Weekly Underlying Thesis Score distribution (40 records): highest 84, median 75.0, 90th percentile 82.0, 95th percentile 83.0, 21 records at 75 or above, and 0 at 85 or above.

Weekly Options Setup Score distribution (8 records): highest 87, median 68.5, 90th percentile 84.9, 95th percentile 85.95, 2 records at 75 or above, and 1 at 85 or above. Only MRVL became a new qualified setup; META's higher score was blocked by duplicate-signal governance.

Historical diagnostics show apparent separation between 75-79 and 80-84 score buckets at some horizons, but the mature samples are only 1-6 per bucket/horizon and all qualified records are calls. Contract outcomes also show material time-decay/selection risk even when underlyings are correct. No Underlying Thesis Score, Options Setup Score, DTE, delta, IV, spread, or account-risk threshold was changed.

## State Decisions

- Current Universe: unchanged; monthly refresh recommended.
- Open theses: unchanged; no live thesis was opened.
- Rejected candidates: unchanged; no new repeated permanent reject justified a write.
- Shadow portfolio: one new canonical MRVL 2026-11-20 250C chain, already written by the September 29 daily run.
- Daily ledger: not rewritten by this weekly review. The October 2 run was completed late; the missing October 1 run remains the operational defect.
- Live orders, simulated reviews, modifications, and cancellations: 0.

## Next Research Actions

1. Add automation alerts for delayed finalization and for any target session with no run artifact; preserve same-session evidence when late completion is unavoidable.
2. Preserve the October 1 AMZN and NVDA checkpoints as missed; do not backfill them with later quotes.
3. Complete the governed monthly Current Universe rebuild and explicitly revisit expired temporary blocks.
4. Continue MRVL's 5/10/20/30D checkpoints and CRWD's remaining horizons without duplicate signal groups.
5. Recheck PANW and OKTA only with fresh same-date spreads/OI/volume; recheck NBIS only if IV/premium improves; keep COHR behind its earnings/expiration conflict.
6. Complete LITE's provisional path and participation review; keep P, RBRK, and ZS behind volume confirmation.
7. Accumulate a larger, outcome-complete and eventually two-sided sample before changing thresholds. Do not manufacture bearish trades merely to create a put sample.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
