# Weekly Research Review

Review date: 2026-09-20
Review window: 2026-09-14 through 2026-09-20, covering scanner runs on 2026-09-14, 2026-09-15, 2026-09-16, and 2026-09-18 plus checkpoint/validation artifacts through 2026-09-20
Automation: Robinhood Agent Weekly Options Research Review
Mode: Research-only / Proposal-only / Shadow-trading
Order status: No live orders placed, modified, canceled, or reviewed for live execution
Run status: Degraded complete weekly consolidation
Strategy mode: Options primary, equities as Approved Underlying Universe

## Executive Summary

Decision: `NO LIVE TRADE`. The week produced one new canonical setup-quality pass: CRWD 2026-11-20 250C, classified as `SHADOW_ONLY_QUALIFIED` because one contract required about $2,140 against a $100 account. No `PM_PROPOSAL` passed account fit, no `review_option_order` was required, and no live order action was taken.

All options work stayed within v2.0 launch scope: single-leg long calls only. No puts qualified. No 0DTE, naked selling, cash-secured puts, covered calls, spreads, margin-driven selling, earnings lottery trades, or cheap-contract substitutions were recorded.

The main weekly health finding is checkpoint discipline: 2026-09-15, 2026-09-16, 2026-09-17, and 2026-09-18 prospective option quote checkpoints were captured and ingested, but a 2026-09-14 NVDA 5D checkpoint was due and not captured on its target session. That miss is separate from permanent `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE` limitations, which remain valid warnings rather than validation failures.

## Weekly Run Health

| Date | Run ID | Status | Scanner Execution | Options Steps | Health Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-09-14 | `2026-09-14-daily-scanner-dry-run` | Degraded complete | 3/3 matched | Correctly skipped chains | CRWD/PANW were extended; Tier 2 names lacked clean direction. |
| 2026-09-15 | `2026-09-15-daily-scanner-dry-run` | Degraded complete | 3/3 matched | CRWD chain/instruments/quotes | CRWD shadow setup persisted canonically. |
| 2026-09-16 | `2026-09-16-daily-scanner-dry-run` | Degraded complete | 3/3 matched | Correctly skipped chains | No fresh non-duplicate qualified finalist. |
| 2026-09-18 | `2026-09-18-daily-scanner-dry-run` | Degraded complete | 3/3 matched | Correctly skipped chains | No fresh non-duplicate qualified finalist; MSFT checkpoint ingested. |

Health summary:

- Successful/degraded/failed runs: 4 degraded-complete scanner runs, 0 failed scanner runs.
- Scanner coverage: all configured scanners matched expected IDs in every scanner run.
- Tool coverage: account state, portfolio, positions, open orders, scanners, quotes, fundamentals, tradability, earnings/event context, indexes, selected histories, option chains/instruments/quotes, outcome analytics, strategy diagnostics, integrity audit, and validation artifacts were represented.
- Missing/degraded fields: capped visible scanner rows, unavailable full financial statements, transcript-truncated historical payloads, interpolated zero-volume equity-history bars on 2026-09-18 snapshots, and older option history not supported by source.
- v2.0 options steps: no run incorrectly skipped options work after a candidate passed the gate. Chains were skipped only when direction, duplicate-signal control, universe eligibility, extension risk, or suitability did not pass.
- Order tools: no `review_option_order`, `place_option_order`, `cancel_option_order`, `place_equity_order`, or scanner/watchlist write tool was used.

## Prospective Checkpoint Preflight

Run-date preflight for 2026-09-20 returned `count: 0`, so no Robinhood option quote read was required. A zero-item due manifest was treated as a successful no-op.

Weekly checkpoint audit:

