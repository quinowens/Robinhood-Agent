# Daily Research Log

Date: 2026-09-24  
Run time: 18:04 CT through deferred completion  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed  
Run ID: 2026-09-24-daily-scanner-dry-run  
Run status: degraded complete  
Data completeness: 100% for 15 named candidates; 3.92% terminal coverage of 383 connector-visible deduplicated symbols  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: NO NEW OPTIONS PROPOSAL

Primary reason: no September 24 option contract snapshot with contemporaneous bid/ask, Greeks, IV, and liquidity was retained before the calendar rolled to September 25.

Supporting reasons:

- META and AMD had the strongest qualified bullish underlying evidence, but a September 25 option quote cannot be frozen as a September 24 entry snapshot.
- P, AKAM, and MRNA were temporarily blocked by extension; AKAM's scanner price of 134.13 materially exceeded its settled 110.41 close.
- MU was inside the five-trading-day blackout for verified September 30 earnings.
- The $100 account imposes a $1 single-trade planned-risk cap; normal 30-90 DTE contracts are unlikely to fit, and no cheap far-OTM or short-DTE substitution was attempted.

What would change the decision:

- A fresh post-session run that captures option chains and quotes on the same trading date for META, AMD, or another qualified finalist.
- Settled follow-through for extended names with acceptable volume and risk/reward.
- A preferred long call or put that passes setup quality and the account's premium-risk rules.

## Run Health / Tool Coverage

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Raw scanner rows persisted | 403 |
| Deduplicated visible symbols | 383 |
| Named candidates with terminal status | 15 |
| Named candidate completeness | 100% |
| Visible-symbol terminal coverage | 3.92% |
| New option chains researched | 0 |
| Due option checkpoints | 1 |
| Due option quotes captured | 1 |
| Due outcome records updated | 1 |
| Missed due option captures | 0 |

Publish decision: degraded complete. The scanners matched and ran, raw rows were preserved before normalization, and all 15 named candidates received terminal classifications. The run is degraded because Momentum results were capped at 200 of 398 matches, fewer than 90% of visible symbols received terminal records, full financial statements and option historicals were unavailable, and the run did not preserve a same-date option setup snapshot before rollover.

## Market / Index Context

| Market | September 24 close | Trend read |
| --- | ---: | --- |
| SPY | 767.18 | Above 50-day (~761) and 200-day (~718) averages; positive 50-day slope |
| QQQ | 741.10 | Above 50-day (~712) and 200-day (~665) averages; positive 50-day slope |
| SPX | 7,704.13 | September 24 venue observation |
| NDX | 30,478.86 | September 24 venue observation |
| Breadth / VIX | N/A | Not exposed in retained run data |

Market Health Score: 70/100, Constructive. Benchmark trends were supportive, while unavailable breadth and volatility readings capped confidence.

## Scanner Summary

| Scanner | Scan ID | Total Matches | Rows Returned | Sort | Resolution |
| --- | --- | ---: | ---: | --- | --- |
| Momentum Candidates | 26cdeb14-da13-493f-b0c6-783468971a16 | 398 | 200 | % Change desc | exact match |
| Options Activity Radar | 7068db65-2a47-470c-bde9-94d66f36b806 | 120 | 120 | Implied volatility desc | exact match |
| Earnings Risk Radar | 737924f1-e94f-4ad4-ba98-6c12fcaafaa9 | 83 | 83 | Earnings date desc | exact match |

Top momentum rows included AKAM, P, RVTY, MRNA, ILMN, TEM, NBIS, RKLB, AFRM, IONQ, and META. Cross-scanner attention appeared in P, NBIS, RKLB, IONQ, META, AMD, AMZN, and MU. Options activity was used only as context and never as direction.

## Underlying Candidate Table

| Rank | Symbol | Sources | Thesis Score | Completeness | Direction | Tier / Eligibility | Final Status | Primary Block |
| ---: | --- | --- | ---: | ---: | --- | --- | --- | --- |
| 1 | META | Momentum, Options Activity | 84 | 91% | bullish | Tier 2 / eligible | WATCH | missing same-date option snapshot |
| 2 | AMD | Momentum, Options Activity | 82 | 90% | bullish | provisional Tier 2 / eligible | WATCH | missing same-date option snapshot |
| 3 | P | Momentum, Options Activity | 80 | 90% | bullish | provisional Tier 2 / blocked | TEMP_BLOCK | unconfirmed extension |
| 4 | MU | all three scanners | 80 | 92% | bullish blocked | Watchlist | TEMP_BLOCK | earnings blackout |
| 5 | RVTY | Momentum | 79 | 89% | bullish | provisional Tier 2 / eligible | WATCH | missing option snapshot |
| 6 | ILMN | Momentum | 79 | 89% | bullish | provisional Tier 2 / eligible | WATCH | missing option snapshot |
| 7 | TEM | Momentum | 77 | 87% | bullish | provisional Tier 2 / eligible | WATCH | missing option snapshot |
| 8 | NBIS | Momentum, Options Activity | 77 | 88% | bullish watch | Watchlist | WATCH | outside Current Universe |
| 9 | MRNA | Momentum | 76 | 88% | bullish blocked | Watchlist | TEMP_BLOCK | unconfirmed extension |
| 10 | AKAM | Momentum | 75 | 90% | bullish blocked | Watchlist | TEMP_BLOCK | unsettled after-hours move |
| 11 | RKLB | Momentum, Options Activity | 74 | 87% | neutral | Watchlist | WATCH | trend failure |
| 12 | IONQ | Momentum, Options Activity | 73 | 87% | neutral | Watchlist | WATCH | trend failure |
| 13 | GOOGL | Momentum | 70 | 91% | neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | no fresh edge |
| 14 | AMZN | Momentum, Options Activity | 69 | 91% | neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | no fresh edge |
| 15 | AFRM | Momentum | 66 | 87% | neutral | Watchlist | WATCH | trend failure |

