# Daily Scanner Dry Run - 2026-09-16

Date: 2026-09-16  
Run time: 15:45 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed  
Run ID: `2026-09-16-daily-scanner-dry-run`  
Run status: degraded complete  
Data completeness: 100% terminal status coverage for reviewed candidates; degraded by capped scanner-visible rows, unavailable full financial statements, transcript-truncated historical payloads, and older uncaptured option history unavailable by source  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: NO NEW OPTIONS PROPOSAL / SHADOW TRACKING ONLY.

Primary reason: no official Tier 1/Tier 2 or validated provisional Tier 2 name produced a fresh, non-duplicative directional options setup today.

Supporting reasons:

- The strongest momentum scanner leaders, including SMTC, LITE, CRDO, COHR, ALAB, GEV, BE, INTC, HPE, and AMD, were outside official Tier 1/Tier 2 or watchlist-only and extended after sharp same-day moves.
- Official Tier 2 names were mostly flat, down, or only weakly confirmed: NVDA, AMZN, AVGO, PANW, META, and CRWD did not justify new option-chain work.
- META and CRWD already have recent canonical shadow setups; duplicating the same thesis would overcount signals.
- The account remains a $100 cash Agentic account with no positions, no open orders, and $100 buying power, so even qualified one-contract long-premium setups would likely remain account-fit failures.

What would change the decision:

- A Tier 2 name develops fresh momentum plus clear directional evidence without duplicating an active signal group.
- An outside-universe scanner leader clears the full provisional Tier 2 path after follow-through, not on a same-day extension.
- Preferred contract premiums become compatible with account risk limits without using far-OTM or short-DTE substitutions.

## Market Context

Market-regime validation:

- `SPX`: 7551.81.
- `NDX`: 28945.0605.
- `VIX`: 17.71.
- Volatility conditions: moderate/choppy, not panic.
- Breadth / participation: selective; semiconductors, optical infrastructure, AI infrastructure, and cybersecurity had visible pockets of strength.
- Leading sectors: scanner leadership concentrated in semiconductors/optical AI infrastructure, mostly outside the official Current Universe.

Interpretation: market context permits research, outcome tracking, and watchlist review, but does not justify extension chasing or duplicate option setups.

## Scanner Summary

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 397 | `% Change desc` | Matched |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 95 | `Implied volatility desc` | Matched |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 191 | `Earnings date desc` | Matched |

Momentum was led by SMTC, LITE, CRDO, FTAI, COHR, ALAB, GEV, BE, INTC, and HPE. Options Activity was noisy at the top with microcap/sub-$5/high-IV rows, but included MU, INTC, HPE, AMD, NVDA, META, AMZN, and AAPL after filtering. Earnings Risk was mainly a risk-control list; high-market-cap near-term reports included LEN, AZO, KBH, THO, MLKN, and WOR.

## Run Health

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Retried calls | 0 |
| Raw rows persisted | 3 scanner payload summaries |
| Deduplicated candidates reviewed | 22 |
| Candidates with terminal status | 22 |
| Completeness percentage | 100% |
| Option checkpoints due / captured / updated / missed | 2 / 2 / 2 / 0 |

Publish decision: degraded complete. The run is usable for research, state continuity, and validation, but not a clean full-data publication because scanner payloads are connector-visible summaries and full financial statements are not exposed.

## Underlying Candidate Table

