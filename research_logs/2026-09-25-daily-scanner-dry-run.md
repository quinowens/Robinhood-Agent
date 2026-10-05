# Daily Scanner Dry Run — 2026-09-25

Date: 2026-09-25  
Run time: 15:31-15:47 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed, modified, canceled, reviewed, or submitted  
Run ID: `2026-09-25-daily-scanner-dry-run`  
Run status: `DEGRADED_COMPLETE`  
Strategy version: 2.0.1  
Strategy mode: `options_primary`

## Executive Decision

Decision: **NO TRADE**. No option chain was opened because no finalist passed the Options Suitability Gate.

MSFT had the strongest underlying evidence, but the first compliant 30+ DTE window crosses tentative October 28 earnings. QCOM could not complete the provisional Tier 2/Portfolio Manager path for the same event-window reason, and CRDO remained temporarily blocked by extension plus a declining 50-day trend. Options activity was treated only as context and did not create direction.

What would change the decision:

- MSFT supplies a clean post-earnings setup or a future pre-event window with at least 30 DTE.
- QCOM completes provisional Tier 2 evidence and a full Portfolio Manager proposal after event risk clears.
- CRDO holds its move through a settled follow-through session and repairs its 50-day trend.

## Run Health and Tool Coverage

| Metric | Result |
| --- | --- |
| Account/tool preflight | Complete |
| Saved scanners resolved | 3 of 3 matched |
| Scanner executions | 3 of 3 succeeded |
| Raw rows persisted | 504 |
| Deduplicated visible symbols | 483 |
| Named terminal records | 15 (3.11% visible coverage) |
| Option checkpoint | Due 1; captured 1; updated 1; missed 0 |
| Outcome retrieval | Underlying/SPY/QQQ 49 of 49; option 21 of 49 |
| Validation | Passed with warnings; 0 errors/orphans |
| Live order actions | 0 |

Publish status is degraded because Momentum exposed 200 of 397 matches, Earnings Risk exposed 200 of 281 matches, full financial statements and option historicals are unavailable, and only the progressive finalist set received direct enrichment. The limitations were preserved rather than backfilled or inferred.

## Market and Index Context

- SPX: 7,743.41; NDX: 30,608.1343; VIX: 14.87.
- SPY closed near 771.30, above its 20-day (765.35), 50-day (761.56), and 200-day (718.45) averages; the 50-day slope remained positive.
- QQQ closed near 744.44, above its 20-day (720.87), 50-day (712.65), and 200-day (665.59) averages.
- Regime: constructive, with low-to-mid-teens volatility, but scanner leadership was concentrated in semiconductors, AI infrastructure, and several high-IV names.

## Scanner Summary

| Scanner | Scan ID | Total matches | Visible rows | Sort | Quality read |
| --- | --- | ---: | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 397 | 200 | % Change desc | Useful large-cap leaders; capped output |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 104 | 104 | Implied volatility desc | Top tail dominated by microcaps/high IV; useful lower-row context |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 281 | 200 | Earnings date desc | Effective risk control; capped output |

Cross-scanner large-cap attention included MSFT, QCOM, CRDO, BE, PYPL, DELL, SMCI, AKAM, COST, and AAPL. Scanner overlap increased confidence only; it did not add underlying-score points or establish direction.

## Underlying Candidate Table

| Rank | Symbol | Sources | Score / completeness / confidence | Direction | Tier / eligibility | Final class | Primary block |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | MSFT | Momentum + Options Activity | 82 / 92% / 84% | Bullish | Tier 2 / eligible | STOCK_THESIS_ONLY | No compliant pre-earnings expiration window |
| 2 | QCOM | Momentum + Options Activity | 80 / 90% / 78% | Bullish | Watchlist / not promoted | TEMP_BLOCK | Provisional PM path incomplete |
| 3 | CRDO | Momentum + Options Activity | 73 / 90% / 82% | Bullish watch | Watchlist / extension block | TEMP_BLOCK | Unconfirmed extension |
| 4 | BE | Momentum + Options Activity | 76 / 68% / 70% | Bullish watch | Watchlist | TEMP_BLOCK | Unconfirmed extension |
| 5 | PYPL | Momentum + Options Activity | 75 / 68% / 67% | Bullish watch | Watchlist | WATCH | Incomplete critical data |
| 6 | DELL | Momentum + Options Activity | 74 / 67% / 66% | Bullish watch | Watchlist | WATCH | Incomplete critical data |
| 7 | SMCI | Momentum + Options Activity | 72 / 66% / 68% | Bullish watch | Watchlist | WATCH | Outside Current Universe |
| 8 | AKAM | Momentum + Options Activity | 73 / 66% / 68% | Bullish watch | Watchlist | WATCH | Incomplete critical data |
| 9 | COST | Momentum + Options Activity | 74 / 66% / 70% | Bullish watch | Watchlist | TEMP_BLOCK | Post-earnings review unsettled |
| 10 | NVDA | Options Activity | 76 / 78% / 74% | Neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | Options activity alone insufficient |
| 11 | META | Options Activity | 75 / 80% / 76% | Neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | Failed bullish setup is not bearish |
| 12 | AMZN | Options Activity | 73 / 78% / 71% | Neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | Options activity alone insufficient |
| 13 | MU | Options Activity + Earnings Risk | 76 / 76% / 84% | Neutral | Watchlist / earnings block | TEMP_BLOCK | September 30 earnings |
| 14 | AVGO | Momentum | 74 / 76% / 70% | Neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | No fresh directional edge |
| 15 | AAPL | Momentum + Options Activity | 74 / 67% / 68% | Bullish watch | Watchlist | WATCH | Outside Current Universe |

