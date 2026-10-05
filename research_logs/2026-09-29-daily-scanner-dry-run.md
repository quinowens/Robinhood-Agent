# Daily Scanner Dry Run — 2026-09-29

Date: 2026-09-29  
Run time: 15:30-15:39 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed, modified, canceled, reviewed, or submitted  
Run ID: `2026-09-29-daily-scanner-dry-run`  
Run status: `DEGRADED_COMPLETE`  
Strategy version: 2.0.2  
Strategy mode: `options_primary`

## Executive Decision

Decision: **NO LIVE TRADE / ONE NEW SHADOW-ONLY QUALIFIED SETUP**.

MRVL completed the provisional Tier 2 path and its 2026-11-20 250C passed contract-quality review. The option is hypothetical only: one contract requires about $3,275, far above the $100 account value and buying power, so the setup is `SHADOW_ONLY_QUALIFIED` and has been frozen for 1/5/10/20/30-trading-day tracking.

META's 2026-11-20 720C was a strong contract, but a canonical META bullish signal from September 9 is still active through its forward-evaluation window; no duplicate shadow signal was created. NBIS remained `WATCH` because the 230C carried about 88.13% IV and a 3.97% midpoint spread.

## Run Health and Tool Coverage

| Metric | Result |
| --- | --- |
| Account/tool preflight | Complete |
| Saved scanners resolved | 3 of 3 matched by name, ID, filters, and sort |
| Scanner executions | 3 of 3 succeeded |
| Raw rows persisted | 504 |
| Deduplicated visible symbols | 486 |
| Named terminal records | 15 (3.09% visible coverage) |
| Option checkpoint | Due 0; captured 0; updated 0; missed 0 — successful no-op |
| Option setup records | 3 |
| New option shadow trades | 1 (MRVL 250C) |
| Validation | Passed with warnings; 0 errors/orphans |
| Live order actions | 0 |

Publish status is degraded because Momentum and Earnings Risk were capped at 200 visible rows, only the progressive finalist set received direct enrichment, and full financial statements, breadth, formal sector participation, individual trade-history P/L, and option historical bars were unavailable.

## Account and Portfolio Preflight

- Agentic account: `••••8691`; cash account; broker options level 2.
- Account value / cash / buying power / option buying power: $100 / $100 / $100 / $100.
- Equity positions: 0. Option positions: 0.
- Open equity orders: 0. Open option orders: 0.
- Three-month realized P/L: $0; closing trades: 0.
- Current open premium risk: $0. No drawdown breaker or kill switch was evident.
- Strategy permission remains limited to single-leg long calls and long puts.

## Market and Index Context

- SPX: 7,670.84; NDX: 30,339.33; VIX: 16.04.
- SPY retained close: 765.61; above 20-day (765.16), 50-day (762.01), and 200-day (730.44) averages; 50-day slope positive.
- QQQ retained close: 736.53; above 20-day (721.88), 50-day (713.48), and 200-day (684.66) averages; 50-day slope positive.
- Market Health Score: 65, **Constructive**.
- Missing breadth and formal sector participation prevented a stronger classification. Selective bullish research is allowed, but it does not override extension, liquidity, IV, or account-risk rules.

## Scanner Summary

| Scanner | Scan ID | Total | Visible | Sort | Quality read |
| --- | --- | ---: | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 398 | 200 | % Change desc | Useful large-cap movement discovery; capped |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 104 | 104 | Implied volatility desc | Useful context; high-IV tail remained noisy |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 250 | 200 | Earnings date desc | Effective event filter; capped |

The leading momentum rows were CCL (+13.1%), BE (+11.1%), RCL (+7.4%), LITE (+6.0%), and SMMT (+5.9%). Cross-scanner attention included BE, ORCL, CCL, META, AMZN, NVDA, and AVGO. Options activity did not add direction or underlying-score points.

## Underlying Candidate Table

