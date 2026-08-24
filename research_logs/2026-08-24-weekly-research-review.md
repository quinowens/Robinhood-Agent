# Weekly Research Review - 2026-08-24

Automation: Robinhood Agent Weekly Options Research Review  
Mode: Research-only / proposal-only / shadow-trading  
Review window: 2026-08-17 through 2026-08-23 scanner activity, plus current 2026-08-24 read-only account/quote/earnings refresh  
Source path note: configured workspace `/Users/quinowens/Desktop/Robinhood-Agent-v1.6` contains only spillover logs/data; source-of-truth policy, strategy, state, structured records, validation, and backtests were read from `/Users/quinowens/Desktop/Robinhood-Agent`.

## Executive Summary

Decision: NO LIVE TRADE. One canonical v2.0 long-call setup reached `SHADOW_ONLY_QUALIFIED` during the week: AMZN 2026-10-16 265C from the 2026-08-19 daily run. It passed setup quality but failed account fit because one standard contract required about $1,400 of premium against the $100 Agentic account.

No `PM_PROPOSAL` was appropriate. No live order review, placement, modification, or cancellation was performed. The workflow remained inside v2.0 launch scope: single-leg long calls/puts only, no 0DTE, no selling, no spreads, no earnings lottery trades, and no forced cheap-contract substitution.

Weekly setup summary:

| Date | Underlying | Contract | DTE | Mid / Ask | Setup Score | Account Fit | Final Decision |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 2026-08-18 | NKE | 2026-09-18 42.50C | 31 | 0.71 mid / 0.72 ask | 61 | PASS by affordability only | WATCH / SHADOW context, not canonical qualified setup |
| 2026-08-19 | AMZN | 2026-10-16 265C | 58 | 14.00 mid | 82 | FAIL | SHADOW_ONLY_QUALIFIED |
| 2026-08-21 | N/A | No option chain work | N/A | N/A | N/A | N/A | NO TRADE |
| 2026-08-22 | N/A | No option chain work | N/A | N/A | N/A | N/A | NO TRADE |

The NKE review on 2026-08-18 was affordable and liquid, but the underlying edge and selected low-delta recovery setup were not strong enough to classify as a high-quality shadow setup. The AMZN setup is the only canonical qualified options record for this review window.

## Weekly Run Health

Four daily scanner logs were available for the week: 2026-08-18, 2026-08-19, 2026-08-21, and 2026-08-22. No 2026-08-17, 2026-08-20, or 2026-08-23 daily scanner report was present in either workspace.

| Date | Run ID | Status | Scanner Calls | Options Steps | Completeness / Coverage | Notes |
| --- | --- | --- | ---: | --- | --- | --- |
| 2026-08-18 | `2026-08-18-daily-scanner-dry-run` | Degraded | 3/3 | One NKE reviewed in simulation | Degraded local source/raw persistence | Local shell/file access failed during that run; report preserved summary only. |
| 2026-08-19 | `2026-08-19-daily-scanner-dry-run` | Complete with shadow-only | 3/3 | AMZN chain/instrument/quote only | 100% scoped terminal coverage | Correctly created canonical setup, shadow trade, outcome record, and run manifest. |
| 2026-08-21 | `2026-08-21-daily-scanner-dry-run` | Degraded, no finalist | 3/3 | Correctly skipped chains | 100% scoped terminal coverage | Raw full Earnings payload degraded; no gate pass. |
| 2026-08-22 | `2026-08-22-daily-scanner-dry-run` | Degraded, weekend/no fresh tape | 3/3 | Correctly skipped chains | 100% scoped terminal coverage | Saturday run reflected Friday 2026-08-21 market/after-hours state. |

Read-only refresh on 2026-08-24 confirmed the three configured saved scanners still exist with expected IDs and filters. The Agentic account remains a $100 cash account with $100 buying power, no equity positions, no option positions, and no equity or option orders since 2026-08-17.

Missing/degraded fields: full row-by-row scanner payload persistence for large scans, structured 2026-08-18/21/22 records in the full repo, and mature options outcome fields. No run appears to have incorrectly skipped v2.0 options steps: Aug 21/22 stopped before chains because no underlying passed direction plus Options Suitability Gate.

## Market / Benchmark Context

