# Daily Scanner Dry Run - 2026-09-14

Date: 2026-09-14  
Run time: 15:34 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed  
Run ID: `2026-09-14-daily-scanner-dry-run`  
Run status: degraded complete  
Data completeness: 100% terminal status coverage for reviewed candidates; degraded by capped scanner rows, unavailable full financials, and transcript-truncated historical payloads  
Strategy version: 2.0.1  
Strategy mode: options_primary

## Executive Decision

Decision: NO TRADE. No candidate cleared the full path to option-chain work today.

Primary reason: the best official Current Universe momentum names, CRWD and PANW, were both extended same-day cybersecurity breakouts, while other Tier 2 names had no independent directional edge.

Supporting reasons:

- CRWD and PANW are approved Tier 2 underlyings, but 13%+ one-day moves require follow-through review before long-call research.
- ZS and RBRK were strong large-cap scanner leads but remain outside the official Current Universe and did not pass provisional Tier 2 today.
- NVDA, AVGO, AMZN, COHR, and TER weakness was not converted into bearish long-put proposals; failed bullish action is not automatically bearish.
- Account fit remains small-account validation mode: $100 account value, $100 cash, and $100 option buying power.

What would change the decision:

- CRWD or PANW holds the breakout after a complete regular session and passes a fresh extension review.
- An official Tier 2 name develops an independent bullish or bearish thesis not based only on options activity.
- A validated provisional Tier 2 candidate clears critical data, direction, event, trend, and account-fit checks.

## Run Health / Tool Coverage

- Account preflight: Agentic cash account ending 8691 is active with broker option level 2; strategy permission remains only long calls and long puts.
- Existing exposure: no equity positions, no nonzero option positions, no open equity orders, and no queued option orders.
- Saved scanners: Momentum Candidates, Options Activity Radar, and Earnings Risk Radar all matched configured IDs. No substitutions were made.
- Tool coverage: account, portfolio, positions, orders, scanners, quotes, fundamentals, tradability, direct earnings results, earnings calendar, index context, and selected equity historicals were refreshed.
- Degradation: full financial statements were not exposed, scanner rows were frontend-limited for Momentum and Earnings Risk, and historical payloads were too large for full transcript preservation.

## Market / Index Context

- SPX: 7619.98.
- NDX: 29127.1576.
- VIX: 17.10.

Market context was selective and choppier than the prior run. It allows research, but not extension chasing or options-activity-driven direction.

## Scanner Summary

| Scanner | Config status | Total items | Useful signal quality |
| --- | --- | ---: | --- |
| Momentum Candidates | Matched expected ID | 396 | Useful for cybersecurity/software strength: ZS, RBRK, CRWD, PANW, OKTA, FTNT, NET. Several leads were extended. |
| Options Activity Radar | Matched expected ID | 127 | Top tail remained noisy with microcap/sub-$5/high-IV names; useful overlap for ZS, PANW, GOOGL, META, MSFT, AVGO. |
| Earnings Risk Radar | Matched expected ID | 216 | Mostly microcap event risk; high-market-cap calendar flagged KMTS, FPS, TCOM, LEN, and LUXE. |

## Underlying Candidate Table

| Symbol | Sources | Tier | Direction | Score | Confidence | Decision | Primary block |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| CRWD | Momentum, Tier 2 | Tier 2 | Bullish but extended | 76 | 76 | TEMP_BLOCK | blocked_by_extension |
| PANW | Momentum, Options Activity, Tier 2 | Tier 2 | Bullish but extended | 75 | 75 | TEMP_BLOCK | blocked_by_extension |
| ZS | Momentum, Options Activity | Outside universe | Bullish but extended | 73 | 75 | TEMP_BLOCK | blocked_by_extension |
| RBRK | Momentum | Outside universe | Bullish but extended | 71 | 72 | TEMP_BLOCK | blocked_by_extension |
| GOOGL | Momentum, Options Activity, Tier 2 | Tier 2 | Bullish watch | 78 | 73 | WATCH | no_directional_edge |
| META | Options Activity, Tier 2 | Tier 2 | Neutral/bullish watch | 76 | 69 | WATCH | no_directional_edge |
| NVDA | Options Activity, Tier 2 | Tier 2 | Neutral | 74 | 72 | WATCH | no_directional_edge |
| AVGO | Options Activity, Tier 2 | Tier 2 | Neutral/bearish watch | 72 | 72 | WATCH | no_directional_edge |
| MSFT | Options Activity, Tier 2 | Tier 2 | Neutral | 75 | 68 | WATCH | no_directional_edge |
| AMZN | Options Activity, Tier 2 | Tier 2 | Neutral | 73 | 70 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| COHR | Options Activity, Watchlist | Watchlist only | Neutral/bearish watch | 64 | 76 | WATCH | outside_official_current_universe |
| TER | Options Activity | Outside universe | Neutral/bearish watch | 62 | 75 | WATCH | outside_official_current_universe |

