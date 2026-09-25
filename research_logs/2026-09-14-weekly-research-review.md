# Weekly Research Review

Review date: 2026-09-14
Review window: 2026-09-08 through 2026-09-11 trading activity, plus read-only account cross-check on 2026-09-14
Automation: Robinhood Agent Weekly Options Research Review
Mode: Research-only / Proposal-only / Shadow-trading
Order status: No orders placed, modified, canceled, or reviewed for live execution
Run status: Degraded complete weekly consolidation
Strategy mode: Options primary, equities as Approved Underlying Universe

## Executive Summary

Decision: `NO LIVE TRADE`. The weekly pipeline produced two canonical setup-quality passes, both classified as `SHADOW_ONLY_QUALIFIED` because account fit failed. No `PM_PROPOSAL` reached account-fit pass, no `review_option_order` was required, and no live order action was taken.

| Date | Underlying | Contract | DTE | Setup Score | Account Fit | Final Decision |
| --- | --- | --- | ---: | ---: | --- | --- |
| 2026-09-08 | AVGO | 2026-10-16 370C | 38 | 76 | FAIL | `SHADOW_ONLY_QUALIFIED` |
| 2026-09-09 | META | 2026-10-16 650C | 37 | 80 | FAIL | `SHADOW_ONLY_QUALIFIED` |

Two additional sampled option records, BE 2026-10-16 270C and QCOM 2026-10-16 180C, stayed `WATCH`; they were not qualified shadow setups. The September 10 and September 11 runs correctly stopped before option-chain work because no candidate cleared the Options Suitability Gate.

All weekly options work stayed inside v2.0 launch scope: single-leg long calls only. No puts qualified. No 0DTE, naked selling, cash-secured puts, covered calls, spreads, margin-driven selling, earnings lottery trades, or cheap-contract substitutions were recorded.

The decisive blocker remains account fit. A 2026-09-14 read-only portfolio cross-check confirmed the Agentic cash account ending `8691` still has $100 account value, $100 cash, and $100 buying power, with no equity or options value. The qualified one-contract premiums were about $1,832.50 for AVGO and $3,557.50 for META, far above buying power and premium-risk limits.

## Weekly Run Health

| Date | Run ID | Status | Scanner Execution | Options Steps | Health Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-09-08 | `2026-09-08-daily-scanner-dry-run` | Degraded complete | 3/3 matched | AVGO, BE, QCOM chains/instruments/quotes | AVGO shadow setup persisted canonically; BE/QCOM stayed watch-only. |
| 2026-09-09 | `2026-09-09-daily-scanner-dry-run` | Degraded complete | 3/3 matched | META chain/instruments/quotes | META shadow setup persisted canonically. |
| 2026-09-10 | `2026-09-10-daily-scanner-dry-run` | Degraded complete | 3/3 matched | Correctly skipped chains | Event risk and no-directional-edge blocks stopped option work. |
| 2026-09-11 | `2026-09-11-daily-scanner-dry-run` | Degraded complete | 3/3 matched | Correctly skipped chains | HPE/DELL were extended outside-universe leads; Tier 2 names lacked direction. |

Health summary:

- Successful/degraded/failed runs: 4 degraded-complete runs, 0 failed runs.
- Scanner coverage: all three configured scanners matched expected IDs each day.
- Tool coverage: account, portfolio, positions, orders, realized P/L where used, scanners, quotes, fundamentals, tradability, direct earnings, index context, selected option chains, selected option instruments, and option quotes were available across the week.
- Missing/degraded fields: capped visible scanner rows, unavailable full financial statements, unavailable option historicals and option-level-upgrade info in later runs, and truncated historical payloads in some session transcripts.
- v2.0 options steps: no run incorrectly skipped options work after a candidate passed the gate. Chains were skipped only when underlying direction, event timing, universe status, or suitability did not pass.
- Order tools: no `review_option_order`, `place_option_order`, `cancel_option_order`, `place_equity_order`, or scanner/watchlist write tool was used.

## Market / Benchmark Context

| Date | SPX | NDX | VIX | Read |
| --- | ---: | ---: | ---: | --- |
| 2026-09-08 | 7673.52 | 29507.7014 | 15.72 | Constructive but selective. |
| 2026-09-09 | 7636.36 | 29421.553 | 16.46 | Constructive/selective, software and mega-cap context. |
| 2026-09-10 | 7591.70 | 29103.5128 | 17.84 | Choppier; event-heavy scanner tape. |
| 2026-09-11 | 7656.98 | 29368.4389 | 15.84 | Constructive again with lower VIX. |

Market context permitted selective long-premium research but did not override earnings, extension, universe, directional-thesis, or account-fit rules.

## Scanner Review

