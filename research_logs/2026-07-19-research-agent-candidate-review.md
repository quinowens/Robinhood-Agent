# Research Agent Candidate Review

Date: 2026-07-19  
Review window: 2026-07-13 to 2026-07-17  
Account mode: Research-only / Proposal-only  
Order status: No orders placed

## Executive decision

Decision: NO TRADE

Primary reason:

This is a Research Agent candidate review only. The Current Universe remains unpopulated, and no candidate has passed the Portfolio Manager pre-trade checklist or received user approval as a documented mid-month exception.

Supporting reasons:

- Candidate inputs came from weekly scanner dry runs, the weekly review, prior Research Agent outputs, and current state files.
- Robinhood read-only fundamentals and historical bars were available for the main queue, but the real-time quote request failed at transport.
- Exact earnings dates were not available for every candidate in this run.
- Several candidates lack a full 200-session history from the retrieved bar window, so 200-day SMA checks are marked `N/A` where unsupported.
- Missing or incomplete data reduced confidence.

Final Research Agent decision: NO TRADE / research-only.

## Inputs reviewed

- `research_logs/2026-07-19-weekly-research-review.md`
- `research_logs/2026-07-13-daily-scanner-dry-run.md`
- `research_logs/2026-07-14-daily-scanner-dry-run.md`
- `research_logs/2026-07-15-daily-scanner-dry-run.md`
- `research_logs/2026-07-16-daily-scanner-dry-run.md`
- `research_logs/2026-07-17-daily-scanner-dry-run.md`
- `research_logs/2026-07-12-research-agent-candidate-review.md`
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
- Robinhood read-only fundamentals and historical bars for `SPY`, `QQQ`, `NVDA`, `AAPL`, `NBIS`, `TSM`, `CRDO`, `PYPL`, `ASTS`, `PANW`, `AMD`, `TSLA`, `ABT`, `UNH`, `META`, `MSFT`, `AMZN`, `FIG`, `VG`, and `TEAM`

## Method

The review applied the v1.6 Research Agent framework:

1. Build the queue from the weekly review, repeated scanner leaders, prior candidate reviews, and recent daily logs.
2. Apply Mandatory Rejection Filters before scoring.
3. Penalize missing data, earnings proximity, unverified 200-day trend, weak or unverified relative strength, high valuation, negative earnings, high volatility, limited public history, ADR/policy risk, and options-activity-only signals.
4. Score candidates from 0-100 using the `research_agent.md` and `universe.md` composite factors.
5. Classify each name as Tier 1 candidate, Tier 2 candidate, Watchlist, Watch only, Reject, or Blocked by earnings.

Scores are preliminary research scores. They do not create entry eligibility and do not override the unpopulated Current Universe.

## Benchmark context

Robinhood fundamentals snapshot, market date 2026-07-20:

| Symbol | Market cap | Avg volume | 52-week range | Read |
| --- | ---: | ---: | --- | --- |
| SPY | $784.8B | 45.4M | $619.29-$760.40 | Broad-market benchmark; still near 52-week high but off July 17 close |
| QQQ | $470.0B | 36.1M | $551.68-$748.65 | Growth benchmark; more stretched than SPY by valuation |

Market-regime limitations:

- Historical bars were retrieved, but the real-time quote call failed at transport.
- 50-day trend could be estimated from retrieved bars for many symbols, but 200-day SMA could not be fully computed from the available window for all names.
- Breadth and volatility were `N/A`.
- Scanner logs showed constructive pockets, but late-week weakness in several major technology and semiconductor names prevents a high-conviction entry posture.

## Candidate summary table

