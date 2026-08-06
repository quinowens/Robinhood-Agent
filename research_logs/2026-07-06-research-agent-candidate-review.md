# Research Agent Candidate Review

Date: 2026-07-06  
Run time: 10:01 CT market-data snapshot  
Account mode: Research-only / Proposal-only  
Order status: No orders placed

## Executive Decision

Decision: NO TRADE

Primary reason:

This is a Research Agent candidate review, not a Portfolio Manager trade proposal. The Current Universe is still not officially populated, and no candidate has completed the full Portfolio Manager pre-trade checklist.

Supporting reasons:

- Candidates came from scanner logs and weekly review output, not an official broad monthly Current Universe refresh.
- Research scores below are preliminary and intended to prioritize deeper work.
- No account equity, buying power, open positions, open orders, stop loss, target, sector exposure, drawdown breaker, or kill-switch check was performed.
- Several candidates have late-July or early-August earnings dates that require fresh blackout checks before any future proposal.
- No live orders were placed or proposed.

## Inputs Reviewed

- `research_agent.md`
- `scanner_engine.md`
- `pipeline_config.md`
- `universe.md`
- `portfolio_manager_agent.md`
- `research_logs/2026-07-06-weekly-research-review.md`
- Robinhood read-only fundamentals, quotes, monthly historicals, weekly historicals, and earnings results

## Method

The review used the existing Research Agent framework:

- Mandatory filters: liquidity, market cap, unsupported/security-quality risk, earnings blackout risk, and critical missing data.
- Momentum / RS proxy: January 2026 open to July 2, 2026 official close versus `SPY`.
- Recent trend proxy: June 2026 open to July 2, 2026 official close and distance from June/52-week highs.
- Earnings risk: next unreported earnings date from Robinhood earnings results.
- Confidence: reduced for event proximity, high volatility, negative EPS profiles, missing exact 50/200-day moving averages, and lack of account-specific tradability/fractional checks.

Important limitation:

This report uses monthly and weekly historical data as a first-pass trend and relative-strength review. It does not replace a full daily 50/200-day moving average calculation or Portfolio Manager review.

## Benchmark Context

| Symbol | Jan 2026 Open | Prior Close Date | Prior Close | 2026-to-Date Proxy | June Trend Proxy |
| --- | ---: | --- | ---: | ---: | ---: |
| SPY | 685.71 | 2026-07-02 | 744.78 | +8.6% | -1.4% |
| QQQ | 620.06 | 2026-07-02 | 712.60 | +14.9% | -3.3% |

Interpretation:

The market backdrop is still constructive on the 2026-to-date proxy, but June showed short-term softness. Candidates that strongly outperformed `SPY` over six months but fell sharply from June highs should be treated as volatile watchlist names, not automatic Tier 1 candidates.

## Candidate Summary

| Symbol | Theme | Market Cap | Avg Vol 30D | 2026 Proxy | Alpha vs SPY | June Trend | Earnings | Score | Confidence | Tier Rec | Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |
| AAPL | Mega-cap technology | $4.59T | 68.3M | +13.4% | +4.8% | -0.3% | 2026-07-30 verified | 78 | 76 | Watchlist | Research further |
| SNDK | Storage / semiconductor | $270.5B | 12.0M | +614.0% | +605.4% | +0.8% | 2026-08-13 tentative | 74 | 66 | Watchlist | Research further |
| GLW | Optical / electronic components | $172.1B | 17.7M | +121.3% | +112.7% | +11.7% | 2026-07-28 verified | 74 | 67 | Watchlist | Research further |
| INTC | Semiconductors | $634.4B | 131.3M | +218.6% | +210.0% | +10.0% | 2026-07-23 verified | 72 | 64 | Watchlist | Research further |
| AMKR | Semiconductor packaging | $17.8B | 6.5M | +69.7% | +61.1% | +2.9% | 2026-07-27 tentative | 72 | 65 | Watchlist | Research further |
| NBIS | AI infrastructure | $55.8B | 18.1M | +147.9% | +139.3% | -11.7% | 2026-08-06 tentative | 68 | 60 | Watchlist | Watch only |
| MRNA | Biotechnology | $32.8B | 9.1M | +167.4% | +158.8% | +69.4% | 2026-07-31 tentative | 68 | 58 | Watchlist | Watch only |
| HOOD | Brokerage / fintech | $103.9B | 33.9M | -2.4% | -11.0% | +25.3% | 2026-07-29 verified | 66 | 62 | Watchlist | Watch only |
| ASTS | Satellite communications | $31.8B | 24.3M | +14.5% | +5.9% | -21.7% | 2026-08-10 tentative | 61 | 55 | Reject / Watch | Watch only |
| AMZN | Mega-cap technology / retail | $2.61T | 62.9M | +4.9% | -3.7% | -8.9% | 2026-07-30 tentative | 62 | 62 | Reject / Watch | Watch only |
| MSFT | Mega-cap software | $2.86T | 48.5M | -19.4% | -28.0% | -16.0% | 2026-07-29 tentative | 58 | 58 | Reject / Watch | Watch only |
| NFLX | Streaming / internet services | $321.2B | 48.9M | -17.5% | -26.1% | -9.4% | 2026-07-16 verified | 56 | 55 | Reject | Reject for now |
| IREN | Data center / crypto-linked infra | $15.7B | 43.0M | -0.5% | -9.1% | -37.6% | 2026-08-27 tentative | 54 | 50 | Reject | Reject for now |
| COIN | Crypto-linked finance | $43.3B | 8.9M | -28.2% | -36.8% | -7.7% | 2026-07-30 tentative | 52 | 50 | Reject | Reject for now |
| FIG | Software / product design | $11.0B | 18.9M | -43.8% | -52.4% | -18.9% | 2026-09-02 tentative | 50 | 48 | Reject | Reject for now |

