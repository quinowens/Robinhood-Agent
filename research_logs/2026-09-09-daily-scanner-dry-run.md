# Daily Scanner Dry Run - 2026-09-09

## Executive Decision

Decision: NO TRADE. One setup-quality pass was found: META 2026-10-16 650C, frozen as `SHADOW_ONLY_QUALIFIED` because account fit fails. No `PM_PROPOSAL` was produced for live execution.

No live orders were placed, modified, or canceled. `review_option_order` was not called.

## Run Health / Tool Coverage

- Mode: research-only / proposal-only / shadow-trading.
- Account preflight: agentic cash account ending 8691 is active, option level 2, account value $100, cash $100, option buying power $100.
- Existing exposure: no equity positions, no nonzero option positions, no queued equity orders, no queued option orders.
- Realized P/L: $0 YTD realized P/L and no closing trades; no drawdown breaker triggered from broker data.
- Saved scanners: Momentum Candidates, Options Activity Radar, and Earnings Risk Radar all matched configured IDs. No substitutions were made.
- Tool coverage: scanners, account, portfolio, positions, orders, realized P/L, quotes, fundamentals, tradability, direct earnings, earnings calendar, index context, selected option chains, selected option instruments, and selected option quotes were refreshed.
- Degradation: scanner exports were connector-capped to visible rows while total item counts were retained; full financial-statement APIs were not exposed; some historical payloads were truncated in the session transcript.

## Market / Index Context

- SPX: 7636.36.
- NDX: 29421.553.
- VIX: 16.46.

Market context was constructive but selective. The scanner tape favored software/cloud, mega-cap platforms, and semiconductors. VIX remained mid-teens, so selective long-premium research was permitted, but account-fit, universe, earnings, and extension rules controlled final decisions.

## Scanner Summary

| Scanner | Config status | Total items | Useful signal quality |
| --- | --- | ---: | --- |
| Momentum Candidates | Matched expected ID | 399 | Useful, with NET, META, DDOG, MRVL, AMD, MU among visible high-quality rows. |
| Options Activity Radar | Matched expected ID | 95 | Noisy at the top due microcap/sub-$5/high-IV rows; useful after permanent filters. |
| Earnings Risk Radar | Matched expected ID | 331 | Correctly flagged near-term earnings risk including ORCL and LEN. |

## Underlying Candidate Table

| Symbol | Sources | Tier | Direction | Score | Confidence | Decision | Primary block |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| META | Momentum, Options Activity, Tier 2 | Tier 2 | Bullish | 78 | 74 | SHADOW_ONLY_QUALIFIED | account_fit_premium_risk |
| NET | Momentum, Options Activity | Outside universe | Bullish but extended | 74 | 68 | TEMP_BLOCK | blocked_by_extension |
| MRVL | Momentum, Options Activity | Outside universe | Bullish watch | 76 | 71 | WATCH | outside_official_current_universe |
| AMD | Momentum, Options Activity, Watchlist | Watchlist only | Bullish watch | 75 | 70 | WATCH | outside_official_current_universe |
| MU | Momentum, Options Activity, Watchlist | Watchlist only | Bullish watch | 74 | 68 | WATCH | outside_official_current_universe |
| NVDA | Options Activity, Tier 2 | Tier 2 | Neutral | 78 | 70 | WATCH | no_directional_edge |
| GOOGL | Options Activity, Tier 2 | Tier 2 | Neutral | 76 | 68 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| AMZN | Options Activity, Tier 2 | Tier 2 | Neutral | 74 | 66 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| MSFT | Momentum, Tier 2 | Tier 2 | Neutral | 74 | 65 | WATCH | no_directional_edge |
| AVGO | Tier 2 review | Tier 2 | Neutral | 76 | 68 | WATCH | no_directional_edge |
| ORCL / LEN | Earnings Risk | Mixed | Neutral blackout | 0 | 90 | TEMP_BLOCK | blocked_by_earnings |

## Options Setup Table

