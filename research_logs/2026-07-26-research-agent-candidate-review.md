# Research Agent Candidate Review

Date: 2026-07-26  
Review window: 2026-07-20 to 2026-07-24  
Account mode: Research-only / Proposal-only  
Order status: No orders placed

## Executive decision

Decision: NO TRADE

This is a Research Agent candidate review only. Candidate scores use the weekly review, recent daily scanner logs, prior Research Agent output, current state files, and read-only Robinhood fundamentals / quotes / technical indicators pulled on 2026-07-29. The Current Universe remains unpopulated, several names are blocked by earnings, and no candidate has passed the Portfolio Manager pre-trade checklist.

Final Research Agent decision: NO TRADE / research-only.

## Inputs reviewed

- `research_logs/2026-07-26-weekly-research-review.md`
- `research_logs/2026-07-20-daily-scanner-dry-run.md`
- `research_logs/2026-07-22-daily-scanner-dry-run.md`
- `research_logs/2026-07-23-daily-scanner-dry-run.md`
- `research_logs/2026-07-24-daily-scanner-dry-run.md`
- `research_logs/2026-07-19-research-agent-candidate-review.md`
- `state/current_universe.json`
- `state/open_theses.json`
- `state/rejected_candidates.json`
- `research_agent.md`
- `scanner_engine.md`
- `pipeline_config.md`
- `universe.md`
- `portfolio_manager_agent.md`
- `strategy.md`
- `options_strategy.md`
- Robinhood read-only fundamentals and quotes for `SPY`, `QQQ`, `NOW`, `AAPL`, `NBIS`, `SMCI`, `AMD`, `CBRS`, `AMZN`, `GOOG`, `GOOGL`, `DLR`, `SLB`, `MU`, `TMO`, `RTX`, `DHR`, `UNP`, `SNDK`, `AVGO`, `CRDO`, `PANW`, `CSX`, `XOM`, `MSTR`, `MARA`, `QRHC`, `PACK`, `CPIX`, and `HOWL`
- Robinhood 50-day and 200-day SMA snapshots for `SPY`, `NOW`, `AAPL`, `NBIS`, `SMCI`, `AMD`, `CBRS`, `DLR`, `SLB`, `MU`, `TMO`, `RTX`, `DHR`, `UNP`, and `AVGO`
- Robinhood earnings data / calendar for selected candidates and large-cap near-term earnings risks

## Method

The review applied the v1.6 Research Agent framework:

1. Build the queue from the weekly review, repeated scanner leaders, prior candidate reviews, and recent daily logs.
2. Apply Mandatory Rejection Filters before scoring.
3. Penalize missing data, earnings proximity, weak 50-day / 200-day trend, unverified relative strength, high valuation, negative or incomplete earnings, high volatility, limited history, ADR / policy risk, and options-activity-only signals.
4. Score candidates from 0-100 using the `research_agent.md` and `universe.md` composite factors.
5. Classify each name as Tier 1 candidate, Tier 2 candidate, Watchlist, Watch only, Reject, or Blocked by earnings.

Scores are preliminary research scores. They do not create entry eligibility and do not override the unpopulated Current Universe.

## Benchmark context

Robinhood market data snapshot pulled 2026-07-29:

| Symbol | Last price | Market cap | Avg volume | 50-day SMA | 200-day SMA | Read |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| SPY | $731.67 | $779.6B | 45.9M | $744.86 | $699.23 | Below 50-day, above 200-day; market regime not fully constructive |
| QQQ | $665.85 | $446.0B | 39.4M | N/A | N/A | Growth benchmark off recent highs; full trend not computed |

Market-regime limitations:

- Breadth, volatility trend, sector relative-strength tables, account state, positions, buying power, and order state were not validated.
- SPY below its 50-day SMA reduces aggressiveness even though it remains above its 200-day SMA.
- Relative strength versus SPY was not fully computed for every candidate, so scores and confidence are reduced.

## Candidate summary table

