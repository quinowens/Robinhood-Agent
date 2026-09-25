# Daily Scanner Dry Run - 2026-09-15

Date: 2026-09-15  
Run time: 15:40 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed  
Run ID: `2026-09-15-daily-scanner-dry-run`  
Run status: degraded complete  
Data completeness: 100% terminal status coverage for reviewed candidates; degraded by capped scanner-visible rows, unavailable full financials, transcript-truncated historical payloads, and older uncaptured option history unavailable by source  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: SHADOW ONLY / NO LIVE TRADE.

Primary reason: CRWD produced a qualified long-call setup after follow-through, but the selected one-contract premium is $2,140 against a $100 account.

Supporting reasons:

- CRWD is an official Tier 2 Current Universe underlying, appeared in both Momentum Candidates and Options Activity Radar, and cleared the Options Suitability Gate.
- The selected CRWD 2026-11-20 250C has 66 DTE, about 0.512 delta, 1,765 open interest, 294 volume, and an $21.40 midpoint.
- Account fit failed decisively: one contract would risk about 2,140% of account value.
- SWKS, TEM, RVTY, and other scanner leaders remain outside the Current Universe and did not pass provisional Tier 2 today.
- AVGO, META, and AMZN options activity did not create independent direction.

What would change the decision:

- Account size or premium-risk cap increases enough to support one-contract long-premium setups.
- CRWD continues to hold the breakout while preferred-contract spreads tighten.
- A Current Universe or validated provisional Tier 2 name develops a cleaner lower-premium setup without degrading contract quality.

## Market Context

Market-regime validation:

- `SPX`: 7585.73.
- `NDX`: 28937.8378.
- `VIX`: 17.20.
- Volatility conditions: moderate; not panic, but not cheap-premium conditions.
- Breadth / participation: selective; life sciences, semiconductors, energy/refiners, and cybersecurity had visible pockets of strength.
- Leading sectors: cybersecurity was the only approved-universe pocket that produced a serious options candidate.

Interpretation: market context permits research and shadow validation, but not extension chasing or account-cap-busting live premium risk.

## Scanner Summary

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 397 | `% Change desc` | Matched |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 81 | `Implied volatility desc` | Matched |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 182 | `Earnings date desc` | Matched |

Momentum was led by SWKS, TEM, RVTY, ILMN, CIEN, TMO, QCOM, and CRWD. Options Activity remained noisy at the top with microcap/sub-$5 names, but included CRWD, COIN, TSLA, AVGO, META, and AMZN after filtering. Earnings Risk was mostly a rejection/risk filter; high-market-cap calendar names included FPS, TCOM, LEN, LUXE, and ABVX.

## Run Health

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Retried calls | 0 |
| Raw rows persisted | 3 scanner payload summaries |
| Deduplicated candidates reviewed | 19 |
| Candidates with terminal status | 19 |
| Completeness percentage | 100% |
| Option checkpoints due / captured / updated / missed | 1 / 1 / 1 / 0 |

Publish decision: degraded complete. The run is usable for research/shadow tracking, but not a clean full-data publication because scanner payloads are connector-visible summaries and full financial statements are not exposed.

## Underlying Candidate Table

| Symbol | Sources | Tier | Direction | Score | Confidence | Decision | Primary block |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| CRWD | Momentum, Options Activity, Tier 2 | Tier 2 | Bullish | 78 | 76 | SHADOW_ONLY_QUALIFIED | account_fit_premium_risk |
| SWKS | Momentum | Outside universe | Bullish but extended | 70 | 72 | TEMP_BLOCK | outside_current_universe |
| TEM | Momentum | Outside universe | Bullish but extended | 67 | 70 | TEMP_BLOCK | outside_current_universe |
| RVTY | Momentum | Outside universe | Bullish watch | 68 | 70 | WATCH | outside_current_universe |
| AVGO | Options Activity, Tier 2 | Tier 2 | Neutral/bearish watch | 73 | 72 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| META | Options Activity, Tier 2 | Tier 2 | Neutral/bullish watch | 76 | 70 | WATCH | no_directional_edge |
| AMZN | Options Activity, Tier 2 | Tier 2 | Neutral | 72 | 70 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| ANET | Momentum | Watchlist | Bullish watch | 70 | 68 | WATCH | outside_official_current_universe |
| COHR | Momentum | Watchlist | Bullish watch | 67 | 68 | WATCH | outside_official_current_universe |
| COIN / HOOD / CRCL / TSLA | Options Activity | Outside universe | Neutral or bearish watch | N/A | N/A | WATCH | outside_current_universe |