| Scanner | Weekly Match Range | Quality Read |
| --- | ---: | --- |
| Momentum Candidates | 397-399 | Useful for surfacing AVGO, META, NET, MRVL, AMD, MU, CPRT, ORCL, HPE, DELL, SMCI, and ANET, but many leads were event-heavy or extended. |
| Options Activity Radar | 67-136 | Useful as options context after filters; top rows remained noisy with microcap, sub-$5, and high-IV names. |
| Earnings Risk Radar | 252-331 | Correctly highlighted ORCL, LEN, ADBE, KR, and other event-risk names; direct earnings data controlled final blocks. |

Scanner frequency was not treated as bullish or bearish evidence. Options Activity Radar remained options context, not direction.

## Underlying Queue

| Priority | Symbol | Weekly Evidence | Next Action |
| ---: | --- | --- | --- |
| 1 | META | Official Tier 2; 2026-09-09 bullish setup qualified with score 80, strong liquidity, and account-fit failure only. | Track shadow outcome; require fresh directional confirmation before any new chain work. |
| 2 | AVGO | Official Tier 2; 2026-09-08 bullish setup qualified with score 76, but spread was a secondary caution. | Track shadow outcome; refresh post-earnings/event and trend context before next setup. |
| 3 | NVDA | Official Tier 2; frequent options activity but no fresh direction this week. | Watch for renewed underlying thesis; do not escalate on options activity alone. |
| 4 | GOOGL | Official Tier 2; repeated no-directional-edge outputs with scores up to 78. | Continue neutral watch until directional evidence improves. |
| 5 | MSFT | Official Tier 2; recurring review name, neutral/no edge this week. | Refresh trend/RS before any future options research. |
| 6 | AMZN | Official Tier 2; neutral/no edge on reviewed days. | Watch for recovery in directional evidence. |
| 7 | PANW, CRWD | Official Tier 2; mostly watch/no-directional-edge. | Keep post-event and trend review active. |
| 8 | HPE, DELL | Strong September 11 scanner overlap but extended and outside official Current Universe. | Recheck after complete-session follow-through; possible provisional Tier 2 review only if full criteria pass. |
| 9 | MRVL, AMD, MU, QCOM, BE | Interesting non-official or watchlist names; sampled or reviewed but not promoted. | Require full provisional Tier 2 path and clean timing before escalation. |
| 10 | ORCL, CPRT, ADBE, KR | Event/post-earnings leads. | Keep temporarily blocked until post-earnings rules clear. |

## Directional Thesis Review

Bullish candidates that reached options research:

| Symbol | Directional Read | Confidence | Outcome |
| --- | --- | ---: | --- |
| AVGO | Bullish on 2026-09-08 | 75 | Qualified setup, account fit failed, shadow-only. |
| META | Bullish on 2026-09-09 | 74 | Qualified setup, account fit failed, shadow-only. |

Bullish-watch or bullish-but-extended candidates that did not qualify included BE, QCOM, NET, MRVL, AMD, HPE, DELL, DOCN, CRWV, LITE, and NBIS. Neutral or unsupported direction dominated official Tier 2 reviews for NVDA, GOOGL, MSFT, AMZN, CRWD, PANW, and AVGO/META on non-setup days. Failed bullish evidence was not converted into bearish long-put proposals.

## Options Setup Review

| Underlying | Contract | Delta | Bid / Ask / Mid | Spread % Mid | OI / Volume | IV | Breakeven | Quality |
| --- | --- | ---: | --- | ---: | --- | ---: | ---: | --- |
| AVGO | 2026-10-16 370C | 0.524882 | 18.00 / 18.65 / 18.325 | 3.55 | 6814 / 1719 | 0.386760 | 388.33 | Qualified; spread secondary caution. |
| BE | 2026-10-16 270C | 0.597647 | 34.45 / 35.60 / 35.025 | 3.28 | 5157 / 5346 | 0.878945 | 305.03 | Watch only; outside universe and setup score 62. |
| QCOM | 2026-10-16 180C | 0.451542 | 8.00 / 8.25 / 8.125 | 3.08 | 4597 / 1029 | 0.463054 | 188.13 | Watch only; outside official Current Universe. |
| META | 2026-10-16 650C | 0.553752 | 35.30 / 35.85 / 35.575 | 1.55 | 13017 / 4285 | 0.394210 | 685.58 | Qualified. |

Options Setup Score distribution for canonical setup records this week:

| Metric | Options Setup Score |
| --- | ---: |
| Count | 4 |
| Highest | 80 |
| Median | 72 |
| 90th percentile | 78.8 |
| 95th percentile | 79.4 |
| Count >= 70 | 2 |
| Count >= 75 | 2 |
| Count >= 80 | 1 |

Qualified-only setup scores were 76 and 80. Both were calls in the 37-38 DTE bucket with deltas around 0.52-0.55. No put sample qualified.

## Account-Fit / Shadow-Only Review

| Setup | One-Contract Premium | Buying Power | Premium / Account | Account-Fit Result |
| --- | ---: | ---: | ---: | --- |
| AVGO 370C | $1,832.50 | $100 | 1832.5% | FAIL |
| META 650C | $3,557.50 | $100 | 3557.5% | FAIL |

