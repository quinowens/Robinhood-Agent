# Weekly Research Review — 2026-09-28

Review window: 2026-09-21 through 2026-09-25  
Run date: 2026-09-28  
Operating mode: Research-only / Proposal-only / Shadow-trading  
Strategy mode: Options-primary; equities remain the Approved Underlying Universe  
Execution status: No orders placed, modified, canceled, reviewed, or submitted

## Executive Summary

Decision: **NO TRADE / NO NEW OPTIONS PROPOSAL**.

The five scheduled daily runs all completed with degraded status. Scanner discovery was healthy enough to produce a useful research queue, but result caps, unavailable full financial statements and option historicals, low full-population terminal coverage, and two late runs that missed same-date setup snapshots prevented full-quality publication. The only new contract work was on September 22: SHOP 2026-11-20 145C, TWLO 2026-11-20 280C, and PANW 2026-11-20 380C. All three remained `WATCH`; SHOP was a long-premium chase after a sharp move, while TWLO and PANW failed execution-quality checks. Their one-contract premiums also exceeded the $100 account, but setup quality failed first, so affordability was secondary rather than the primary block.

The mandatory September 28 option checkpoint preflight returned zero due option IDs and was a successful no-op. Across the five daily sessions, 9 checkpoint records were due, 8 quotes were captured, 9 outcome records were updated at least partially, and 1 quote was uncaptured. The uncaptured item was a legacy synthetic NVDA 2026-09-18 230C identifier on September 21; the quote attempt was persisted and the option component remains permanently unavailable. It was not backfilled with a later quote.

Outcome evidence remains too small for threshold changes. The observed long-call sample was weak at 5D and 10D, while 30D outcomes sharply separated underlying correctness from contract correctness: all four observed 30D underlyings were positive, but only one option was positive and the median option return was -100%. No put setup exists in the canonical sample, so call-versus-put comparison is unavailable.

The Current Universe file is stale relative to the evidence window: its last official refresh is 2026-08-03, it has no Tier 1 names, and several temporary-block dates are long expired. This weekly review does not rewrite it. A governed monthly refresh is the appropriate next action.

## Weekly Run Health

| Date | Run status | Scanner success | Visible rows | Named terminal records | New option setups | Checkpoints due / captured / updated / missed |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2026-09-21 | Degraded complete | 3/3 | Connector-capped | 15 plus permanent-filter bucket | 0 | 2 / 1 / 2 / 1 |
| 2026-09-22 | Degraded complete | 3/3 | 600 | 15 plus permanent-filter bucket | 3 WATCH | 1 / 1 / 1 / 0 |
| 2026-09-23 | Degraded complete | 3/3 | 470 | 15 plus permanent-filter bucket | 0 | 4 / 4 / 4 / 0 |
| 2026-09-24 | Degraded complete | 3/3 | 403 | 15 | 0 | 1 / 1 / 1 / 0 |
| 2026-09-25 | Degraded complete | 3/3 | 504 | 15 | 0 | 1 / 1 / 1 / 0 |
| **Week** | **0 successful / 5 degraded / 0 failed** | **15/15** | — | **78 named records** | **3 WATCH** | **9 / 8 / 9 / 1** |

All configured scanners resolved to their documented IDs and ran each day. All runs recorded no live actions and preserved their scoped artifacts. Options-primary steps were not silently skipped: September 21 failed the suitability gate; September 22 completed chain, instrument, quote, scoring, and account-fit work; September 23 and 24 stopped because same-date contract snapshots were unavailable after rollover; September 25 failed the suitability gate before chain work.

Recurring degradation:

- Momentum and/or Earnings Risk results were capped at 200 visible rows on most days.
- Full financial statements, option historicals, and individual P/L trade history were unavailable from the active tool surface.
- Full-population terminal coverage was below 90%; the progressive named finalist set was complete.
- September 23 and 24 did not retain same-date option setup snapshots before the research window rolled.
- Some same-session equity history bars were interpolated or unavailable; retained quote/session data were labeled rather than silently substituted.

Repository validation passed. Integrity status is `PASS_WITH_WARNINGS`: 13 complete qualified chains, zero orphaned shadow records, zero orphaned option outcomes, and zero update failures. The 28 overdue observations are permanent source limitations, led by `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE`, not retryable current-run failures. Integrity also reports four unaccounted scheduled runs, which should be reconciled separately from market-data limitations.

## Market / Benchmark Context

The daily Market Health Score was approximately 70-72, or `Constructive`. SPY and QQQ remained above their 50-day and 200-day averages with generally positive 50-day slopes. The latest retained September 25 closes were about 771.30 for SPY and 744.44 for QQQ; VIX was 14.87 when available. Breadth was frequently unavailable, so the regime did not qualify as fully confirmed `Strong`.

