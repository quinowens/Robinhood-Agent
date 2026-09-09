# Weekly Research Review

Review date: 2026-09-07  
Review window: 2026-08-31 through 2026-09-04 trading activity, plus read-only current-state cross-check on 2026-09-07  
Automation: Robinhood Agent Weekly Options Research Review  
Mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed, modified, canceled, or reviewed for live execution  
Run status: Degraded complete weekly consolidation  
Strategy mode: Options primary, equities as Approved Underlying Universe

## Executive Summary

Decision: `NO LIVE TRADE`. No `PM_PROPOSAL` reached account-fit pass, no `review_option_order` was needed, and no live order action was taken.

The week produced four canonical `SHADOW_ONLY_QUALIFIED` long-call records and one watch-only sampled setup:

| Date | Underlying | Contract | DTE | Setup Score | Account Fit | Final Decision |
| --- | --- | --- | ---: | ---: | --- | --- |
| 2026-09-01 | AAPL | 2026-10-16 325C | 45 | 76 | FAIL | `SHADOW_ONLY_QUALIFIED` |
| 2026-09-02 | NVDA | 2026-10-16 225C | 44 | 78 | FAIL | `SHADOW_ONLY_QUALIFIED` |
| 2026-09-03 | MSFT | 2026-10-16 510C | 43 | 76 | FAIL | `SHADOW_ONLY_QUALIFIED` |
| 2026-09-04 | NVDA | 2026-10-16 230C | 42 | 79 | FAIL | `SHADOW_ONLY_QUALIFIED` |
| 2026-09-04 | ALAB | 2026-10-16 310C | 42 | 61 | FAIL secondary | `WATCH` |

All serious option structures stayed inside v2.0 scope: single-leg long calls only. No puts qualified. No 0DTE, selling, spreads, cash-secured puts, covered calls, naked options, margin-driven selling, earnings lottery trades, or cheap-contract substitutions were recorded.

The decisive live blocker remains account fit. The Agentic account ending `8691` is a cash account with $100 account value, $100 cash, $100 buying power, no equity positions, no option positions, and no queued or confirmed equity/options orders. Qualified one-contract long-call premiums ranged from about $1,052.50 to $1,835.00, far above the account's usable buying power and risk caps.

## Weekly Run Health

| Date | Run ID | Status | Scanner Execution | Options Steps | Health Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-08-31 | `2026-08-31-daily-scanner-dry-run` | Degraded complete | 3/3 | Correctly skipped chains | No underlying passed direction, event risk, and suitability together. |
| 2026-09-01 | `2026-09-01-daily-scanner-dry-run` | Degraded complete | 3/3 | AAPL chain/instruments/quotes | AAPL shadow setup persisted canonically; capped scanner rows and RUT restriction noted. |
| 2026-09-02 | `2026-09-02-daily-scanner-dry-run` | Degraded complete | 3/3 | NVDA chain/instruments/quotes | NVDA shadow setup persisted canonically. |
| 2026-09-03 | `2026-09-03-daily-scanner-dry-run` | Degraded complete | 3/3 | MSFT chain/instruments/quotes | Interrupted run completed late; frozen MSFT entry uses official option close and is marked degraded. |
| 2026-09-04 | `2026-09-04-daily-scanner-dry-run` | Degraded complete | 3/3 | NVDA and ALAB option research | NVDA shadow persisted; ALAB stayed watch-only because setup quality and extension risk failed. |

Health summary:

- Successful/degraded/failed runs: 5 degraded-complete runs, 0 failed runs.
- Scanner coverage: all three configured scanners matched current saved scanner IDs during the 2026-09-07 cross-check.
- Tool coverage: account, portfolio, positions, orders, scanners, quotes, histories, index context, earnings, option chains, option instruments, and option quotes were available across the weekly evidence.
- Missing/degraded fields: full uncapped scanner exports remained unavailable; RUT quote is restricted through the connector; no direct breadth tool was available; 2026-09-03 MSFT bid/ask fields are degraded.
- v2.0 options steps: no run incorrectly skipped options work after a candidate passed the gate. Chains were skipped when the underlying thesis or options suitability did not pass.
- Order tools: no `review_option_order`, `place_option_order`, `cancel_option_order`, `place_equity_order`, or order replacement tool was called.

