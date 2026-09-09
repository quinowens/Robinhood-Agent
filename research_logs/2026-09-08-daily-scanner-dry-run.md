# Daily Scanner Dry Run - 2026-09-08

## Executive Decision

NO TRADE. The scanner produced one setup-quality pass: AVGO 2026-10-16 370C, frozen as `SHADOW_ONLY_QUALIFIED` because account fit fails. No PM_PROPOSAL was produced for live execution.

No live orders were placed, modified, or canceled. `review_option_order` was not called.

## Run Health / Tool Coverage

- Mode: research-only / proposal-only / shadow-trading.
- Account preflight: agentic cash account ending 8691 is active, option level 2, account value $100, cash $100, option buying power $100.
- Existing exposure: no equity positions, no nonzero option positions, no queued equity orders, no queued option orders.
- Saved scanners: Momentum Candidates, Options Activity Radar, and Earnings Risk Radar all matched configured IDs. No substitutions were made.
- Tool coverage: scanner rows, quotes, fundamentals, tradability, direct earnings data, broad market context, selected option chains, selected option instruments, and selected option quotes were refreshed.
- Degradation: scanner exports were connector-capped to visible rows while total item counts were retained. Full financial statement APIs were not available in the exposed read-only tool set.

## Market / Index Context

- SPX: 7673.52.
- NDX: 29507.7014.
- VIX: 15.72.

Market context was constructive but selective. Scanner breadth favored growth, AI infrastructure, semiconductors, and several high-IV speculative names. This regime is permissive for selective long premium research, but it does not override account-fit or extension rules.

## Scanner Summary

| Scanner | Config status | Total items | Useful signal quality |
| --- | --- | ---: | --- |
| Momentum Candidates | Matched expected ID | 399 | Broad but extension-heavy; top rows required same-day chase blocks. |
| Options Activity Radar | Matched expected ID | 136 | Noisy at the top due microcap/sub-$5/extreme-IV rows; useful after permanent filters. |
| Earnings Risk Radar | Matched expected ID | 300 | Correctly flagged ORCL verified 2026-09-10 PM earnings blackout. |

## Underlying Candidate Table

| Symbol | Sources | Tier | Direction | Score | Confidence | Decision | Primary block |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| AVGO | Momentum, Options Activity, Tier 2 | Tier 2 | Bullish | 77 | 75 | SHADOW_ONLY_QUALIFIED | account_fit_premium_risk |
| BE | Momentum, Options Activity | Outside universe | Bullish but extended | 74 | 68 | WATCH | outside_official_current_universe |
| QCOM | Options Activity | Outside universe | Bullish watch | 73 | 66 | WATCH | outside_official_current_universe |
| ORCL | Momentum, Earnings Risk, Tier 2 | Tier 2 | Neutral earnings blackout | 72 | 65 | TEMP_BLOCK | blocked_by_earnings |
| NVDA | Options Activity, Tier 2 | Tier 2 | Neutral | 78 | 70 | WATCH | no_directional_edge |
| GOOGL | Options Activity, Tier 2 | Tier 2 | Neutral | 76 | 68 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| MSFT | Tier 2 review | Tier 2 | Neutral | 74 | 64 | WATCH | no_directional_edge |
| META | Options Activity, Tier 2 | Tier 2 | Neutral | 72 | 62 | NO_DIRECTIONAL_EDGE | no_directional_edge |
| CRWD | Tier 2 review | Tier 2 | Neutral | 72 | 61 | WATCH | no_directional_edge |
| PANW | Tier 2 review | Tier 2 | Neutral watch | 73 | 62 | WATCH | no_directional_edge |
| ROIV | Momentum | Outside universe | Neutral extended | 66 | 59 | TEMP_BLOCK | blocked_by_extension |
| DOCN | Momentum | Outside universe | Bullish but extended | 70 | 62 | TEMP_BLOCK | blocked_by_extension |
| CRWV | Momentum, Options Activity | Watchlist only | Bullish but extended | 71 | 63 | TEMP_BLOCK | blocked_by_extension |
| LITE | Momentum | Outside universe | Bullish but extended | 72 | 62 | TEMP_BLOCK | blocked_by_extension |
| NBIS | Momentum, Options Activity | Watchlist only | Bullish watch | 71 | 63 | WATCH | outside_official_current_universe |

