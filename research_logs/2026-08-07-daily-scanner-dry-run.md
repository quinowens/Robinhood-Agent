# Daily Scanner Dry Run - 2026-08-07

Date: 2026-08-07  
Run time: 10:34 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed, modified, canceled, reviewed, or proposed for live execution  
Run ID: `2026-08-07-daily-scanner-dry-run`  
Run status: degraded  
Data completeness: 86%  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: 1 SHADOW-ONLY QUALIFIED OPTIONS SETUP; NO LIVE TRADE

Primary reason: `NVDA` passed underlying research, options suitability, and contract scoring, but failed account fit because one contract required $977.50 premium allocation versus a $100 account.

Supporting reasons:

- The Agentic account `...8691` had $100 account value, $100 cash/buying power, no equity positions, no option positions, and no queued/confirmed/partially-filled equity or option orders.
- The Agentic account initially required app approval; after the user approved Level 2 in the Robinhood app, a fresh `get_accounts` call verified `option_level_2`.
- Broker capability now permits buying calls and puts, covered calls, cash-covered puts, and exercise; spreads are unavailable. Strategy scope remains long calls and long puts only.
- Current Universe has no Tier 1 names. Tier 2 names remain research-valid; account fit failed separately and did not rewrite underlying eligibility.
- Top scanner momentum rows were mostly outside Current Universe and were post-earnings gap moves from 2026-08-06 PM reports.
- Options Activity Radar was again noisy at the top, led by low-market-cap, low-price, high-IV rows.

What would change the decision:

- Account value and option buying power increase enough for disciplined long-premium risk sizing.
- A Tier 2 or validated provisional Tier 2 candidate clears event, trend, setup-quality, and account-fit checks with fresh raw history.
- A specific single-leg long call or put is reviewed with exact contract terms and then explicitly approved by the user before any future live execution.

## Run Health And Tool Coverage

| Area | Result | Notes |
| --- | --- | --- |
| Account preflight | Complete | Agentic account `...8691`, cash account, $100 value and buying power. |
| Portfolio exposure | Complete | No equity positions, no options positions, no checked open equity/options orders. |
| Options access | Complete after user action | Fresh `get_accounts` verified `option_level_2`. |
| Saved scanner resolution | Complete | All configured scanner names and IDs matched exactly. |
| Scanner execution | Complete, persistence degraded | Three configured scanners ran; visible rows and totals persisted. |
| Direct earnings data | Complete for decision candidates | Used for Tier 2 names and scanner leaders. |
| Enrichment | Partial | Quotes, fundamentals, financials, and earnings pulled; some financial rows returned null. |
| Market context | Partial | SPX/NDX resolved and quoted; RUT restricted and DJI not returned. |
| Options chains/contracts | Scoped | Pulled only NVDA chain, selected instruments, and selected quotes. |

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Retried calls | 0 |
| Raw rows persisted | visible rows plus scanner totals |
| Deduplicated decision candidates | 31 |
| Candidates with terminal status | 31 |
| Completeness percentage | 86% |

Publish decision: degraded daily log; do not publish or mutate Current Universe from this daily run.

## Market / Index Context

| Instrument | Latest observed | Prior / context | Interpretation |
| --- | ---: | --- | --- |
| SPX | 7759.01 at 2026-08-07 10:34 CT | Live index quote | Broad market constructive intraday. |
| NDX | 29731.0516 at 2026-08-07 10:34 CT | Live index quote | Growth leadership constructive intraday. |
| SPY | 773.48 vs 768.56 prior close | +0.64% intraday approx. | Broad ETF positive. |
| QQQ | 723.195 vs 714.65 prior close | +1.20% intraday approx. | Nasdaq proxy positive. |
| RUT | N/A | Robinhood MCP restricted RUT quotes | Missing; not estimated. |
| DJI | N/A | `get_indexes` did not return DJI | Missing; not estimated. |

Market-regime validation: constructive enough for research, but not sufficient to override account, earnings, universe, trend, or options-access rules.

## Scanner Summary

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 180 | `% Change desc` | success, raw persistence degraded |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 61 | `Implied volatility desc` | success |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 306 | `Earnings date desc` | success, raw persistence degraded |

Scanner quality:

- Momentum captured real large-cap post-earnings moves in `TEAM`, `TWLO`, `HALO`, `ABNB`, `COHR`, `MCHP`, `SPCX`, `PLTR`, and `RKLB`.
- Options Activity overlapped with a few liquid names, but most top rows were low-market-cap or low-price high-IV noise.
- Earnings Risk Radar continued to surface many microcap rows; it remains a risk reminder, not a trade source.

## Underlying Candidate Table

| Symbol | Sources | Latest quote / event | Status | Primary block |
| --- | --- | --- | --- | --- |
| NVDA | Tier 2, Momentum | 224.50-224.62 vs 218.99 prior; earnings 2026-08-26 PM | SHADOW_ONLY_QUALIFIED | `account_risk` |
| GOOGL | Tier 2, Momentum | 356.89 vs 357.75 prior; next tentative 2026-10-28 PM | NO_DIRECTIONAL_EDGE | `weak_relative_strength` |
| AMZN | Tier 2 | 278.14 vs 272.26 prior; reported 2026-07-30 PM | TEMP_BLOCK | `blocked_by_extension` |
| MSFT | Tier 2 | 502.43 vs 499.86 prior; reported 2026-07-29 PM | TEMP_BLOCK | `blocked_by_extension` |
| META | Tier 2 | 595.30 vs 589.90 prior; reported 2026-07-29 PM with EPS miss | TEMP_BLOCK | `blocked_by_extension` |
| CRWD | Tier 2 | 211.91 vs 207.39 prior; earnings 2026-08-26 PM | WATCH | `shadow_research_limit` |
| PANW | Tier 2 | 363.30 vs 359.49 prior; earnings 2026-09-01 PM | WATCH | `financial_quality_caution` |
| AVGO | Tier 2 | 425.99 vs 420.565 prior; earnings 2026-09-02 PM | WATCH | `correlation_cluster_limit` |
| TEAM | Momentum, Options Activity | +29.96%; reported 2026-08-06 PM | WATCH | `blocked_by_extension` |
| TWLO | Momentum | +29.84%; reported 2026-08-06 PM | WATCH | `blocked_by_extension` |
| HALO | Momentum | +15.70%; reported 2026-08-06 PM | WATCH | `blocked_by_extension` |
| ABNB | Momentum, Options Activity | +15.50%; reported 2026-08-06 PM | WATCH | `blocked_by_extension` |
| COHR | Watchlist, Momentum | +13.76%; earnings 2026-08-12 PM | TEMP_BLOCK | `blocked_by_earnings` |
| MCHP | Momentum | +13.68%; reported 2026-08-06 PM | WATCH | `blocked_by_extension` |
| SPCX | Momentum, Options Activity | +10.52%; financials null | WATCH | `outside_current_universe` |
| PLTR | Watchlist, Momentum, Options Activity | +8.52%; reported 2026-08-03 PM | WATCH | `outside_current_universe` |
| RKLB | Watchlist, Momentum | +7.86%; earnings 2026-08-10 PM | TEMP_BLOCK | `blocked_by_earnings` |
| AAOI | Options Activity | +10.69%; reported 2026-08-06 PM | WATCH | `outside_current_universe` |
| TENX | Options Activity | IV 4.35; market cap below $500M | REJECT | `penny_stock_or_microcap` |
| HTZ | Options Activity | $2.27; market cap below $1B; repeated row | REJECT | `penny_stock_or_microcap` |
| MARA | Options Activity | market cap about $4.06B; crypto adjacency | REJECT | `outside_current_universe` |

## Options Setup Table

| Rank | Underlying | Direction | Contract | DTE | Strike | Options Setup Score | Account Fit | Decision | Primary Block |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| 1 | NVDA | bullish | 2026-09-18 230C | 42 | 230 | 79 | FAIL | SHADOW_ONLY_QUALIFIED | `account_risk` |
| 2 | CRWD | bullish | N/A | N/A | N/A | N/A | not evaluated | WATCH | `shadow_research_limit` |
| 3 | AVGO | bullish | N/A | N/A | N/A | N/A | not evaluated | WATCH | `correlation_cluster_limit` |

