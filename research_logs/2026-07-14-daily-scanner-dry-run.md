# Daily Research Log

Date: 2026-07-14  
Run time: 19:51 CT  
Account mode: Research-only / Proposal-only  
Order status: No orders placed

## Executive decision

Decision: NO TRADE

Primary reason:

The Current Universe is still not populated by an official broad monthly refresh, so all scanner rows remain research inputs only under v1.6 rules.

Supporting reasons:

- Existing saved Robinhood scanners were run read-only; no scanner was created, edited, or deleted.
- No candidate is approved as Tier 1 or Tier 2 in the Current Universe.
- Scanner rank is not trade rank; full trend, relative-strength, fundamentals, market-regime, account-state, stop, target, and risk-at-stop checks were not completed.
- Options Activity Radar again started with low-price, low-market-cap, high-IV rows that fail or heavily penalize before scoring.
- Earnings Risk Radar surfaced many names inside the next-7-day earnings window, blocking new entries under the 5-trading-day blackout rule.

What would change the decision:

- Complete the official monthly Current Universe refresh.
- Validate trend, relative strength versus `SPY`, fundamentals, earnings timing, market regime, and account state for repeated higher-quality candidates.
- Route only validated Tier 1 / Tier 2 names through the Portfolio Manager Pre-Trade Checklist.

## Market context

Market-regime validation:

- `SPY` trend: Not independently validated in this scanner dry run.
- `QQQ` trend: Not independently validated in this scanner dry run.
- Volatility conditions: N/A.
- Breadth / participation: N/A.
- Leading sectors: Scanner rows showed pockets of strength in semiconductors, AI/data-center infrastructure, energy, financials, metals/miners, and selected industrials / software. Broad sector leadership was not independently validated.

Interpretation:

Scanner output is live market-discovery input only. Momentum Candidates returned many liquid large-cap rows, but most visible rows had relative volume shown as `1`, so participation quality needs deeper validation before any research handoff. Options Activity provided useful confirmation for a few liquid names, but its highest-IV rows were mostly low-quality speculation.

## Scanner summary

Live Robinhood saved scanners were run at report time. Large scans returned more total matches than the visible row set shown by the tool, so the candidate review below is based on visible scanner rows only.

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 396 | `% Change desc` | Primary opportunity feed; top visible rows included `CAH`, `UMC`, `EOG`, `NBIS`, `IOT`, `ASML`, `WULF`, `MLI`, `INTC`, and `MU` |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 47 | `Implied volatility desc` | Research-only signal; visible rows included low-quality high-IV names plus liquid confirmations such as `NBIS`, `WULF`, `TSM`, `IBM`, `PLTR`, `TSLA`, `NVDA`, `MS`, `C`, and `WFC` |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 310 | `Earnings date desc` | Risk-control feed; visible near-term rows included `AMX`, `AVB`, `CCI`, `CME`, `CSX`, `EQNR`, `EQR`, `IBM`, `KEY`, `MLI`, `MMLP`, `NOW`, `GM`, `HAL`, `IBKR`, `MMM`, `NOC`, and many smaller banks / microcaps |

## Top research candidates

Preliminary statuses below are scanner-pipeline statuses only. They are not final Research Agent scores because full trend, relative-strength, fundamentals, earnings, market-regime, and account checks were not completed.

