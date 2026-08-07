# Scanner Engine

## Purpose

The Scanner Engine defines the dynamic discovery pipeline for the Robinhood Agent.

The system should not rely on stale watchlists. Saved scanners act as market sensors that continuously surface candidates from different opportunity buckets.

Scanner results are **underlying research inputs only**. A scanner hit is never a trade signal or options direction signal by itself.

---

## Current Scanner Mode

**Mode:** Research-only / Proposal-only

The agent may list and run saved scanners without additional approval. Creating or modifying scanners is a real account write and should be done only when the user has approved the scanner name, purpose, filters, and sorting. Call `get_scanner_filter_specs` before proposing a creation or filter update.

---

## Active Robinhood Scanners

| Scanner | Scan ID | Purpose | Status |
| --- | --- | --- | --- |
| Momentum Candidates | `26cdeb14-da13-493f-b0c6-783468971a16` | Underlying movement / opportunity discovery | Active |
| Options Activity Radar | `7068db65-2a47-470c-bde9-94d66f36b806` | Options context, attention, and IV review input | Active, research only |
| Earnings Risk Radar | `737924f1-e94f-4ad4-ba98-6c12fcaafaa9` | Upcoming earnings risk filter | Active |

These scanners live inside Robinhood, not in this repository. IDs are expected values, not unquestionable truth: call `get_scans` at run start, match both name and ID, and mark the run degraded if an expected scan is missing or mismatched.

---

## Dynamic Pipeline

```text
Run Saved Scanners
        ↓
Collect Raw Candidates
        ↓
Normalize Fields
        ↓
Remove Duplicates
        ↓
Tag Source Scanner(s)
        ↓
Apply Eligibility Filters
        ↓
Research Agent Scoring
        ↓
Directional Thesis Classification
        ↓
Options Suitability Gate
        ↓
Options Contract Research for Finalists
        ↓
Theme + Sector Grouping
        ↓
Tier Assignment
        ↓
Portfolio Manager Review
        ↓
Proposal / Watch / Reject
```

---

## Candidate Sources

### 1. Momentum Candidates

Primary source for underlying movement and opportunity discovery.

Current filters:

- Market cap greater than $10B
- Volume greater than 2M shares
- Sorted by daily percent change descending

Use this scanner to identify where capital is flowing today. Downstream validation must record momentum direction, average dollar volume, relative volume, price versus the 200-day SMA, and whether the one-day move exceeds 10% or 15%. A high positive daily move does not automatically mean buy calls.

### 2. Options Activity Radar

Options-context source for unusual attention, relative options activity, and IV context.

Current preset:

- Relative options volume greater than 2
- Stocks only
- Sorted by implied volatility descending

This scanner may prioritize underlyings for options research, but options activity alone is not enough to create direction or trade.

Before Options Activity contributes any positive scoring impact, the underlying should:

- Have at least $10B market cap or already belong to the Current Universe.
- Have sufficient average dollar volume.
- Have a qualifying primary momentum or research signal.
- Be outside the earnings blackout window.
- Not have an unconfirmed extreme one-day move.

Options Activity Radar should contribute to `options_setup_score` or `options_decision_confidence` when supported by contract evidence. It should not inflate the Underlying Thesis Score or create a bullish/bearish thesis by itself. The existing saved scanner may continue unchanged until the user explicitly approves a Robinhood scanner modification.

### 3. Earnings Risk Radar

Risk-control scanner.

Current preset:

- Earnings date within the next 7 days
- Stocks only

This scanner should be used to block new entries close to earnings. It must not permanently reject or remove an otherwise qualified universe member.

---

## Deduplication Rules

If the same ticker appears in multiple scanners, merge the candidate into one research record.

Example:

```json
{
  "symbol": "RIVN",
  "sources": ["Momentum Candidates", "Options Activity Radar"],
  "scanner_signals": {
    "momentum": true,
    "options_activity": true,
    "earnings_risk": false
  }
}
```

A ticker appearing in more than one positive scanner may receive a small decision-confidence boost. A ticker appearing in Earnings Risk Radar retains its tier but receives `eligibility: blocked_by_earnings` when the event is inside the pre-earnings blackout window or the post-earnings settled-session review has not cleared. After earnings, direct earnings data is primary; Earnings Risk Radar is secondary confirmation only.

---

## Initial Pipeline Scoring

Scanner-level scoring is not the final score. It is only the first pass.

| Signal | Suggested Impact |
| --- | ---: |
| Large-cap momentum hit | +10 |
| High relative volume | +5 |
| Qualified high options activity | +0 underlying score; options-context input only |
| Multiple positive scanner confirmation | +0 research score; up to +3 decision confidence |
| Upcoming earnings within 5 trading days | Temporary entry block; no universe-score penalty |
| Market cap below strategy threshold | Reject or -30 |
| Volume below strategy threshold | Reject or -20 |
| Extreme one-day move above 15% | -10 unless follow-through confirms |
| Missing key data | -5 to -15 |

The Research Agent must still apply the full scoring model in `research_agent.md`.

---

## Pipeline Output Schema

Every pipeline run should produce a structured candidate table:

| Rank | Symbol | Sources | Scanner Signal | Market Cap | Volume | Earnings Risk | Research Status | Next Action |
| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |

Valid next actions:

- Research further
- Send to Portfolio Manager
- Watch only
- Reject
- Blocked by earnings

Every raw scanner result must also be persisted with:

```text
run_id, timestamp, scanner_id, ticker, rank, price, daily_change,
volume, average_volume, average_dollar_volume, relative_volume,
market_cap, relative_options_volume, implied_volatility, earnings_date
```

Unavailable values must be `null` or `N/A`, never omitted silently.

---

## Guardrails

The Scanner Engine must not:

- Treat scanner rank as trade rank
- Buy because a ticker is up on the day
- Buy because options volume is high
- Trade earnings purely because a scanner surfaced the name
- Use microcap movers as default ideas
- Override universe, risk, or portfolio rules

---

## Daily Research Workflow

1. Check account, positions, and open orders.
2. List saved scans, resolve the configured names/IDs, and run all matched active scanners.
3. Merge and deduplicate candidates.
4. Flag earnings risks using direct calendar/results tools, with the Earnings Risk Radar as secondary confirmation.
5. Pull fundamentals, reported financials, tradability, and batched quotes for top candidates.
6. Pull historicals and benchmark/index context where trend validation is needed.
7. Score the candidates.
8. Group names by theme and sector.
9. Classify directional thesis for qualified finalists.
10. Run Options Suitability Gate before option-chain work.
11. Pull option chains/instruments/quotes only for qualified finalists.
12. Rank contracts and calculate Options Setup Score.
13. Send only validated option setups to the Portfolio Manager.
14. Produce a proposal-only / shadow-trading report.

---

## Options Integration

Options activity can improve options-context confidence, but options remain under the stricter process in `options_strategy.md`.

Options are currently research-only unless:

1. The account has the required options level.
2. The exact contract is reviewed.
3. The user approves the specific reviewed order.
4. The trade obeys premium-risk caps.

No autonomous options execution. `review_option_order` is a simulation/review step only.