Daily logs described market context as constructive but selective. On 2026-08-19, SPY and QQQ were above 50-day and 200-day moving averages, supporting selective bullish research. On 2026-08-21/22, SPX/NDX/VIX context remained non-hostile, but candidate-specific trend damage and event risk dominated.

Read-only quote refresh on 2026-08-24 around 14:35 UTC showed SPY 763.69 versus 765.72 prior close and QQQ 705.76 versus 713.44 prior close. That is softer index context than the prior Friday close, especially for QQQ, and it supports keeping new long-premium proposals selective.

Material underlying refresh highlights as of 2026-08-24:

| Symbol | Refresh Note |
| --- | --- |
| AMZN | 261.46 versus 258.63 prior close; still near the Aug 19 shadow thesis zone, but selected 265C remains unaffordable. Tentative next earnings 2026-10-29 PM, after selected expiration. |
| NVDA | 210.26 versus 214.72 prior close; verified earnings 2026-08-26 PM keeps new entries temporarily blocked. |
| CRWD | 191.90 versus 191.95 prior close; verified earnings 2026-08-26 PM keeps new entries blocked. |
| PANW | 352.89 versus 357.87 prior close; verified earnings 2026-09-01 PM requires event-risk caution. |
| AVGO | 363.09 versus 368.45 prior close; verified earnings 2026-09-02 PM and weak price action argue against fresh calls. |
| GOOGL / MSFT | Modestly firmer on 2026-08-24, but weekly logs still lacked a clean directional options thesis. |

## Scanner Review

| Scanner | Weekly Role | Observation |
| --- | --- | --- |
| Momentum Candidates | Underlying movement discovery | Useful but broad/noisy. It surfaced HOOD, COIN, FCX, AVGO, MSFT, GOOGL, NVDA, AMZN, MRVL, and other large names. Frequency was not treated as bullish evidence by itself. |
| Options Activity Radar | Options context | Useful context for AMZN, NVDA, AVGO, HOOD, SOFI, COIN, MSTR, FCX, PLTR, and NKE, but top rows were often microcap/high-IV rejects. It did not create direction. |
| Earnings Risk Radar | Event-risk confirmation | Correctly blocked or flagged NVDA, CRWD, MRVL, BBY, CRM, WDAY, IREN, INTU, SMTC, KEYS, PANW, and AVGO. |

Scanner totals where logged:

| Date | Momentum | Options Activity | Earnings Risk |
| --- | ---: | ---: | ---: |
| 2026-08-18 | 286 | 71 | 289 |
| 2026-08-19 | 398 | 139 | 333 |
| 2026-08-21 | 43 | 2 | 362 |
| 2026-08-22 | 400 | 110 | 327 |

## Underlying Queue

| Priority | Symbol | Weekly Evidence | Next Action |
| ---: | --- | --- | --- |
| 1 | AMZN | Only canonical qualified setup this week; Tier 2 score 82; bullish call shadow recorded. | Track option/underlying outcome; recheck trend and 20-day area before any new setup. |
| 2 | NVDA | Recurring Tier 2, options activity, and prior shadow history; now verified earnings block. | No new long premium until after 2026-08-26 PM earnings and first complete post-event session. |
| 3 | CRWD | Tier 2 cybersecurity name; earnings block. | Post-earnings review after 2026-08-26 PM. |
| 4 | GOOGL | Highest Tier 2 score tied with AMZN; recurring neutral/no fresh edge. | Refresh trend/RS; options only if direction becomes explicit. |
| 5 | MSFT | Tier 2, large liquid, modestly firm on refresh; no clean weekly option thesis. | Watch for regained relative strength and explicit direction. |
| 6 | META | Prior qualified shadow history but weak weekly trend; no clean Aug 21/22 edge. | Reassess only if price structure improves; avoid duplicate stale call signals. |
| 7 | AVGO | Tier 2, options activity, but weak price action and verified 2026-09-02 PM earnings. | Keep event-risk watch; no fresh setup through blackout. |
| 8 | PANW | Tier 2 with upcoming 2026-09-01 PM earnings. | Event-risk watch; no new setup unless outside blackout and direction clears. |
| 9 | HOOD / SOFI / FCX / PLTR | Recurring scanner/watchlist interest. | Provisional Tier 2 only with complete scoring, tradability, earnings, histories, and benchmark RS. |
| 10 | MRVL / NBIS / COIN / MSTR / BMNR | Scanner-active but outside universe, missing data, crypto adjacency, or event/trend risk. | Watch/reject as applicable; do not promote from frequency alone. |