| Rank | Symbol | Sources | Scanner Signals | Preliminary Status | Notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | NBIS | Momentum Candidates, Options Activity Radar | Large-cap momentum, high volume, options confirmation | Research further | Market cap about $53.4B; volume about 18.0M; daily move about 2.5%; repeated AI infrastructure candidate, outside Current Universe |
| 2 | WULF | Momentum Candidates, Options Activity Radar | Momentum plus options attention | Watch only | Market cap about $10.4B, just above preference; volume about 58.0M; crypto/data-center adjacency and volatility require penalty |
| 3 | TSM | Momentum Candidates, Options Activity Radar | Mega-cap semiconductor momentum, options confirmation | Research further | Market cap about $1.98T; volume about 14.4M; repeated high-quality semiconductor row; earnings status needs full validation |
| 4 | MS | Momentum Candidates, Options Activity Radar | Large-cap financial momentum, options attention | Research further | Market cap about $348.7B; volume about 9.3M; financials earnings season risk requires close timing check |
| 5 | NVDA | Momentum Candidates, Options Activity Radar | Mega-cap AI / semiconductor liquidity, options confirmation | Research further | Market cap about $4.93T; volume about 124.8M; repeated highest-priority research name, but outside Current Universe |
| 6 | DINO | Momentum Candidates, Options Activity Radar | Refiner momentum plus options attention | Research further | Market cap about $14.7B; volume about 2.35M; cyclicality and near-threshold liquidity need deeper review |
| 7 | CAH | Momentum Candidates | Large-cap healthcare distribution momentum | Research further | Market cap about $54.7B; volume about 3.1M; top visible momentum row, but no options confirmation and outside Current Universe |
| 8 | UMC | Momentum Candidates | Large-cap semiconductor momentum, high volume | Research further | Market cap about $60.2B; volume about 13.2M; ADR / semiconductor-cycle risks need validation |
| 9 | EOG | Momentum Candidates | Large-cap energy momentum | Research further | Market cap about $74.4B; volume about 2.9M; energy-cycle exposure and sector concentration need review |
| 10 | IOT | Momentum Candidates | Large-cap software momentum | Research further | Market cap about $21.5B; volume about 4.4M; needs trend, relative strength, fundamentals, and earnings check |

## Blocked / rejected names

| Symbol | Source | Reason Code | Earnings Risk Flag | Decision |
| --- | --- | --- | --- | --- |
| LOOP | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| NAUT | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| SPRO | Options Activity Radar | `penny_stock_or_microcap`, `high_volatility` | false | Reject |
| KNDI | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| SCM | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| AVIR | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| AEHR | Options Activity Radar | `market_cap_below_preference`, `extended_one_day_move`, `high_volatility` | false | Reject for now |
| ATAI | Options Activity Radar | `market_cap_below_preference`, `high_volatility`, `options_activity_alone_insufficient` | false | Reject for now |
| SB | Options Activity Radar | `market_cap_below_preference`, `high_volatility`, `options_activity_alone_insufficient` | false | Reject for now |
| SDGR | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `high_volatility` | false | Reject for now |
| MMLP | Earnings Risk Radar | `blocked_by_earnings`, `penny_stock_or_microcap`, `insufficient_liquidity` | true | Reject |
| AMX | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| AVB | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| CCI | Earnings Risk Radar | `blocked_by_earnings` | true | Blocked by earnings |
| CME | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| CSX | Earnings Risk Radar | `blocked_by_earnings` | true | Blocked by earnings |
| EQNR | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings` | true | Blocked by earnings |
| IBM | Earnings Risk Radar, Options Activity Radar | `blocked_by_earnings`, `options_activity_alone_insufficient` | true | Blocked by earnings |
| KEY | Earnings Risk Radar | `blocked_by_earnings` | true | Blocked by earnings |
| MLI | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings` | true | Blocked by earnings |
| NOW | Earnings Risk Radar | `blocked_by_earnings` | true | Blocked by earnings |
| GM | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings` | true | Blocked by earnings |
| HAL | Earnings Risk Radar | `blocked_by_earnings` | true | Blocked by earnings |
| IBKR | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings` | true | Blocked by earnings |
| MMM | Earnings Risk Radar | `blocked_by_earnings` | true | Blocked by earnings |
| NOC | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |

## Reason codes

- `outside_current_universe`
- `blocked_by_earnings`
- `failed_tradability`
- `penny_stock_or_microcap`
- `insufficient_liquidity`
- `unsupported_asset`
- `leveraged_or_inverse_etf`
- `missing_critical_data`
- `weak_relative_strength`
- `weak_trend`
- `low_volume_quality`
- `market_cap_below_preference`
- `extended_one_day_move`
- `high_volatility`
- `crypto_adjacency`
- `options_activity_alone_insufficient`
- `requires_further_research`