| Symbol | Main evidence | Data snapshot | Mandatory filter result | Score | Confidence | Classification | Decision |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| AAPL | Repeated mega-cap row; July 24 Momentum + Options + Earnings Risk | $5.08T cap; 51.1M avg volume; PE 40.3; above 50/200 SMA; verified earnings 2026-07-30 pm | Blocked by earnings and outside Current Universe | 80 | 78 | Blocked by earnings | Wait |
| RTX | July 23 large-cap defense momentum | $329.6B cap; 5.7M avg volume; PE 36.4; above 50/200 SMA; reported 2026-07-23 am | Pass, but outside Current Universe | 80 | 72 | Tier 2 candidate | Research further |
| DLR | July 24 Momentum + Options data-center REIT | $77.6B cap; 3.5M avg volume; PE 45.9; above 50/200 SMA; reported 2026-07-23 pm | Pass, but outside Current Universe | 78 | 70 | Tier 2 candidate | Research further |
| UNP | July 23 railroad momentum | $173.3B cap; 3.8M avg volume; PE 24.6; above 50/200 SMA; reported 2026-07-23 am | Pass, but outside Current Universe | 77 | 70 | Tier 2 candidate | Research further |
| NOW | Repeated July 22-24 software leader | $128.6B cap; 27.8M avg volume; PE 61.9; above 50-day but below 200-day; reported 2026-07-22 pm | Pass, but trend penalty and outside Current Universe | 76 | 68 | Tier 2 candidate | Research further |
| TMO | July 23 healthcare-tools momentum | $230.4B cap; 2.7M avg volume; PE 29.9; above 50/200 SMA; reported 2026-07-23 am | Pass, but one-day extension and outside Current Universe | 75 | 68 | Tier 2 candidate | Research further |
| AVGO | July 22 liquid semiconductor confirmation; prior leader | $1.84T cap; 18.2M avg volume; PE 62.3; below 50-day but above 200-day | Pass, but trend penalty and outside Current Universe | 74 | 66 | Watchlist | Research further |
| DHR | July 23 healthcare-tools momentum | $138.7B cap; 9.2M avg volume; PE 39.6; above 50-day but below 200-day; reported 2026-07-21 am | Pass, but 200-day trend penalty | 73 | 66 | Watchlist | Research further |
| SLB | July 24 Momentum + Options energy services | $78.3B cap; 14.5M avg volume; PE 20.6; below 50-day, above 200-day; reported 2026-07-24 am | Pass, but cyclical and 50-day trend penalty | 72 | 64 | Watchlist | Research further |
| MU | Repeated July 22-24 memory / semiconductor | $846.5B cap; 47.3M avg volume; PE 19.3; below 50-day, above 200-day | Pass, but high volatility and sharp pullback | 72 | 63 | Watchlist | Research further |
| AMD | July 22 Momentum + Options, July 24 Options | $707.4B cap; 28.7M avg volume; PE 164.4; below 50-day, above 200-day | Pass, but valuation and trend penalty | 70 | 62 | Watchlist | Research further |
| NBIS | Repeated AI infrastructure scanner candidate | $37.6B cap; 21.8M avg volume; PE 50.6; below 50-day, above 200-day; verified earnings 2026-08-12 am | Pass today, but upcoming earnings / volatility reduce confidence | 69 | 60 | Watchlist | Watch |
| CBRS | Repeated AI infrastructure / processor candidate | $53.4B cap; 5.9M avg volume; PE 156.4; below 50/200 SMA | Pass cap/liquidity, but weak trend and valuation | 66 | 56 | Watchlist | Watch |
| SMCI | Repeated AI infrastructure hardware | $19.9B cap; 54.2M avg volume; PE 13.0; below 50/200 SMA | Pass cap/liquidity, but weak trend and volatility | 63 | 58 | Watch only | Watch only |
| AMZN | Repeated mega-cap cloud/retail; July 22-24 Earnings Risk | $2.46T cap; 39.0M avg volume; PE 29.9; verified earnings 2026-07-30 pm | Blocked by earnings and outside Current Universe | 62 | 74 | Blocked by earnings | Wait |
| GOOG / GOOGL | July 23-24 mega-cap attention; reported 2026-07-22 pm | About $4.09T cap; strong volume; PE about 27; technical data not fully computed in this run | Pass earnings now, but incomplete trend / RS and outside Current Universe | 72 | 62 | Watchlist | Research further |
| MARA | Repeated Options Activity reject, crypto adjacency | $4.1B cap; 55.9M avg volume; PE negative | Fails preference / crypto-adjacent quality filters | 30 | 82 | Reject | Keep rejected |
| QRHC | Repeated Options Activity reject | $27.8M cap; 19K avg volume; $1.29 open; PE negative | Fails mandatory filters | 10 | 90 | Reject | Keep rejected |
| PACK | Repeated Options Activity reject | $497.9M cap; 504K avg volume; PE negative | Fails mandatory filters | 18 | 86 | Reject | Keep rejected |
| CPIX | Repeated Options Activity reject | $100.5M cap; 160K avg volume; PE negative | Fails mandatory filters | 15 | 86 | Reject | Keep rejected |
| HOWL | Prior repeated Options Activity reject | $27.8M cap; 605K avg volume; noncompliant status; PE negative | Fails mandatory filters | 8 | 92 | Reject | Keep rejected |