| Symbol | Main evidence | Available data snapshot | Mandatory filter result | Score | Confidence | Classification | Decision |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| NVDA | Repeated weekly leader; AI semiconductor | Market cap about $5.07T; avg volume about 129.9M; PE about 31.8 | Pass, but outside Current Universe | 83 | 76 | Tier 2 candidate | Research further |
| AAPL | Repeated mega-cap row; near 52-week high | Market cap about $4.79T; avg volume about 48.7M; PE about 40.3 | Pass, but outside Current Universe | 81 | 74 | Tier 2 candidate | Research further |
| PANW | July 17 cybersecurity leader; strong 52-week position | Market cap about $291.6B; avg volume about 7.2M; PE about 291 | Pass, but outside Current Universe | 79 | 70 | Tier 2 candidate | Research further |
| TSM | Repeated semiconductor ADR | Market cap about $2.10T; avg volume about 15.2M; PE about 29.6 | Pass, but ADR/earnings checks needed | 78 | 70 | Tier 2 candidate | Research further |
| NBIS | Repeated AI infrastructure lead | Market cap about $46.4B; avg volume about 17.6M; PE about 50.6 | Pass, but volatile and outside Current Universe | 76 | 66 | Tier 2 candidate | Research further |
| AMD | Repeated semiconductor candidate | Market cap about $838.8B; avg volume about 26.2M; PE about 164.4 | Pass, but valuation/volatility penalties | 74 | 66 | Watchlist | Research further |
| PYPL | Repeated fintech row | Market cap about $50.1B; avg volume about 22.5M; PE about 10.6 | Pass, but trend quality needs confirmation | 72 | 64 | Watchlist | Research further |
| CRDO | Repeated data-infrastructure row | Market cap about $40.6B; avg volume about 6.5M; PE about 82.9 | Pass, but high valuation/high beta | 71 | 62 | Watchlist | Research further |
| UNH | Repeated healthcare rebound | Market cap about $382.5B; avg volume about 6.5M; PE about 27.2 | Pass, but event/sector risk needs review | 70 | 62 | Watchlist | Research further |
| ABT | Repeated healthcare row after earnings block | Market cap about $177.0B; avg volume about 14.4M; PE about 31.9 | Blocked earlier by earnings window; refresh required | 68 | 60 | Watchlist | Watch until earnings clear |
| ASTS | Repeated satellite/space lead | Market cap about $22.0B; avg volume about 17.4M; PE negative | Pass liquidity/cap; negative earnings/high beta | 66 | 55 | Watchlist | Watch only |
| FIG | July 13 clean scanner overlap | Market cap about $12.7B; avg volume about 25.1M; PE negative | Pass cap/liquidity; limited history/negative earnings | 64 | 52 | Watch only | Watch only |
| VG | July 13 and 17 LNG/cyclical row | Market cap about $35.1B; avg volume about 15.1M; PE about 13.2 | Pass, but cyclical/limited-history penalties | 64 | 54 | Watch only | Watch only |
| TEAM | July 13 software momentum row | Market cap about $23.7B; avg volume about 3.4M; PE negative | Pass liquidity/cap; weak longer trend/negative earnings | 60 | 54 | Watch only | Watch only |
| TSLA | Repeated but noisy options/momentum attention | Market cap about $1.40T; avg volume about 34.6M; PE about 357.3 | Pass liquidity/cap; options activity alone insufficient | 58 | 54 | Watch only | Watch only |
| TLSA | Repeated Options Activity reject | State evidence: microcap, low price, low liquidity, high IV | Fails mandatory filters | 20 | 82 | Reject | Keep rejected |
| AARD | Repeated Options Activity reject | State evidence: microcap, low liquidity, high IV, sharp move | Fails mandatory filters | 20 | 82 | Reject | Keep rejected |
| AVIR | Repeated Options Activity reject | State evidence: small cap, low price, low volume, high IV | Fails mandatory filters | 24 | 80 | Reject | Keep rejected |
| MMLP | Repeated reject plus earnings risk | State evidence: microcap, low volume, near-term earnings | Fails mandatory filters and earnings block | 15 | 85 | Reject | Keep rejected |
| TTGT | Repeated Options Activity reject | State evidence: microcap, low volume, elevated IV | Fails mandatory filters | 22 | 82 | Reject | Keep rejected |
| ATAI | Repeated high-IV/extreme-move reject | State evidence: below market-cap preference, high IV, extended move | Fails quality/preference filters | 35 | 72 | Reject | Keep rejected |
| FRMM | Repeated low-liquidity earnings-risk reject | State evidence: microcap, very low volume, near-term earnings | Fails mandatory filters and earnings block | 12 | 86 | Reject | Keep rejected |

## Candidate notes

### NVDA

