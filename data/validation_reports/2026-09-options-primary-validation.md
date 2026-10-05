# September 2026 Options-Primary Validation

As-of date: 2026-10-03  
Market data through: 2026-10-02  
Mode: Research-only / proposal-only / shadow-trading

## Decision

The v2.0 options-primary strategy is producing useful research signals, but not enough reliable contract outcomes to change rules. September produced 18 canonical option setup records: 8 `SHADOW_ONLY_QUALIFIED` and 10 `WATCH`. Every setup failed account fit in the $100 account, and all setups were calls; put performance remains untested.

The most important observed distinction is thesis quality versus contract quality. At 30D, all four mature underlyings were positive, while only one option was positive and the median option return was -100%. Long-premium expiration and pricing can defeat a correct directional thesis.

## Current Monthly Finalists

| Underlying | Selected contract | DTE | Delta | Bid / Ask / Mid | Spread | IV | OI / Vol | Score | Decision | Primary block |
| --- | --- | ---: | ---: | --- | ---: | ---: | --- | ---: | --- | --- |
| RBRK | 2026-11-20 110C | 49 | 0.689 | 14.30 / 14.90 / 14.60 | 4.11% | 57.53% | 150 / 7 | 80 | WATCH | Option execution quality |
| U | 2026-11-20 45C | 49 | 0.507 | 3.60 / 3.95 / 3.775 | 9.27% | 68.87% | 3,629 / 509 | 75 | WATCH | Option execution quality |
| TWLO | 2026-12-18 300C | 77 | 0.550 | 34.00 / 36.70 / 35.35 | 7.64% | 69.15% | 310 / 11 | 73 | WATCH | Option execution quality |

No selected contract cleared setup quality. Account fit also failed: one-contract premiums were $1,460, $377.50, and $3,535 versus $100 option buying power and a $1 planned-risk cap. No cheaper far-OTM or short-DTE substitute was selected.

## September Setup Distribution

- Calls / puts: 18 / 0.
- DTE: 10 in 30–45, 7 in 46–60, 1 in 61–90.
- Setup quality: 7 qualified, 1 qualified with degraded quote provenance, 10 watch.
- Final decisions: 8 shadow-only qualified, 10 watch, 0 PM proposals.
- Account fit: 18 failed, 0 passed.
- Qualified preferred-contract premium: median $1,832.50; 75th percentile $2,707.50.
- Current-rule account size required: median $18,325 at the 10% premium-allocation cap or $183,250 at the 1% planned-risk cap; 75th percentile $27,075 or $270,750 respectively.

The generated monthly analytics file contains mixed legacy percent-unit conventions in its raw funding-cap estimate. The figures above apply the current source-of-truth caps directly and supersede that raw legacy-normalized estimate.

## Outcome Evidence

| Horizon | Mature sample | Median underlying return | Median option return | Underlying win rate | Option win rate |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1D | 8 | +0.26% | -1.00% | 62.5% | 50.0% |
| 5D | 8 | -1.17% | -22.85% | 50.0% | 25.0% |
| 10D | 8 | -1.37% | -39.21% | 37.5% | 37.5% |
| 20D | 3 | +1.46% | -21.36% | 66.7% | 0.0% |
| 30D | 4 | +13.94% | -100.00% | 100.0% | 25.0% |

Thirty-day classifications were three `UNDERLYING_WIN_OPTION_LOSS` and one `UNDERLYING_WIN_OPTION_WIN`. DTE, delta, IV, spread, scanner-source, and market-regime comparisons remain directional because samples are small and entirely call-side.

## Integrity and Checkpoints

The 2026-10-03 due manifest contained zero option IDs, a successful no-op. During September, one NVDA checkpoint was missed on 2026-09-14 and one legacy synthetic NVDA identifier returned no quote on 2026-09-21. Neither was backfilled later. The integrity audit reports 24 overdue windows as permanent source limitations, mostly `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE`, with zero update failures.

## Rule Decision

No thresholds, DTE bands, delta preferences, spread rules, or structure permissions changed. More mature observations, a meaningful put sample, and consistent current-schema cap units are required before optimization.

No live orders were placed, modified, canceled, reviewed, or submitted.