The account-fit layer worked correctly. High-quality unaffordable setups were frozen in the dedicated options shadow portfolio instead of being replaced with lower-quality far-OTM or shorter-DTE contracts. `WATCH` stayed distinct from `SHADOW_ONLY_QUALIFIED`.

## Options Outcome Review

The two new weekly shadow setups are too recent for mature 5/10/20/30 trading-day conclusions. Their outcome records exist, but classification fields remain pending/insufficient. A 2026-09-09 validation report showed broader outcome health as degraded: 15 overdue observations were missing because underlying, option, SPY, or QQQ histories were unavailable during maintenance. The validation still passed with warnings and reported no orphaned shadow or outcome records.

Available historical diagnostics across 12 canonical qualified chains show the sample is still small and mixed:

- Calls only; no put performance sample exists.
- 1D mature sample: 6, option win rate 33.3%, underlying win rate 50.0%.
- 5D mature sample: 5, option win rate 0.0%, underlying win rate 40.0%.
- 10D mature sample: 1, option win rate 0.0%, underlying win rate 0.0%.
- 20D and 30D samples were not mature/observable enough for conclusions.

Do not use this sample to change thresholds. The main action is to keep outcome backfill/retry work moving so thesis-right versus contract-right classifications can mature.

## Current Universe Review

`state/current_universe.json` remains the source of truth and was not rewritten.

| Bucket | Names | Weekly Implication |
| --- | --- | --- |
| Tier 1 | None | Still empty; no evidence supports lowering the 85+ threshold. |
| Tier 2 strengthening | META, AVGO | Both produced one qualified shadow-only call setup this week. |
| Tier 2 neutral/watch | NVDA, GOOGL, MSFT, AMZN, CRWD, PANW | Liquidity remains useful, but weekly direction was mostly unsupported. |
| Watchlist / provisional candidates | HPE, DELL, MRVL, AMD, MU, QCOM, BE, SMCI, ANET | Interesting research queue only; no state promotion was authorized. |
| Temporary/event review | ORCL, CPRT, ADBE, KR | Keep blocked until post-earnings/event review clears. |

No monthly refresh was run, no Current Universe membership was changed, and no rejected-candidate state was updated.

## Primary Blocking-Rule Analysis

Structured weekly research records contained 54 rows. Primary blocking rules were:

| Primary Rule | Count | Read |
| --- | ---: | --- |
| `no_directional_edge` | 24 | Most common blocker; options activity or Tier 2 membership did not create direction. |
| `outside_official_current_universe` | 9 | Non-universe/watchlist names were not promoted from daily evidence. |
| `blocked_by_earnings` | 8 | ORCL, CPRT, ADBE, KR, and event buckets. |
| `blocked_by_extension` | 7 | One-day extension blocked same-day long-option proposals. |
| `permanent_filters` | 4 | Microcap/sub-$5/high-IV scanner noise filtered before expensive enrichment. |
| None | 2 | AVGO and META qualified at the underlying/options setup layer, then failed account fit. |

Options-layer primary blocks:

| Primary Rule | Count | Representative Setups |
| --- | ---: | --- |
| `account_fit_premium_risk` | 2 | AVGO 370C, META 650C |
| `outside_official_current_universe` | 2 | BE 270C, QCOM 180C |

Secondary blocks were retained as context only and not double-counted.

## Score And Threshold Calibration

Weekly research-record score distribution:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 54 |
| Highest | 78 |
| Median | 74 |
| 90th percentile | 77 |
| 95th percentile | 78 |
| Count >= 75 | 20 |
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

Calibration observation: Tier 1 remains unreachable in current artifacts, but the outcome sample is too small, immature, and partially degraded to justify changing Underlying Thesis Score or Options Setup Score thresholds. Keep the calibration warning alive for monthly validation, not a weekly rule change.

## State Decisions

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged; no open theses exist.
- `state/rejected_candidates.json`: unchanged; weekly permanent rejects were handled by repeatable filters, and no durable state update was authorized.
- `research_logs/2026-09-14-weekly-research-review.md`: created.
- `research_logs/2026-09-14-research-agent-candidate-review.md`: not created; this run consolidated daily artifacts rather than performing a new full candidate scoring pass.

## Next Research Actions

1. Track AVGO 370C and META 650C at 1/5/10/20/30 trading-day horizons without merging signal groups.
2. Retry/backfill overdue option outcome observations where history tools become available, especially the matured August and early September records.
3. Prioritize META and AVGO for fresh daily review only if directional evidence remains intact; require current quote, event, trend, and account checks.
4. Recheck HPE and DELL after follow-through; do not promote without the full provisional Tier 2 path.
5. Keep ORCL, CPRT, ADBE, and KR in post-earnings/event review until direct earnings and full-session structure requirements clear.
6. Continue filtering Options Activity Radar's microcap/high-IV top tail before expensive enrichment.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