Ticker: NVDA  
Company: NVIDIA Corp.  
Sector / Theme: AI semiconductors  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Scanner Signals: Repeated large-cap momentum and options attention  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe  
Earnings Risk Flag: N/A; refresh required  
Research Score: 83  
Confidence: 76  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Repeated high-quality weekly scanner evidence.
- Market cap and liquidity far exceed v1.6 thresholds.
- Positive earnings profile and durable AI/data-center narrative.

Risks:

- Not in the Current Universe.
- Recent technology weakness late in the week reduces timing confidence.
- Exact earnings blackout check was not completed.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, complete earnings-date validation, account tradability/fractional checks.

Research Agent Decision: Research further as a top input for the official universe refresh. NO TRADE.

### AAPL

Ticker: AAPL  
Company: Apple Inc.  
Sector / Theme: Mega-cap technology / devices  
Scanner Sources: Momentum Candidates  
Scanner Signals: Repeated mega-cap momentum relevance  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe  
Earnings Risk Flag: N/A; refresh required  
Research Score: 81  
Confidence: 74  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Repeated scanner relevance.
- Very large market cap and strong liquidity.
- Near 52-week high in Robinhood fundamentals snapshot.

Risks:

- Elevated PE versus mature growth profile.
- Participation quality varied in daily logs.
- Outside Current Universe.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Research further. NO TRADE.

### PANW

Ticker: PANW  
Company: Palo Alto Networks Inc.  
Sector / Theme: Cybersecurity  
Scanner Sources: Momentum Candidates  
Scanner Signals: Mega-cap cybersecurity momentum  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe  
Earnings Risk Flag: N/A; refresh required  
Research Score: 79  
Confidence: 70  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Strong late-week scanner row and near 52-week high.
- Cybersecurity theme fits strategy.
- Market cap and average volume pass.

Risks:

- Very high PE in fundamentals snapshot.
- Full earnings and 200-day trend validation missing.
- One-week evidence is not enough for Current Universe inclusion.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Research further. NO TRADE.

### TSM

Ticker: TSM  
Company: Taiwan Semiconductor Manufacturing Co.  
Sector / Theme: Semiconductors / foundry  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Scanner Signals: Repeated semiconductor momentum and options confirmation  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe; ADR risk  
Earnings Risk Flag: N/A; refresh required  
Research Score: 78  
Confidence: 70  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Repeated high-quality semiconductor candidate.
- Mega-cap liquidity and reasonable PE versus growth peers.
- Durable AI supply-chain narrative.

Risks:

- ADR/geopolitical risk.
- Earnings timing must be verified before any advancement.
- Outside Current Universe.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Research further. NO TRADE.

### NBIS

Ticker: NBIS  
Company: Nebius Group NV  
Sector / Theme: AI infrastructure / cloud  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Scanner Signals: Repeated AI infrastructure momentum and options confirmation  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe; volatility risk  
Earnings Risk Flag: N/A; refresh required  
Research Score: 76  
Confidence: 66  
Tier Recommendation: Tier 2 candidate

Key Reasons:

- Repeated across July 14, 16, and 17 logs.
- Market cap and volume pass.
- Direct AI infrastructure narrative.

Risks:

- High volatility after a large 52-week range.
- Smaller and less established than mega-cap AI leaders.
- Outside Current Universe.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Research further, but keep confidence below stronger mega-cap candidates. NO TRADE.

### AMD

Ticker: AMD  
Company: Advanced Micro Devices Inc.  
Sector / Theme: Semiconductors  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Scanner Signals: Repeated semiconductor relevance  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe  
Earnings Risk Flag: N/A; refresh required  
Research Score: 74  
Confidence: 66  
Tier Recommendation: Watchlist

Key Reasons:

- Large, liquid semiconductor candidate.
- Repeated scanner relevance.
- Strong AI/accelerator theme.

Risks:

- Very high PE in fundamentals snapshot.
- Volatile price action and late-week technology weakness.
- Outside Current Universe.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Watchlist / research further. NO TRADE.

### PYPL

Ticker: PYPL  
Company: PayPal Holdings Inc.  
Sector / Theme: Fintech / payments  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Scanner Signals: Repeated scanner relevance  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe; trend quality unconfirmed  
Earnings Risk Flag: N/A; refresh required  
Research Score: 72  
Confidence: 64  
Tier Recommendation: Watchlist

