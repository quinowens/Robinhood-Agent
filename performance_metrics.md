# Performance Metrics

## Purpose

The agent must measure itself to improve. This document defines trade logging, daily reporting, research evaluation, portfolio performance, and monthly self-review.

If a metric cannot be computed, report it as `N/A`. Never fabricate a value.

---

## Evaluation Layers

Version 2.0.1 tracks underlying research, options setup quality, scanner-pipeline quality, market-regime context, correlation risk, and shadow-portfolio evidence:

### Research Layer

Measures whether the Research Agent is finding good candidates.

### Portfolio Layer

Measures whether the Portfolio Manager Agent is making good account-fit, premium-allocation, planned-risk, and correlation decisions.

### Options Setup Layer

Measures whether contract selection adds value beyond the underlying thesis.

Separating the two prevents confusing a good stock idea with a bad portfolio decision.

### Options Shadow Portfolio Layer

Measures setups that were genuinely qualified but could not be taken responsibly because of account, buying-power, premium-risk, drawdown, or concentration constraints. These are not normal watchlist items.

`WATCH` means the underlying or option setup was not ready. `SHADOW_ONLY_QUALIFIED` means setup quality passed and account fit failed. The system must freeze the exact selected option setup and score it as though it had been taken.

---

## Research Log Schema

Every evaluated candidate should produce one row:

| Field | Type | Notes |
| --- | --- | --- |
| `research_id` | int | Monotonic counter |
| `date` | date | |
| `ticker` | str | |
| `sector` | str | |
| `scanner_sources` | list[str] | Scanners that surfaced the candidate |
| `scanner_signals` | dict | Momentum/options/earnings/other signal flags |
| `pipeline_status` | enum | `rejected`, `watch_only`, `research_further`, `portfolio_review`, `proposal_candidate`, `blocked_by_earnings`, `blocked_by_risk` |
| `blocked_reason` | str | Required when rejected or blocked |
| `primary_blocking_rule` | str | First decisive rule that caused NO TRADE, blocked, or rejected status |
| `secondary_blocking_rules` | list[str] | Other true but non-decisive blocks; retained for context, not primary attribution |
| `earnings_risk_flag` | bool | True when candidate appears in earnings risk workflow |
| `research_score` | float | 0-100 |
| `data_completeness` | float | 0-100; percentage of required inputs available |
| `decision_confidence` | float | 0-100; confidence in the classification |
| `tier_recommendation` | enum | `tier_1`, `tier_2`, `watchlist`, `reject` |
| `entry_eligibility` | enum | `eligible`, `provisional_tier_2`, `blocked_by_earnings`, `blocked_by_extension`, `blocked_by_market_regime`, `blocked_by_trend`, `blocked_by_portfolio` |
| `eligible_after` | date | Nullable; required when a date can clear a temporary block |
| `next_review_date` | date | Nullable; required when a block needs reassessment |
| `mandatory_rejection_filters_passed` | bool | |
| `missing_data` | list[str] | Empty if complete |
| `key_reasons` | list[str] | |
| `risks` | list[str] | |
| `forward_30d_return` | float | Filled later if tracking available |
| `forward_60d_return` | float | Filled later if tracking available |
| `forward_vs_spy_30d` | float | Filled later if tracking available |
| `forward_vs_qqq_30d` | float | Filled later if tracking available |
| `forward_5d_return` | float | Filled after 5 trading sessions |
| `forward_10d_return` | float | Filled after 10 trading sessions |
| `forward_20d_return` | float | Filled after 20 trading sessions; required for NO TRADE opportunity-cost review |
| `max_favorable_excursion_30d` | float | Best return reached in first 30 sessions |
| `max_adverse_excursion_30d` | float | Worst return reached in first 30 sessions |
| `notes` | str | Optional |

---


---

## Options Proposal Log Schema

Every options idea reviewed by the system should produce one row, even if rejected.

