# Weekly Research Review

Date: 2026-07-19  
Review window: 2026-07-13 to 2026-07-17  
Account mode: Research-only / Proposal-only  
Order status: No orders placed

## Executive decision

Decision: NO TRADE

Primary reason:

The Current Universe remains unpopulated by an official broad monthly refresh. Under v1.6 rules, this week's scanner evidence can identify research candidates, repeated rejects, and future universe-refresh inputs, but it cannot authorize trades or populate the Current Universe by itself.

Supporting reasons:

- Five daily scanner dry-run logs were available for the week.
- No candidate completed full Research Agent validation plus Portfolio Manager pre-trade review.
- No candidate is approved as Tier 1 or Tier 2 in `state/current_universe.json`.
- Earnings Risk Radar repeatedly blocked near-term reporting names.
- Options Activity Radar remained noisy at the top and continued to surface low-quality high-IV names.

Final weekly decision: NO TRADE / research-only.

## Files reviewed

- `research_logs/2026-07-13-daily-scanner-dry-run.md`
- `research_logs/2026-07-14-daily-scanner-dry-run.md`
- `research_logs/2026-07-15-daily-scanner-dry-run.md`
- `research_logs/2026-07-16-daily-scanner-dry-run.md`
- `research_logs/2026-07-17-daily-scanner-dry-run.md`
- `research_logs/2026-07-12-weekly-research-review.md`
- `research_logs/2026-07-12-research-agent-candidate-review.md`
- `state/current_universe.json`
- `state/open_theses.json`
- `state/rejected_candidates.json`
- `pipeline_config.md`
- `scanner_engine.md`
- `research_agent.md`
- `portfolio_manager_agent.md`
- `performance_metrics.md`
- `universe.md`
- `system_prompt.md`
- `strategy.md`
- `options_strategy.md`

## Current state summary

| Area | Status | Review note |
| --- | --- | --- |
| Current Universe | Not populated | No Tier 1, Tier 2, or Watchlist names are approved for live entries |
| Open theses | Empty | No full thesis is documented |
| Rejected candidates | Populated | State already includes the week-supported repeated rejects reviewed below |
| Operating mode | Research-only / Proposal-only | Matches `pipeline_config.md`, `scanner_engine.md`, and `system_prompt.md` |
| Live order permission | Not enabled | No order was placed, simulated, or proposed |

## Repeated research candidates

| Symbol | Evidence this week | Scanner read | Weekly decision |
| --- | --- | --- | --- |
| NVDA | Repeated in July 13, 14, 16, and 17 logs | Mega-cap AI semiconductor; high liquidity; options attention appeared but was not treated as a signal by itself | Highest-priority research input |
| AAPL | Repeated in July 13, 15, 16, and 17 logs | Mega-cap liquidity; recent 52-week high in Robinhood fundamentals snapshot; scanner participation quality varied | Research further |
| NBIS | July 14, 16, and 17; repeatedly named as higher-quality AI infrastructure lead | AI infrastructure, high volume, above market-cap threshold, but high-beta/volatile | Research further |
| TSM | July 14, 15, and 17 | Mega-cap semiconductor ADR; strong liquidity and durable theme; earnings/ADR risk needs control | Research further |
| PYPL | July 13, 15, and 16 | Fintech/value-recovery profile with repeated scanner relevance | Research further, but trend quality must be verified |
| AMD | July 13, 16, and 17 | Mega-cap semiconductor, liquid, repeated but volatile/valuation-sensitive | Research further |
| CRDO | July 14, 16, and 17 | Data-infrastructure connectivity; repeated visible row; elevated valuation and volatility | Watchlist / research further |
| TSLA | July 13, 16, and 17 | Persistent attention, often options-led or negative-momentum; high valuation and volatility | Watch only |
| ASTS | July 16 and 17 | Space/satellite theme with liquid volume; relative-volume and profitability concerns | Watchlist / research further |
| ABT | July 13 earnings block; July 16 and 17 momentum relevance | Large-cap healthcare; blocked earlier by earnings window; better as post-earnings research | Watchlist after earnings clears |
| UNH | July 16 and 17 | Large-cap managed care rebound; defensive healthcare leadership, but recent event/risk context needs review | Watchlist |
| META / MSFT / AMZN / GOOGL | Repeated mega-cap technology mentions, especially July 13 and 15 | Liquid leadership candidates, but several appeared near earnings-risk windows later in the week | Research later with earnings checks |