| Checkpoint Date | Due | Captured | Updated / Ingested | Missed | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| 2026-09-14 | 1 | 0 | 0 | 1 | Missed NVDA 2026-10-16 230C 5D checkpoint; no later quote backfill allowed. |
| 2026-09-15 | 1 | 1 | 1 | 0 | AVGO 370C 5D observed. |
| 2026-09-16 | 2 | 2 | 2 | 0 | AAPL 325C 10D and META 650C 5D observed. |
| 2026-09-17 | 3 | 3 | 3 | 0 | AMZN 265C 20D, NVDA 225C 10D, and CRWD 250C 1D observed from target-date checkpoint. |
| 2026-09-18 | 1 | 1 | 1 | 0 | MSFT 510C 10D observed. |
| 2026-09-19 | 0 | 0 | 0 | 0 | No-op. |
| 2026-09-20 | 0 | 0 | 0 | 0 | No-op. |

Totals: 8 due, 7 captured, 7 updated, 1 missed. The missed 2026-09-14 checkpoint should remain visible as a process gap. Permanent older-history warnings should not be counted as missed prospective checkpoints.

## Market / Benchmark Context

| Date | SPX | NDX | VIX | Read |
| --- | ---: | ---: | ---: | --- |
| 2026-09-14 | 7619.98 | 29127.1576 | 17.10 | Constructive but choppy; no extension chasing. |
| 2026-09-15 | 7585.73 | 28937.8378 | 17.20 | Selective; cybersecurity produced the serious setup. |
| 2026-09-16 | 7551.81 | 28945.0605 | 17.71 | Choppy/selective; no duplicate setup warranted. |
| 2026-09-18 | 7650.50 | 29644.1674 | 14.81 | Constructive, but fresh leaders stayed outside approved universe. |

Market context permitted selective long-premium research but did not override universe, extension, duplicate-signal, earnings, or account-fit rules.

## Scanner Review

| Scanner | Weekly Match Range | Quality Read |
| --- | ---: | --- |
| Momentum Candidates | 396-397 | Useful for finding cybersecurity, semiconductor, optical/AI infrastructure, media, and consulting strength; many leads were extended or outside universe. |
| Options Activity Radar | 81-127 | Useful as options context after filtering; top rows stayed noisy with microcap, low-price, high-IV names. |
| Earnings Risk Radar | 85-216 | Useful for event-risk control and calendar context; not a direction source. |

Scanner frequency was not treated as bullish or bearish evidence. Options Activity Radar remained options context, not direction.

## Underlying Queue

| Priority | Symbol | Weekly Evidence | Next Action |
| ---: | --- | --- | --- |
| 1 | CRWD | Official Tier 2; 2026-09-15 bullish follow-through produced qualified 66 DTE call setup, account-fit failure only; 1D checkpoint later positive. | Continue 5/10/20/30D shadow tracking; require fresh confirmation before another chain. |
| 2 | META | Official Tier 2; recent shadow setup, 5D checkpoint positive; later runs blocked duplicate setup. | Track existing outcome, avoid duplicate bullish signal. |
| 3 | AVGO | Official Tier 2; prior 5D checkpoint observed negative; fresh week was mostly no-directional-edge/watch. | Reassess only with fresh direction and event/trend confirmation. |
| 4 | NVDA | Official Tier 2; options activity and diagnostics sample mixed/weak; one 2026-09-14 checkpoint missed. | Keep tracking remaining valid horizons; do not escalate on options activity alone. |
| 5 | GOOGL, MSFT, AMZN | Official Tier 2; mostly watch/no-directional-edge; MSFT 10D checkpoint negative. | Continue neutral watch and outcome review. |
| 6 | PANW | Official Tier 2; extended on 9/14 and lacked fresh edge later. | Recheck after clean follow-through, not same-day extension. |
| 7 | CRDO, AMD, COHR, ANET | Watchlist names with repeated scanner interest. | Full provisional Tier 2 path required before options research. |
| 8 | SMTC, LITE, WBD, ACN, PSKY, SWKS, TEM, RVTY | Outside-universe scanner leaders. | Research queue only; no state promotion from weekly evidence. |

## Directional Thesis Review

Only CRWD reached options research this week. Directional thesis was bullish with 74 directional confidence and a 30-90 day horizon. Neutral, unsupported, duplicate, or extension-damaged direction dominated the rest of the official Tier 2 reviews. Failed bullish evidence was not converted into bearish long-put proposals.

Options Suitability Gate distribution across 45 weekly research records:

| Status | Count |
| --- | ---: |
| `WATCH` | 26 |
| `TEMP_BLOCK` | 8 |
| `NO_DIRECTIONAL_EDGE` | 6 |
| `REJECT` | 4 |
| `OPTIONS_RESEARCH` | 1 |

## Options Setup Review

| Underlying | Contract | DTE | Delta | Bid / Ask / Mid | Spread % Mid | OI / Volume | IV | Score | Final Decision |
| --- | --- | ---: | ---: | --- | ---: | --- | ---: | ---: | --- |
| CRWD | 2026-11-20 250C | 66 | 0.511795 | 20.55 / 22.25 / 21.40 | 7.94 | 1765 / 294 | 0.581518 | 81 | `SHADOW_ONLY_QUALIFIED` |

Options Setup Score distribution for canonical setup records created this week:

| Metric | Options Setup Score |
| --- | ---: |
| Count | 1 |
| Highest | 81 |
| Median | 81 |
| 90th percentile | 81 |
| 95th percentile | 81 |
| Count >= 70 | 1 |
| Count >= 75 | 1 |
| Count >= 80 | 1 |

No put setup qualified. No account-fit pass occurred.

## Account-Fit / Shadow-Only Review

The Agentic account snapshot remained small-account validation mode: $100 account value, $100 cash, $100 option buying power, no equity positions, no option positions, and no open orders.

| Setup | One-Contract Premium | Buying Power | Premium / Account | Account-Fit Result |
| --- | ---: | ---: | ---: | --- |
| CRWD 250C | $2,140.00 | $100 | 2140% | FAIL |

The account-fit layer worked correctly. The high-quality unaffordable CRWD setup was frozen in the dedicated options shadow portfolio instead of being replaced with a cheaper lower-quality contract. `WATCH` stayed distinct from `SHADOW_ONLY_QUALIFIED`.

## Options Outcome Review

Fresh observed checkpoints this week:

| Underlying | Contract | Horizon | Option Return | Underlying Return | Classification |
| --- | --- | ---: | ---: | ---: | --- |
| AVGO | 2026-10-16 370C | 5D | -75.83% | N/A in weekly table | Observed; contract weak. |
| AAPL | 2026-10-16 325C | 10D | +18.03% | +1.91% | Underlying win / option win. |
| META | 2026-10-16 650C | 5D | +23.82% | +2.58% | Underlying win / option win. |
| AMZN | 2026-10-16 265C | 20D | -75.14% | -5.68% | Underlying loss / option loss. |
| NVDA | 2026-10-16 225C | 10D | -49.17% | -2.25% | Underlying loss / option loss. |
| CRWD | 2026-11-20 250C | 1D | +4.35% | +1.31% | Underlying win / option win. |
| MSFT | 2026-10-16 510C | 10D | -63.05% | -2.42% | Underlying loss / option loss. |

Strategy diagnostics now cover 13 canonical qualified call setups. Samples remain small:

| Horizon | Mature Sample | Option Win Rate | Underlying Win Rate | Median Option Return | Median Underlying Return |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1D | 7 | 42.86% | 57.14% | -3.01% | +0.16% |
| 5D | 7 | 14.29% | 42.86% | -33.17% | -2.64% |
| 10D | 4 | 25.00% | 25.00% | -53.61% | -2.34% |
| 20D | 1 | 0.00% | 0.00% | -75.14% | -5.68% |
| 30D | 0 | N/A | N/A | N/A | N/A |

The emerging lesson is not a threshold change; it is a caution that long premium has underperformed in the small observed sample when the underlying thesis failed or moved too little.

## Current Universe Review

`state/current_universe.json` remains the source of truth and was not rewritten.

| Bucket | Names | Weekly Implication |
| --- | --- | --- |
| Tier 1 | None | Still empty; no weekly evidence supports lowering the 85+ threshold. |
| Tier 2 strengthening | CRWD | One qualified shadow-only call setup plus positive 1D checkpoint. |
| Tier 2 mixed/neutral | META, AVGO, NVDA, GOOGL, MSFT, AMZN, PANW | Existing shadow outcomes are mixed; most fresh reviews lacked non-duplicate direction. |
| Watchlist / provisional queue | CRDO, AMD, COHR, ANET, SMTC, LITE, WBD, ACN, PSKY | Research queue only; no provisional promotion was authorized. |