| Field | Type | Notes |
| --- | --- | --- |
| `option_proposal_id` | int | Monotonic counter |
| `date` | date | |
| `underlying` | str | |
| `option_type` | enum | `call` or `put` |
| `side` | enum | `buy` or `sell` |
| `position_effect` | enum | `open` or `close` |
| `expiration` | date | |
| `strike` | float | |
| `estimated_premium` | float | Per contract |
| `contracts` | int | |
| `premium_allocation_dollars` | float | `premium_per_contract * 100 * contracts` |
| `premium_allocation_pct_account` | float | Premium allocation divided by account equity |
| `max_contractual_loss_dollars` | float | Equal to premium allocation for long options |
| `max_contractual_loss_pct_account` | float | Maximum contractual loss divided by account equity |
| `planned_trade_risk_dollars` | float | Reproducible exit-risk amount; defaults to max contractual loss if unavailable |
| `planned_trade_risk_pct_account` | float | Planned trade risk divided by account equity |
| `setup_quality_status` | enum | `QUALIFIED`, `WATCH`, `TEMP_BLOCK`, or `REJECT` |
| `account_fit_status` | enum | `PASS`, `FAIL`, or `NOT_EVALUATED` |
| `final_decision` | enum | `PM_PROPOSAL`, `SHADOW_ONLY_QUALIFIED`, `WATCH`, `TEMP_BLOCK`, `REJECT`, `STOCK_THESIS_ONLY`, `NO_DIRECTIONAL_EDGE` |
| `account_snapshot_id` | str | Account snapshot used for account-fit decision |
| `underlying_research_score` | float | 0-100 |
| `confidence` | float | 0-100 |
| `liquidity_notes` | str | Bid/ask, volume, open interest when available |
| `earnings_risk` | str | Blackout status or N/A |
| `review_alerts` | list[str] | From review tool when available |
| `decision` | enum | `propose`, `reject`, `watch` |
| `reason` | str | |

Options proposals should be evaluated separately from equity trades so premium risk and expiration behavior do not distort equity metrics.

## Options Shadow Portfolio Schema

Every `SHADOW_ONLY_QUALIFIED` setup must create a shadow record with a frozen entry snapshot:

| Field | Type | Notes |
| --- | --- | --- |
| `option_shadow_trade_id` | str | Stable ID for the frozen shadow setup |
| `option_setup_id` | str | Links to the options setup record |
| `shadow_portfolio` | str | Must be `options_shadow_portfolio` |
| `shadow_reason` | str | Usually account or premium-risk constraint |
| `underlying` | str | |
| `directional_thesis` | enum | `bullish` or `bearish` |
| `option_type` | enum | `call` or `put` |
| `expiration` | date | |
| `strike` | float | |
| `dte_at_entry` | int | |
| `entry_snapshot_at` | datetime | Time the contract was selected |
| `entry_premium` | float | Midpoint/mark used for performance |
| `entry_bid` / `entry_ask` / `entry_midpoint` | float | Quote snapshot |
| `entry_delta` | float | When available |
| `entry_implied_volatility` | float | When available |
| `entry_open_interest` / `entry_volume` | int | When available |
| `entry_breakeven` | float | When available |
| `underlying_price_at_entry` | float | |
| `options_setup_score` | float | |
| `account_snapshot_id` | str | |
| `account_fit_status` | enum | `FAIL` for unaffordable qualified setups |
| `account_fit_reasons` | list[str] | |
| `premium_allocation_dollars` | float | |
| `max_contractual_loss_dollars` | float | |
| `planned_trade_risk_dollars` | float | |
| `premium_stop_rule` | str | Shadow stop logic; no live order |
| `target_logic` | str | Shadow target logic; no live order |
| `time_stop` | str | |
| `underlying_invalidation_level` | str | |

Do not revise a frozen shadow setup to a cheaper or hindsight-improved contract. Later records may update outcomes only.

## Options Shadow Outcome Schema

Track each shadow setup at 1, 5, 10, 20, and 30 trading days:

| Field | Type | Notes |
| --- | --- | --- |
| `option_forward_1d_return` / `5d` / `10d` / `20d` / `30d` | float | Premium return from frozen entry |
| `underlying_forward_1d_return` / `5d` / `10d` / `20d` / `30d` | float | Underlying return from frozen entry |
| `underlying_forward_vs_spy_*` | float | Underlying excess return versus `SPY` |
| `underlying_forward_vs_qqq_*` | float | Underlying excess return versus `QQQ` |
| `option_mfe_20d` / `option_mae_20d` | float | Option max favorable/adverse excursion |
| `underlying_mfe_20d` / `underlying_mae_20d` | float | Underlying max favorable/adverse excursion |
| `planned_stop_triggered` | bool | Whether the planned premium stop would have triggered |
| `planned_target_hit` | bool | Whether the planned target would have hit |
| `thesis_validity_status` | enum | `valid`, `invalidated`, or `unclear` |
| `expired_worthless` | bool | True only after expiration when applicable |
| `directional_thesis_result` | enum | `right`, `wrong`, or `insufficient_data` |
| `contract_selection_result` | enum | `good`, `poor`, or `insufficient_data` |
| `option_vs_underlying_result` | enum | e.g. `option_outperformed`, `underlying_better`, `both_poor` |