## Candidate Notes

### AAPL

Ticker: AAPL  
Company: Apple Inc.  
Sector / Theme: Electronic Technology / mega-cap technology  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Blocked Reason: None today; outside Current Universe  
Earnings Risk Flag: Monitor; verified earnings 2026-07-30  
Research Score: 78  
Confidence: 76  
Tier Recommendation: Watchlist

Key reasons:

- Large, liquid, institutionally relevant candidate.
- 2026 proxy return outperformed `SPY`.
- Recent June trend was roughly flat rather than broken.

Risks:

- Earnings date is later this month.
- Valuation is elevated, with PE around 37 and PB above 42.
- Not approved because Current Universe is not populated.

Research Agent Decision: Research further for universe refresh consideration.

### SNDK

Ticker: SNDK  
Company: Sandisk Corp.  
Sector / Theme: Storage / semiconductor hardware  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Blocked Reason: None today; outside Current Universe  
Earnings Risk Flag: Monitor; tentative earnings 2026-08-13  
Research Score: 74  
Confidence: 66  
Tier Recommendation: Watchlist

Key reasons:

- Extremely strong 2026 momentum and strong scanner confirmation.
- Market cap and liquidity are above strategy preference thresholds.
- EPS trajectory in recent reports improved materially.

Risks:

- Very extended longer-term move.
- Pulled back sharply from the June high near 2354 to the July 2 close near 1745.
- High volatility makes position planning difficult without a full daily trend review.

Research Agent Decision: Research further, but do not promote without pullback/base validation.

### GLW

Ticker: GLW  
Company: Corning Inc.  
Sector / Theme: Optical communications / electronic components  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Blocked Reason: None today; outside Current Universe  
Earnings Risk Flag: Monitor; verified earnings 2026-07-28  
Research Score: 74  
Confidence: 67  
Tier Recommendation: Watchlist

Key reasons:

- Strong 2026 momentum and positive June trend proxy.
- Large enough and liquid enough for further review.
- Thematic fit with optical communications and infrastructure.

Risks:

- Earnings date falls later this month.
- Very high PE around 94.
- Sharp reversal from June high requires trend confirmation.

Research Agent Decision: Research further, with earnings and trend checks required.

### INTC

Ticker: INTC  
Company: Intel Corp.  
Sector / Theme: Semiconductors  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Blocked Reason: None today; outside Current Universe  
Earnings Risk Flag: Monitor; verified earnings 2026-07-23  
Research Score: 72  
Confidence: 64  
Tier Recommendation: Watchlist

Key reasons:

- Strong 2026 momentum and very high liquidity.
- June trend proxy remained positive despite a late-month pullback.
- Large-cap semiconductor exposure fits the seed universe.

Risks:

- Earnings are close enough to require active blackout monitoring.
- PE is negative in Robinhood fundamentals.
- Turnaround profile requires quality penalty.

Research Agent Decision: Research further, but do not move toward proposal before earnings-window check.

### AMKR

Ticker: AMKR  
Company: Amkor Technology Inc.  
Sector / Theme: Semiconductor packaging  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Research further  
Blocked Reason: None today; outside Current Universe  
Earnings Risk Flag: Monitor; tentative earnings 2026-07-27  
Research Score: 72  
Confidence: 65  
Tier Recommendation: Watchlist

Key reasons:

- Strong 2026 return and acceptable liquidity.
- Semiconductor packaging theme is relevant to AI / hardware infrastructure.
- Market cap is above the $10B preference threshold.

Risks:

- Earnings are later this month.
- Smaller market cap than mega-cap leaders.
- Recent reversal from June highs requires daily trend validation.

Research Agent Decision: Research further as a secondary semiconductor candidate.

### NBIS

Ticker: NBIS  
Company: Nebius Group NV  
Sector / Theme: AI infrastructure / cloud software  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Watch only  
Blocked Reason: Outside Current Universe; quality and volatility penalties  
Earnings Risk Flag: Monitor; tentative earnings 2026-08-06  
Research Score: 68  
Confidence: 60  
Tier Recommendation: Watchlist

Key reasons:

- Strong thematic fit and large 2026 momentum.
- Liquidity and market cap meet first-pass thresholds.

Risks:

- June trend proxy turned negative.
- Earnings history shows negative EPS.
- High volatility and recent drawdown from June high reduce confidence.

Research Agent Decision: Watch only until profitability and trend quality improve.

### MRNA

Ticker: MRNA  
Company: Moderna Inc.  
Sector / Theme: Biotechnology  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Watch only  
Blocked Reason: Outside Current Universe; biotech/event risk  
Earnings Risk Flag: Monitor; tentative earnings 2026-07-31  
Research Score: 68  
Confidence: 58  
Tier Recommendation: Watchlist

Key reasons:

- Very strong June trend and strong 2026 momentum.
- Liquidity and market cap pass first-pass thresholds.

Risks:

- Negative PE and repeated negative EPS profile.
- Biotech catalyst risk is high.
- Earnings are later this month.

Research Agent Decision: Watch only unless a full catalyst and risk review supports deeper research.

### HOOD

Ticker: HOOD  
Company: Robinhood Markets Inc.  
Sector / Theme: Brokerage / fintech  
Scanner Sources: Options Activity Radar; near Momentum leadership  
Pipeline Status: Watch only  
Blocked Reason: Outside Current Universe; mixed relative strength  
Earnings Risk Flag: Monitor; verified earnings 2026-07-29  
Research Score: 66  
Confidence: 62  
Tier Recommendation: Watchlist

Key reasons:

- Strong June trend proxy and strong liquidity.
- Large enough for institutional relevance.

Risks:

- 2026 proxy return underperformed `SPY`.
- Earnings are later this month.
- Crypto / retail activity sensitivity can create headline and volatility risk.

Research Agent Decision: Watch only; revisit after earnings or stronger sustained RS.

### ASTS

Ticker: ASTS  
Company: AST SpaceMobile Inc.  
Sector / Theme: Satellite communications  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Watch only  
Blocked Reason: Negative EPS profile and weak June trend  
Earnings Risk Flag: Monitor; tentative earnings 2026-08-10  
Research Score: 61  
Confidence: 55  
Tier Recommendation: Reject / Watch

Key reasons:

- Strong liquidity and thematic relevance.
- 2026 proxy return modestly outperformed `SPY`.

Risks:

- Negative PE and negative EPS history.
- June trend proxy was sharply negative.
- High volatility makes it unsuitable for near-term universe promotion.

Research Agent Decision: Watch only; do not promote.

### AMZN

Ticker: AMZN  
Company: Amazon.com Inc.  
Sector / Theme: Mega-cap technology / retail / cloud  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Watch only  
Blocked Reason: Weak relative strength versus `SPY`  
Earnings Risk Flag: Monitor; tentative earnings 2026-07-30  
Research Score: 62  
Confidence: 62  
Tier Recommendation: Reject / Watch

Key reasons:

- Large, liquid, high-quality business.
- Suitable as a baseline mega-cap during the official universe refresh.

Risks:

- Underperformed `SPY` on the 2026 proxy.
- June trend proxy was negative.
- Earnings are later this month.

Research Agent Decision: Watch only until RS improves.

### MSFT

Ticker: MSFT  
Company: Microsoft Corp.  
Sector / Theme: Mega-cap software / cloud  
Scanner Sources: Options Activity Radar; repeated research relevance  
Pipeline Status: Watch only  
Blocked Reason: Weak trend and weak relative strength  
Earnings Risk Flag: Monitor; tentative earnings 2026-07-29  
Research Score: 58  
Confidence: 58  
Tier Recommendation: Reject / Watch

Key reasons:

- High-quality mega-cap with strong liquidity.

Risks:

- 2026 proxy return substantially underperformed `SPY`.
- June trend proxy was sharply negative.
- Earnings are later this month.