No monthly refresh was run, no Current Universe membership was changed, and no rejected-candidate state was updated.

## Primary Blocking-Rule Analysis

Primary blocking rules across weekly research records:

| Primary Rule | Count | Read |
| --- | ---: | --- |
| `no_directional_edge` | 13 | Most common blocker; scanner or options context did not create direction. |
| `outside_current_universe` | 8 | New scanner names lacked official/provisional eligibility. |
| `no_fresh_directional_edge` | 6 | Tier 2 names had watch-level evidence but no fresh trigger. |
| `outside_official_current_universe` | 5 | Watchlist/outside names stayed research-only. |
| `blocked_by_extension` | 4 | Same-day sharp moves blocked long-call research. |
| `duplicate_recent_shadow_setup` | 4 | Avoided overcounting active META/CRWD-style signal groups. |
| `penny_stock_or_microcap` | 3 | Permanent filters caught noisy high-IV rows. |
| `permanent_filters` | 1 | Aggregated permanent-filter reject bucket. |
| None | 1 | CRWD passed to options research, then failed account fit. |

Options-layer primary blocks:

| Primary Rule | Count | Representative Setup |
| --- | ---: | --- |
| `account_fit_premium_risk` | 1 | CRWD 2026-11-20 250C |

Secondary blocks were retained as context only and not double-counted.

## Score And Threshold Calibration

Weekly research-record score distribution:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 45 |
| Highest | 78 |
| Median | 73 |
| 90th percentile | 76 |
| 95th percentile | 77.8 |
| Count >= 75 | 15 |
| Count >= 85 | 0 |

Official Current Universe score distribution remains the August refresh baseline:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 8 |
| Highest | 82 |
| Median | 78 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 75 | 8 |
| Count >= 85 | 0 |

Calibration observation: Tier 1 remains unreachable in current artifacts, but outcome samples are too small, call-only, and still degraded by source limitations. Do not change Underlying Thesis Score or Options Setup Score thresholds from this weekly sample.

## Validation And Integrity

Post-checkpoint analytics run on 2026-09-20:

- `data/validation_reports/2026-09-20-outcome-analytics.json` created.
- `data/validation_reports/2026-09-20-strategy-diagnostics.json` created.
- `data/validation_reports/2026-09-20-integrity-audit.json` created.
- `data/validation_reports/2026-09-20-validation-output.txt` created.

Validation passed with warnings. Integrity status was `PASS_WITH_WARNINGS`: 13 canonical outcome records, 13 qualified setups, 0 orphaned shadow records, 0 orphaned outcome records, 21 overdue outcome observations, and 0 update failures. The overdue observations are dominated by permanent historical-source limitations and legacy migration vocabulary; they are not live-trading blockers and should not be confused with missed prospective checkpoints.

## State Decisions

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged; no open theses exist.
- `state/rejected_candidates.json`: unchanged; weekly permanent rejects were handled by repeatable filters.
- `research_logs/2026-09-20-weekly-research-review.md`: created.
- `research_logs/2026-09-20-research-agent-candidate-review.md`: not created; this run consolidated existing daily artifacts rather than performing a new full candidate scoring pass.

## Next Research Actions

1. Track CRWD 250C at 5/10/20/30 trading-day horizons and keep it separate from duplicate signal groups.
2. Keep the 2026-09-14 missed NVDA checkpoint visible as a process issue; do not backfill it with a later quote.
3. Continue distinguishing prospective misses from permanent `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE` warnings.
4. Prioritize CRWD, META, and AVGO for fresh review only when direction is current and non-duplicate.
5. Recheck PANW after follow-through; same-day extension should continue to block new long-call research.
6. Keep CRDO, AMD, COHR, ANET, SMTC, LITE, WBD, ACN, and PSKY in the research queue unless a full provisional Tier 2 path clears.
7. Keep Options Activity Radar filtered aggressively; its top tail remains noisy and should not drive direction.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
