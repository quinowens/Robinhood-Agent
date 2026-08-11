# Daily Scanner Dry Run - 2026-08-11

Date: 2026-08-11  
Run time: 12:15 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed, modified, canceled, reviewed, or proposed for live execution  
Run ID: `2026-08-11-daily-scanner-dry-run`  
Run status: degraded  
Data completeness: 87%  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: 2 SHADOW-ONLY QUALIFIED OPTIONS SETUPS; NO LIVE TRADE

Primary reason: `META` and `NVDA` passed scoped underlying and long-call setup checks, but both failed account fit because one standard option contract required premium risk above the $100 Agentic account.

Supporting reasons:

- Agentic account `...8691` is a cash account with $100 account value, $100 cash, $100 buying power, no equity positions, no option positions, and no open equity or option orders found in checked open states.
- Broker option capability remains `option_level_2`; strategy scope remains only single-leg long calls and long puts.
- `META` and `NVDA` were the only Tier 2 Current Universe names with positive visible Momentum scanner rows during the run.
- `SPY` and `QQQ` were slightly negative versus 2026-08-10 close, so market context was mixed rather than broadly supportive.
- Options Activity Radar was dominated by low-price, low-market-cap, high-IV rows and did not create direction.
- No simulated order review was called because research and shadow tracking do not require live-order review.

What would change the decision:

- Account value and option buying power increase enough for disciplined long-premium risk sizing.
- A Tier 2 or validated provisional Tier 2 candidate clears event, trend, options setup, and account-fit checks with fresh raw historical validation.
- A specific single-leg long call or put is reviewed with exact contract terms and then explicitly approved by the user before any future live execution.

## Run Health And Tool Coverage

| Area | Result | Notes |
| --- | --- | --- |
| Account preflight | Complete | Agentic account `...8691`, cash account, $100 value and buying power. |
| Portfolio exposure | Complete | No equity positions and no option positions. |
| Open orders | Complete | Open equity and option states checked for today; no open orders found. |
| Saved scanner resolution | Complete | All configured scanner names and IDs matched exactly. |
| Scanner execution | Complete, persistence degraded | Three configured scanners ran; visible rows and totals persisted. |
| Direct earnings data | Complete for decision candidates | Used for Tier 2 names and scanner/event candidates. |
| Enrichment | Partial | Quotes, fundamentals, financials, earnings, chains, instruments, and option quotes pulled; fresh raw historicals were not available in this run. |
| Market context | Partial | SPX/NDX quoted; RUT restricted and DJI not returned by `get_indexes`. |
| Options chains/contracts | Scoped | Pulled only META and NVDA chains, selected instruments, and selected quotes. |

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Retried calls | 0 |
| Raw rows persisted | visible rows plus scanner totals |
| Deduplicated decision candidates | 24 |
| Candidates with terminal status | 24 |
| Completeness percentage | 87% |

Publish decision: degraded daily log; do not publish or mutate Current Universe from this daily run.

## Market / Index Context

| Instrument | Latest observed | Prior / context | Interpretation |
| --- | ---: | --- | --- |
| SPX | 7747.11 at 2026-08-11 10:31 CT | Live index quote | Slightly mixed broad tape. |
| NDX | 29603.506 at 2026-08-11 10:31 CT | Live index quote | Growth not strongly risk-on intraday. |
| SPY | 772.39 vs 773.03 prior close | -0.08% intraday approx. | Slightly negative. |
| QQQ | 720.16 vs 720.87 prior close | -0.10% intraday approx. | Slightly negative. |
| RUT | N/A | Robinhood MCP restricted RUT quotes | Missing; not estimated. |
| DJI | N/A | `get_indexes` did not return DJI | Missing; not estimated. |

Market-regime validation: mixed enough to require selective evidence and account fit; not hostile enough to prevent shadow research.

## Scanner Summary

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 158 | `% Change desc` | success |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 43 | `Implied volatility desc` | success |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 316 | `Earnings date desc` | success |

Scanner quality:

- Momentum produced useful large-cap context, but many top rows were outside Current Universe.
- Options Activity remained noisy: top rows included `FNGR`, `ARQ`, `SITC`, `PLBY`, `ABAT`, and `QMCO`, mostly low-cap or low-price high-IV names.
- Earnings Risk Radar remained useful as a risk filter, not as a trade source.

## Underlying Candidate Table