## Candidate notes

### AAPL

Ticker: AAPL  
Company: Apple Inc.  
Sector / Theme: Mega-cap technology / devices  
Scanner Sources: Momentum Candidates, Options Activity Radar, Earnings Risk Radar  
Pipeline Status: Blocked by earnings  
Earnings Risk Flag: Verified report on 2026-07-30 pm  
Research Score: 80  
Confidence: 78  
Tier Recommendation: Blocked by earnings

Key Reasons:

- Very large market cap, high liquidity, and price above both checked moving averages.
- New 52-week high in the Robinhood fundamentals snapshot.

Risks:

- Earnings blackout overrides scanner strength.
- Outside Current Universe.
- Elevated valuation for a mature mega-cap profile.

Missing Data:

- Full 30/60-session relative strength versus SPY, account state, tradability / fractional confirmation, and Portfolio Manager checklist.

Research Agent Decision: Wait until earnings risk clears. NO TRADE.

### RTX

Ticker: RTX  
Company: RTX Corp.  
Sector / Theme: Aerospace / defense  
Scanner Sources: Momentum Candidates  
Pipeline Status: Research further  
Earnings Risk Flag: Reported 2026-07-23 am  
Research Score: 80  
Confidence: 72  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Large, liquid defense candidate with price above both checked moving averages.
- Earnings were reported during the review window with actual EPS above estimate in Robinhood data.

Risks:

- One-day earnings reaction requires follow-through.
- Outside Current Universe.
- Relative-strength calculation was incomplete.

Missing Data:

- Full RS, 6-month momentum calculation, sector-strength confirmation, and Portfolio Manager checks.

Research Agent Decision: Research further as a possible universe-refresh input. NO TRADE.

### DLR

Ticker: DLR  
Company: Digital Realty Trust Inc.  
Sector / Theme: Data centers / REIT  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Earnings Risk Flag: Reported 2026-07-23 pm  
Research Score: 78  
Confidence: 70  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Clean data-center theme with Momentum and Options overlap.
- Price was above both checked moving averages.
- Liquidity and market cap pass.

Risks:

- REIT / rate sensitivity.
- July 24 move was extended after earnings.
- Outside Current Universe.

Missing Data:

- Full RS, FFO quality details, sector leadership, and account checks.

Research Agent Decision: Research further. NO TRADE.

### UNP

Ticker: UNP  
Company: Union Pacific Corp.  
Sector / Theme: Railroads / industrial transportation  
Scanner Sources: Momentum Candidates  
Pipeline Status: Research further  
Earnings Risk Flag: Reported 2026-07-23 am  
Research Score: 77  
Confidence: 70  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Large market cap, adequate average volume, and price above both checked moving averages.
- Post-earnings strength fit the weekly sector-rotation pattern.

Risks:

- More cyclical than core AI/software leadership.
- No visible Options Activity confirmation in the top rows.
- Outside Current Universe.

Missing Data:

- Full RS, market breadth, sector strength, and Portfolio Manager checks.

Research Agent Decision: Research further. NO TRADE.

### NOW

