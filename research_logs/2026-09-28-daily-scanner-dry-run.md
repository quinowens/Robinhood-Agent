# Daily Scanner Dry Run — 2026-09-28

Date: 2026-09-28  
Run time: 15:31-15:45 CT  
Account mode: Research-only / Proposal-only / Shadow-trading  
Order status: No orders placed, modified, canceled, reviewed, or submitted  
Run ID: `2026-09-28-daily-scanner-dry-run`  
Run status: `DEGRADED_COMPLETE`  
Strategy version: 2.0.1  
Strategy mode: `options_primary`

## Executive Decision

Decision: **NO TRADE / NO NEW OPTIONS PROPOSAL**.

CRWD produced the strongest underlying evidence and its 2026-11-20 250C remained the best contract expression, but that exact contract and thesis are already tracked from the canonical 2026-09-15 signal group. A second shadow record would duplicate active evidence. PANW and OKTA reached fresh contract review but remained `WATCH`: PANW failed execution quality with an 18.21% midpoint spread and open interest of 9; OKTA had a 7.86% spread, 59.18% IV, and did not complete the provisional Tier 2 path. Account affordability was secondary because neither new setup passed setup quality.

What would change the decision:

- PANW or OKTA supplies materially tighter same-date spreads with adequate open interest and volume.
- CRWD forms a genuinely new, independently invalidatable thesis after the current signal group matures or closes.
- A candidate completes the full provisional Tier 2 path without earnings, trend, volume, or contract-quality blocks.

## Run Health and Tool Coverage

| Metric | Result |
| --- | --- |
| Account/tool preflight | Complete |
| Saved scanners resolved | 3 of 3 matched by name and ID |
| Scanner executions | 3 of 3 succeeded |
| Raw rows persisted | 515 |
| Deduplicated visible symbols | 502 |
| Named terminal records | 15 (2.99% visible coverage) |
| Option checkpoint | Due 0; captured 0; updated 0; missed 0 — successful no-op |
| New option setup records | 2 `WATCH` records |
| New option shadow trades | 0 |
| Validation | Passed with warnings; 0 errors/orphans |
| Live order actions | 0 |

Publish status is degraded because Momentum exposed 200 of 395 matches, Earnings Risk exposed 200 of 210 matches, full financial statements and option historicals are unavailable, and the progressive named finalist set—not the entire visible population—received direct enrichment.

## Account and Portfolio Preflight

- Agentic account: `••••8691`; cash account; broker options level 2.
- Account value / cash / buying power / option buying power: $100 / $100 / $100 / $100.
- Equity positions: 0. Option positions: 0.
- Open equity orders: 0. Open option orders: 0.
- Three-month realized P/L: $0; closing trades: 0.
- Current open premium risk: $0. Drawdown breaker and kill switch: not active from available account evidence.
- Strategy permission remains limited to single-leg long calls and long puts. Broker permission does not expand strategy scope.

## Market and Index Context

- SPX: 7,683.69; NDX: 30,276.81; VIX: 16.07.
- SPY latest retained close: 771.35; 20-day 765.35; 50-day 761.57; 200-day 718.45; positive 50-day slope.
- QQQ latest retained close: 744.50; 20-day 720.87; 50-day 712.65; 200-day 665.59; positive 50-day slope.
- Market Health Score: approximately 70, `Constructive`. Breadth was unavailable, so the regime did not qualify as fully confirmed `Strong`.
- Interpretation: selective bullish research is permitted, but the regime does not override volume, event, execution-quality, or account-risk rules.

## Scanner Summary

| Scanner | Scan ID | Total matches | Visible rows | Sort | Quality read |
| --- | --- | ---: | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 395 | 200 | % Change desc | Useful leaders; capped output |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 115 | 115 | Implied volatility desc | Top tail dominated by microcaps/high IV |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 210 | 200 | Earnings date desc | Effective event-risk filter; capped output |