## Options Setup Table

No new contract was scored. There were zero PM_PROPOSAL, SHADOW_ONLY_QUALIFIED, QUALIFIED_BUT_NOT_ACCOUNT_FIT, or new option WATCH records. Pulling September 25 quotes would contaminate a September 24 signal, so the options workflow stopped before chain work.

## Prospective Option Checkpoint

| Due record | Horizon | Option return | Underlying return | Result |
| --- | ---: | ---: | ---: | --- |
| NVDA 2026-09-18 225C | 30D | -100.00% | +0.51% | underlying win / option loss |

Checkpoint summary: due 1, captured 1, updated 1, missed 0. The expired contract had no live market and was valued at zero through the prospective checkpoint path. Older uncaptured horizons remain OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE and are permanent, non-retryable warnings.

## Provisional Tier 2 Review

AMD, RVTY, ILMN, and TEM met the run-scoped underlying threshold for provisional Tier 2. P also met the quality threshold but was temporarily blocked by extension. These classifications do not rewrite the monthly Current Universe.

- AMD: strongest provisional candidate; trend, relative strength, and volume aligned, but no same-date contract snapshot remained.
- RVTY and ILMN: strong trend and relative strength; RVTY lacked 1.5x volume confirmation, and both lacked a reproducible option snapshot.
- TEM: trend and volume qualified, while negative earnings quality reduced confidence.
- P: high-quality momentum evidence, but the move exceeded 10% and requires settled follow-through.

## Blocked / Rejected Names

| Symbol / bucket | Primary reason | Secondary reasons | Decision |
| --- | --- | --- | --- |
| META, AMD, RVTY, ILMN, TEM | missing same-date option snapshot | account fit not evaluated; outside monthly universe where applicable | WATCH |
| P, MRNA | unconfirmed extension | outside Current Universe | TEMP_BLOCK |
| AKAM | unsettled after-hours move | conflicting price timestamps; outside Current Universe | TEMP_BLOCK |
| MU | earnings blackout | outside Current Universe | TEMP_BLOCK |
| NBIS | outside Current Universe | valuation risk; missing option snapshot | WATCH |
| RKLB, IONQ, AFRM | trend failure | outside Current Universe | WATCH |
| GOOGL, AMZN | no fresh directional edge | trend weakness; options activity insufficient for AMZN | NO_DIRECTIONAL_EDGE |
| Visible microcap options/earnings rows | penny stock or microcap | insufficient liquidity; high IV/event risk | REJECT before enrichment |

## Missing / Conflicting Data

- Full financial statements, option historicals, technical-indicator endpoint, and individual P/L trade history were unavailable.
- Momentum exposed 200 of 398 matching rows.
- Daily historical data ended at the prior settled session during the September 24 run; settled quote-close records were used for September 24 prices.
- AKAM's scanner/all-day price materially exceeded the settled close, so its move was blocked as unsettled.
- No same-date contract quote snapshot was retained for new finalists before rollover.
- Breadth and VIX were unavailable.

## Scanner Quality

Momentum surfaced several liquid large-cap candidates, but extension and weak confirmation reduced immediate option suitability. Options Activity Radar remained noisy at the top with microcap/high-IV names, though its cross-confirmation improved attention prioritization for META, AMD, P, NBIS, RKLB, and IONQ. Earnings Risk Radar correctly supported the MU blackout.

## Option Setup Quality

No new setup-quality score was created because reproducible same-date contract evidence is mandatory. The due NVDA checkpoint again showed why direction and contract selection must be judged separately: the underlying finished slightly positive at 30D while the expired call lost all premium.

## State-File Decision

state/current_universe.json unchanged.  
state/open_theses.json unchanged.  
state/rejected_candidates.json unchanged; no newly observed permanent reject met the repeated-reject threshold.

## Portfolio Manager Recommendation

Decision: NO TRADE

Account snapshot: $100 total value, $100 cash, $100 buying power, zero equity positions, zero option positions, zero open equity orders, zero open option orders, and zero realized P/L over three months.

No specific new contract reached PM review. Current open premium risk is $0 and post-proposal premium risk remains $0. No drawdown breaker or kill switch was triggered.

## Shadow-Tracking Decision

No new option shadow trade was opened. Fifteen underlying signal-outcome records were scheduled, including blocked and no-trade classifications. The one due option outcome checkpoint was captured and updated.

## Validation

Repository validation passed. Data integrity returned PASS_WITH_WARNINGS with zero errors, zero orphaned outcome records, zero orphaned shadow records, and 13 complete qualified chains. Outcome health remains degraded because 28 older windows are permanently unavailable under the source's option-history limitation; there were no update failures.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.

