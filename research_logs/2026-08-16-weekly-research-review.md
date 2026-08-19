# Weekly Research Review - 2026-08-16

Automation: Robinhood Agent Weekly Options Research Review  
Mode: Research-only / proposal-only / shadow-trading  
Review window: 2026-08-11 through 2026-08-14 daily scanner runs, plus current state, August validation, and relevant backtests  
Source path note: the configured workspace path `Robinhood-Agent-v1.6` was stale; repository evidence was read from `/Users/quinowens/Desktop/Robinhood-Agent`.

## Executive Summary

Decision: NO LIVE TRADE. Four canonical long-call setups reached `SHADOW_ONLY_QUALIFIED` this week, all blocked by account-fit premium risk rather than setup quality. No setup reached `PM_PROPOSAL` because one standard contract exceeded the $100 Agentic account value and buying power.

Canonical shadow setups added or reviewed:

| Date | Underlying | Contract | DTE | Mid | Setup Score | Account Fit | Final Decision |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 2026-08-11 | NVDA | 2026-09-18 220C | 38 | 10.75 | 80 | FAIL | SHADOW_ONLY_QUALIFIED |
| 2026-08-11 | META | 2026-09-18 610C | 38 | 26.60 | 78 | FAIL | SHADOW_ONLY_QUALIFIED |
| 2026-08-12 | NVDA | 2026-09-18 225C | 37 | 10.325 | 78 | FAIL | SHADOW_ONLY_QUALIFIED |
| 2026-08-13 | META | 2026-10-16 600C | 64 | 31.55 | 80 | FAIL | SHADOW_ONLY_QUALIFIED |

A same-day 2026-08-11 META shadow rerun exists, but it is explicitly non-canonical and supersedes the earlier setup only for audit/backfill context; analytics should use canonical rows only. On 2026-08-14, no candidate passed directional thesis plus Options Suitability Gate, so the run correctly skipped option-chain work.

## Weekly Run Health

All four scheduled daily dry runs executed the three configured scanners and completed with `DEGRADED` status. There were no failed runs and no live-order reviews, placements, modifications, or cancellations.

| Date | Run ID | Status | Scanner Calls | Options Finalists | Completeness | Notes |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 2026-08-11 | `2026-08-11-daily-scanner-dry-run` | DEGRADED | 3/3 | 2 | 87% | META and NVDA reached shadow-only long-call records. |
| 2026-08-11 | `2026-08-11-daily-scanner-shadow-rerun` | DEGRADED | 3/3 | 1 | 78% | Same-day META repair/rerun; non-canonical duplicate controls present. |
| 2026-08-12 | `2026-08-12-daily-scanner-dry-run` | DEGRADED | 3/3 | 1 | 86% | NVDA reached shadow-only; account fit failed. |
| 2026-08-13 | `2026-08-13-daily-scanner-dry-run` | DEGRADED | 3/3 | 3 | 84% | META qualified; PANW/NVDA sampled but WATCH due event risk. |
| 2026-08-14 | `2026-08-14-daily-scanner-dry-run` | DEGRADED | 3/3 | 0 | 82% | Correctly skipped options steps after no clean gate pass. |

Primary degradation themes: connector-visible scanner rows did not include full raw result payloads; some logs used transcript-limited row preservation; daily runs were not official universe refreshes; no run should overwrite Current Universe. The v2.0 options steps were not incorrectly skipped: Aug 11-13 used scoped options research after underlying gate pass, and Aug 14 stopped before chains because no candidate passed direction plus suitability.

## Market And Benchmark Context

Daily logs described SPY/QQQ context as constructive on longer trend but mixed or modestly negative intraday later in the week. On 2026-08-14, SPY was 776.09 versus 777.88 prior close (-0.23%) and QQQ was 730.01 versus 732.07 prior close (-0.28%). Scanner leadership concentrated in semiconductors, storage, optical networking, fintech, and AI-infrastructure names, but many were outside the approved Current Universe or extended.

This market context did not justify overriding event risk, universe status, weak intraday action, or missing directional thesis. Neutral or damaged tape was not treated as an automatic long-put signal.

## Scanner Review

The configured scanner set remained intact:

| Scanner | Role | Weekly Observation |
| --- | --- | --- |
| Momentum Candidates | Underlying movement discovery | Useful for surfacing META/NVDA and watchlist interest, but scanner frequency was not treated as bullish evidence by itself. |
| Options Activity Radar | Options context | Confirmed attention in NVDA, MU, SNDK, NBIS, SMCI, AMZN and others, but also produced persistent high-IV micro/small-cap noise. It did not create direction. |
| Earnings Risk Radar | Event-risk confirmation | Useful for NVDA, CRWD, PANW, AVGO, COHR and post-earnings extension names. It blocked or reduced setup quality rather than rejecting universe membership. |

Raw scanner match totals increased through the week: Momentum 158/153/208/289; Options Activity 43/40/63/112; Earnings Risk 316/323/332/338 for Aug 11-14 respectively. Visible rows were persisted, but full scanner totals exceeded the connector payload available to the transcript.