This distinction is required: an underlying thesis can be right while contract selection is poor, such as when long premium underperforms the stock because IV was too expensive.

## Options Setup Metrics

Track v2.0 options records separately from equity/underlying records.

| Metric | Purpose |
| --- | --- |
| Bullish thesis hit rate | Measures long-call directional quality |
| Bearish thesis hit rate | Measures long-put directional quality |
| Options setup-score bucket performance | Calibrates setup thresholds |
| DTE bucket performance | Compares 30-45, 46-60, 61-90, and other DTE bands |
| Delta bucket performance | Measures mid-delta versus low/high delta outcomes |
| Call versus put performance | Separates bullish and bearish playbooks |
| IV/premium bucket performance | Tests whether long premium is overpriced |
| Spread/liquidity bucket performance | Tests whether liquidity rules prevent losses |
| Account-fit failures | Measures qualified setups that the current account cannot safely take |
| Thesis/contract classification | Distinguishes right thesis from poor contract choice |
| Funding requirement distribution | Estimates capital needed to participate in qualified setups |

Outcome classes:

- `THESIS_RIGHT_CONTRACT_RIGHT`
- `THESIS_RIGHT_CONTRACT_POOR`
- `THESIS_WRONG`
- `INSUFFICIENT_DATA`

Funding-need analytics should report the count of qualified setups, count and percentage failing account fit, median preferred-contract premium, 75th percentile preferred-contract premium, and the account size needed to satisfy current premium-risk caps for median and 75th percentile setups.

Options-specific performance must not be merged into equity performance in a way that hides expiration, spread, or premium-risk behavior.

## Trade Log Schema

Every closed trade must produce one row:

| Field | Type | Notes |
| --- | --- | --- |
| `trade_id` | int | Monotonic counter |
| `ticker` | str | |
| `sector` | str | GICS sector or thematic tag |
| `entry_date` | date | |
| `exit_date` | date | |
| `entry_price` | float | |
| `exit_price` | float | |
| `stop_price` | float | Initial stop defined at entry |
| `target_price` | float | Initial target defined at entry |
| `shares` | float | Fractional shares allowed if platform supports it |
| `position_dollars` | float | `shares * entry_price` |
| `risk_dollars` | float | `shares * (entry_price - stop_price)` |
| `pnl_dollars` | float | `shares * (exit_price - entry_price)` minus commissions / fees |
| `pnl_pct` | float | `pnl_dollars / position_dollars` |
| `r_multiple` | float | `pnl_dollars / risk_dollars` |
| `outcome` | enum | `win`, `loss`, or `breakeven` |
| `exit_reason` | enum | `stop_hit`, `target_hit`, `trend_break`, `rs_deterioration`, `time_stop`, `earnings_exit`, `manual` |
| `rules_violated` | list[str] | Empty if clean |
| `research_score_at_entry` | float | From Research Agent |
| `data_completeness_at_entry` | float | From Research Agent |
| `decision_confidence_at_entry` | float | From Research Agent |
| `notes` | str | Optional |

---

## Core Metrics

Track over daily, monthly, YTD, and all-time windows.

### Win Rate

```text
win_rate = wins / (wins + losses)
```

Breakeven trades are excluded.

### Profit Factor

```text
gross_profit = sum(pnl_dollars where pnl_dollars > 0)
gross_loss   = sum(pnl_dollars where pnl_dollars < 0)
profit_factor = gross_profit / abs(gross_loss)
```

### R-Multiple

```text
r_multiple = pnl_dollars / risk_dollars
```

Track average win R, average loss R, and total R.

### Max Drawdown

```text
peak_equity_t = max(equity_curve up to time t)
drawdown_t    = (peak_equity_t - equity_t) / peak_equity_t
max_drawdown  = max(drawdown_t over the window)
```

### Opportunity Capture

A skipped trade is any setup the agent explicitly evaluated, scored as meeting entry criteria, but did not enter.

```text
opportunity_capture = trades_taken / (trades_taken + qualified_trades_skipped)
```

---

## Research Quality Metrics

Track whether Research Agent scores have predictive value.

