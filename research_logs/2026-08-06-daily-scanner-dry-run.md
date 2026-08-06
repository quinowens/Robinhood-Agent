# Daily Scanner Dry Run - 2026-08-06

Date: 2026-08-06  
Run time: 18:00 CT  
Account mode: Research-only / Proposal-only  
Order status: No orders placed or proposed  
Run ID: `2026-08-06-daily-scanner-dry-run`  
Run status: degraded  
Data completeness: 88%

## Executive Decision

Decision: NO TRADE

Primary reason: no candidate passed Current Universe, event-risk, Portfolio Manager approval, and exact risk-term requirements.

Supporting reasons:

- The Agentic account `...8691` had $100 total value, $100 cash/buying power, no equity positions, no option positions, and no open queued/confirmed/partially-filled equity or option orders.
- Current Universe has no Tier 1 names. Tier 2 names remain PM-review only and require explicit user/PM approval before any order terms.
- The strongest scanner rows were outside the Current Universe, same-day earnings movers, recent post-earnings extensions, upcoming earnings blocks, or Options Activity-only noise.
- No order review, order placement, order cancellation, scanner modification, or watchlist modification tools were called.

What would change the decision:

- A Tier 2 candidate receives explicit Portfolio Manager/user approval with fresh quote, earnings, trend, entry, stop, target, and sizing checks.
- Event blocks clear and the next settled-session data confirms trend quality without excessive extension.
- Full scanner row export becomes available so every row can be persisted, not only visible rows and totals.

## Run Health And Call Coverage

| Area | Result | Notes |
| --- | --- | --- |
| Account preflight | Complete | Agentic account `...8691`, cash account, $100 total value and $100 buying power. |
| Portfolio exposure | Complete | No equity positions, no options positions, no open equity/options orders in checked open states. |
| Saved scanner resolution | Complete | All configured scanner names and IDs matched exactly. |
| Scanner execution | Complete, persistence degraded | Momentum, Options Activity, and Earnings Risk all ran; visible rows and totals were persisted. |
| Direct earnings data | Complete for decision candidates | `get_earnings_results` used for enriched names; calendar used for broader event context. |
| Enrichment | Partial | Quotes, fundamentals, financials, tradability, and direct earnings pulled for strongest names; `TIGO` and `SPCX` financial rows were null. |
| Market context | Partial | SPX/NDX resolved and quoted; RUT restricted and DJI not returned. |
| Price book | Skipped | No finalist required Level 2 execution-quality review. |

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Retried calls | 0 |
| Raw rows persisted | visible rows plus scanner totals |
| Deduplicated decision candidates | 30 |
| Candidates with terminal status | 30 |
| Completeness percentage | 88% |

Publish decision: degraded daily log; do not publish or mutate Current Universe from this daily run.

## Market / Index Context

| Instrument | Latest observed | Prior / context | Interpretation |
| --- | ---: | --- | --- |
| SPX | 7720.04 at 2026-08-06 15:09 ET | 2026-08-05 close 7723.55 from index history | Broad index roughly flat-to-soft versus prior settled index bar. |
| NDX | 29444.2598 at 2026-08-06 15:09 ET | 2026-08-05 close 29487.790634 from index history | Growth index modestly soft. |
| SPY | 768.8271 after-hours vs 769.79 prior close | 2026-08-06 quote refresh | Broad ETF slightly below prior close. |
| QQQ | 716.29 after-hours vs 717.30 prior close | 2026-08-06 quote refresh | Nasdaq proxy slightly below prior close. |
| RUT | N/A | Robinhood MCP restricted RUT quotes | Missing; reported as unavailable, not estimated. |
| DJI | N/A | `get_indexes` did not return DJI | Missing; not estimated. |

Market-regime validation: adequate for research, but not strong enough to override Current Universe rules, event risk, temporary blocks, or missing data.

## Scanner Summary

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 351 | `% Change desc` | success |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 146 | `Implied volatility desc` | success |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 312 | `Earnings date desc` | success |

Useful signals:

- Momentum surfaced real large-cap or liquid moves in `INSM`, `U`, `TIGO`, `ALAB`, `MSFT`, `COHR`, `AMD`, and `CRDO`.
- Options Activity overlapped with a few liquid names such as `NVDA`, `AAOI`, `RKLB`, `SPCX`, and `INSM`, but this was confirmation only, not trade evidence.
- Earnings Risk Radar helped confirm event clusters; direct earnings tools remained primary.

Noisy rows:

- Options Activity was led by `SURG`, `NRXS`, `HTZ`, `NRDY`, and `BYND`, mostly low-priced or low-quality rows with extreme volatility.
- Earnings Risk Radar contained many microcap/low-liquidity names and should stay a secondary risk-control scanner.

## Enriched Candidate Table

| Symbol | Sources | Latest quote / event | Status | Reason codes |
| --- | --- | --- | --- | --- |
| GOOGL | Tier 2 | 358.50 AH vs 362.43 prior close; next tentative 2026-10-28 PM | research-further | `tier2_pm_approval_required`, `requires_fresh_terms` |
| NVDA | Tier 2, Options Activity | 219.50 AH vs 219.22 prior close; verified 2026-08-26 PM | research-further | `tier2_pm_approval_required`, `upcoming_earnings_monitor` |
| CRWD | Tier 2 | 210.75 AH vs 209.86 prior close; verified 2026-08-26 PM | research-further | `tier2_pm_approval_required`, `upcoming_earnings_monitor` |
| PANW | Tier 2 | 365.05 AH vs 362.66 prior close; verified 2026-09-01 PM | research-further | `tier2_pm_approval_required`, `latest_financial_margin_negative` |
| AVGO | Tier 2 | 422.00 AH vs 418.28 prior close; verified 2026-09-02 PM | research-further | `tier2_pm_approval_required`, `upcoming_earnings_monitor` |
| AMZN | Tier 2 | 272.20 AH vs 272.65 prior close; reported 2026-07-30 PM | blocked-by-risk | `temporary_extension_block_until_2026-08-07` |
| MSFT | Tier 2, Momentum | 498.46 AH vs 487.46 prior close; reported 2026-07-29 PM | blocked-by-risk | `temporary_extension_block_until_2026-08-07` |
| META | Tier 2 | 588.43 AH vs 588.77 prior close; reported 2026-07-29 PM | blocked-by-risk | `temporary_extension_block_until_2026-08-07`, `prior_eps_miss` |
| INSM | Momentum, Options Activity | 131.47 AH vs 99.02 prior close; reported 2026-08-06 AM | watch-only | `outside_current_universe`, `same_day_earnings`, `extended_one_day_move` |
| U | Momentum, Options Activity | 40.6345 AH vs 35.47 prior close; reported 2026-08-06 AM | watch-only | `outside_current_universe`, `same_day_earnings`, `extended_one_day_move` |
| TIGO | Momentum | 104.32 AH vs 91.79 prior close; reported 2026-08-06 AM | watch-only | `outside_current_universe`, `same_day_earnings`, `missing_financials` |
| ALAB | Momentum | 335.813 AH vs 318.43 prior close; reported 2026-08-04 PM | watch-only | `outside_current_universe`, `post_earnings_extension` |
| AAOI | Options Activity | 122.2241 AH vs 128.56 prior close; reports 2026-08-06 PM | blocked-by-earnings | `outside_current_universe`, `earnings_today_pm` |
| SNDK | Options Activity | 1274.00 AH vs 1350.50 prior close; reported 2026-08-05 PM | watch-only | `outside_current_universe`, `post_earnings_reversal` |
| RKLB | Momentum, Options Activity | 76.10 AH vs 74.82 prior close; verified 2026-08-10 PM | blocked-by-earnings | `outside_current_universe`, `earnings_within_window` |
| COHR | Watchlist, Momentum | 342.85 AH vs 328.22 prior close; verified 2026-08-12 PM | blocked-by-earnings | `earnings_within_window`, `watchlist_not_entry_eligible` |
| AMD | Watchlist, Momentum | 490.98 AH vs 482.05 prior close; reported 2026-08-04 PM | blocked-by-earnings | `post_event_block`, `watchlist_not_entry_eligible` |
| CRDO | Watchlist, Momentum | 230.40 AH vs 224.63 prior close; next tentative 2026-09-02 PM | watch-only | `watchlist_not_entry_eligible`, `outside_tier2_approval` |
| SURG | Options Activity | 0.3257 vs 0.2234 prior close; microcap/noncompliant | rejected | `penny_stock_or_microcap`, `high_volatility`, `repeated_reject` |
| ARAY | Earnings Risk | 0.2857 vs 0.2743 prior close; existing persistent reject | rejected | `penny_stock_or_microcap`, `insufficient_liquidity`, `repeated_reject` |