| Rank | Symbol | Sources | Score / completeness / confidence | Direction | Tier / eligibility | Final class | Primary block |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | META | Momentum + Options Activity | 84 / 90% / 84% | Bullish | Tier 2 / eligible | WATCH | Existing active signal group |
| 2 | MRVL | Momentum | 82 / 88% / 80% | Bullish | Provisional Tier 2 / eligible | SHADOW_ONLY_QUALIFIED | Account-fit premium risk |
| 3 | NBIS | Momentum | 79 / 85% / 75% | Bullish | Watchlist / not promoted | WATCH | Option IV/premium risk |
| 4 | LITE | Momentum | 78 / 86% / 76% | Bullish | Watchlist | WATCH | Provisional path incomplete |
| 5 | BE | Momentum + Options Activity | 77 / 88% / 84% | Bullish | Watchlist / extension-blocked | TEMP_BLOCK | 11% one-day extension |
| 6 | AMAT | Momentum | 75 / 87% / 74% | Bullish watch | Watchlist | WATCH | Weak 60-day trend |
| 7 | COHR | Momentum | 69 / 86% / 79% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Trend |
| 8 | SMMT | Momentum | 68 / 84% / 78% | Neutral | Watchlist | WATCH | Volatility/risk quality |
| 9 | GLW | Momentum | 67 / 87% / 80% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Trend |
| 10 | CCL | Momentum + Options Activity + Earnings Risk | 66 / 90% / 91% | Neutral | Earnings-blocked | TEMP_BLOCK | Same-day earnings |
| 11 | ORCL | Momentum + Options Activity | 64 / 88% / 84% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Trend |
| 12 | DASH | Momentum | 61 / 86% / 82% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Trend |
| 13 | RCL | Momentum | 60 / 88% / 84% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Trend |
| 14 | CVNA | Momentum | 58 / 87% / 85% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Trend |
| 15 | FICO | Options Activity | 54 / 88% / 94% | Neutral | Extension-blocked | NO_DIRECTIONAL_EDGE | 26.6% event decline |

## Options Setup Table

| Rank | Underlying | Contract | DTE | Bid / Ask / Mid | Delta | Spread | OI / Vol | IV | Setup score | Account fit | Final |
| ---: | --- | --- | ---: | --- | ---: | ---: | --- | ---: | ---: | --- | --- |
| 1 | META | 2026-11-20 720C | 52 | 59.30 / 60.70 / 60.00 | 0.609 | 2.33% | 1,961 / 309 | 43.35% | 87 | FAIL | WATCH — active signal |
| 2 | MRVL | 2026-11-20 250C | 52 | 32.50 / 33.00 / 32.75 | 0.640 | 1.53% | 4,697 / 370 | 64.17% | 84 | FAIL | SHADOW_ONLY_QUALIFIED |
| 3 | NBIS | 2026-11-20 230C | 52 | 34.60 / 36.00 / 35.30 | 0.610 | 3.97% | 3,622 / 295 | 88.13% | 72 | FAIL | WATCH |

MRVL's frozen one-contract premium and maximum contractual loss are $3,275, or 32.75 times account value. Planned trade risk defaults to maximum contractual loss because no deterministic premium-stop sizing rule is adopted. No cheaper, farther-OTM, or shorter-DTE contract was substituted.

## Provisional Tier 2 Review

MRVL completed the run-scoped provisional Tier 2 path: score 82, completeness 88%, confidence 80%, verified tradability/liquidity/earnings timing, constructive directional evidence, and a qualified option contract. It remains a proposal-only research classification until the next governed universe refresh.

NBIS did not complete promotion because its selected contract failed IV/premium and spread quality. LITE was not promoted because the configured top-three contract-research limit was reached before a full Portfolio Manager proposal could be completed.

## Blocked and Rejected Names