| Metric | Purpose |
| --- | --- |
| Average 30-day return by score bucket | Shows if high scores outperform low scores |
| Average alpha vs `SPY` by score bucket | Measures relative quality |
| Tier 1 forward performance | Validates Tier 1 quality |
| Tier 2 forward performance | Validates reduced-size candidates |
| Watchlist promotion rate | Shows whether watchlist adds value |
| False positive rate | High score but weak forward result |
| Rejection opportunity cost | Forward performance of rejected candidates |
| Scanner-source alpha | Forward alpha grouped by discovery source |
| Score monotonicity | Whether higher score buckets produce better outcomes |
| Options confirmation lift | Difference between qualified momentum names with and without options confirmation |

Track the same fixed forward horizons for Tier 1, Tier 2, Watchlist, score-based rejects, permanent-filter rejects, and scanner-only candidates. Do not evaluate only promoted candidates.

### Required Validation Questions

Monthly validation must answer these questions when sample size allows:

1. Did higher score buckets outperform lower score buckets?
2. Did high-scoring candidates outperform `SPY` and `QQQ`?
3. Which scanner sources produced positive or negative alpha?
4. Did Options Activity confirmation add measurable predictive value?
5. Did temporary earnings and extension blocks save losses or create negative opportunity value?
6. Did permanent rejection filters prevent repeated low-quality research spend?
7. Did the shadow portfolio outperform cash, `SPY`, and `QQQ` after realistic risk sizing?
8. For every NO TRADE candidate, what happened 5, 10, and 20 trading days later?

If fewer than 20 observed 30-day outcomes are available for a category, label the conclusion directional only.

For blocked or rejected candidates, group forward outcomes by `primary_blocking_rule`. At minimum, report count, median 20-day return, 20-day excess return versus `SPY`, win rate, max favorable excursion, and max adverse excursion. This is the evidence used to decide whether earnings, extension, Watchlist status, or tier cutoffs are helping or hurting.

### Blocking Rule Attribution

When multiple blocks apply, assign exactly one `primary_blocking_rule` and put the rest in `secondary_blocking_rules`.

Use this attribution order unless a more specific source-of-truth file overrides it:

1. Permanent rejection filters, such as unsupported asset, penny stock, OTC, failed tradability, or unresolved critical data.
2. Earnings blackout or unsettled post-earnings review.
3. Account, buying-power, open-order, kill-switch, or drawdown constraint.
4. Portfolio concentration or correlation-cluster constraint.
5. Market regime block.
6. Trend or relative-strength failure.
7. Unconfirmed extension.
8. Watchlist or outside-universe status.
9. Low score, low confidence, or insufficient completeness.

Example:

```text
Ticker: NVDA
Primary blocking rule: blocked_by_earnings
Secondary blocking rules:
- blocked_by_extension
- blocked_by_market_regime
```

Only the primary rule receives opportunity-cost credit or blame. Secondary rules remain useful for diagnostics but must not be counted as separate missed opportunities.

---

## Market Health Score

Market regime should be scored, not only treated as ON/OFF.

| Component | Max Points | Evidence |
| --- | ---: | --- |
| `SPY` trend | 20 | Above 50 SMA, above 200 SMA, positive 50-day slope |
| `QQQ` trend | 20 | Above 50 SMA, above 200 SMA, positive 50-day slope |
| Breadth | 20 | Advance/decline quality and percent of stocks above 50 SMA |
| Volatility | 20 | VIX level, VIX trend, and volatility expansion/contraction |
| Sector participation | 20 | Number and quality of leading sectors |

Classification:

| Score | Classification | Default Action |
| ---: | --- | --- |
| 80-100 | Strong | Normal proposal-only risk caps may apply |
| 65-79 | Constructive | New entries allowed only for high-quality Tier 1/Tier 2 setups |
| 50-64 | Mixed | Reduce risk; require stronger confirmation |
| 0-49 | Hostile | No new entries unless explicitly approved as an exception |

Risk scaling should be documented in `templates/market_regime_snapshot.json` and saved to `data/market_regime/` when market context is used in a decision.

---

## Correlation And Concentration Metrics

Sector caps are necessary but not sufficient. The Portfolio Manager must also watch economic clustering.

Track candidates and positions by correlation cluster, such as:

- `mega_cap_ai_platforms`
- `semiconductors_ai_infrastructure`
- `cloud_software`
- `cybersecurity`
- `fintech`
- `broad_market_etf`
- `healthcare_innovation`

Before serious funding, monthly validation should estimate:

- Cluster exposure if all approved proposals had been taken.
- Pairwise return correlation for active holdings and finalists when enough history exists.
- Shadow-portfolio drawdowns during market stress windows.
- Whether multiple tickers are effectively one AI/mega-cap technology bet.

If correlation data is missing and exposure would concentrate in one theme, treat that as a Portfolio Manager risk warning.