## Options Setup Table

| Rank | Symbol | Contract | Mid | Delta | IV | OI / Vol | Setup score | Setup status | Account fit | Final decision |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 1 | AVGO | 2026-10-16 370C | 18.325 | 0.524882 | 0.386760 | 6814 / 1719 | 76 | QUALIFIED | FAIL | SHADOW_ONLY_QUALIFIED |
| 2 | BE | 2026-10-16 270C | 35.025 | 0.597647 | 0.878945 | 5157 / 5346 | 62 | WATCH | FAIL | WATCH |
| 3 | QCOM | 2026-10-16 180C | 8.125 | 0.451542 | 0.463054 | 4597 / 1029 | 68 | WATCH | FAIL | WATCH |

AVGO was the only setup-quality pass. The 370C was selected over the 360C and 380C because it balanced delta, liquidity, premium, and breakeven without using a cheap far-OTM substitution. The spread was slightly above the preferred 3% midpoint threshold, so it remains a secondary caution rather than a hard block.

## Provisional Tier 2 Review

No daily promotion was written. BE and QCOM were the best non-universe review names, but neither cleared the conservative promotion bar. BE had strong scanner overlap but high IV, high premium, and same-day extension. QCOM had cleaner option pricing but lacked enough independent directional confirmation and was not refreshed with direct earnings-result data.

## Blocked / Rejected Names

- ORCL: `TEMP_BLOCK`; verified earnings on 2026-09-10 PM; earnings lottery trades prohibited.
- ROIV, DOCN, CRWV, LITE: `TEMP_BLOCK`; one-day extension blocked same-day long-option proposals.
- BE: `WATCH`; outside official Current Universe, high IV, premium risk, and extension.
- QCOM: `WATCH`; outside official Current Universe and provisional promotion not confirmed.
- NVDA, GOOGL, MSFT, META, CRWD, PANW: `WATCH` or `NO_DIRECTIONAL_EDGE`; options activity or Tier 2 membership did not create independent direction.
- PDSB, MNTK, OPTT, AMBR, CRBP, BXBL, ARBE, ORBS: `REJECT`; permanent filters blocked microcap/sub-$5/extreme-IV scanner noise before expensive enrichment.

Blocked and rejected candidates have research records preserving primary and secondary blocking rules for opportunity-cost review.

## Missing / Conflicting Data

- Full financial statement enrichment was not exposed in the available tool set.
- Scanner row output was capped to visible rows while total counts were retained.
- QCOM direct earnings results were not refreshed, so it stayed watch-only.
- No conflict was found between saved scanner IDs and `pipeline_config.md`.

## Scanner Quality

Momentum Candidates was useful but extension-heavy. Options Activity Radar was noisy at the top and required permanent filters before enrichment. Earnings Risk Radar performed its main risk function by flagging ORCL's verified near-term earnings.

## Option Setup Quality

AVGO qualified on structure, DTE, delta, liquidity, earnings timing, and current-universe membership. BE and QCOM were sampled after progressive filtering but did not qualify for shadow tracking.

## State-File Decision

No state files were rewritten. `state/current_universe.json` remains the official universe source, and `state/rejected_candidates.json` was not changed because today's obvious permanent rejects were already covered by repeatable filters rather than needing new durable state entries.

## Portfolio Manager Recommendation

Do not open a live position. The AVGO 370C midpoint premium is about $1,832.50 versus $100 option buying power, creating about 1832.5% account-value premium exposure for one contract. Account fit fails even though setup quality passes.

## Shadow-Tracking Decision

Created one options shadow trade:

- `optshadow-2026-09-08-AVGO-20261016-370C`
- Underlying: AVGO
- Contract: 2026-10-16 370C
- Entry midpoint: 18.325
- Max contractual loss: $1,832.50
- Final decision: `SHADOW_ONLY_QUALIFIED`

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