## Options Setup Table

| Rank | Symbol | Contract | DTE | Setup score | Setup status | Account fit | Final decision | Primary block |
| ---: | --- | --- | ---: | ---: | --- | --- | --- | --- |
| 1 | CRWD | 2026-11-20 250C | 66 | 81 | QUALIFIED | FAIL | SHADOW_ONLY_QUALIFIED | account_fit_premium_risk |

Selected contract snapshot: bid 20.55, ask 22.25, midpoint 21.40, delta 0.5118, IV 0.5815, open interest 1,765, volume 294, breakeven 271.40. One-contract premium risk is $2,140.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written. SWKS and TEM had the strongest outside-universe momentum, but both were extended same-day moves and require follow-through review. RVTY, ILMN, CIEN, TMO, and QCOM were interesting large-cap scanner leads but did not clear the Current Universe/provisional path during this daily run.

## Blocked / Rejected Names

- SWKS, TEM: `TEMP_BLOCK`; outside Current Universe and extended one-day moves.
- RVTY, ILMN, CIEN, TMO, QCOM: `WATCH`; outside Current Universe, not promoted today.
- AVGO, META, AMZN: `WATCH` or `NO_DIRECTIONAL_EDGE`; options activity did not create direction.
- COIN, HOOD, CRCL, TSLA, TSM: `WATCH`; outside Current Universe and/or no clean options-primary setup.
- PDSB, XFOR, TXMD, VRA, CTMX, CRBP, BDRX and many Earnings Risk rows: `REJECT`; permanent filters for microcap, low price, insufficient liquidity, high volatility, or event risk.

## Missing / Conflicting Data

- Full financial statements were not exposed in the available connector tools.
- Scanner rows were preserved as visible connector payload summaries, not full 397/81/182-row dumps.
- Historical payloads were available, but long outputs were transcript-truncated.
- The AVGO 2026-09-08 shadow option 5D checkpoint was captured and ingested; the older uncaptured 1D option observation remains `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE`.

## Scanner Quality

Momentum Candidates was useful for broad sector context and surfaced CRWD as an approved-universe continuation candidate. Options Activity Radar was noisy at the top and required aggressive permanent filtering before enrichment. Earnings Risk Radar was mainly useful as a risk-control list, not as an opportunity source.

## Option Setup Quality

CRWD setup quality passed. The 2026-11-20 250C was preferred over cheaper, shorter, or farther-OTM alternatives because it preserved 66 DTE, a roughly 0.51 delta, strong open interest, and reasonable thesis fit. Its spread was not perfect, so setup score stayed at 81 rather than a higher grade.

## State-File Decision

No state files were rewritten. `state/current_universe.json` remains the official universe source. `state/open_theses.json` remains empty. `state/rejected_candidates.json` was not changed because the permanent rejects were already handled by repeatable filters.

## Portfolio Manager Recommendation

Do not open a live position. Record CRWD as `SHADOW_ONLY_QUALIFIED` in the Options Shadow Portfolio and track 1/5/10/20/30 trading-day outcomes. Account fit failed because one contract risks $2,140 against a $100 account; no lower-quality cheap substitute was selected.

## Shadow-Tracking Decision

Created one frozen option shadow trade:

| Underlying | Frozen Contract | Entry Midpoint | DTE | Delta | Setup Score | Account Fit Reason | Tracking |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| CRWD | 2026-11-20 250C | 21.40 | 66 | 0.5118 | 81 | $2,140 premium exceeds $100 account | 1/5/10/20/30d |

The frozen setup lives in `data/options_setup_records/2026-09-15-daily-scanner-dry-run.jsonl`, `data/option_shadow_trades/2026-09-15-daily-scanner-dry-run.jsonl`, and `data/option_signal_outcomes/2026-09-15-daily-scanner-dry-run.jsonl`.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