| Rank | Symbol | Contract | Mid | Delta | IV | OI / Vol | Setup score | Setup status | Account fit | Final decision |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 1 | META | 2026-10-16 650C | 35.575 | 0.553752 | 0.394210 | 13017 / 4285 | 80 | QUALIFIED | FAIL | SHADOW_ONLY_QUALIFIED |
| 2 | MRVL | 2026-10-16 240C | 18.225 | 0.510563 | 0.672862 | 3356 / 954 | 68 | WATCH | FAIL | WATCH |
| 3 | AMD | 2026-10-16 520C | 35.050 | 0.546836 | 0.508055 | 2192 / 695 | 70 | WATCH | FAIL | WATCH |
| 4 | NET | 2026-10-16 320C | 22.075 | 0.508213 | 0.606403 | 63 / 85 | 52 | TEMP_BLOCK | FAIL | TEMP_BLOCK |

META was selected over the 660C because the 650C had better open interest, better volume, a slightly stronger delta fit, and no affordability-driven compromise. The setup still fails account fit because one contract requires about $3,557.50 of premium.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written. MRVL and AMD were the closest non-official Tier 2 candidates, but both stayed watch-only because the daily run should not rewrite `state/current_universe.json`, setup quality did not exceed the current-universe candidate, and account fit would fail either way. NET was blocked by same-day extension. MU remains watch-only with verified 2026-09-30 earnings to monitor.

## Blocked / Rejected Names

- NET: `TEMP_BLOCK`; >10% same-day extension and weak sampled option liquidity.
- MRVL, AMD, MU: `WATCH`; outside official Tier 2/provisional promotion not written; option premium/account fit fail.
- NVDA, GOOGL, AMZN, MSFT, AVGO: `WATCH` or `NO_DIRECTIONAL_EDGE`; options activity or Tier 2 membership did not create independent direction.
- ORCL, LEN: `TEMP_BLOCK`; near-term earnings risk.
- SKYA, PLRX, IRD, ARBE, CYPH, CTRM, EVMN, ATLX, ODD, GFUZ, ANNX, SOHU, XPOF, OPTT: `REJECT`; permanent filters blocked microcap/sub-$5/high-IV or extreme-move scanner noise before expensive enrichment.

Blocked and rejected candidates have research records preserving primary and secondary blocking rules for opportunity-cost review.

## Missing / Conflicting Data

- Full financial-statement enrichment was not exposed in the available Robinhood tool set.
- Scanner row output was capped to visible rows while total counts were retained.
- Historical payloads were available but truncated in the session transcript, so trend conclusions were conservative.
- No conflict was found between saved scanner IDs and `pipeline_config.md`.

## Scanner Quality

Momentum Candidates was useful today and surfaced several institutionally relevant names. Options Activity Radar remained noisy at the top, but after permanent filters it gave useful context for META, MRVL, AMD, MU, NVDA, GOOGL, AMZN, and AAPL. Earnings Risk Radar performed its main risk-control function.

## Option Setup Quality

META qualified on DTE, delta, liquidity, spread, current-universe membership, and event timing. MRVL and AMD were reasonable research samples but not shadow-qualified because they are not official Tier 2/provisional promotions and account fit fails. NET failed setup quality because the move was extended and the sampled contract had weak liquidity and a wide spread.

## State-File Decision

No state files were rewritten. `state/current_universe.json` remains the official universe source. `state/open_theses.json` remains empty. `state/rejected_candidates.json` was not changed because today's obvious permanent rejects are handled by repeated permanent filters rather than needing durable new state entries.

## Portfolio Manager Recommendation

Do not open a live position. The META 650C midpoint premium is about $3,557.50 versus $100 option buying power, creating about 3557.5% account-value premium exposure for one contract. Account fit fails even though setup quality passes.

## Shadow-Tracking Decision

Created one options shadow trade:

- `optshadow-2026-09-09-META-20261016-650C`
- Underlying: META
- Contract: 2026-10-16 650C
- Entry midpoint: 35.575
- Max contractual loss: $3,557.50
- Final decision: `SHADOW_ONLY_QUALIFIED`

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