| Symbol | Sources | Tier | Direction | Score | Confidence | Decision | Primary block |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| SMTC | Momentum | Outside universe | Bullish but extended | 70 | 72 | TEMP_BLOCK | outside_current_universe |
| LITE | Momentum | Outside universe | Bullish but extended | 69 | 70 | TEMP_BLOCK | outside_current_universe |
| CRDO | Momentum, Watchlist | Watchlist | Bullish watch | 72 | 72 | WATCH | outside_official_current_universe |
| COHR | Momentum, Watchlist | Watchlist | Bullish watch | 69 | 70 | WATCH | outside_official_current_universe |
| AMD | Momentum, Options Activity, Watchlist | Watchlist | Bullish watch | 73 | 72 | WATCH | outside_official_current_universe |
| NVDA | Options Activity, Tier 2 | Tier 2 | Neutral/watch | 74 | 72 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| META | Options Activity, Tier 2 | Tier 2 | Bullish watch | 76 | 72 | WATCH | duplicate_recent_shadow_setup |
| AMZN | Options Activity, Tier 2 | Tier 2 | Neutral | 72 | 70 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| AVGO | Momentum, Tier 2 | Tier 2 | Neutral/watch | 74 | 72 | WATCH | no_fresh_directional_edge |
| PANW | Momentum, Tier 2 | Tier 2 | Bullish watch | 75 | 72 | WATCH | no_fresh_directional_edge |
| CRWD | Tier 2 | Tier 2 | Bullish watch | 77 | 74 | WATCH | duplicate_recent_shadow_setup |

## Options Setup Table

No new option-chain work was performed. No candidate cleared the combination of official/provisional universe eligibility, fresh directional thesis, non-duplicate signal status, and Options Suitability Gate.

| Rank | Symbol | Contract | DTE | Setup score | Setup status | Account fit | Final decision | Primary block |
| ---: | --- | --- | ---: | ---: | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A | N/A | NO NEW SETUP | no_fresh_qualified_finalist |

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written. SMTC and LITE had the strongest same-day momentum but were extended and outside the Current Universe. CRDO, COHR, AMD, HPE, INTC, GEV, and BE remain research/watch candidates only unless follow-through plus full critical data clears the provisional path.

## Blocked / Rejected Names

- SMTC, LITE: `TEMP_BLOCK`; outside Current Universe and extended one-day moves.
- CRDO, COHR, AMD: `WATCH`; current watchlist or outside official Tier 2, not promoted today.
- NVDA, AMZN: `NO_DIRECTIONAL_EDGE`; options activity did not create direction.
- META, CRWD: `WATCH`; recent canonical shadow setups already exist, so no duplicate setup.
- AVGO, PANW: `WATCH`; official Tier 2 but no fresh options-primary trigger.
- ORIO, PDSB, OPTT, MNOV, HRTX and many Earnings Risk rows: `REJECT`; permanent filters for microcap, sub-$5 price, insufficient liquidity, high volatility, or event risk.

## Missing / Conflicting Data

- Full financial statements were not exposed in the available connector tools.
- Scanner rows were preserved as visible connector payload summaries, not full 397/95/191-row dumps.
- Historical payloads were available but long outputs were transcript-truncated.
- Older uncaptured option horizons remain `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE`, which is a permanent source limitation and did not fail validation.

## Scanner Quality

Momentum Candidates was useful for identifying AI/optical/semiconductor strength, but many leaders were outside the official universe and extended. Options Activity Radar remained noisy at the top; permanent filters prevented spending enrichment calls on microcap/sub-$5/high-IV rows. Earnings Risk Radar was useful for blocking/reporting near-term event risk, not for trade direction.

## Option Setup Quality

No new setup quality score was assigned because no candidate reached option-chain work. Existing shadow outcomes improved: AAPL 10D and META 5D were observed from today’s prospective checkpoint.

## State-File Decision

No state files were rewritten. `state/current_universe.json` remains the official universe source. `state/open_theses.json` remains empty. `state/rejected_candidates.json` was not changed because today’s permanent rejects were handled by repeatable filters rather than durable new state.

## Portfolio Manager Recommendation

Do not open a live position. Keep account in validation mode. Continue tracking existing AAPL, META, AVGO, CRWD, NVDA, MSFT, and AMZN shadow records according to scheduled horizons. No exact order review was required or performed.

## Shadow-Tracking Decision

No new option shadow trade was created. Two due option checkpoint observations were captured and ingested:

| Underlying | Frozen Contract | Horizon | Entry Mid | Checkpoint Mark | Option Return | Underlying Return |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| AAPL | 2026-10-16 325C | 10D | 12.20 | 14.40 | 18.03% | 1.91% |
| META | 2026-10-16 650C | 5D | 35.575 | 44.05 | 23.82% | 2.58% |

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