## Options Setup Table

| Rank | Symbol | Contract | DTE | Setup score | Setup status | Account fit | Final decision | Primary block |
| ---: | --- | --- | ---: | ---: | --- | --- | --- | --- |
| 1 | None | N/A | N/A | N/A | NOT_EVALUATED | NOT_EVALUATED | NO TRADE | no_candidate_cleared_options_suitability |

No option chains were pulled because no underlying passed the Options Suitability Gate. No options setup record, option shadow trade, or option outcome tracking row was created.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written. ZS and RBRK were the strongest new large-cap scanner leads, but both were outside the official Current Universe and extended by more than 14% in one day. COHR and TER were downside options-activity names but did not form validated bearish setups.

## Blocked / Rejected Names

- CRWD: `TEMP_BLOCK`; official Tier 2 but extended 13.9% on the day.
- PANW: `TEMP_BLOCK`; official Tier 2 with cross-scanner overlap but extended 13.1% on the day.
- ZS, RBRK: `TEMP_BLOCK`; outside Current Universe and extended.
- GOOGL, META, MSFT, AMZN: `WATCH` or `NO_DIRECTIONAL_EDGE`; options activity did not create direction.
- NVDA, AVGO: `WATCH`; weakness was not a validated long-put setup.
- COHR, TER: `WATCH`; outside official Current Universe and no clean bearish options thesis.
- Options Activity and Earnings rows such as MREO, GRO, LITS, FSP, IRIX, HAIN, CRBP, ATNM, CNTY, EVTL, and BDRX: `REJECT`; permanent filters blocked microcap, sub-$5, low-liquidity, high-IV, or event-risk scanner noise.

## Missing / Conflicting Data

- Full financial-statement enrichment was not exposed in the available Robinhood tool set.
- Scanner visible rows were capped for Momentum Candidates and Earnings Risk Radar while total counts were retained.
- Equity historical payloads were available but transcript-truncated, so trend conclusions remained conservative.
- No conflict was found between saved scanner IDs and `pipeline_config.md`.

## Scanner Quality

Momentum Candidates was useful and surfaced a clear cybersecurity/software risk-on pocket. Options Activity Radar was useful only after filtering; its top rows remained dominated by low-quality high-IV names. Earnings Risk Radar was mostly a permanent-filter source today, with only a few large-cap event checks.

## Option Setup Quality

No setup quality pass was produced. The pipeline stopped before option-chain work because serious leads were either extended, outside the official universe/provisional path, lacked independent direction, or were already represented by existing canonical shadow records.

## State-File Decision

No state files were rewritten. `state/current_universe.json` remains the official universe source. `state/open_theses.json` remains empty. `state/rejected_candidates.json` was not changed because today's obvious permanent rejects are handled by repeatable filters rather than requiring durable new entries.

## Portfolio Manager Recommendation

Do not open a live position. No exact reviewed option order was prepared, and `review_option_order` was not called. Account fit remains small-account validation mode with $100 option buying power, which would fail most one-contract long-premium setups even if setup quality passed.

## Shadow-Tracking Decision

No new option shadow trade was created. Existing recent shadow records, including AVGO from 2026-09-08 and META from 2026-09-09, remain canonical; today did not produce a distinct qualified setup worth freezing.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