Cross-scanner attention included CCL, CMG, LI, NVDA, MU, NKE, and several earnings-risk names. Scanner overlap increased confidence only; it did not add underlying-score points or establish direction.

## Underlying Candidate Table

| Rank | Symbol | Sources | Score / completeness / confidence | Direction | Tier / eligibility | Final class | Primary block |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | CRWD | Momentum | 83 / 90% / 82% | Bullish | Tier 2 / eligible | OPTIONS_RESEARCH monitor | Existing active signal group |
| 2 | OKTA | Momentum | 82 / 87% / 79% | Bullish | Watchlist / not promoted | WATCH | Option execution quality |
| 3 | P | Momentum | 81 / 86% / 76% | Bullish watch | Watchlist | WATCH | Low volume quality |
| 4 | PANW | Momentum | 80 / 89% / 79% | Bullish | Tier 2 / eligible | WATCH | Option execution quality |
| 5 | RBRK | Momentum | 80 / 86% / 76% | Bullish watch | Watchlist | WATCH | Low volume quality |
| 6 | TWLO | Momentum | 80 / 88% / 78% | Bullish | Watchlist / earnings block | STOCK_THESIS_ONLY | Earnings / no compliant pre-event window |
| 7 | ZS | Momentum | 78 / 85% / 74% | Bullish watch | Watchlist | WATCH | Low volume quality |
| 8 | NVDA | Momentum + Options Activity | 78 / 90% / 78% | Neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | No fresh directional edge |
| 9 | META | Options Activity | 77 / 89% / 80% | Neutral | Tier 2 / eligible | NO_DIRECTIONAL_EDGE | Failed bullish setup is not bearish |
| 10 | ROIV | Momentum | 75 / 85% / 72% | Neutral | Watchlist | WATCH | Mixed / weak trend |
| 11 | SHOP | Momentum | 74 / 86% / 73% | Neutral | Watchlist | NO_DIRECTIONAL_EDGE | Weak 30-day relative strength |
| 12 | CMG | Momentum + Options Activity | 65 / 86% / 80% | Neutral | Watchlist | WATCH | Weak long-term trend |
| 13 | BURL | Momentum | 64 / 86% / 82% | Neutral | Watchlist | WATCH | Weak long-term trend |
| 14 | LI | Momentum + Options Activity | 60 / 85% / 83% | Neutral | Reject | REJECT | Weak long-term trend |
| 15 | NKE | Momentum + Earnings Risk | 58 / 90% / 91% | Neutral | Earnings-blocked | TEMP_BLOCK | Verified October 1 earnings |

Scores are run-scoped Underlying Thesis Scores. Data completeness and decision confidence remain separate. Full financial statements were unavailable and explicitly reduced completeness.

## Options Setup Table

| Rank | Underlying | Contract | DTE | Bid / Ask / Mid | Delta | Spread | OI / Vol | Setup score | Account fit | Decision | Primary block |
| ---: | --- | --- | ---: | --- | ---: | ---: | --- | ---: | --- | --- | --- |
| 1 | CRWD | 2026-11-20 250C | 53 | 27.45 / 28.00 / 27.725 | 0.619 | 1.98% | 1,906 / 84 | 82 monitoring estimate | FAIL | Existing shadow monitor; no duplicate | Existing active signal group |
| 2 | OKTA | 2026-11-20 200C | 53 | 18.95 / 20.50 / 19.725 | 0.574 | 7.86% | 543 / 115 | 74 | FAIL | WATCH | Option execution quality |
| 3 | PANW | 2026-11-06 390C | 39 | 26.45 / 31.75 / 29.10 | 0.556 | 18.21% | 9 / 16 | 62 | FAIL | WATCH | Option execution quality |

CRWD was not written as a new setup or shadow trade because the exact 250C contract is already the canonical frozen setup from September 15. OKTA and PANW were written as `WATCH` option setup records. No order review was requested or needed.

## Provisional Tier 2 Review

No provisional Tier 2 promotion was written.

