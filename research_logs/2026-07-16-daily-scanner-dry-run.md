# Daily Research Log

Date: 2026-07-16  
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
- Options Activity Radar was again dominated by low-price, low-market-cap, low-liquidity, high-IV rows that fail or heavily penalize before scoring.
- Earnings Risk Radar produced a large near-term earnings block, so visible earnings names are not eligible for new entries.

What would change the decision:

- Complete the official monthly Current Universe refresh.
- Validate trend, relative strength versus `SPY`, fundamentals, earnings timing, market regime, and account state for repeated higher-quality candidates.
- Route only validated Tier 1 / Tier 2 names through the Portfolio Manager Pre-Trade Checklist.

## Market context

Market-regime validation:

- `SPY` trend: N/A; not independently validated in this scanner dry run.
- `QQQ` trend: N/A; not independently validated in this scanner dry run.
- Volatility conditions: N/A; index endpoint returned symbols but no usable current values.
- Breadth / participation: N/A.
- Leading sectors: Scanner rows showed visible strength in healthcare, medical devices, defensives / staples, banks, telecom, and selected ADRs. Broad sector leadership was not independently validated.

Interpretation:

Scanner output is live market-discovery input only. Momentum Candidates surfaced many liquid large-cap rows, but most visible rows had relative volume below 1.0, limiting participation confidence. Options Activity supplied a few liquid confirmations, especially `ABT`, `UNH`, and `CFG`, but the top of that scanner remained noisy and unsuitable as a standalone long-equity signal.

## Scanner summary

Live Robinhood saved scanners were run at report time. Large scans returned more total matches than can be fully reviewed in this dry-run report, so candidate review is based on visible scanner rows returned by the tool.

| Scanner | Scan ID | Matches | Sort | Read |
| --- | --- | ---: | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | 166 | `% Change desc` | Primary opportunity feed; top visible rows included `ABT`, `DXCM`, `IR`, `TME`, `GIS`, `BAX`, `MDT`, `CFG`, `BTI`, `BSX`, `ORLY`, `UNH`, `XPEV`, `VOD`, `INFY`, `NKE`, `MRK`, `ZTS`, `FAST`, `CSX`, `PYPL`, `AAPL`, and later downside rows in semiconductors / AI infrastructure such as `NVDA`, `AMD`, `AVGO`, `NBIS`, `RKLB`, `ASTS`, and `CRDO` |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | 31 | `Implied volatility desc` | Research-only signal; noisy top rows included `QRHC`, `NHTC`, `NMRA`, `ARMP`, `INV`, `EVTL`, `VMD`, `GNE`, `ATAI`, and `CTMX`; cleaner liquid confirmations included `ABT`, `UNH`, `CFG`, and `TSLA` |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | 321 | `Earnings date desc` | Risk-control feed; visible near-term rows included `AAL`, `ABCB`, `ACI`, `ALLE`, `CMCSA`, `CSX`, `FCX`, `FISV`, `GOOG`, `GOOGL`, `HBAN`, `UNP`, `AMX`, `AVB`, `CCI`, `CME`, `EQNR`, `EQR`, `FRMM`, and many smaller banks / microcaps |

## Top research candidates

Preliminary statuses below are scanner-pipeline statuses only. They are not final Research Agent scores because full trend, relative-strength, fundamentals, earnings, market-regime, and account checks were not completed.

| Rank | Symbol | Sources | Scanner Signals | Preliminary Status | Notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | ABT | Momentum Candidates, Options Activity Radar | Large-cap momentum, options confirmation, liquid volume | Research further | Market cap about $155.5B; volume about 14.2M; daily move about 11.1%; strong visible signal but extended one-day move needs follow-through validation |
| 2 | UNH | Momentum Candidates, Options Activity Radar | Mega-cap healthcare momentum plus options attention | Research further | Market cap about $380.1B; volume about 7.5M; relative volume about 1.1; needs trend, RS, and earnings timing verification |
| 3 | IR | Momentum Candidates | Large-cap industrial momentum with relative volume above 1.0 | Research further | Market cap about $31.0B; volume about 2.8M; daily move about 7.0%; no visible options confirmation |
| 4 | DXCM | Momentum Candidates | Large-cap medical device momentum | Research further | Market cap about $28.1B; volume about 2.6M; relative volume below 1.0 limits participation confidence |
| 5 | MDT | Momentum Candidates | Large-cap healthcare momentum | Research further | Market cap about $103.0B; volume about 3.9M; needs trend and relative-strength validation |
| 6 | BSX | Momentum Candidates | Large-cap medical device momentum, liquid volume | Research further | Market cap about $64.0B; volume about 6.9M; no visible options confirmation |
| 7 | ORLY | Momentum Candidates | Large-cap consumer defensive / auto retail momentum | Research further | Market cap about $68.6B; volume about 4.9M; relative volume low, so participation quality is incomplete |
| 8 | PYPL | Momentum Candidates | Repeated fintech research lead | Watch only | Market cap about $49.0B; volume about 14.1M; relative volume very low today and no visible options confirmation in this run |
| 9 | AAPL | Momentum Candidates | Mega-cap liquidity and repeated scanner relevance | Watch only | Market cap about $4.81T; volume about 18.2M; outside Current Universe and no full Research Agent validation |
| 10 | GIS | Momentum Candidates | Defensive / staples momentum | Watch only | Market cap about $19.9B; volume about 4.5M; relative volume below 0.4 and no visible options confirmation |

Watch-only / lower-confidence names:

| Symbol | Sources | Reason |
| --- | --- | --- |
| TME | Momentum Candidates | ADR profile, price below $10, relative volume below 0.4 |
| BTI | Momentum Candidates | ADR / tobacco defensive; needs quality, trend, and event review |
| XPEV | Momentum Candidates | ADR / EV risk and relative volume below 0.4 |
| TSLA | Options Activity Radar | Liquid mega-cap, but options activity alone is insufficient and daily momentum was negative |
| CHKP | Options Activity Radar | Market cap passes threshold, but volume was far below preferred liquidity floor |
| CACI | Options Activity Radar | Market cap barely passes threshold, but volume was far below preferred liquidity floor |

## Blocked / rejected names

| Symbol | Source | Reason Code | Earnings Risk Flag | Decision |
| --- | --- | --- | --- | --- |
| QRHC | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| NHTC | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| NMRA | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| ARMP | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| INV | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| EVTL | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| VMD | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| GNE | Options Activity Radar | `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility` | false | Reject |
| ATAI | Options Activity Radar | `market_cap_below_preference`, `extended_one_day_move`, `high_volatility`, `options_activity_alone_insufficient` | false | Reject for now |
| CTMX | Options Activity Radar | `market_cap_below_preference`, `insufficient_liquidity`, `high_volatility` | false | Reject for now |
| MAN | Options Activity Radar | `market_cap_below_preference`, `extended_one_day_move`, `options_activity_alone_insufficient` | false | Reject for now |
| DSGR | Options Activity Radar | `market_cap_below_preference`, `extended_one_day_move`, `options_activity_alone_insufficient` | false | Reject for now |
| AAL | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| CMCSA | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| CSX | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| FCX | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| FISV | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| GOOG | Earnings Risk Radar | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| GOOGL | Earnings Risk Radar | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| HBAN | Earnings Risk Radar, Momentum Candidates | `blocked_by_earnings`, `outside_current_universe` | true | Blocked by earnings |
| AMX | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| AVB | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| CCI | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| CME | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
| EQNR | Earnings Risk Radar | `blocked_by_earnings`, `low_volume_quality` | true | Blocked by earnings |
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
- `options_activity_alone_insufficient`
- `requires_further_research`

## Scanner quality notes

- Useful signals: Momentum Candidates produced the cleanest research feed, led by liquid large-cap rows such as `ABT`, `DXCM`, `IR`, `MDT`, `CFG`, `BSX`, `ORLY`, `UNH`, `PYPL`, and `AAPL`.
- Useful confirmations: `ABT`, `UNH`, and `CFG` appeared in both Momentum Candidates and Options Activity Radar. Options activity remains a secondary research-confidence input only.
- Noisy rows: Options Activity Radar was led by low-price / low-market-cap / high-IV rows including `QRHC`, `NHTC`, `NMRA`, `ARMP`, `INV`, `EVTL`, `VMD`, `GNE`, `ATAI`, and `CTMX`.
- Repeated rejects: `ATAI` reappeared after a 2026-07-14 options-only reject-for-now note; today it again showed below-threshold market cap, high IV, and an extreme one-day move. `FRMM` reappeared in Earnings Risk Radar and was already documented in rejected-candidate state as a repeated low-quality options reject.
- Obvious false positives: Several options-only rows had high relative options volume but failed the core long-equity quality process before scoring.
- Earnings-risk blocks: `AAL`, `CMCSA`, `CSX`, `FCX`, `FISV`, `GOOG`, `GOOGL`, `HBAN`, `AMX`, `AVB`, `CCI`, `CME`, `EQNR`, and `FRMM` are blocked for new entries while inside the near-term earnings window.

## Common-sense check

- Did the pipeline recommend low-quality scanner noise? No. The highest-IV low-quality Options Activity rows were rejected before ranking.
- Did the pipeline over-filter everything? No. Liquid research candidates remain from Momentum Candidates and a few momentum-plus-options overlaps.
- Did it miss obvious repeated leaders? Not from visible rows. Repeated high-quality names such as `AAPL`, `PYPL`, and major semiconductors / AI infrastructure names remained visible, though several were weak today.
- Are any candidates extended after a one-day move? Yes. `ABT`, `ATAI`, `MAN`, and `DSGR` require extension / follow-through checks before any serious research handoff.
- Are any candidates repeatedly appearing across scanner runs? Yes. Higher-quality repeated research names include `AAPL`, `PYPL`, `TSLA`, `NVDA`, `AMD`, `NBIS`, `ASTS`, and `CRDO`. Repeated low-quality or blocked names include `ATAI` and `FRMM`.

Conclusion:

The scanner pipeline is functioning as a discovery workflow, not a trade system. Momentum Candidates remains the most useful scanner. Options Activity Radar supplied a few liquid confirmations but was again noisy at the top. Earnings Risk Radar correctly blocked near-term reporting names. The correct portfolio decision remains `NO TRADE`.

## State file decision

- `state/current_universe.json`: Not updated. Daily scanner dry runs cannot populate the Current Universe.
- `state/open_theses.json`: Not updated. No thesis advanced to portfolio review.
- `state/rejected_candidates.json`: Updated only for `ATAI` and `FRMM`, obvious repeated rejects supported by current scanner rows and prior logs / state.

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
2. Prioritize full Research Agent review for repeated higher-quality names: `ABT`, `UNH`, `IR`, `DXCM`, `MDT`, `BSX`, `AAPL`, and `PYPL`.
3. Use repeated high-quality scanner names as inputs to the first official Current Universe refresh.

No buy or sell orders were placed or proposed.
