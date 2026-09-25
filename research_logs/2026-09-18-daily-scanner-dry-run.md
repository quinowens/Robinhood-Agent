# Daily Scanner Dry Run - 2026-09-18

Date: 2026-09-18  
Run time: after close, completed 01:55 CT on 2026-09-19  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed  
Run ID: `2026-09-18-daily-scanner-dry-run`  
Run status: degraded complete  
Data completeness: 100% terminal status coverage for reviewed candidates; degraded by capped scanner-visible rows, unavailable full financial statements, interpolated latest equity-history bars, and older uncaptured option history unavailable by source  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: NO NEW OPTIONS PROPOSAL / SHADOW TRACKING ONLY.

Primary reason: no official Tier 1/Tier 2 or validated provisional Tier 2 name produced a fresh, non-duplicate directional options setup after the Friday session.

Supporting reasons:

- Momentum leaders WBD, ACN, and PSKY were outside the approved Current Universe; WBD/PSKY also carry negative-earnings media-turnaround quality risk.
- Official Tier 2 names surfaced mostly through Options Activity Radar, which is context only and cannot create direction by itself.
- META, CRWD, AVGO, MSFT, and NVDA already have recent shadow/outcome history; duplicating similar call theses would overcount the same signals.
- The Agentic account remains a $100 cash account with no holdings or open orders, so even qualified one-contract long-premium setups would likely remain account-fit failures.

What would change the decision:

- A Tier 2 name develops a fresh directional trigger with no duplicate active signal group.
- An outside-universe scanner leader clears the full provisional Tier 2 path after follow-through and critical-data confirmation.
- Preferred contracts become affordable under premium-risk caps without far-OTM or short-DTE substitution.

## Market Context

Market-regime validation:

- `SPX`: 7650.50.
- `NDX`: 29644.1674.
- `VIX`: 14.81.
- Volatility conditions: constructive/lower volatility, not panic.
- Breadth / participation: selective; scanner leadership included media, consulting/IT services, semiconductors, mega-cap platforms, and speculative high-IV names.
- Leading sectors: mega-cap AI/platforms and semiconductors stayed highly liquid, but fresh scanner momentum was not concentrated in approved Tier 2.

Interpretation: market context permits research and outcome tracking, but does not justify outside-universe promotion, duplicate option setups, or account-cap-busting premium risk.

## Scanner Summary

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 397 | `% Change desc` | Matched |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 108 | `Implied volatility desc` | Matched |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 85 | `Earnings date desc` | Matched |

Momentum was led by WBD, ACN, PSKY, MFG, GH, A, OTIS, SN, AMCR, and NXPI. Options Activity remained noisy at the top with UPXI, LITS, XFOR, KLTR, MYO, and other sub-$5 or microcap/high-IV names, but included NBIS, ORCL, AMD, NVDA, AVGO, META, GOOGL, AMZN, and MSFT after filtering. Earnings Risk was mainly a risk-control list; high-market-cap upcoming reports included AZO, CTAS, PAYX, GIS, SNX, DRI, and COST.

## Run Health

| Metric | Value |
| --- | ---: |
| Expected scanner calls | 3 |
| Successful scanner calls | 3 |
| Failed scanner calls | 0 |
| Retried calls | 0 |
| Raw rows persisted | 3 scanner payload summaries |
| Deduplicated candidates reviewed | 24 |
| Candidates with terminal status | 24 |
| Completeness percentage | 100% |
| Option checkpoints due / captured / updated / missed | 1 / 1 / 1 / 0 |

Publish decision: degraded complete. The run is usable for research, outcome tracking, and validation, but not a clean full-data publication because scanner payloads are connector-visible summaries and older option-history gaps remain permanently unavailable from the source.

## Underlying Candidate Table