## Directional Thesis Review

The serious bullish evidence was concentrated in AMZN on 2026-08-19. NKE had a recovery-oriented bullish idea on 2026-08-18, but not enough underlying edge for a live-quality or canonical shadow setup. HOOD, SOFI, FCX, COIN, MSTR, and MRVL had scanner strength but lacked approved universe status or complete provisional Tier 2 evidence.

No bearish thesis qualified. META/CVNA-style bearish or corrective ideas from Aug 18 were either unaffordable, event/noise dependent, or not repeated with enough weekly evidence. The workflow correctly avoided converting failed bullish setups into puts.

Neutral or unsupported direction remained `NO_DIRECTIONAL_EDGE`, `WATCH`, or `TEMP_BLOCK`.

## Options Setup Review

Canonical options setup for the week:

| Underlying | Contract | Type | DTE Bucket | Delta | Spread % Mid | OI / Vol | IV | Score | Completeness | Confidence |
| --- | --- | --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| AMZN | 2026-10-16 265C | Long call | 46-60 | 0.555 | 2.86% | 5,342 / 1,387 | 0.302 | 82 | 95 | 78 |

The AMZN contract had a suitable 58 DTE window, near-0.55 delta, strong open interest/volume, acceptable spread, and expiration before tentative next earnings. Setup quality passed.

Non-canonical / watch context:

| Underlying | Contract | Type | Notes |
| --- | --- | --- | --- |
| NKE | 2026-09-18 42.50C | Long call | Affordable and liquid, but Options Setup Score 61 and weak recovery-dependent thesis kept it WATCH / shadow context rather than canonical qualification. |
| AAPL / META / CVNA / MU | Calls or puts considered on 2026-08-18 | Long calls/puts only | Contract quality or direction could exist, but preferred contracts exceeded account fit and no canonical weekly record was created. |

No puts became canonical. No 0DTE, spreads, covered calls, cash-secured puts, naked selling, or margin-driven structures were used.

## Account-Fit / Shadow-Only Review

The Agentic account remains a process-validation account: $100 value, $100 cash, $100 buying power, no holdings, and no recent orders. AMZN one-contract premium was $1,400, or 1,400% of account value, so account fit failed. The correct classification is `SHADOW_ONLY_QUALIFIED`, not `PM_PROPOSAL`.

The system correctly did not force a lower-quality far-OTM, shorter-DTE, or cheaper substitute contract. Account-fit failure is a funding constraint and should inform shadow analytics, not weaken the AMZN underlying thesis.

## Options Outcome Review

The AMZN shadow outcome record exists but has no mature 1/5/10/20/30 trading-day results yet. Earlier August NVDA/META shadow setups from the prior weekly review also still require forward tracking. Outcome classification remains `INSUFFICIENT_DATA`.

Current sample limits:

| Slice | Observation |
| --- | --- |
| Call vs put | Weekly canonical sample: 1 call, 0 puts. |
| DTE | Weekly canonical sample: one 46-60 DTE setup. |
| Delta | Weekly canonical sample: one near-0.55 delta setup. |
| Spread/liquidity | AMZN acceptable; NKE affordable but lower-quality thesis/setup. |
| IV/premium | AMZN IV 0.302; outcome sample too young for calibration. |
| Account-fit failures | 1/1 canonical weekly setups failed account fit. |

Do not draw performance conclusions from this sample yet.

## Current Universe Review

Current Universe remains populated from the 2026-08-03 official catch-up refresh. No weekly evidence authorizes rewriting `state/current_universe.json`.

| Bucket | Names | Weekly Implication |
| --- | --- | --- |
| Tier 1 | None | Still empty; no evidence supports lowering the 85+ threshold from this small sample. |
| Tier 2 strengthening | AMZN | Generated the only canonical qualified setup this week. |
| Tier 2 event-blocked / watch | NVDA, CRWD, PANW, AVGO | Earnings risk dominates next action. |
| Tier 2 neutral / weak trend | GOOGL, MSFT, META | Watch for explicit direction; no options proposal without it. |
| Provisional candidates | HOOD, SOFI, FCX, PLTR | Require full provisional Tier 2 evidence before chains/proposals. |
| Caution candidates | MRVL, NBIS, COIN, MSTR, BMNR | Outside universe, missing data, crypto adjacency, event risk, or trend damage. |