Scores for the directly enriched finalists are reproducible from quote, fundamental, earnings, tradability, historical, volume, and benchmark data. Lower-ranked rows are preliminary and explicitly lose completeness/confidence because expensive enrichment stopped after the progressive finalist set.

## Options Setup Table

| Underlying | Suitability Gate | Chain work | Options Setup Score | Options completeness / confidence | Decision |
| --- | --- | --- | --- | --- | --- |
| MSFT | Fail for option expression | Not pulled | N/A | N/A | STOCK_THESIS_ONLY |
| QCOM | Fail | Not pulled | N/A | N/A | TEMP_BLOCK |
| CRDO | Fail | Not pulled | N/A | N/A | TEMP_BLOCK |

There were no serious contract finalists, so no contract rank, selection reason, premium risk, or option setup score was manufactured. No `PM_PROPOSAL`, `SHADOW_ONLY_QUALIFIED`, or `QUALIFIED_BUT_NOT_ACCOUNT_FIT` record was created.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written.

- QCOM met several underlying-quality conditions but could not complete the required full Portfolio Manager proposal because a compliant 30+ DTE thesis window would cross verified November 4 earnings.
- CRDO remained below the Tier 2 score threshold and was temporarily blocked by extension/trend damage.
- BE, PYPL, DELL, SMCI, AKAM, COST, and AAPL did not receive complete critical-data enrichment and therefore could not be promoted.

## Blocked and Rejected Names

| Symbol(s) | Primary block | Secondary blocks |
| --- | --- | --- |
| MSFT | no compliant pre-earnings expiration window | tentative Oct. 28 earnings; small-account premium risk |
| QCOM | provisional PM path incomplete | verified Nov. 4 earnings; outside universe |
| CRDO, BE | unconfirmed extension | trend/high-IV/outside-universe constraints |
| PYPL, DELL, AKAM | incomplete critical data | outside Current Universe |
| SMCI, AAPL | outside Current Universe | high IV or incomplete data |
| COST | post-earnings review unsettled | incomplete data |
| MU | earnings blackout | outside Current Universe |
| NVDA, AMZN | options activity alone insufficient | no independent direction |
| META | failed bullish setup not bearish | negative tape; weak volume |
| AVGO | no fresh directional edge | sub-1.5x volume |

All 15 terminal records received new 5/10/20-day opportunity-cost tracking seeds; 30/60-day fields were also retained for schema compatibility.

## Missing or Conflicting Data

- Full financial statements, option historicals, a technical-indicator endpoint, and individual P&L trade history are not exposed by the current connector.
- Daily historical bars had not published September 25 at capture time, so same-session regular-hours 30-minute bars were aggregated for checkpoint closes and clearly preserved as such.
- Momentum and Earnings Risk outputs were frontend-capped.
- The MSFT October 28 date is tentative; QCOM November 4 is verified.
- Scanner Last values and official closing prints differed slightly after hours; official/same-session data controlled calculations.

## Scanner and Option Setup Quality

Scanner quality was adequate for discovery but not for direction. Momentum identified actionable research leaders, Options Activity was noisy at the high-IV top, and Earnings Risk provided useful blocking context. Permanent filters excluded obvious microcap/low-price noise before direct enrichment.

Option setup quality: no setup passed. This is a successful gate outcome, not a missing-contract failure. Pulling chains after the gate failed would have violated the progressive options workflow.

## Mandatory Prospective Option Checkpoint

The due manifest contained META 2026-10-16 600C at its 30D horizon.

- Due: 1
- Captured: 1
- Updated: 1
- Missed: 0
- Entry midpoint: 31.55
- September 25 adjusted mark: 153.28
- Option return: +385.83%
- Underlying return: +27.68%
- SPY excess return: +28.52%
- QQQ excess return: +25.99%
- Classification: `UNDERLYING_WIN_OPTION_WIN`

Older uncaptured option horizons remain permanently unavailable because the source has no historical option-bars endpoint. Those statuses are allowed and did not fail validation.

## State-File Decision

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged.
- `state/rejected_candidates.json`: unchanged.

No daily evidence justified rewriting the official universe or adding a repeated permanent reject.

## Portfolio Manager Recommendation

Decision: **NO TRADE**.

The account remains a $100 cash validation account with Level 2 broker capability, zero equity/options positions, zero open orders, and zero three-month realized P/L. Setup quality and account fit were kept separate, but no setup reached contract qualification. Account size was not used to justify a cheap far-OTM or short-DTE substitute.

## Shadow-Tracking Decision

No new option shadow trade or option signal-outcome record was created because no exact contract qualified. The existing META checkpoint was updated. Fifteen underlying no-trade opportunity-cost records were added for 5/10/20-day tracking.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.