Ticker: NOW  
Company: ServiceNow Inc.  
Sector / Theme: Enterprise software / workflow automation  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Earnings Risk Flag: Reported 2026-07-22 pm  
Research Score: 76  
Confidence: 68  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Strongest repeated weekly scanner candidate.
- High liquidity and market cap.
- Earnings were reported during the review window with actual EPS above estimate in Robinhood data.

Risks:

- Price was below its 200-day SMA despite being above the 50-day SMA.
- PE remains elevated.
- Outside Current Universe.

Missing Data:

- Full relative strength versus SPY, 6-month momentum, account checks, and entry / stop / target.

Research Agent Decision: Research further, but do not elevate to live eligibility. NO TRADE.

### NBIS

Ticker: NBIS  
Company: Nebius Group NV  
Sector / Theme: AI infrastructure / cloud  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Watch  
Earnings Risk Flag: Verified upcoming report on 2026-08-12 am  
Research Score: 69  
Confidence: 60  
Tier Recommendation: Watchlist

Key Reasons:

- Repeated weekly scanner evidence and direct AI infrastructure narrative.
- Liquidity and market cap pass.

Risks:

- Price was below its 50-day SMA, indicating damaged short-term trend.
- Upcoming earnings will enter the blackout window soon.
- High volatility and non-US domicile reduce confidence.

Missing Data:

- Full RS, revenue / margin quality, tradability checks, and account checks.

Research Agent Decision: Watch; reassess after trend stabilizes and earnings risk clears. NO TRADE.

### Rejects

`MARA`, `QRHC`, `PACK`, `CPIX`, and `HOWL` remain rejected or rejected-for-trade because they fail mandatory or core preference filters. `QRHC`, `PACK`, `CPIX`, and `HOWL` are low-market-cap / low-liquidity names; `HOWL` also carried a noncompliant status in Robinhood fundamentals. `MARA` remains crypto-adjacent, below the preferred market-cap threshold, negative-PE, and options-activity-led.

Research Agent Decision: Keep rejected. NO TRADE.

## Research queue after review

| Queue | Symbols | Action |
| --- | --- | --- |
| Priority research | `RTX`, `DLR`, `UNP`, `NOW`, `TMO` | Validate RS, sector strength, post-earnings follow-through, and universe-refresh suitability |
| Secondary research | `AVGO`, `DHR`, `SLB`, `MU`, `AMD`, `GOOG`, `GOOGL` | Recheck trend and RS; keep as future universe-refresh inputs |
| Watch until risk clears | `AAPL`, `AMZN`, `NBIS` | Wait for earnings blackout / upcoming earnings risk to clear |
| Watch only | `CBRS`, `SMCI` | Require trend repair before elevation |
| Reject | `MARA`, `QRHC`, `PACK`, `CPIX`, `HOWL` | Keep out of research queue unless future evidence materially changes |

## State file decision

- `state/current_universe.json`: Not updated. Candidate scores do not satisfy an official monthly Current Universe refresh and user approval requirements.
- `state/open_theses.json`: Not updated. No full thesis was documented with all required supporting evidence.
- `state/rejected_candidates.json`: Not updated. The repeated rejects supported by the week are already reflected in state.

## Next actions

1. On the next scanner run, confirm whether `RTX`, `DLR`, `UNP`, `NOW`, and `TMO` hold follow-through after their earnings-related moves.
2. Compute full 30/60-session relative strength versus `SPY` before any promotion.
3. Recheck `AAPL`, `AMZN`, and `NBIS` after earnings blackout rules clear.
4. Keep `CBRS` and `SMCI` watch-only until price reclaims key trend levels.
5. Preserve scanner hits as research inputs only until the official Current Universe refresh is completed.

## Portfolio Manager action recommendation

Decision: NO TRADE

Primary reason:

No candidate is approved for entry because the Current Universe is not officially populated.

Supporting reasons:

- No candidate is Tier 1 or Tier 2 in `state/current_universe.json`.
- Several high-quality names are blocked by earnings or have incomplete RS / market-regime validation.
- Account equity, buying power, positions, open orders, sector exposure, stop loss, target, risk-at-stop, drawdown breakers, and kill switch were not validated.
- Proposal-only mode prohibits live execution.

Final recommendation: NO TRADE / research-only.
