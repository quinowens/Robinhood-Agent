# Daily Research Log

Date: 2026-07-17  
Run time: 10:31 CT  
Account mode: Research-only / Proposal-only  
Order status: No orders placed

## Executive decision

Decision: NO TRADE

Primary reason:

The Current Universe remains unpopulated by an official broad monthly refresh, so every scanner row is research input only under v1.6 rules.

Supporting reasons:

- Existing saved Robinhood scanners were run read-only; no scanner was created, edited, or deleted.
- No candidate is approved as Tier 1 or Tier 2 in the Current Universe.
- Scanner rank is not trade rank; full trend, relative-strength, fundamentals, market-regime, account-state, stop, target, and risk-at-stop checks were not completed.
- Options Activity Radar was again dominated by low-price, low-market-cap, low-liquidity, high-IV rows that fail Mandatory Rejection Filters or require heavy penalties before scoring.
- Earnings Risk Radar produced a large near-term earnings block, so visible earnings names are not eligible for new entries.

What would change the decision:

- Complete the official monthly Current Universe refresh.
- Validate trend, relative strength versus `SPY`, fundamentals, earnings timing, market regime, and account state for repeated higher-quality candidates.
- Route only validated Tier 1 / Tier 2 names through the Portfolio Manager Pre-Trade Checklist.

## Market context

Market-regime validation:

- `SPY` trend: N/A; not independently validated in this scanner dry run.
- `QQQ` trend: N/A; not independently validated in this scanner dry run.
- Volatility conditions: N/A.
- Breadth / participation: N/A.
- Leading sectors: Live scanner rows showed visible relative strength in space / satellite, healthcare, pharmaceuticals, cybersecurity, energy, telecom, staples, and selected defensive large caps. Broad sector leadership was not independently validated.

Interpretation:

Scanner output is live market-discovery input only. Momentum Candidates produced a broad liquid large-cap feed, but many top positive rows had relative volume below 1.0, limiting participation confidence. The downside portion of Momentum Candidates also included several major technology / semiconductor names, so the scanner feed does not support an aggressive growth entry posture without a full market-regime and relative-strength pass.

## Scanner summary

Live Robinhood saved scanners were run at report time. Large scans returned more total matches than can be fully reviewed in this dry-run report, so candidate review is based on visible scanner rows returned by the tool.

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 202 | `% Change desc` | Primary opportunity feed; top visible positive rows included `ASTS`, `VG`, `SKHY`, `NBIS`, `TAK`, `MRK`, `CMG`, `BE`, `PANW`, `GE`, `BMY`, `SHEL`, `MO`, `PBR`, `CSCO`, `ABT`, `UNH`, `ORCL`, `RKLB`, `AAPL`, and downside rows such as `NVDA`, `TSLA`, `NFLX`, `MSFT`, `META`, `AMD`, `TSM`, `INTC`, `CRDO`, and `CBRS` |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 33 | `Implied volatility desc` | Research-only signal; noisy top rows included `PRPL`, `CRWS`, `CMCM`, `SOHU`, `NPKI`, `DEFT`, `JAN`, `PLG`, `VGZ`, `BV`, `INOD`, `MMED`, and `USAS`; cleaner liquid confirmations included `CCJ`, `TSLA`, `NFLX`, `NVDA`, and `KHC` |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 338 | `Earnings date desc` | Risk-control feed; visible near-term rows included `AXP`, `BX`, `CHTR`, `CNI`, `COKE`, `ENSG`, `EW`, `FIX`, `HCA`, `HIG`, `IBRX`, `DECK`, `DGX`, `DLR`, `DOW`, `FCX`, `GEV`, `GOOG`, `GOOGL`, `HBAN`, `HON`, `INTC`, `LMT`, `NEM`, and many smaller banks / microcaps |

## Top research candidates

Preliminary statuses below are scanner-pipeline statuses only. They are not final Research Agent scores because full trend, relative-strength, fundamentals, earnings, market-regime, and account checks were not completed.