Research Agent Decision: Watch only; do not promote until trend/RS improves.

### NFLX

Ticker: NFLX  
Company: Netflix Inc.  
Sector / Theme: Streaming / internet services  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Rejected  
Blocked Reason: Weak trend and upcoming earnings risk  
Earnings Risk Flag: Monitor closely; verified earnings 2026-07-16  
Research Score: 56  
Confidence: 55  
Tier Recommendation: Reject

Key reasons:

- Large and liquid.

Risks:

- Underperformed `SPY` on the 2026 proxy.
- June trend proxy was negative.
- Earnings are close enough that this should not be advanced without a fresh blackout check.

Research Agent Decision: Reject for now.

### IREN

Ticker: IREN  
Company: IREN Ltd.  
Sector / Theme: Data center / crypto-linked infrastructure  
Scanner Sources: Options Activity Radar; repeated research relevance  
Pipeline Status: Rejected  
Blocked Reason: Weak trend and weak relative strength  
Earnings Risk Flag: Monitor; tentative earnings 2026-08-27  
Research Score: 54  
Confidence: 50  
Tier Recommendation: Reject

Key reasons:

- Liquidity is strong and market cap is above the preference threshold.

Risks:

- 2026 proxy underperformed `SPY`.
- June trend proxy was very weak.
- Crypto-linked / AI-infrastructure volatility requires stricter risk review.

Research Agent Decision: Reject for now.

### COIN

Ticker: COIN  
Company: Coinbase Global Inc.  
Sector / Theme: Crypto-linked finance  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Rejected  
Blocked Reason: Weak relative strength and crypto-linked volatility  
Earnings Risk Flag: Monitor; tentative earnings 2026-07-30  
Research Score: 52  
Confidence: 50  
Tier Recommendation: Reject

Key reasons:

- Liquidity and market cap are sufficient for research.

Risks:

- 2026 proxy return materially underperformed `SPY`.
- June trend proxy was negative.
- Earnings are later this month.
- Crypto-linked headline and volatility risk remain high.

Research Agent Decision: Reject for now.

### FIG

Ticker: FIG  
Company: Figma  
Sector / Theme: Software / product design  
Scanner Sources: Momentum Candidates, Options Activity Radar  
Pipeline Status: Rejected  
Blocked Reason: Weak trend, weak relative strength, negative PE  
Earnings Risk Flag: Monitor; tentative earnings 2026-09-02  
Research Score: 50  
Confidence: 48  
Tier Recommendation: Reject

Key reasons:

- Liquidity and market cap barely pass first-pass thresholds.

Risks:

- 2026 proxy return materially underperformed `SPY`.
- June trend proxy was negative.
- Negative PE and newer public-company profile reduce confidence.

Research Agent Decision: Reject for now.

## Research Queue After Review

Priority 1 - deeper daily trend / RS validation:

1. `AAPL`
2. `SNDK`
3. `GLW`
4. `INTC`
5. `AMKR`

Priority 2 - watch only, needs better confirmation:

1. `NBIS`
2. `MRNA`
3. `HOOD`
4. `ASTS`
5. `AMZN`
6. `MSFT`

Rejected for now:

1. `NFLX`
2. `IREN`
3. `COIN`
4. `FIG`

## State File Decision

No state files were changed.

Rationale:

- The Current Universe must not be populated from this report alone.
- No candidate reached a clean Tier 1 or Tier 2 recommendation.
- Several higher-scoring names require daily trend validation and earnings-window monitoring before any official universe consideration.
- This report is research-only and does not authorize Portfolio Manager action.

## Next Actions

1. Run exact daily 50-day and 200-day SMA checks on Priority 1 names.
2. Refresh earnings blackout status before any further review of `INTC`, `GLW`, `AMKR`, `HOOD`, `MSFT`, `AAPL`, `AMZN`, `COIN`, `MRNA`, and `NFLX`.
3. Use Priority 1 names as inputs to the first official Current Universe refresh, not as automatic approvals.
4. Keep `NBIS`, `MRNA`, `HOOD`, `ASTS`, `AMZN`, and `MSFT` as watch-only until trend and RS improve or earnings risk clears.
5. Do not revisit `NFLX`, `IREN`, `COIN`, or `FIG` unless scanner evidence improves materially.

## Portfolio Manager Action Recommendation

Decision: NO TRADE

Recommendation:

Research-only. Do not place live orders. Do not propose trades. Do not change core strategy rules based on this candidate review. The next correct action is exact daily trend/relative-strength validation for Priority 1 names and earnings-window monitoring before any Current Universe consideration.

No buy or sell orders were placed or proposed.