| Symbol | Sources | Latest quote / event | Status | Primary block |
| --- | --- | --- | --- | --- |
| META | Tier 2, Momentum | 608.91 vs 594.92 prior; next tentative 2026-10-28 PM | SHADOW_ONLY_QUALIFIED | `account_risk` |
| NVDA | Tier 2, Momentum | 219.30 vs 217.55 prior; earnings 2026-08-26 PM | SHADOW_ONLY_QUALIFIED | `account_risk` |
| GOOGL | Tier 2 | 351.02 vs 357.52 prior; next tentative 2026-10-28 PM | NO_DIRECTIONAL_EDGE | `weak_relative_strength` |
| AMZN | Tier 2 | 273.13 vs 278.09 prior; reported 2026-07-30 PM | WATCH | `weak_relative_strength` |
| MSFT | Tier 2 | 501.51 vs 506.06 prior; reported 2026-07-29 PM | WATCH | `weak_relative_strength` |
| CRWD | Tier 2 | 222.38 vs 225.16 prior; earnings 2026-08-26 PM | TEMP_BLOCK | `blocked_by_earnings` |
| PANW | Tier 2 | 382.69 vs 385.04 prior; earnings 2026-09-01 PM | WATCH | `financial_quality_caution` |
| AVGO | Tier 2 | 420.68 vs 422.40 prior; earnings 2026-09-02 PM | WATCH | `correlation_cluster_limit` |
| COHR | Watchlist, Momentum, Earnings Risk | earnings 2026-08-12 PM | TEMP_BLOCK | `blocked_by_earnings` |
| SE | Momentum | +13.98%, outside universe | WATCH | `outside_current_universe` |
| FNGR | Options Activity | $0.2899, IV 3.85, $17.7M cap | REJECT | `penny_stock_or_microcap` |
| QMCO | Options Activity | +53.5%, $462.7M cap, IV 1.30 | REJECT | `penny_stock_or_microcap` |

## Options Setup Table

| Rank | Underlying | Direction | Contract | DTE | Strike | Options Setup Score | Account Fit | Decision | Primary Block |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| 1 | NVDA | bullish | 2026-09-18 220C | 38 | 220 | 80 | FAIL | SHADOW_ONLY_QUALIFIED | `account_risk` |
| 2 | META | bullish | 2026-09-18 610C | 38 | 610 | 78 | FAIL | SHADOW_ONLY_QUALIFIED | `account_risk` |

NVDA selected shadow setup: 2026-09-18 220 call, bid 10.70 / ask 10.80 / midpoint 10.75, spread 0.93% of midpoint, delta 0.5235, IV 0.3818, open interest 40,761, volume 2,338, breakeven 230.75. One contract has $1,075 premium allocation and maximum contractual loss.

META selected shadow setup: 2026-09-18 610 call, bid 26.25 / ask 26.95 / midpoint 26.60, spread 2.63% of midpoint, delta 0.5153, IV 0.3476, open interest 1,860, volume 404, breakeven 636.60. One contract has $2,660 premium allocation and maximum contractual loss.

No cheap far-OTM or short-dated substitutions were considered.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was made.

- `SE`, `CRCL`, `CHYM`, `DKNG`, and `NBIS` had visible Momentum strength but did not receive full provisional Tier 2 validation.
- `COHR` remains watchlist only and is blocked by verified earnings on 2026-08-12 PM.
- Options Activity-only rows were rejected or watched unless independently supported by universe membership, tradability, fundamentals, trend, liquidity, and event checks.

## Blocked / Rejected Names

| Group | Symbols | Primary / secondary blocks |
| --- | --- | --- |
| Account-fit failures | META, NVDA | `account_risk`; standard contracts exceed $100 buying power |
| No directional edge / watch | GOOGL, AMZN, MSFT | `weak_relative_strength`; negative day versus mixed market |
| Earnings or event blocks | CRWD, COHR | `blocked_by_earnings`; direct earnings dates verified |
| Watch / caution | PANW, AVGO | `financial_quality_caution`, `correlation_cluster_limit` |
| Outside-universe scanner leaders | SE, CRCL, CHYM, DKNG, NBIS | `outside_current_universe`; no full provisional Tier 2 validation |
| Permanent-style rejects this run | FNGR, ARQ, SITC, PLBY, ABAT, QMCO | low cap / low price / high IV / options activity alone insufficient |

## Missing / Conflicting Data

- Fresh raw equity historicals were not available, so 50/200-day SMA and exact RS calculations were not independently recomputed.
- Full scanner payload export remains degraded by large connector responses; visible rows, scanner totals, filters, and source tags were preserved.
- `RUT` quotes were restricted; `DJI` did not resolve via `get_indexes`.
- `META` extension-block clearance was not written to `state/current_universe.json`; daily evidence only supports proposal-only/shadow classification.

## State-File Decision

| File | Decision | Reason |
| --- | --- | --- |
| `state/current_universe.json` | unchanged | Daily run may not rewrite official Current Universe. |
| `state/open_theses.json` | unchanged | Shadow setups are not live theses. |
| `state/rejected_candidates.json` | unchanged | New low-quality rows were not yet repeated enough for state update. |

## Portfolio Manager Recommendation

Decision: SHADOW_ONLY_QUALIFIED; NO LIVE TRADE

Next action:

1. Track `META` 2026-09-18 610C and `NVDA` 2026-09-18 220C as shadow-only qualified setups.
2. Keep `CRWD` and `COHR` blocked by verified earnings timing.
3. Keep `GOOGL`, `AMZN`, and `MSFT` in watch/no-directional-edge status until relative strength improves.
4. Continue rejecting Options Activity-only low-cap/high-IV rows unless independent quality evidence appears.

## Shadow-Tracking Decision

Opened one new hypothetical option shadow-tracking record for `META` and refreshed `NVDA` shadow context with a current 2026-09-18 220C setup. These are not live orders, reviewed orders, or approval requests. Terminal research records preserve primary blocking rules for 5/10/20-day opportunity-cost review.

## Execution Statement

No order review, order placement, order cancellation, scanner modification, watchlist modification, or option exercise tool was called.

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