Constructive benchmark trends supported selective bullish research, but did not override extension, earnings, stale snapshot, liquidity, or account-risk rules. Leadership was concentrated in growth, semiconductors, AI infrastructure, and several high-IV names.

## Scanner Review

### Momentum Candidates

Momentum remained the best movement-discovery source. It repeatedly surfaced actionable large-cap or institutional-quality names, including META, MSFT, AMD, PANW, SHOP, TWLO, U, P, QCOM, and MU. Its top tail was often extension-heavy, so scanner rank or recurrence did not establish direction.

### Options Activity Radar

The radar was noisy at the high-IV/microcap end and was used only as attention and liquidity context. It helped prioritize cross-confirmed names such as META, SHOP, U, AMD, QCOM, and MSFT, but never created a bullish or bearish thesis. The stored outcome set has no observed forward returns for comparing confirmed versus unconfirmed momentum, so options-activity lift remains unmeasurable.

### Earnings Risk Radar

Earnings Risk Radar functioned correctly as a risk filter. It supported the MU blackout, SNX event block, and the event-window rejection of otherwise constructive MSFT and QCOM option expressions. No outcome sample yet supports a quantitative claim about avoided losses.

## Weekly Underlying Research Queue

| Priority | Symbol(s) | Weekly evidence | Next research action |
| ---: | --- | --- | --- |
| 1 | MSFT | Improved from neutral/watch to 82, bullish, `STOCK_THESIS_ONLY`; official Tier 2 | Revisit after tentative 2026-10-28 earnings or when a compliant 30+ DTE pre-event window exists |
| 2 | META | Weekly high 84 with bullish evidence on September 24, but otherwise neutral/blocked; existing shadow signal already tracked | Require fresh independent direction and same-date contract snapshot; do not duplicate the old signal group |
| 3 | AMD | Improved from 73 outside-universe watch to 82 provisional Tier 2 with trend/volume confirmation | Re-run full provisional path with same-date option data; consider in monthly universe refresh |
| 4 | TWLO / SHOP | Scores 82 / 80 and valid run-scoped provisional Tier 2 promotions; both reached options research | Reassess after consolidation; require normalized IV/spread and no long-premium chase |
| 5 | U / P | Scores 80 / 79-80; U had strong trend, P remained extended | Capture same-date contract data for U; require settled follow-through for P |
| 6 | RVTY / ILMN / TEM | Scores 79 / 79 / 77 on September 24 and provisional Tier 2 evidence | Refresh direct fundamentals, earnings timing, and same-date contract quality |
| 7 | QCOM | Score 80 with strong relative evidence, but provisional PM path and event window incomplete | Revisit after verified 2026-11-04 earnings |
| 8 | PANW | Official Tier 2, score 77, bullish, reached options research | Wait for spread improvement and cleaner earnings/expiration compatibility |
| 9 | CRWD | Score 76; recent qualified shadow setup already exists | Track existing 250C outcomes; avoid duplicate signal-group counting |
| 10 | MU | Improved to 80 but remained earnings-blocked for 2026-09-30 | Perform first-complete-session post-earnings review; do not auto-clear |

Lower-priority recurring names include GOOGL, AMZN, NVDA, and AVGO. Their scanner frequency was high, but weekly direction was neutral or weakening. AKAM, MRNA, BE, and CRDO require settled follow-through or trend repair. NBIS, IONQ, RKLB, PYPL, DELL, SMCI, and AAPL remain watch-only pending stronger independent evidence and/or complete critical data.

## Directional Thesis Review

The 78 weekly underlying records contained 37 scores at or above the Tier 2 numerical threshold, but only 3 candidates reached `OPTIONS_RESEARCH`. Direction and timing were the dominant filters.

- Bullish serious candidates: TWLO, SHOP, PANW, U, P, EQNR, META, AMD, RVTY, ILMN, TEM, MSFT, QCOM, and selected blocked/watch names.
- Neutral or unsupported recurring names: AMZN, GOOGL, NVDA, AVGO, and META on most sessions. These correctly produced `NO_DIRECTIONAL_EDGE` or `WATCH`, not put proposals.
- Bearish candidates: none qualified. A failed bullish call or negative tape was not converted into a long-put thesis.

Options Suitability Gate totals were: 41 `WATCH`, 15 `NO_DIRECTIONAL_EDGE`, 13 `TEMP_BLOCK`, 5 `REJECT`, 3 `OPTIONS_RESEARCH`, and 1 `STOCK_THESIS_ONLY`.

## Options Setup Review