| Rank | Symbol | Sources | Scanner Signals | Preliminary Status | Notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | ASTS | Momentum Candidates | Large-cap momentum, liquid volume, space / satellite theme | Research further | Market cap about $16.4B; volume about 13.5M; daily move about 6.2%; relative volume only about 0.25 and outside Current Universe |
| 2 | PANW | Momentum Candidates | Mega-cap cybersecurity momentum | Research further | Market cap about $288.5B; volume about 3.3M; daily move about 2.7%; needs trend, RS, fundamentals, and earnings validation |
| 3 | MRK | Momentum Candidates | Mega-cap pharma momentum, liquid volume | Research further | Market cap about $315.2B; volume about 5.3M; defensive healthcare strength but relative volume below 1.0 |
| 4 | CMG | Momentum Candidates | Large-cap consumer momentum, liquid row | Research further | Market cap about $43.9B; volume about 7.4M; needs trend, RS, and earnings timing check |
| 5 | BE | Momentum Candidates | Large-cap clean energy momentum, liquid volume | Research further | Market cap about $58.8B; volume about 6.3M; high-beta profile and prior volatility require risk-quality review |
| 6 | NBIS | Momentum Candidates | AI infrastructure momentum, repeated scanner relevance | Research further | Market cap about $43.6B; volume about 11.4M; repeated higher-quality research lead but outside Current Universe |
| 7 | ABT | Momentum Candidates | Large-cap healthcare momentum, repeated scanner relevance | Research further | Market cap about $172.1B; volume about 7.9M; prior momentum-plus-options confirmation, but today no visible options confirmation in the run |
| 8 | ORCL | Momentum Candidates | Mega-cap software / infrastructure liquidity | Watch only | Market cap about $357.8B; volume about 16.4M; relative volume below 0.3 and outside Current Universe |
| 9 | AAPL | Momentum Candidates | Mega-cap liquidity and repeated scanner relevance | Watch only | Market cap about $4.89T; volume about 23.5M; positive but modest scanner move, outside Current Universe |
| 10 | NVDA | Options Activity Radar | Mega-cap AI options attention, high liquidity | Watch only | Market cap about $5.02T; volume about 72.3M; options activity alone is insufficient and daily momentum was negative |

Watch-only / lower-confidence names:

| Symbol | Sources | Reason |
| --- | --- | --- |
| VG | Momentum Candidates | Large-cap LNG profile, but relative volume below 1.0 and needs business-history / earnings review |
| SKHY | Momentum Candidates | ADR profile and relative volume below 1.0; still a semiconductor memory research input |
| RKLB | Momentum Candidates | Liquid space / defense-adjacent row, but high-beta volatility and outside Current Universe |
| TSLA | Options Activity Radar, Momentum Candidates | Liquid mega-cap, but negative daily momentum and options activity alone is not a trade signal |
| NFLX | Options Activity Radar, Momentum Candidates | Liquid large cap, but sharp negative daily move and prior research rejection / earnings risk history require caution |
| KHC | Momentum Candidates, Options Activity Radar | Defensive large cap with options confirmation, but low relative volume and weaker momentum quality |

## Blocked / rejected names

| Symbol | Source | Reason Code | Earnings Risk Flag | Decision |
| --- | --- | --- | --- | --- |
| PRPL | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| CRWS | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| CMCM | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| SOHU | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| NPKI | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `high_volatility` | false | Reject for now |
| DEFT | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| JAN | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `options_activity_alone_insufficient` | false | Reject for now |
| PLG | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| VGZ | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| BV | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `options_activity_alone_insufficient` | false | Reject for now |
| INOD | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `high_volatility` | false | Reject for now |
| MMED | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `high_volatility` | false | Reject for now |
| USAS | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `high_volatility` | false | Reject for now |
| AXP | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality`, `outside_current_universe` | true | Blocked by earnings |
| BX | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality`, `outside_current_universe` | true | Blocked by earnings |
| CHTR | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality`, `outside_current_universe` | true | Blocked by earnings |
| EW | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality`, `outside_current_universe` | true | Blocked by earnings |
| FCX | Earnings Risk Radar | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| GOOG | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| GOOGL | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| HBAN | Earnings Risk Radar | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| INTC | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| FRMM | Earnings Risk Radar | `blocked_by_earnings`, `penny_stock_or_microcap`, `insufficient_liquidity` | true | Reject |

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