| Symbol(s) | Primary block | Secondary blocks |
| --- | --- | --- |
| MRVL | Account-fit premium risk | Small-account validation mode |
| META | Existing active signal group | Account-fit premium risk |
| NBIS | Option IV/premium risk | Spread quality; account-fit premium risk |
| CCL | Same-day earnings / unsettled post-event review | Extension; weak medium-term trend |
| BE, FICO | Unconfirmed extension | Valuation or damaged trend |
| AMAT, COHR, GLW, ORCL, DASH, RCL, CVNA | Trend / relative strength | Outside Current Universe where applicable |
| LITE | Provisional path incomplete | Negative trailing PE; research-limit stop |
| SMMT | Volatility/risk quality | Negative earnings; incomplete trend |

All 15 candidates received 5/10/20-day opportunity-cost tracking seeds. Only the primary blocking rule receives attribution credit or blame.

## Missing or Conflicting Data

- Full financial statements, option historical bars, individual trade-history P/L, breadth, and formal sector-participation data were unavailable.
- Momentum and Earnings Risk results were capped.
- Daily historical bars included an interpolated September 29 placeholder for some symbols; the final regular-hours quote controlled signal prices, while completed bars controlled moving-average calculations.
- Several future earnings dates are tentative. AMAT's November 12 date and GLW's October 27 date were verified; MRVL, META, NBIS, and most others were tentative.
- Scanner prices and official/live quotes can differ by capture time; final option quotes were captured at the end of the regular session.

## Scanner Quality

Momentum remained useful for large-cap movement discovery. Options Activity was useful only after permanent market-cap/liquidity filtering and independent directional evidence. Earnings Risk correctly identified CCL's same-day event and MU's near-term report. The permanent-first filter prevented microcap/high-IV rows from consuming full enrichment calls.

## Option Setup Quality

MRVL passed on 52-DTE horizon fit, 0.64 delta, 1.53% spread, and substantial open interest/volume, with elevated but still reviewable 64.17% IV. META had the highest contract score but was not duplicated while an active canonical signal remains. NBIS failed on long-premium cost quality: high IV and a wider spread outweighed otherwise acceptable delta and open interest.

## Mandatory Prospective Option Checkpoint

`python3 scripts/update_option_outcomes.py --list-due-option-checkpoints --as-of 2026-09-29` returned:

- Due: 0
- Captured: 0
- Updated: 0
- Missed: 0
- Status: successful no-op

No unrelated contracts were pulled for checkpointing, and no later quote was assigned to an earlier target date.

## Outcome Analytics and Validation

- Outcome analytics, strategy diagnostics, and integrity checks were regenerated after the checkpoint.
- Repository validation passed.
- Integrity: `PASS_WITH_WARNINGS`; 14 complete qualified chains; 0 errors; 0 orphaned shadow records; 0 orphaned option outcomes; 0 update failures.
- 29 older outcome windows remain overdue or permanently unavailable, mostly because option history is unsupported or target-session snapshots were not captured. `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE` remains an allowed permanent status.
- Four historical scheduled-run ledger gaps remain an existing warning.
- No strategy threshold or rule change was applied.

## State-File Decision

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged.
- `state/rejected_candidates.json`: unchanged.

The daily run logged MRVL as provisional Tier 2 in its research record but did not rewrite the official universe. No new repeated permanent reject justified a state-file change.

## Portfolio Manager Recommendation

Decision: **NO LIVE TRADE**.

The account remains a $100 validation account with no positions or open orders. MRVL is a valid shadow-only setup but cannot fit buying power or premium-risk limits. META was not duplicated, and NBIS failed setup quality before account fit could matter.

## Shadow-Tracking Decision

One new canonical shadow chain was created for MRVL 2026-11-20 250C:

- Option setup: `optsetup-2026-09-29-MRVL-20261120-250C`
- Shadow trade: `optshadow-2026-09-29-MRVL-20261120-250C`
- Outcome record: `optoutcome-2026-09-29-MRVL-20261120-250C`
- Checkpoints: 1/5/10/20/30 trading days
- Frozen midpoint: $32.75; contract premium: $3,275

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.