NVDA selected shadow setup: 2026-09-18 230 call, 42 DTE, bid 9.70 / ask 9.85 / midpoint 9.775, spread 1.53% of midpoint, delta 0.4649, IV 0.3888, open interest 30,278, volume 2,906, breakeven 239.78. One contract has $977.50 premium allocation, $977.50 maximum contractual loss, and $977.50 planned trade risk because no reproducible smaller planned-exit loss was available.

No simulated order review was called because research and shadow tracking do not require live-order review. No cheap far-OTM or short-dated substitutions were considered.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was made.

- `TEAM`, `TWLO`, `HALO`, `ABNB`, and `MCHP` had strong scanner momentum but were outside Current Universe and in fresh post-earnings extension windows.
- `COHR`, `PLTR`, and `RKLB` are current watchlist names, not Tier 1/Tier 2 entries; `COHR` and `RKLB` are blocked by verified upcoming earnings.
- `SPCX` had scanner overlap but missing financials and outside-universe status.

## Blocked / Rejected Names

| Group | Symbols | Primary / secondary blocks |
| --- | --- | --- |
| Account-fit failures | NVDA | `account_risk`; $100 account cannot support normal long-premium risk |
| Research-valid but not contract-evaluated | CRWD, PANW, AVGO | `shadow_research_limit`, `financial_quality_caution`, or `correlation_cluster_limit` |
| No directional edge | GOOGL | `weak_relative_strength`; lagged positive market |
| Current Universe temporary blocks | AMZN, MSFT, META | `blocked_by_extension`; settled clearance still needed |
| Post-earnings outside-universe gaps | TEAM, TWLO, HALO, ABNB, MCHP | `blocked_by_extension`, `outside_current_universe` |
| Earnings blocks | COHR, RKLB | `blocked_by_earnings`, watchlist not entry-eligible |
| Watch/outside universe | SPCX, PLTR, AAOI | `outside_current_universe`, options activity insufficient |
| Permanent rejects | TENX, HTZ, MARA | microcap/low-price/high-IV/options-activity-only or crypto-adjacent repeat |

## Missing / Conflicting Data

- Full Momentum and Earnings Risk scanner row persistence remains degraded by transcript truncation. Visible rows, totals, filters, and source tags were preserved.
- `RUT` was restricted by the Robinhood MCP; `DJI` did not resolve via `get_indexes`.
- `TEAM`, `HALO`, and `SPCX` financial rows returned null.
- No exposed callable equity-historicals tool was available in this run, so fresh SMA/relative-strength calculations could not be independently recomputed.
- Missing or incomplete fields reduced completeness and confidence. The NVDA option setup had enough contract data for shadow tracking, but failed account fit.

## State-File Decision

| File | Decision | Reason |
| --- | --- | --- |
| `state/current_universe.json` | unchanged | Daily run may not rewrite official Current Universe. |
| `state/open_theses.json` | unchanged | NVDA was shadow-tracked, not opened as a live thesis. |
| `state/rejected_candidates.json` | updated | `HTZ` added and `MARA` refreshed as repeated permanent rejects. |
| `state/account_capabilities.json` | created | Broker Level 2 capability recorded separately from strategy permission. |

## Portfolio Manager Recommendation

Decision: SHADOW_ONLY_QUALIFIED; NO LIVE TRADE

Next action:

1. Keep `NVDA` as a shadow-qualified Tier 2 options setup and account-fit blocked until premium-allocation and planned-risk rules are satisfied.
2. Keep `CRWD`, `PANW`, and `AVGO` as research-valid Tier 2 watch names until contract setup quality is evaluated in a future run.
3. Revisit `AMZN`, `MSFT`, and `META` after a settled follow-through review, not during the extension-block date intraday.
4. Track the top post-earnings scanner movers for opportunity-cost review, but do not promote them without full Tier 2 provisional evidence.
5. Ignore Options Activity-only noise unless it is independently supported by universe eligibility, tradability, fundamentals, trend, liquidity, and event checks.

## Shadow-Tracking Decision

Opened one hypothetical option shadow-tracking record for `NVDA` 2026-09-18 230C. It is not a live order, not a reviewed order, and not an approval request. The run also preserved terminal research records with primary blocking rules for 5/10/20-day opportunity-cost review.

## Execution Statement

No order review, order placement, order cancellation, scanner modification, watchlist modification, or option exercise tool was called.

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