## Primary Blocking-Rule Analysis

Primary blockers for the review window should be counted by decisive layer, not double-counted secondary context.

Underlying / direction blockers:

| Rule | Representative Symbols | Interpretation |
| --- | --- | --- |
| `blocked_by_earnings` | NVDA, CRWD, MRVL, BBY, CRM, WDAY, IREN, INTU, SMTC, KEYS | Earnings Risk Radar functioned as intended. |
| `outside_current_universe` | HOOD, SOFI, FCX, PLTR, MRVL | Scanner strength did not bypass universe governance. |
| `no_fresh_directional_edge` | MSFT, GOOGL, AVGO, TSLA | Neutral evidence correctly stopped options proposals. |
| `weak_trend` / `weak_relative_strength` | META, AMZN on later runs, AVGO | Trend damage kept otherwise liquid names on watch. |
| `missing_critical_data` | NBIS | Missing financials prevented provisional promotion. |
| `penny_stock_or_microcap` | HOWL, CBAT, NNVC, UPXI, CAN, CTSO, AIFC, IGC, SKYA, GNLX, CYPH | Options Activity Radar remained noisy at high-IV extremes. |
| `crypto_adjacency` | COIN, MSTR, BMNR, CAN | Strategy caution applied consistently. |

Options/account blockers:

| Rule | Representative Symbols | Interpretation |
| --- | --- | --- |
| `account_fit_premium_risk` | AMZN; also AAPL/META/CVNA/MU/NKE near-the-money context from Aug 18 | High-quality contracts generally exceed the $100 account. |
| `options_suitability_gate_not_passed` | Aug 21/22 candidate set | Correct stop before chain work. |
| `weak_underlying_edge` | NKE 42.50C context | Affordability alone is not enough for a qualified setup. |

## Score And Threshold Calibration

Structured 2026-08-19 research records:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 6 |
| Highest | 82 |
| Median | 76.5 |
| 90th percentile | 81.0 |
| 95th percentile | 81.5 |
| Count >= 65 | 6 |
| Count >= 75 | 4 |
| Count >= 85 | 0 |

Weekly canonical options setup-score distribution:

| Metric | Options Setup Score |
| --- | ---: |
| Count | 1 |
| Highest | 82 |
| Median | 82 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 75 | 1 |
| Count >= 80 | 1 |

The August validation report already flags that the highest underlying score is below the Tier 1 threshold. This week adds another highest score of 82, but the sample is too small and too account-constrained to change thresholds. Keep Tier 1/Tier 2 and Options Setup calibration unchanged until more canonical outcomes mature.

## State Decisions

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged; no open theses.
- `state/rejected_candidates.json`: unchanged; repeated microcap rejects were recognized, but no weekly state rewrite is authorized.
- `data/options_setup_records/2026-08-19-daily-scanner-dry-run.jsonl`: read as canonical AMZN setup evidence; unchanged.
- `data/option_shadow_trades/2026-08-19-daily-scanner-dry-run.jsonl`: read as canonical AMZN shadow evidence; unchanged.
- `data/option_signal_outcomes/2026-08-19-daily-scanner-dry-run.jsonl`: read as forward-tracking placeholder; unchanged.

## Next Research Actions

1. Track AMZN 2026-10-16 265C at 1, 5, 10, 20, and 30 trading days, separating underlying thesis result from contract-selection result.
2. Continue prior canonical NVDA and META shadow outcome tracking from Aug 11-13.
3. Recheck NVDA and CRWD only after 2026-08-26 PM earnings and the first complete post-event trading session.
4. Recheck PANW before/after 2026-09-01 PM and AVGO before/after 2026-09-02 PM; do not hold new long-premium exposure through unresolved events.
5. Refresh GOOGL/MSFT/META trend and relative strength if they reappear in Momentum or Options Activity, but keep neutral names out of options research.
6. For HOOD/SOFI/FCX/PLTR, require the full provisional Tier 2 path before option-chain work.
7. Preserve account-fit separation: high-quality unaffordable setups should stay in options shadow tracking; do not replace them with worse cheap contracts.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