| Symbol | Sources | Tier | Direction | Score | Confidence | Decision | Primary block |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| WBD | Momentum | Outside universe | Bullish but low quality | 66 | 76 | WATCH | outside_current_universe |
| ACN | Momentum | Outside universe | Bullish watch | 70 | 74 | WATCH | outside_current_universe |
| PSKY | Momentum | Outside universe | Neutral/watch | 63 | 78 | WATCH | outside_current_universe |
| GOOGL | Options Activity, Tier 2 | Tier 2 | Bullish watch | 78 | 74 | WATCH | no_fresh_directional_edge |
| META | Options Activity, Tier 2 | Tier 2 | Neutral/watch | 75 | 72 | WATCH | duplicate_recent_shadow_setup |
| AMZN | Momentum, Options Activity, Tier 2 | Tier 2 | Neutral/bullish watch | 74 | 72 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| MSFT | Options Activity, Tier 2 | Tier 2 | Neutral/watch | 73 | 75 | WATCH | no_fresh_directional_edge |
| NVDA | Options Activity, Tier 2 | Tier 2 | Bullish watch | 76 | 73 | WATCH | no_fresh_directional_edge |
| AVGO | Options Activity, Tier 2 | Tier 2 | Bullish watch | 76 | 73 | WATCH | no_fresh_directional_edge |
| PANW | Tier 2 review | Tier 2 | Neutral/watch | 74 | 72 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| CRWD | Tier 2 review | Tier 2 | Bullish watch | 75 | 72 | WATCH | duplicate_recent_shadow_setup |

## Options Setup Table

No new option-chain work was performed. No candidate cleared the combination of official/provisional universe eligibility, fresh non-duplicate directional thesis, and Options Suitability Gate.

| Rank | Symbol | Contract | DTE | Setup score | Setup status | Account fit | Final decision | Primary block |
| ---: | --- | --- | ---: | ---: | --- | --- | --- | --- |
| N/A | N/A | N/A | N/A | N/A | N/A | N/A | NO NEW SETUP | no_fresh_qualified_finalist |

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written. WBD, ACN, and PSKY had the strongest Momentum Candidates ranks, but each remains outside the Current Universe and did not clear daily promotion standards. NBIS, ORCL, AMD, MU, and other options-activity names remain watch/research context only unless follow-through and full critical data justify a future provisional review.

## Blocked / Rejected Names

- WBD, ACN, PSKY: `WATCH`; outside Current Universe and not validated as provisional Tier 2.
- GOOGL, NVDA, AVGO, MSFT: `WATCH`; official Tier 2 but no fresh non-duplicate options-primary trigger.
- META, CRWD: `WATCH`; recent canonical shadow setups already exist, so no duplicate setup.
- AMZN, PANW: `NO_DIRECTIONAL_EDGE`; scanner or review context did not create a decisive long-call or long-put thesis.
- UPXI, LITS, XFOR, KLTR, MYO, SPRU, AIBZ and many Earnings Risk rows: `REJECT`; permanent filters for microcap, sub-$5 price, insufficient liquidity, high volatility, event risk, or options activity alone.

## Missing / Conflicting Data

- Full financial statements were not exposed through the available connector tools.
- Scanner rows were preserved as visible connector payload summaries, not full 397/108/85-row dumps.
- Equity historicals for 2026-09-18 returned interpolated zero-volume bars for MSFT, SPY, and QQQ; the source behavior was preserved in the snapshot.
- Older uncaptured option horizons remain `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE` or no-row gaps and did not fail repo validation.

## Scanner Quality

Momentum Candidates found real large-cap activity, but the top names were outside the approved Current Universe and did not fit the options-primary quality bar. Options Activity Radar remains noisy at the top and requires permanent filters before enrichment. Earnings Risk Radar was useful for risk control and calendar context, not direction.

## Option Setup Quality

No new setup quality score was assigned because no candidate reached option-chain work. The mandatory prospective checkpoint updated MSFT 2026-10-16 510C at the 10D horizon: entry mid 18.35, checkpoint adjusted mark 6.78, option return -63.05%, underlying return -2.42%, excess return versus SPY -1.05%, and excess return versus QQQ -2.31%.

## State-File Decision

No state files were rewritten. `state/current_universe.json` remains the official universe source. `state/open_theses.json` remains empty. `state/rejected_candidates.json` was not changed because today’s permanent rejects were handled by repeatable filters rather than durable new state.

## Portfolio Manager Recommendation

Do not open a live position. Keep account in validation mode. Continue tracking existing AAPL, META, AVGO, CRWD, NVDA, MSFT, and AMZN shadow records according to scheduled horizons. No exact order review was required or performed.

## Shadow-Tracking Decision

No new option shadow trade was created. One due option checkpoint observation was captured and ingested:

| Underlying | Frozen Contract | Horizon | Entry Mid | Checkpoint Mark | Option Return | Underlying Return |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| MSFT | 2026-10-16 510C | 10D | 18.35 | 6.78 | -63.05% | -2.42% |

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