---

## Benchmark Tracking

Benchmarks:

| Benchmark | Proxy | Role |
| --- | --- | --- |
| S&P 500 | `SPY` | Broad market reference |
| Nasdaq 100 | `QQQ` | Tech/growth reference |

```text
agent_return = (equity_end - equity_start) / equity_start
benchmark_return = (close_end - close_start) / close_start
alpha_vs_benchmark = agent_return - benchmark_return
```

The agent should aim to outperform at least one benchmark and ideally both.

---

## Rule Violations

Target: zero.

Any rule violation must be logged with:

- Date
- Rule violated
- Trade or proposal involved
- Cause
- Corrective action

---

## Daily Report Additions

Daily scanner dry runs and research reports should follow `templates/daily_research_log.md` when possible and should be saved to `research_logs/YYYY-MM-DD-description.md`.

```text
Day Summary
- Equity start / end:
- Daily P/L $ / %:
- Drawdown from peak:
- Trades taken:
- Trades skipped:
- Wins / Losses / BE:
- Research candidates evaluated:
- Rule violations:
- Current operating mode:
```

Use explicit zeroes when an activity did not occur. Use `N/A` only when a value cannot be computed. A missing field is not equivalent to zero.

## Structured Collection Requirements

In addition to Markdown reports, preserve:

1. Raw scanner snapshots using `templates/raw_scanner_snapshot.json`.
2. Research records using `templates/research_record.json`.
3. Universe-run manifests using `templates/universe_run_manifest.json`.
4. Signal outcomes using `templates/signal_outcome.json`.
5. Options setup records using `templates/options_setup_record.json`.
6. Option shadow trades using `templates/option_shadow_trade.json`.
7. Option signal outcomes using `templates/option_signal_outcome.json`.

JSON Lines is preferred for append-only collections. Raw records must be retained before normalization. Each record must include a stable `run_id` or `research_id`.

## Shadow Portfolio

While execution remains proposal-only, record every fully qualified setup as a hypothetical trade with entry, stop, target, risk-based shares, rule-driven exit, and taken/skipped reason. Shadow results must remain separate from real account results.

Use `templates/shadow_trade.json` and append records to `data/shadow_trades/*.jsonl`.

The shadow portfolio should answer:

- What would have happened over 30, 60, and 90 trading days?
- Which qualified setups were skipped, and why?
- Did risk sizing improve or reduce returns?
- Did conservative blocks reduce drawdown?
- Did the agent outperform `SPY` and `QQQ` after realistic entry/exit rules?

Run `python3 scripts/analyze_outcomes.py` during monthly review to summarize available evidence.

---

## Monthly Review

Run on the first weekend after the last trading day of each calendar month. Output to `backtests/YYYY-MM-review.md`.

### Performance Summary

| Metric | Value |
| --- | --- |
| Trades taken | |
| Trades skipped | |
| Opportunity capture | |
| Win rate | |
| Average win ($ / R) | |
| Average loss ($ / R) | |
| Profit factor | |
| Max drawdown (% / $) | |
| Realized P/L ($ / %) | |
| Rule violations | |
| `SPY` return | |
| `QQQ` return | |
| Alpha vs `SPY` | |
| Alpha vs `QQQ` | |

### Research Review

| Metric | Value |
| --- | --- |
| Candidates evaluated | |
| Tier 1 candidates | |
| Tier 2 candidates | |
| Watchlist candidates | |
| Average Tier 1 forward return | |
| Average Tier 2 forward return | |
| Best research signal | |
| Worst research signal | |
| Missing data issues | |

### Rule Change Governance

Do not change rules casually.

A rule change requires:

1. Evidence from performance data.
2. Written rationale.
3. Expected benefit.
4. Risk of the change.
5. Changelog entry.


---

## Scanner Pipeline Metrics

The dynamic pipeline must be evaluated over time.

Track these metrics monthly:

| Metric | Purpose |
| --- | --- |
| Scanner candidates reviewed | Measures pipeline workload |
| Candidates rejected | Shows filter strictness |
| Candidates sent to Portfolio Manager | Measures research quality |
| Proposals generated | Measures actionable output |
| Trades taken | Measures selectivity |
| Scanner source of winning trades | Identifies useful scanners |
| Scanner source of losing trades | Identifies noisy scanners |
| False positives by scanner | Finds scanners that create bad research leads |
| Earnings blocks avoided | Measures risk-control value |

A scanner that produces many candidates but few high-quality proposals should be tightened or retired.