## Market / Benchmark Context

Read-only 2026-09-07 cross-check used 2026-09-04 market data because markets were not providing a newer regular session in the connector snapshot.

| Instrument | Latest Available Snapshot |
| --- | ---: |
| SPX | 7718.60 as of 2026-09-04 |
| NDX | 29544.1551 as of 2026-09-04 |
| VIX | 14.53 as of 2026-09-04 |
| SPY | 2026-09-04 regular close 770.19 |
| QQQ | 2026-09-04 regular close 718.96 |

Market interpretation: constructive but selective. SPY and QQQ recovered from the 2026-09-01 dip by 2026-09-03/04, and VIX stayed mid-teens. That context supported selective bullish research but did not override earnings blocks, post-earnings review, weak tape, extension risk, or account-fit rules.

## Scanner Review

| Scanner | Role | Weekly Match Range | Quality Read |
| --- | --- | ---: | --- |
| Momentum Candidates | Underlying movement discovery | 397-398 | Useful for surfacing AAPL, NVDA, MSFT, CRWD, PANW, DELL, SNOW, ALAB, SNDK, CBRS, ORCL, CRDO, MU, and HOOD as research inputs. |
| Options Activity Radar | Options context only | 80-125 | Useful for confirming option attention in large liquid names, but top rows were repeatedly noisy low-price/high-IV candidates. |
| Earnings Risk Radar | Event-risk confirmation | 342-345 | Correctly highlighted near-term event names; direct earnings data controlled final blocks. |

Scanner frequency was not treated as bullish or bearish evidence. Options Activity Radar remained options context, not direction.

## Underlying Queue

| Priority | Symbol | Weekly Evidence | Next Action |
| ---: | --- | --- | --- |
| 1 | NVDA | Official Tier 2; two qualified long-call shadow setups, improving post-earnings structure, verified next earnings after October expiration. | Lead options-primary research candidate; track 225C and 230C separately without merging signals. |
| 2 | MSFT | Official Tier 2; 2026-09-03 qualified long-call setup, but 2026-09-04 weakness and degraded bid/ask require care. | Refresh trend/RS and quote quality before any further proposal. |
| 3 | AAPL | Provisional Tier 2 research-only setup on 2026-09-01; not official Current Universe Tier 2. | Continue shadow outcome tracking; no live-quality proposal without validated provisional path or explicit exception. |
| 4 | GOOGL | Official Tier 2, but repeatedly neutral/no directional edge through the week. | Watch for renewed directional evidence; options activity alone is insufficient. |
| 5 | AMZN | Official Tier 2, but mostly neutral/flat to weak after prior momentum. | Watch for trend recovery and fresh thesis evidence. |
| 6 | CRWD | Official Tier 2; post-earnings volatility and reversal kept it blocked/watch. | Reassess after post-earnings structure stabilizes. |
| 7 | PANW | Official Tier 2; reported 2026-09-01 PM and sold off afterward. | Keep post-earnings review active. |
| 8 | AVGO | Official Tier 2; reported 2026-09-02 PM, then remained neutral/watch. | Keep post-earnings review active. |
| 9 | ALAB | Strong movement and sampled option, but outside official Current Universe and extended with high IV/spread. | Watch only; no shadow qualification from this sampled contract. |
| 10 | ORCL, CRDO, MU, HOOD, SMCI, DELL, SNOW, SNDK, CBRS | Recurring scanner or event names. | Require full provisional Tier 2 path and clean event/timing review before options escalation. |

## Directional Thesis Review

Bullish candidates that reached options research:

| Symbol | Directional Read | Confidence | Outcome |
| --- | --- | ---: | --- |
| AAPL | Bullish on 2026-09-01 | 72 | Qualified setup, account fit failed, shadow-only. |
| NVDA | Bullish on 2026-09-02 and 2026-09-04 | 73-74 | Qualified setups, account fit failed, shadow-only. |
| MSFT | Bullish on 2026-09-03 | 72 | Qualified degraded-quote setup, account fit failed, shadow-only. |