| Underlying | Contract | DTE / delta | Bid / ask / midpoint | Spread % midpoint | IV | OI / volume | Setup score | Completeness / confidence | Decision |
| --- | --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |
| SHOP | 2026-11-20 145C | 59 / 0.590 | 15.95 / 16.50 / 16.225 | 3.39% | 61.15% | 2,138 / 321 | 78 | 95% / 74% | WATCH: long-premium chase |
| TWLO | 2026-11-20 280C | 59 / 0.587 | 33.30 / 35.70 / 34.50 | 6.96% | 69.43% | 152 / 48 | 70 | 93% / 72% | WATCH: execution quality |
| PANW | 2026-11-20 380C | 59 / 0.531 | 30.80 / 33.85 / 32.325 | 9.44% | 56.20% | 1,082 / 21 | 69 | 93% / 70% | WATCH: execution quality |

All contracts were long calls in the preferred 30-90 DTE and 0.35-0.70 delta ranges. Breakevens were 161.23 for SHOP, 314.50 for TWLO, and 412.33 for PANW. SHOP had the strongest liquidity but poor entry timing after a roughly 48% option-midpoint expansion. TWLO and PANW had materially wide spreads; PANW also carried earnings close to expiration. No long put, 0DTE, short option, covered call, cash-secured put, or multi-leg structure was considered.

## Account Fit / Shadow-Only Review

The account snapshot remained approximately $100 total value, $100 cash, $100 option buying power, no positions, no open orders, and no current open premium risk. The one-contract premiums were $1,622.50, $3,450.00, and $3,232.50. Planned trade risk defaults to maximum contractual loss, so all three failed the $1 single-trade planned-risk cap and buying-power test.

Final weekly classifications:

- `PM_PROPOSAL`: 0
- `SHADOW_ONLY_QUALIFIED`: 0 new
- `QUALIFIED_BUT_NOT_ACCOUNT_FIT`: 0 new
- `WATCH`: 3 contract records
- `TEMP_BLOCK` / `REJECT`: 0 contract records

No contract was setup-quality qualified, so none could become shadow-only qualified. Affordability did not cause substitution into a worse far-OTM or short-DTE contract. Existing META, AVGO, CRWD, NVDA, MSFT, AAPL, and AMZN shadow/outcome groups remain historical evidence and were not duplicated.

## Options Outcome Review

Weekly checkpoint observations:

| Contract / horizon | Option return | Underlying return | Classification |
| --- | ---: | ---: | --- |
| NVDA 2026-10-16 230C / 10D | -42.54% | -3.36% | Underlying loss / option loss |
| AVGO 2026-10-16 370C / 10D | -35.88% | -1.59% | Underlying loss / option loss |
| META 2026-10-16 650C / 10D | +181.66% | +13.88% | Underlying win / option win |
| CRWD 2026-11-20 250C / 5D | +45.33% | +8.23% | Underlying win / option win |
| META 2026-09-18 610C / 30D | -100.00% | +24.20% | Thesis right / contract poor |
| NVDA 2026-09-18 220C / 30D | -100.00% | +3.68% | Thesis right / contract poor |
| NVDA 2026-09-18 225C / 30D | -100.00% | +0.51% | Thesis right / contract poor |
| META 2026-10-16 600C / 30D | +385.83% | +27.68% | Underlying win / option win |
| Legacy NVDA 2026-09-18 230C / 30D | N/A | Underlying/benchmarks updated | Option quote permanently unavailable |

Canonical qualified-setup diagnostics now cover 13 signal groups, all long calls:

| Horizon | Mature sample | Median underlying return | Median option return | Underlying win rate | Option win rate |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1D | 7 | +0.16% | -3.01% | 57.14% | 42.86% |
| 5D | 6 | -1.17% | -22.85% | 50.00% | 16.67% |
| 10D | 4 | -2.48% | -39.21% | 25.00% | 25.00% |
| 20D | 0 | N/A | N/A | N/A | N/A |
| 30D | 4 | +13.94% | -100.00% | 100.00% | 25.00% |

The 30D sample is the clearest warning: three of four observations were `UNDERLYING_WIN_OPTION_LOSS`. Expiration choice, premium paid, and time management can defeat an otherwise correct thesis. Sample sizes remain far below the repository's 20-observation standard for anything stronger than directional commentary.

DTE, delta, spread/liquidity, IV/premium, scanner-source, and market-regime comparisons remain underpowered. There are no puts, no mature 20D samples, and no observed blocked-candidate outcome returns. Account fit failed for all 19 canonical setup records, while 13 nevertheless qualified for shadow tracking; this is a funding constraint, not evidence that lower-quality contracts should be selected.

## Current Universe Review

`state/current_universe.json` remains officially populated but was last refreshed on 2026-08-03. It contains zero Tier 1 names and eight Tier 2 names: GOOGL, AMZN, MSFT, NVDA, META, CRWD, PANW, and AVGO.