## Underlying Queue

Priority research queue for next week:

| Priority | Symbol | Reason | Next Action |
| ---: | --- | --- | --- |
| 1 | NVDA | Recurring Tier 2, repeated options research, strong contract liquidity. | Recheck after earnings-event risk; no new long premium inside event window without clear exit rule. |
| 2 | META | Recurring Tier 2, two qualified call setups, but latest Aug 14 tape lost fresh directional edge. | Reassess relative strength and post-extension follow-through before new call research. |
| 3 | GOOGL | Highest Current Universe score at 82, but repeatedly neutral/no edge. | Refresh trend/RS; options only if direction becomes explicit. |
| 4 | AMZN | Highest score at 82; post-earnings/extension context and weak tape persisted. | Confirm block clearance and fresh direction. |
| 5 | MSFT | Score 81; trend damage/no fresh confirmation. | Watch for regained RS and clean 30-90 DTE call setup. |
| 6 | CRWD | Tier 2 but verified earnings 2026-08-26 PM. | Keep temporary event block until post-earnings review. |
| 7 | PANW | Tier 2 cybersecurity, bullish sample on Aug 13 but blocked by 2026-09-01 PM earnings/event risk. | Recheck after event-risk window; no shadow unless setup quality passes. |
| 8 | AVGO | Tier 2; options activity/semiconductor context but weak trend and 2026-09-02 PM earnings monitor. | Keep watch/event review. |
| 9 | MU / SNDK / AMD / RDDT | Watchlist/outside-current-universe scanner interest. | Consider provisional Tier 2 only with complete scoring, tradability, earnings, histories, and benchmark RS. |
| 10 | NBIS / SMCI / CRWV | Recurrent scanner interest but post-earnings extension and outside-current-universe blocks. | Review only after settled follow-through; do not chase extension. |

## Directional Thesis Review

Across 56 research records, 14 rows had bullish direction and 42 were neutral. No bearish thesis qualified; no long puts were proposed. Five rows reached `OPTIONS_RESEARCH`; most others were `WATCH`, `TEMP_BLOCK`, `NO_DIRECTIONAL_EDGE`, or `REJECT`.

Serious directional candidates:

| Symbol | Weekly Direction | Confidence | Result |
| --- | --- | ---: | --- |
| NVDA | Bullish early week, neutral by Aug 14 | 50-74 | Qualified twice for long-call shadow; later blocked by earnings/event risk. |
| META | Bullish Aug 11 and Aug 13, neutral by Aug 14 | 45-74 | Qualified twice for long-call shadow; later no fresh edge. |
| PANW | Bullish sample Aug 13 | ~68 | WATCH/TEMP context due earnings-event risk and setup score 68. |
| AVGO | Mostly neutral; brief bullish/watch context | 45-68 | No options proposal; insufficient direction/weak trend. |
| MU/SNDK/AMD/RDDT/NBIS | Bullish scanner interest outside Current Universe | 55-60 | WATCH/TEMP_BLOCK; no provisional Tier 2 promotion. |

The workflow correctly did not treat a failed bullish setup as bearish.

## Options Setup Review

All qualified options were long calls. No puts, 0DTE, spreads, covered calls, cash-secured puts, naked selling, or margin-driven structures appeared.

Canonical option setup quality:

| Underlying | Expiration | Strike | DTE Bucket | Delta | Spread % Mid | OI | Volume | Score | Completeness | Confidence |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| NVDA | 2026-09-18 | 220C | 30-45 | 0.5235 | 0.93% | 40,761 | 2,338 | 80 | 92 | 76 |
| META | 2026-09-18 | 610C | 30-45 | 0.5153 | 2.63% | 1,860 | 404 | 78 | 92 | 74 |
| NVDA | 2026-09-18 | 225C | 30-45 | 0.5097 | 1.45% | 55,362 | 2,505 | 78 | 92 | 76 |
| META | 2026-10-16 | 600C | 61-90 | 0.4966 | 1.58% | 6,849 | 325 | 80 | 94 | 78 |

The setup scores clustered at 78-80. Liquidity and spreads were generally acceptable for the selected contracts. The unresolved issue was account fit, not contract quality. The non-canonical 2026-08-11 META rerun unit issue has been fixed by storing `premium_per_contract` and `option_mid` in option-price units while storing `contract_premium_dollars` separately.

## Account-Fit And Shadow-Only Review

Every canonical qualified setup failed account fit because one standard contract exceeded the $100 account value and buying power. Premium risk ranged from about $1,032.50 to $3,155 per contract for the Aug 12-13 records, and the Aug 11 canonical option midpoints imply $1,075 for NVDA and $2,660 for META. The Portfolio Manager correctly classified these as `SHADOW_ONLY_QUALIFIED` and did not substitute cheaper far-OTM or shorter-DTE contracts.

No `PM_PROPOSAL` was appropriate. Account fit failure is an account constraint and funding requirement signal, not a reason to downgrade the underlying thesis or replace the selected contract.

## Options Outcome Review