Neutral or unsupported candidates included GOOGL, AMZN, META, CRWD, PANW, AVGO on most reviewed days. Failed bullish evidence was not converted into bearish long-put proposals. No bearish thesis reached options research quality.

## Options Setup Review

| Underlying | Contract | Delta | Bid / Ask / Mid | Spread | OI / Volume | IV | Breakeven | Quality |
| --- | --- | ---: | --- | ---: | --- | ---: | ---: | --- |
| AAPL | 2026-10-16 325C | 0.540903 | 12.05 / 12.35 / 12.20 | 2.459% | 9,035 / 2,956 | 0.249818 | 337.20 | Qualified. |
| NVDA | 2026-10-16 225C | 0.529743 | 10.45 / 10.60 / 10.525 | 1.425% | 19,907 / 6,911 | 0.332221 | 235.53 | Qualified. |
| MSFT | 2026-10-16 510C | 0.438723 | N/A / N/A / 18.35 | N/A | 39,609 / 818 | 0.250563 | 522.90 | Qualified but quote snapshot degraded. |
| NVDA | 2026-10-16 230C | 0.543052 | 11.15 / 11.30 / 11.225 | 1.34% | 38,398 / 4,953 | 0.342950 | 241.23 | Qualified. |
| ALAB | 2026-10-16 310C | 0.562377 | 33.55 / 35.25 / 34.40 | 4.94% | 733 / 286 | 0.810400 | 344.40 | Watch only: extension, IV, spread, outside-universe status. |

Options Setup Score distribution for canonical selected setups this week:

| Metric | Options Setup Score |
| --- | ---: |
| Count | 5 |
| Highest | 79 |
| Median | 76 |
| 90th percentile | 79 |
| 95th percentile | 79 |
| Count >= 70 | 4 |
| Count >= 75 | 4 |
| Count >= 80 | 0 |

## Account-Fit / Shadow-Only Review

| Setup | One-Contract Premium | Buying Power | Premium / Account | Account-Fit Result |
| --- | ---: | ---: | ---: | --- |
| AAPL 325C | $1,220.00 | $100 | 1220.0% | FAIL |
| NVDA 225C | $1,052.50 | $100 | 1052.5% | FAIL |
| MSFT 510C | $1,835.00 | $100 | 1835.0% | FAIL |
| NVDA 230C | $1,122.50 | $100 | 1122.5% | FAIL |
| ALAB 310C | $3,440.00 | $100 | 3440.0% | Setup failed before account fit could be decisive. |

The account-fit layer worked correctly. High-quality unaffordable contracts were frozen in shadow tracking instead of being replaced with cheaper, lower-quality contracts. `WATCH` remained distinct from `SHADOW_ONLY_QUALIFIED`.

## Options Outcome Review

The four new weekly shadow setups are too recent for 5/10/20/30 trading-day classifications. A 2026-09-07 read-only option quote cross-check using 2026-09-04 marks showed early movement only:

| Shadow Setup | Entry Mid | Latest 2026-09-04 Mark | Early Premium Return |
| --- | ---: | ---: | ---: |
| AAPL 2026-10-16 325C | 12.20 | 8.90 | -27.05% |
| NVDA 2026-10-16 225C | 10.525 | 13.975 | +32.78% |
| MSFT 2026-10-16 510C | 18.35 | 12.90 | -29.70% |
| NVDA 2026-10-16 230C | 11.225 | 11.225 | 0.00% from same-day frozen mark |

These are not mature outcomes. Directional thesis result, contract selection result, and option-versus-underlying result remain `insufficient_data` or pending until scheduled horizons mature.

Call vs put result: all weekly setups were calls; no put sample exists.  
DTE result: all sampled contracts sat in the 42-45 DTE bucket.  
Delta result: qualified contracts stayed near 0.44-0.54 delta; no low-delta affordability substitution was used.  
Liquidity result: mega-cap option liquidity was generally acceptable, except MSFT's degraded bid/ask snapshot and ALAB's wider spread/high IV.

## Current Universe Review

`state/current_universe.json` remains the source of truth and was not rewritten.