- Useful signals: Momentum Candidates produced the cleanest research feed, with liquid large-cap rows including `ASTS`, `NBIS`, `MRK`, `CMG`, `BE`, `PANW`, `GE`, `BMY`, `SHEL`, `CSCO`, `ABT`, `UNH`, `ORCL`, `RKLB`, and `AAPL`.
- Useful confirmations: `KHC`, `TSLA`, `NFLX`, and `NVDA` appeared in Options Activity Radar and were also visible in Momentum Candidates, but several had negative daily momentum. Options activity remains a secondary research-confidence input only.
- Noisy rows: Options Activity Radar was led by low-price / low-market-cap / low-liquidity / high-IV rows such as `PRPL`, `CRWS`, `CMCM`, `SOHU`, `NPKI`, `DEFT`, `PLG`, `VGZ`, `BV`, `INOD`, `MMED`, and `USAS`.
- Repeated rejects: `FRMM` reappeared again in Earnings Risk Radar with about $76.8M market cap, $5.66 last price, about 37K visible volume, and near-term earnings. This supports keeping and refreshing its persistent rejected-candidate state.
- Obvious false positives: The highest-IV options rows mostly failed the long-equity quality process before scoring. Several had tiny market caps, sub-$5 prices, weak volume, or all three.
- Earnings-risk blocks: `AXP`, `BX`, `CHTR`, `EW`, `FCX`, `GOOG`, `GOOGL`, `HBAN`, `INTC`, `NEM`, and `FRMM` are blocked for new entries while inside the near-term earnings window.

## Common-sense check

- Did the pipeline recommend low-quality scanner noise? No. The highest-IV low-quality Options Activity rows were rejected before ranking.
- Did the pipeline over-filter everything? No. Liquid research candidates remain from Momentum Candidates, but none is trade-eligible without the official Current Universe.
- Did it miss obvious repeated leaders? Not from visible rows. `NVDA`, `AAPL`, `NBIS`, `TSLA`, `AMD`, `TSM`, and `CRDO` remained visible, though several were weak today.
- Are any candidates extended after a one-day move? No visible top research candidate had an extreme one-day move above 15%, but `ASTS`, `NBIS`, `BE`, and `RKLB` still require volatility and follow-through review.
- Are any candidates repeatedly appearing across scanner runs? Yes. Higher-quality repeated research names include `NVDA`, `AAPL`, `NBIS`, `ASTS`, `TSLA`, `AMD`, `TSM`, and `CRDO`. The clearest repeated reject with current evidence is `FRMM`.

Conclusion:

The scanner pipeline is functioning as a discovery workflow, not a trade system. Momentum Candidates remains the most useful scanner. Options Activity Radar supplied a few liquid confirmations but was noisy at the top. Earnings Risk Radar correctly blocked near-term reporting names. The correct portfolio decision remains `NO TRADE`.

## State file decision

- `state/current_universe.json`: Not updated. Daily scanner dry runs cannot populate the Current Universe.
- `state/open_theses.json`: Not updated. No thesis advanced to portfolio review.
- `state/rejected_candidates.json`: Updated only for `FRMM`, an obvious repeated reject supported by current scanner rows and prior logs / state.

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
2. Prioritize full Research Agent review for repeated higher-quality names: `ASTS`, `NBIS`, `PANW`, `AAPL`, `NVDA`, `TSLA`, `AMD`, `TSM`, and `CRDO`.
3. Use repeated high-quality scanner names as inputs to the first official Current Universe refresh.

No buy or sell orders were placed or proposed.