Option outcome files exist for the four canonical shadow setups plus the one non-canonical Aug 11 META rerun. They currently carry forward-tracking identifiers but no mature performance outcome fields yet: thesis-right, contract-right, 1/5/10/20/30-day returns, MFE/MAE, target/stop, and expiration outcomes are still insufficient data. That is expected because the records were created this week and need forward trading days.

Current classification evidence:

| Slice | Observation |
| --- | --- |
| Call vs put | 4 canonical calls, 0 puts; no bearish sample. |
| DTE | Three canonical 30-45 DTE setups, one 61-90 DTE setup. |
| Delta | All near 0.50 delta; no low-delta affordability substitution. |
| Liquidity | NVDA liquidity strongest; META acceptable but lower volume. |
| IV/premium | IV around 0.34-0.38; outcome sample too young for calibration. |
| Account-fit failures | 4/4 canonical qualified setups failed account fit. |

## Current Universe Review

Current Universe remains populated from the 2026-08-03 official catch-up refresh. No weekly state rewrite is authorized from these degraded daily runs.

| Bucket | Names | Weekly Implication |
| --- | --- | --- |
| Tier 1 | None | Still empty; no candidate reached 85+. |
| Tier 2 strengthening | NVDA, META | Both generated qualified shadow-only call setups, but current event/timing still matters. |
| Tier 2 stable but no direction | GOOGL, AMZN, MSFT | High scores but no clean options direction by week end. |
| Tier 2 event/watch | CRWD, PANW, AVGO | Maintain event-risk monitoring; no fresh PM proposal. |
| Watchlist/provisional candidates | MU, SNDK, AMD, RDDT, NBIS, SMCI, CRWV | Scanner interest exists, but no validated provisional Tier 2 promotion. |

No Current Universe, open thesis, or rejected-candidate state file should be changed from this weekly review.

## Primary Blocking-Rule Analysis

Research-record primary blockers, counting the weekly persisted rows once each, were led by `outside_current_universe` (15), `earnings_event_risk` (6), `penny_stock_or_microcap` (5), `no_fresh_directional_edge` (4), `account_risk` (3), `weak_relative_strength` (3), `extended_one_day_move` (2), `blocked_by_earnings` (2), `blocked_by_extension_review` (2), `weak_trend` (2), and smaller single-count rules.

Underlying blocks and options/account blocks should remain separated:

| Layer | Main Primary Blocks | Interpretation |
| --- | --- | --- |
| Underlying eligibility | outside_current_universe, penny_stock_or_microcap, extended_one_day_move | Scanner leaders were often not approved underlyings or were extended/noisy. |
| Direction/options gate | no_directional_edge, earnings_event_risk, weak_trend | Neutral or event-risk names correctly stopped before proposal. |
| Account fit | account_risk/account_fit_premium_risk | Qualified setup blocked only by account size; preserve in shadow tracking. |

Secondary blocks were retained as context in records but should not be double-counted.

## Score And Threshold Calibration

Weekly research-score distribution across persisted records with numeric scores:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 46 |
| Highest | 82 |
| Median | 77 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 65 | 40 |
| Count >= 75 | 32 |
| Count >= 85 | 0 |

Weekly options setup-score distribution for canonical qualified setups:

| Metric | Options Setup Score |
| --- | ---: |
| Count | 4 |
| Highest | 80 |
| Median | 79 |
| 90th percentile | 80 |
| 95th percentile | 80 |
| Count >= 75 | 4 |
| Count >= 80 | 2 |

August validation already flags `highest_score_below_tier_1_threshold`: highest 82, median 80, 90th 82, 95th 82, Tier 1 threshold 85, Tier 1 count 0. This supports monitoring Tier 1 calibration, but not changing thresholds from one small weekly options sample. Keep the current Tier 1/Tier 2 and Options Setup thresholds unchanged until more outcome data exists.

## State Decisions

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged; no open theses.
- `state/rejected_candidates.json`: unchanged; no new permanent rejection update was clearly authorized from weekly evidence.
- `data/validation_reports/2026-08-validation-summary.json`: read as validation context; not regenerated in this weekly pass.
- New weekly report saved to `research_logs/2026-08-16-weekly-research-review.md`.

## Next Research Actions

1. Track canonical NVDA and META option shadow outcomes at 1, 5, 10, 20, and 30 trading days, separating thesis-right from contract-right.
2. Recheck NVDA and CRWD around the 2026-08-26 PM earnings event; keep long-premium setups blocked or watch-only unless exit/event rules are clean.
3. Recheck PANW before 2026-09-01 PM and AVGO before 2026-09-02 PM; do not force options exposure through earnings.
4. Re-evaluate META only if relative strength and direction reappear; avoid duplicate same-signal shadow entries unless the signal_group policy clearly marks canonical replacement.
5. For MU, SNDK, AMD, RDDT, NBIS, SMCI, and CRWV, require full provisional Tier 2 evidence before option chains.
6. Keep the explicit option-price versus contract-dollar premium fields under validation so future performance analytics do not mix units.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