## Blocked / Rejected Names

| Group | Symbols | Reason |
| --- | --- | --- |
| Tier 2 research-further only | GOOGL, NVDA, CRWD, PANW, AVGO | Need explicit PM/user approval and fresh exact terms before any proposal. |
| Temporary Current Universe blocks | AMZN, MSFT, META | Extension blocks remain through 2026-08-07. |
| Same-day earnings movers | INSM, U, TIGO, AAOI | New entries blocked until post-event review. |
| Recent post-event / upcoming event blocks | ALAB, SNDK, RKLB, COHR, AMD | Recent or upcoming verified earnings prevent action. |
| Watch-only outside Tier 1/Tier 2 | CRDO, MU, SPCX, RKLB, ALAB, SNDK | Daily run cannot promote universe membership. |
| Persistent rejects | SURG, ARAY, EVTL, AARD | Prior repeated-reject state or current microcap/low-quality evidence. |

## Missing / Conflicting Data

- Full raw scanner row persistence remains degraded because large scanner payloads were truncated in the tool transcript. Visible rows, totals, filters, and source tags were preserved.
- `get_earnings_calendar` returned a large payload that was truncated in transcript; direct `get_earnings_results` covered decision candidates.
- `get_financials` returned null for `TIGO` and `SPCX`.
- `RUT` was restricted by the Robinhood MCP; `DJI` did not resolve via `get_indexes`.
- Equity historicals were pulled for benchmarks and enriched candidates, but large payloads were truncated in the transcript. No trade evidence depended on unavailable rows; any future exact proposal still needs fresh raw history and benchmark-relative calculations.

Any unresolved conflict affecting eligibility, earnings, sizing, or order terms remains a NO TRADE condition.

## Scanner Quality

Useful signals:

- Momentum captured real event-driven strength, especially `INSM`, `U`, `TIGO`, and AI/semiconductor infrastructure names.
- Current Universe overlap helped prevent scanner-only names from being treated as trade candidates.
- Earnings Risk Radar was useful as a reminder to verify direct event dates for `AAOI`, `RKLB`, and `COHR`.

False positives:

- `SURG` was the clearest false positive: sub-$1 price, about $8.2M market cap from fundamentals, Noncompliant status, and extreme IV/options activity.
- `INSM`, `U`, and `TIGO` looked strong on momentum but were same-day earnings reactions outside the Current Universe.
- `AAOI` had options activity but reports after the close today, making it blocked regardless of other signals.

Repeated rejects:

- `SURG` was updated in `state/rejected_candidates.json` because it was already a repeated July reject and reappeared today as the top Options Activity false positive.
- `ARAY` remains a persistent reject already recorded on 2026-08-05.

## State-File Decision

| File | Decision | Reason |
| --- | --- | --- |
| `state/current_universe.json` | unchanged | Daily runs must not update Current Universe. |
| `state/open_theses.json` | unchanged | No thesis advanced. |
| `state/rejected_candidates.json` | updated for `SURG` only | Existing repeated reject reappeared with stronger current evidence. |

## Portfolio Manager Recommendation

Decision: NO TRADE

Next action:

1. Keep `GOOGL`, `NVDA`, `CRWD`, `PANW`, and `AVGO` as research-further Tier 2 names only.
2. Revisit `AMZN`, `MSFT`, and `META` after the 2026-08-07 extension blocks expire.
3. Revisit same-day and upcoming earnings names only after event windows clear and settled data confirms trend quality.
4. Continue ignoring Options Activity-only microcap/high-IV rows unless independently supported by universe eligibility, liquidity, fundamentals, trend, and earnings checks.

No buy, sell, option, cancellation, scanner-write, or watchlist-write action was placed, reviewed, or proposed during this dry run.