## Scanner quality notes

- Useful signals: Momentum Candidates produced the cleanest research feed, led by liquid large-cap rows such as `CAH`, `UMC`, `EOG`, `NBIS`, `IOT`, `ASML`, `INTC`, `MU`, `CRDO`, `TSM`, and `NVDA`.
- Useful confirmations: `NBIS`, `WULF`, `TSM`, `MS`, `DINO`, `NVDA`, and `C` appeared in both Momentum Candidates and Options Activity Radar, but options activity remains only a secondary research-confidence input.
- Noisy rows: Options Activity Radar was led by low-price / low-market-cap / high-IV rows including `LOOP`, `NAUT`, `SPRO`, `KNDI`, `SCM`, `AVIR`, `AEHR`, `ATAI`, `SB`, and `SDGR`.
- Repeated rejects: `AVIR` repeated from the 2026-07-09 Options Activity reject list with the same low-quality profile. `MMLP` reappeared in Earnings Risk Radar and was already in rejected-candidate state.
- Obvious false positives: Options Activity alone highlighted several names with no qualifying long-equity quality confirmation.
- Earnings-risk blocks: `AMX`, `AVB`, `CCI`, `CME`, `CSX`, `EQNR`, `IBM`, `KEY`, `MLI`, `MMLP`, `NOW`, `GM`, `HAL`, `IBKR`, `MMM`, and `NOC` are blocked for new entries while inside the near-term earnings window.

## Common-sense check

- Did the pipeline recommend low-quality scanner noise? No. The highest-IV low-quality Options Activity rows were rejected before ranking.
- Did the pipeline over-filter everything? No. Liquid research candidates remain from Momentum Candidates and a few momentum-plus-options overlaps.
- Did it miss obvious repeated leaders? Not from visible rows. `NVDA`, `TSM`, `NBIS`, `WULF`, `CRDO`, and `SNDK` were visible in current or recent scanner workflows.
- Are any candidates extended after a one-day move? Yes. `AEHR` was the clearest visible extreme one-day move; `NBIS`, `WULF`, `CAH`, `UMC`, and `EOG` still need follow-through and trend checks.
- Are any candidates repeatedly appearing across scanner runs? Yes. Higher-quality repeated research names include `NVDA`, `TSM`, `NBIS`, `CRDO`, `SNDK`, and `WULF`. Repeated low-quality rejects include `AVIR` and `MMLP`.

Conclusion:

The scanner pipeline is functioning as a discovery workflow, not a trade system. Momentum Candidates remains the most useful scanner. Options Activity Radar supplied a few liquid confirmations but was noisy at the top. Earnings Risk Radar correctly blocked near-term reporting names. The correct portfolio decision remains `NO TRADE`.

## State file decision

- `state/current_universe.json`: Not updated. Daily scanner dry runs cannot populate the Current Universe.
- `state/open_theses.json`: Not updated. No thesis advanced to portfolio review.
- `state/rejected_candidates.json`: Updated only for `AVIR` and `MMLP`, obvious repeated rejects supported by current scanner rows and prior logs.

## Portfolio Manager action recommendation

Decision: NO TRADE

Primary reason:

No candidate is approved for entry because the Current Universe is not officially populated.

Supporting reasons:

- No candidate completed final Research Agent scoring.
- No candidate completed the Portfolio Manager Pre-Trade Checklist.
- Account equity, buying power, current positions, open orders, sector exposure, stop loss, target, and risk-at-stop were not validated.
- Proposal-only mode prohibits live execution.

Next action:

1. Keep all scanner names as research candidates only.
2. Prioritize full Research Agent review for repeated higher-quality names: `NVDA`, `TSM`, `NBIS`, `CRDO`, `SNDK`, `WULF`, `MS`, and `DINO`.
3. Use repeated high-quality scanner names as inputs to the first official Current Universe refresh.

No buy or sell orders were placed or proposed.