## Repeated rejects

`state/rejected_candidates.json` already reflects the repeated rejects supported by this week's logs. No additional state write is required from this weekly review.

| Symbol | Weekly evidence | State status | Review decision |
| --- | --- | --- | --- |
| TLSA | Reappeared July 13 with same low-price, microcap/low-liquidity, high-IV Options Activity profile | Present | Keep rejected |
| AARD | Reappeared July 13; already a repeated low-quality Options Activity reject | Present | Keep rejected |
| AVIR | Repeated from prior Options Activity reject list and reappeared July 14 | Present | Keep rejected |
| MMLP | Reappeared July 14 and July 15 in Earnings Risk Radar with microcap/low-liquidity profile | Present | Keep rejected |
| TTGT | Reappeared July 15 after July 13 Options Activity rejection | Present | Keep rejected |
| ATAI | Reappeared July 16 after July 14 reject-for-now note; high IV and extreme move | Present | Keep rejected |
| FRMM | Reappeared July 16 and July 17 in Earnings Risk Radar with microcap/low-volume/earnings risk | Present | Keep rejected |

One-day or reject-for-now rows such as `REFR`, `MENS`, `BLRX`, `ISPR`, `GNLX`, `CBUS`, `DOUG`, `GAIA`, `FAC`, `WOLF`, `QRHC`, `NHTC`, `NMRA`, `ARMP`, `INV`, `EVTL`, `VMD`, `GNE`, `CTMX`, `PRPL`, `CRWS`, `CMCM`, `SOHU`, `NPKI`, `DEFT`, `JAN`, `PLG`, `VGZ`, `BV`, `INOD`, `MMED`, and `USAS` were not added to state from this weekly review because the week did not establish enough permanent repeated-reject evidence for every name.

## Scanner quality review

| Scanner | Quality read | Action |
| --- | --- | --- |
| Momentum Candidates | Best source of usable candidates. It surfaced liquid large-cap and mid/large-cap leads across AI infrastructure, semiconductors, cybersecurity, healthcare, energy, software, and mega-cap technology. | Keep as primary discovery source |
| Options Activity Radar | Useful only as confirmation. Highest-IV rows were repeatedly low-price, low-market-cap, low-liquidity, or extended names that fail before scoring. | Keep strict Mandatory Rejection Filters before ranking |
| Earnings Risk Radar | Valuable risk-control feed. It blocked many otherwise recognizable large-cap names during earnings season. | Keep as high-priority blocker |

Useful sources:

- Momentum Candidates produced the cleanest research feed: `NVDA`, `AAPL`, `NBIS`, `TSM`, `PYPL`, `PANW`, `ABT`, `UNH`, `ASTS`, `CRDO`, `AMD`, `FIG`, `VG`, `TEAM`, and `XOM`.
- Options Activity Radar was useful only when it overlapped with liquid names such as `NVDA`, `NBIS`, `TSM`, `PYPL`, `XOM`, `ABT`, `UNH`, `TSLA`, or `KHC`.
- Earnings Risk Radar was the most reliable risk-control scanner and should continue to override otherwise interesting scanner rows during blackout windows.

Noisy sources and false positives:

- Options Activity Radar repeatedly surfaced microcaps, low-price names, very high implied volatility rows, and thin-volume names that fail `penny_stock_or_microcap`, `insufficient_liquidity`, `high_volatility`, or `options_activity_alone_insufficient`.
- `TSLA` remained a liquid but noisy attention signal: repeated appearance does not equal constructive momentum.
- `WULF`, `ASTS`, `CRDO`, `NBIS`, and `FIG` require volatility, limited-history, or profitability penalties even when market cap and volume pass.

Momentum signal quality:

- Momentum quality was strongest where repeated scanner evidence aligned with large market cap, strong average volume, and durable themes: `NVDA`, `AAPL`, `TSM`, `NBIS`, `PANW`, `PYPL`, `ABT`, and `UNH`.
- Several visible Momentum rows had relative volume near or below 1.0, reducing confidence.
- Energy and cyclicals appeared early in the week (`VG`, `XOM`, `VLO`, `EQNR`, `DINO`), but sector concentration and cyclicality require separate validation.
- Late-week technology weakness in `NVDA`, `TSLA`, `MSFT`, `META`, `AMD`, `TSM`, `INTC`, and `CRDO` argues against an aggressive growth-entry posture without full trend and RS checks.

## Earnings-risk blocks

Names blocked by Earnings Risk Radar or named as near-term earnings blocks this week included:

`BOKF`, `CCK`, `DPZ`, `RYAAY`, `STLD`, `WRB`, `HDB`, `CFG`, `FITB`, `GE`, `IBN`, `RF`, `SCHW`, `TFC`, `TRV`, `AA`, `ABT`, `BAC`, `C`, `ERIC`, `FAST`, `AMX`, `AVB`, `CCI`, `CME`, `CSX`, `EQNR`, `IBM`, `KEY`, `MLI`, `MMLP`, `NOW`, `GM`, `HAL`, `IBKR`, `MMM`, `NOC`, `EQT`, `GGG`, `HAS`, `NVS`, `AAL`, `CMCSA`, `FCX`, `FISV`, `GOOG`, `GOOGL`, `HBAN`, `AXP`, `BX`, `CHTR`, `EW`, `INTC`, `NEM`, and `FRMM`.

Names approaching or requiring refreshed blackout checks before deeper work:

- `ABT`, `UNH`, `GOOG`, `GOOGL`, `INTC`, `IBM`, `MSFT`, `AMZN`, `META`, `AAPL`, `TSM`, `PANW`, `PYPL`, `NBIS`, `CRDO`, and `ASTS`.

## Names deserving deeper research

Priority queue for Research Agent scoring:

1. `NVDA`, `AAPL`, `NBIS`, `TSM`, `PANW` - strongest repeated large-cap or institutionally relevant technology / infrastructure candidates.
2. `PYPL`, `ABT`, `UNH`, `AMD`, `CRDO` - repeated scanner relevance but require stronger trend, RS, earnings, valuation, and quality validation.
3. `ASTS`, `FIG`, `VG`, `TEAM`, `XOM` - useful candidates from the week, but each needs extra penalties for limited history, cyclicality, profitability, or trend quality.
4. `TSLA`, `WULF`, `RKLB`, `KHC`, `NFLX` - watch-only or lower-confidence names because signal quality, earnings risk, or volatility is not clean enough.

## State file decision

- `state/current_universe.json`: Not updated. Weekly scanner evidence alone cannot populate the Current Universe under `universe.md`.
- `state/open_theses.json`: Not updated. No full thesis was documented with market regime, trend, RS, fundamentals, earnings timing, risk controls, and Portfolio Manager evidence.
- `state/rejected_candidates.json`: Not updated by this weekly review. The repeated rejects supported by the July 13-17 logs are already present in state.

## Next research actions

1. Run full Research Agent candidate scoring for `NVDA`, `AAPL`, `NBIS`, `TSM`, `PANW`, `PYPL`, `ABT`, `UNH`, `AMD`, `CRDO`, and `ASTS`.
2. Refresh earnings dates before any name is promoted beyond research status.
3. Compute 50-day trend, 200-day trend where enough bars exist, and 30/60-session relative strength versus `SPY`.
4. Penalize any candidate with missing tradability, earnings, or trend data.
5. Use repeated high-quality scanner evidence as input to the first official Current Universe refresh, not as approval by itself.

## Portfolio Manager action recommendation

Decision: NO TRADE

Primary reason:

No candidate is approved for entry because the Current Universe is not officially populated and no candidate completed the Portfolio Manager Pre-Trade Checklist.

Supporting reasons:

- Account equity, buying power, current positions, open orders, sector exposure, stop loss, target, risk-at-stop, drawdown breakers, and kill-switch status were not validated.
- Scanner hits remain research inputs only.
- Proposal-only mode prohibits live execution.

Final recommendation: NO TRADE / research-only.