- OKTA cleared the numerical underlying threshold, but the 200C did not pass execution-quality review and the Portfolio Manager could not produce a live-quality proposal.
- P and RBRK had strong trend evidence but lacked volume confirmation.
- TWLO had a bullish stock thesis, but its first 30+ DTE expiration crosses tentative October 29 earnings.
- The official Current Universe remains stale and should be rebuilt through the governed monthly refresh rather than patched by this daily run.

## Blocked and Rejected Names

| Symbol(s) | Primary block | Secondary blocks |
| --- | --- | --- |
| CRWD | Existing active signal group | Account-fit premium risk |
| PANW, OKTA | Option execution quality | Wide spread; account-fit premium risk; OKTA outside universe |
| TWLO, NKE | Earnings/event window | Outside universe; trend/volume issues |
| P, RBRK, ZS | Low volume quality | Outside Current Universe |
| BURL, CMG, LI, ROIV | Weak or mixed trend | Outside Current Universe; event/context limits |
| NVDA, META | No fresh directional edge | Options activity alone insufficient |
| SHOP | Weak relative strength | Outside Current Universe |

All 15 terminal underlying records received 5/10/20-day opportunity-cost tracking seeds. Only the primary blocking rule receives attribution credit or blame.

## Missing or Conflicting Data

- Full reported financial statements, option historical bars, and individual P/L trade history are unavailable from the active tool surface.
- Most daily histories had not yet published a September 28 daily bar; the 15:59 CT regular-hours quote was used as the signal price and labeled accordingly.
- Momentum and Earnings Risk results were capped.
- Several future earnings dates are tentative, including PANW, OKTA, CRWD, TWLO, and META. NKE and CMG dates were verified.
- Scanner prices and official prior-session closes differ by design; final regular-hours quotes controlled the signal snapshot.

## Scanner Quality

Momentum remained useful for large-cap movement discovery. Options Activity Radar remained noisy at its high-IV top and was used only as context. Earnings Risk Radar correctly surfaced near-term event exposure. Permanent filters prevented microcap/high-IV noise from receiving expensive enrichment.

## Option Setup Quality

No new contract passed. PANW failed on spread and open interest; OKTA failed on spread/IV and provisional eligibility; CRWD remained an already-active canonical shadow signal. Account size was never used to justify a cheaper far-OTM or short-DTE substitute.

## Mandatory Prospective Option Checkpoint

The command `python3 scripts/update_option_outcomes.py --list-due-option-checkpoints --as-of 2026-09-28` returned zero due option IDs.

- Due: 0
- Captured: 0
- Updated: 0
- Missed: 0
- Status: successful no-op

No unrelated option quotes were pulled for checkpointing and no later quote was assigned to an earlier target date.

## Outcome Analytics and Validation

- Analytics and strategy diagnostics were regenerated after the checkpoint no-op.
- Repository validation passed.
- Integrity: `PASS_WITH_WARNINGS`; 13 complete qualified chains; 0 errors; 0 orphaned shadow records; 0 orphaned option outcomes; 0 update failures.
- 28 older outcome windows remain permanently unavailable, primarily because `OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE`; this is an allowed permanent status.
- Four unaccounted scheduled runs remain an existing ledger warning and require separate reconciliation.
- No strategy threshold or rule change was applied.

## State-File Decision

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged.
- `state/rejected_candidates.json`: unchanged.

No daily evidence justified rewriting the official universe, opening a live thesis, or adding a repeated permanent reject.

## Portfolio Manager Recommendation

Decision: **NO TRADE**.

The $100 account has no positions or open orders and remains a validation account. PANW and OKTA failed setup quality before account fit; CRWD remains an existing shadow-only qualified setup with no duplicate record. Current premium risk is $0 and no post-proposal risk was added.

## Shadow-Tracking Decision

No new option shadow trade or option signal-outcome record was created. The existing canonical CRWD 2026-11-20 250C shadow setup remains the relevant evidence chain. Two new `WATCH` option records were created for PANW and OKTA; 15 underlying signal-outcome records were added.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