- Strengthening: MSFT ended the week at 82 with a bullish stock thesis; META briefly reached 84; PANW reached options research; CRWD's existing setup gained at its 5D checkpoint.
- Mixed: NVDA and META outcome evidence shows both strong and failed contract expressions; new direction was inconsistent.
- Weakening: GOOGL, AMZN, and AVGO repeatedly lacked fresh direction or showed trend weakness; AVGO's 10D call checkpoint was negative.
- Provisional/watchlist pressure: AMD, TWLO, SHOP, U, P, RVTY, ILMN, TEM, EQNR, and QCOM produced Tier 2-level scores during the week, but event, extension, snapshot, or contract-quality blocks prevented promotion into a durable state change.
- Temporary blocks: the official file contains several August `eligible_after` or `next_review_date` values that have expired. Expiry is a review trigger, not automatic eligibility.

Recommendation: perform the governed monthly universe refresh at the next authorized monthly-review run. Do not patch individual tiers or clear blocks from this weekly evidence.

## Primary Blocking-Rule Analysis

Underlying primary blocks were normalized only for weekly diagnosis; secondary reasons were not double-counted:

| Normalized underlying block | Count | Interpretation |
| --- | ---: | --- |
| No fresh directional edge / neutral thesis | 20 | Most common; scanner activity did not become direction |
| Outside Current Universe | 13 | Repeated pressure for a monthly refresh, not automatic promotion |
| Trend failure / damaged structure | 13 | Concentrated in watchlist and neutral names |
| Missing same-date option snapshot | 7 | Operational quality issue on September 23-24 |
| Extension / unsettled move | 7 | Correctly prevented chasing long premium |
| Earnings or event block | 4 | MU and SNX were the clearest cases |
| Incomplete critical data | 3 | Prevented promotion and contract work |
| Penny stock / microcap permanent filter | 3 | Rejected before expensive enrichment |

Options primary blocks were separate: execution quality for TWLO and PANW (2), and long-premium chase for SHOP (1). Account-fit premium risk applied to all three as a secondary block, because none passed setup quality.

## Score and Options Threshold Calibration

Weekly Underlying Thesis Score distribution across 78 named records:

| Metric | Value |
| --- | ---: |
| Highest | 84 |
| Median | 74.0 |
| 90th percentile | 80.0 |
| 95th percentile | 80.3 |
| Count at 75+ Tier 2 numerical threshold | 37 |
| Count at 85+ Tier 1 threshold | 0 |

The distribution supports selectivity: many names cleared the numerical Tier 2 score, but critical-data, direction, timing, eligibility, and options-quality gates reduced that group to three contract reviews. No weekly candidate reached Tier 1. Do not lower the Tier 1 threshold from one week, but the continued absence of Tier 1 names and the stale August universe justify the formal calibration audit required by `universe.md` during the next monthly refresh.

Weekly Options Setup Score distribution for the three reviewed contracts:

| Metric | Value |
| --- | ---: |
| Highest | 78 |
| Median | 70 |
| 90th percentile | 76.4 |
| 95th percentile | 77.2 |
| Count at 75+ descriptive bucket | 1 |
| Qualified setups | 0 |

The repository defines no single mechanical passing score for options; setup qualification remains multi-factor. Across all 19 canonical setup records, the highest score is 82, median 78, 90th percentile 80.2, and 95th percentile 81.1; 13 are qualified shadow-only signals. The tiny and call-only mature sample does not justify changing score thresholds, DTE bands, delta preferences, or spread limits.

## State Decisions

- `state/current_universe.json`: unchanged; weekly evidence is insufficient and the file requires a governed refresh.
- `state/open_theses.json`: unchanged; no live thesis or position was opened.
- `state/rejected_candidates.json`: unchanged; no new repeated permanent reject justified a durable state write.
- No new option setup, shadow trade, or option outcome signal group was created by this weekly review.
- Validation artifacts were written for 2026-09-28 after checkpoint preflight and outcome maturation.

## Next Research Actions

1. Run the overdue governed monthly Current Universe refresh and threshold calibration; explicitly re-evaluate expired temporary blocks.
2. Revisit MSFT and QCOM only after their earnings windows; keep MSFT as a stock thesis without forcing an option expression.
3. Re-run same-date option research for AMD, U, RVTY, ILMN, and TEM when a fresh qualifying session exists.
4. Require consolidation and normalized premium for SHOP and TWLO; require materially tighter spreads for TWLO and PANW.
5. Capture all future due option quotes on the exact target session and continue to keep missed prospective captures separate from permanent option-history limitations.
6. Track CRWD 250C, META calls, AVGO 370C, and NVDA calls without creating duplicate signal groups.
7. Reconcile the integrity audit's four unaccounted scheduled runs and improve same-date setup snapshot capture before expanding scanner coverage.
8. Keep thresholds frozen until larger, two-sided (call and put), outcome-complete samples exist.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