Key Reasons:

- Repeated in July 13, 15, and 16 logs.
- Market cap and liquidity pass.
- Valuation is less stretched than many high-beta technology names.

Risks:

- Prior trend quality is uncertain.
- Fintech turnaround setups require stronger evidence than scanner hits.
- Outside Current Universe.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Research further, but keep as Watchlist. NO TRADE.

### CRDO

Ticker: CRDO  
Company: Credo Technology Group Holding Ltd.  
Sector / Theme: Data-infrastructure connectivity  
Scanner Sources: Momentum Candidates  
Scanner Signals: Repeated data-infrastructure relevance  
Pipeline Status: Research further  
Blocked Reason: Outside Current Universe; valuation/volatility risk  
Earnings Risk Flag: N/A; refresh required  
Research Score: 71  
Confidence: 62  
Tier Recommendation: Watchlist

Key Reasons:

- Repeated in July 14, 16, and 17 logs.
- Market cap and average volume pass.
- Strong data-center connectivity theme.

Risks:

- High PE and high-beta price action.
- Smaller company profile than mega-cap semiconductor leaders.
- Outside Current Universe.

Missing Data:

- Real-time quote snapshot, exact 200-day SMA, earnings-date validation, account checks.

Research Agent Decision: Research further, but keep below Tier 2 confidence. NO TRADE.

### Watch-only group

`ASTS`, `FIG`, `VG`, `TEAM`, and `TSLA` remain watch-only.

- `ASTS`: passes market-cap and liquidity preferences, but negative PE, high-beta profile, and speculative satellite narrative reduce confidence.
- `FIG`: passes cap and liquidity, but limited public history and negative PE block stronger classification.
- `VG`: passes cap and liquidity, but LNG/cyclical exposure and limited-history profile require a conservative score.
- `TEAM`: passes cap and average-volume preference, but negative PE and weaker longer trend reduce score.
- `TSLA`: passes cap and liquidity, but options activity and attention are not enough; valuation and volatility remain major penalties.

## Research queue after review

| Priority | Symbols | Next step |
| ---: | --- | --- |
| 1 | `NVDA`, `AAPL`, `PANW`, `TSM`, `NBIS` | Full universe-refresh research packet |
| 2 | `AMD`, `PYPL`, `CRDO`, `UNH`, `ABT` | Trend, RS, earnings, and valuation validation |
| 3 | `ASTS`, `FIG`, `VG`, `TEAM`, `TSLA` | Watch-only follow-up; require cleaner evidence before promotion |
| Reject archive | `TLSA`, `AARD`, `AVIR`, `MMLP`, `TTGT`, `ATAI`, `FRMM` | Keep rejected unless future evidence materially changes |

## State file decision

- `state/current_universe.json`: Not updated. Candidate scoring from a weekly review does not satisfy the official monthly universe-refresh process or user approval requirement for mid-month exceptions.
- `state/open_theses.json`: Not updated. No candidate has a fully documented thesis with complete trend, RS, earnings, risk, account, and Portfolio Manager evidence.
- `state/rejected_candidates.json`: Not updated. Repeated rejects supported by this week are already present in state.

## Next actions

1. Build a full universe-refresh candidate packet for `NVDA`, `AAPL`, `PANW`, `TSM`, and `NBIS`.
2. Pull fresh earnings dates before any scoring upgrade.
3. Re-run historical trend and relative-strength checks with enough bars for 200-day SMA where possible.
4. Keep options-related context as underlying sentiment only; no option contract review is justified from this report alone.
5. Maintain rejected-state discipline for repeated low-quality Options Activity rows.

## Portfolio Manager action recommendation

Decision: NO TRADE

Primary reason:

No candidate is currently entry-eligible because the Current Universe is not populated and no Portfolio Manager pre-trade checklist has been completed.

Supporting reasons:

- No user-approved mid-month exception exists.
- Account equity, buying power, holdings, open orders, sector exposure, stop loss, target, and risk-at-stop were not validated.
- Missing quote/earnings/trend data reduces confidence.
- Proposal-only mode prohibits live execution.

Final recommendation: NO TRADE / research-only.