| Bucket | Names | Weekly Implication |
| --- | --- | --- |
| Tier 1 | None | Still empty; no evidence supports lowering the 85+ threshold. |
| Tier 2 strengthening | NVDA | Best repeated official-universe options evidence this week. |
| Tier 2 mixed/watch | MSFT, GOOGL, AMZN, META | MSFT produced one setup but weakened next day; GOOGL/AMZN/META lacked fresh direction. |
| Tier 2 post-earnings caution | CRWD, PANW, AVGO | Event/reaction review remains the key blocker. |
| Provisional/watch candidates | AAPL, ALAB, ORCL, CRDO, MU, HOOD, SMCI, DELL, SNOW | Require complete provisional Tier 2 evidence and clean timing before any live-quality proposal. |

No monthly refresh was run, no Current Universe membership was changed, and no rejected-candidate state was updated.

## Primary Blocking-Rule Analysis

Structured weekly research records showed 62 rows. Primary blocking rules were:

| Primary Rule | Count | Read |
| --- | ---: | --- |
| `no_directional_edge` | 18 | Most common blocker; options activity alone was not direction. |
| `blocked_by_earnings` | 13 | PANW, AVGO, ORCL, SNOW, DELL, CRDO, and event buckets. |
| `post_earnings_review` | 8 | CRWD, NVDA, PANW, AVGO required settled structure checks. |
| `blocked_by_extension` | 7 | ALAB, SNDK, CBRS, HOOD and other sharp movers. |
| `penny_stock_or_microcap` | 5 | Options Activity Radar top-tail noise remained filtered. |
| `no_fresh_scanner_edge` | 4 | Current Universe names without fresh confirmation. |
| `account_fit_premium_risk` | 1 in research rows, 4 decisive qualified setup records | Account fit blocked all qualified option setups. |

Options-layer primary blocks:

| Primary Rule | Count | Representative Setups |
| --- | ---: | --- |
| `account_fit_premium_risk` | 4 | AAPL 325C, NVDA 225C, MSFT 510C, NVDA 230C |
| `blocked_by_extension` / setup watch | 1 | ALAB 310C |
| `duplicate_recent_shadow_setup` | 1 research row | NVDA on 2026-09-03 was not double-counted after the 2026-09-02 shadow setup. |

Secondary blocks were retained as context only and not double-counted.

## Score And Threshold Calibration

Official Current Universe score distribution:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 8 |
| Highest | 82 |
| Median | 78 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 75 | 8 |
| Count >= 85 | 0 |

Daily scoped score distributions were not official monthly-refresh evidence. The 2026-09-03 scoped manifest had highest 80, median 72, Tier 1 count 0, Tier 2 count 1. The 2026-09-04 scoped manifest had highest 81, median 71, Tier 1 count 0, Tier 2 count 1.

Calibration observation: Tier 1 remains unreachable in current August/early September artifacts, but the outcome sample is too small and too immature to justify changing Underlying Thesis Score or Options Setup Score thresholds. Keep the calibration warning alive for monthly validation, not a weekly rule change.

## State Decisions

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged; no open theses exist.
- `state/rejected_candidates.json`: unchanged; no new repeated permanent reject state update was authorized by this weekly review.
- `research_logs/2026-09-07-weekly-research-review.md`: created.
- `research_logs/YYYY-MM-DD-research-agent-candidate-review.md`: not created because this run consolidated existing daily artifacts rather than performing a new full candidate scoring pass.

## Next Research Actions

1. Track AAPL, NVDA, MSFT, and NVDA shadow setups at 1/5/10/20/30 trading-day horizons without merging separate signal groups.
2. Prioritize NVDA and MSFT for next daily options-primary review, but require fresh trend, quote, event, and account checks.
3. Keep PANW and AVGO in post-earnings review until first-session and follow-through requirements are satisfied.
4. Keep AAPL and ALAB out of live-quality consideration unless they pass the provisional Tier 2 path or the user approves a one-off exception.
5. Preserve the account-fit blocker as a learning signal: preferred contracts remain too expensive for the $100 validation account.
6. Continue filtering Options Activity Radar's microcap/high-IV top tail before expensive enrichment.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
