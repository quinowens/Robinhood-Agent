# Options Strategy

## Purpose

This file defines the core v2.0.1 options strategy.

Equities remain the research substrate. Options are the primary proposed trade expression when a qualified underlying has a clear directional thesis and a liquid, defined-risk contract can express that thesis efficiently.

The goal is selective asymmetric exposure with defined premium risk, not high trade frequency.

---

## Current Options Mode

**Mode:** Proposal-only / shadow-trading by default

The agent may research underlyings, retrieve option chains, retrieve option instruments, retrieve option quotes, retrieve option historicals when useful, and present hypothetical option proposals or shadow records. Simulated option-order review is reserved for future live-execution preparation.

The agent may **not** place live option orders unless the user explicitly approves the exact reviewed order after seeing:

- Underlying symbol and thesis direction
- Contract type
- Strike
- Expiration and DTE
- Premium and max premium at risk
- Bid, ask, midpoint, and spread notes
- Earnings/event risk
- Options setup score, completeness, and confidence
- Account fit status
- Pre-trade alerts from `review_option_order` when a future live order is being prepared

No standing permission exists for autonomous options execution.

Research, scoring, hypothetical Portfolio Manager proposals, and shadow tracking do not require `review_option_order`, exact user approval, or live-order readiness.

---

## Launch Scope

Phase 1 v2.0 supports only single-leg long-premium options:

- `LONG_CALL`
- `LONG_PUT`

Disabled in v2.0:

- 0DTE
- Naked short calls
- Naked short puts
- Cash-secured puts
- Covered calls
- Multi-leg spreads
- Margin-driven option selling
- Earnings lottery trades

Future schemas may support call debit spreads and put debit spreads, but they are not enabled by default.

Broker capability is recorded separately from strategy permission. The Agentic account is broker-approved for Level 2 options capability: buying calls, buying puts, selling covered calls, selling cash-covered puts, and exercising options. Spreads are broker-unavailable. Covered calls and cash-secured puts remain strategy-disabled.

---

## Two-Stage Decision

Every option idea requires two separate decisions:

1. Is the underlying worth taking directional exposure to?
2. Is there an option contract that expresses the thesis with acceptable timing, liquidity, volatility, and risk?

A strong underlying does not automatically create an option proposal.

Directional thesis values:

- `bullish`: may proceed to long-call research.
- `bearish`: may proceed to long-put research.
- `neutral`: no options proposal.

Options Activity Radar may add options context, but it may not create direction by itself. A failed bullish setup is not automatically a bearish setup.

---

## Options Suitability Gate

Before pulling large chains, decide whether options are appropriate for the thesis.

Statuses:

- `OPTIONS_RESEARCH`
- `STOCK_THESIS_ONLY`
- `WATCH`
- `TEMP_BLOCK`
- `NO_DIRECTIONAL_EDGE`
- `REJECT`

Because v2.0 is options-primary, `STOCK_THESIS_ONLY` does not create an equity purchase proposal. It is logged as a valid underlying thesis with no acceptable option expression.

Reject or block options research when:

- Direction is not clear.
- Thesis horizon is undefined.
- Earnings/event risk is unresolved.
- Underlying liquidity or tradability is insufficient.
- Account options access cannot be verified for account-fit classification.
- No plausible expiration window has enough DTE.
- Long premium would introduce obviously unacceptable IV/event risk.
- Critical contract, account, or risk data is missing.

---

## Progressive Options Data Workflow

Do not pull full option chains for every scanner hit.

Use this sequence:

```text
Underlying filters
  -> Underlying Thesis Score
  -> Directional thesis
  -> Options Suitability Gate
  -> get_option_chains
  -> filter expirations
  -> get_option_instruments
  -> filter strikes/contracts
  -> get_option_quotes
  -> get_option_historicals when needed
  -> rank contracts
  -> Portfolio Manager review
```

If a desired metric is unavailable, mark it unavailable, reduce options data completeness if material, and continue only when the remaining evidence is sufficient.

Never fabricate Greeks, IV metrics, open interest, volume, or historical volatility.

---

## Contract Selection

Preferred DTE:

- 30-90 DTE
- Reject below 30 DTE unless a documented future rule permits it.
- Hard-disable 0DTE in v2.0.

Preferred delta:

- Approximately 0.35-0.70 delta when available.
- Delta is a ranking input, not a directional signal.
- Do not buy very low-delta contracts simply because they are affordable.

Rank contracts by:

- Thesis horizon fit
- DTE
- Delta
- Breakeven
- Bid/ask spread
- Open interest when available
- Volume when available
- Premium
- IV/premium reasonableness
- Catalyst and expiration timing
- Strike relationship to underlying price

Do not force a far-OTM or very-short-expiration contract to fit buying power.

---

## Options Setup Score

Every serious contract candidate receives a score separate from the underlying score.

| Component | Max Points |
| --- | ---: |
| Contract liquidity / execution quality | 25 |
| Expiration / thesis-horizon fit | 20 |
| IV / premium reasonableness | 20 |
| Delta / strike / breakeven fit | 15 |
| Catalyst / event compatibility | 10 |
| Defined exit / reward-risk quality | 10 |
| **Total** | **100** |

Persist:

- `underlying_research_score`
- `options_setup_score`
- `options_data_completeness`
- `options_decision_confidence`
- component scores

Do not create an arbitrary passing threshold that makes qualification structurally unreachable. Log the distribution and calibrate thresholds from outcomes.

---

## Contract Ranking

For each qualified underlying:

1. Rank candidate contracts.
2. Retain a small set of finalists.
3. Select the best contract for PM review.
4. Optionally show 1-2 alternates for transparency.

Each finalist must include:

- `contract_rank`
- `selection_reason`

Lower premium does not automatically outrank a better contract.

---

## Account Fit Separation

Setup quality and account affordability are separate.

Statuses:

- `PM_PROPOSAL`
- `SHADOW_ONLY_QUALIFIED`
- `WATCH`
- `TEMP_BLOCK`
- `REJECT`

Rules:

- Setup quality PASS plus account fit PASS becomes `PM_PROPOSAL`.
- Setup quality PASS plus account fit FAIL becomes `SHADOW_ONLY_QUALIFIED`.
- Setup failures become `WATCH`, `TEMP_BLOCK`, or `REJECT`.
- Deprecated account-fit failure labels must not be written by v2.0.1 records.
- `SHADOW_ONLY_QUALIFIED` must be recorded in the dedicated Options Shadow Portfolio with the exact selected setup frozen at signal time.
- Do not solve affordability by selecting a lower-quality far-OTM or short-DTE contract.
- Account fit must not rewrite Current Universe membership, tier, canonical eligibility, research score, or directional thesis.

`WATCH` is not a shadow portfolio decision. Use `WATCH` when the stock is interesting but the underlying, timing, direction, or contract setup is not fully qualified. Use `SHADOW_ONLY_QUALIFIED` only when setup quality is good enough to take if account/risk constraints allowed it.

The frozen shadow record must include the exact option instrument ID when available, expiration, strike, type, DTE, bid, ask, midpoint or mark, delta, implied volatility, open interest, volume, breakeven, underlying price, selected-entry timestamp, option setup score, account snapshot, account-fit failure reasons, and planned premium stop, target, time stop, and invalidation rules.

Persist:

- `signal_group_id`
- `supersedes_setup_id`
- `is_canonical`
- `setup_quality_status`
- `account_fit_status`
- `account_fit_reasons`
- `final_decision`
- `account_snapshot_id`
- `account_snapshot_as_of`
- `option_shadow_trade_id` when `final_decision` is `SHADOW_ONLY_QUALIFIED`
- `option_signal_outcome_id` for forward tracking

---

## Premium Risk

Long-option risk is measured by premium allocation and maximum contractual loss.

Every proposal must include:

- Premium per contract
- Option-price units and contract-dollar units separately, for example `option_mid: 23.50` and `contract_premium_dollars: 2350.00`
- Number of contracts
- Premium allocation dollars
- Premium allocation as percentage of account
- Maximum contractual loss dollars
- Maximum contractual loss as percentage of account
- Planned trade risk dollars
- Planned trade risk as percentage of account
- Current open options premium risk
- Post-proposal premium risk
- Correlation-cluster exposure after proposal

For single-leg long calls and puts, maximum contractual loss equals the premium allocation plus applicable fees. If there is no reproducible planned-exit calculation, planned trade risk defaults to maximum contractual loss; never invent a smaller planned-risk value.

Current launch rule: planned trade risk for single-leg long calls and long puts is `default_max_contractual_loss` unless a future source-of-truth document defines a deterministic exit method with reproducible stop-price calculation, stop validity conditions, and outcome-review handling. A "50% premium stop" or any other heuristic may be discussed as a candidate rule, but it must not be written into `planned_trade_risk_dollars` or used for account-fit sizing until formally adopted.

Keep these caps distinct:

- `max_premium_allocation_pct_account`
- `max_planned_trade_risk_pct_account`
- `max_total_open_premium_exposure_pct_account`
- `max_correlated_open_premium_exposure_pct_account`

---

## Exit And Invalidation

Every option proposal must include an exit plan before entry:

- Underlying invalidation level
- Option-premium stop rule
- Profit objective or target logic
- Time stop
- Minimum remaining DTE / expiration-management rule
- Earnings/event exit requirement
- Thesis invalidation event

Do not keep an option open solely because it still has time. Do not average down. Do not roll automatically.

---

## Required Proposal Format

```text
EXECUTIVE DECISION: HYPOTHETICAL OPTIONS PROPOSAL

UNDERLYING
Symbol:
Universe Tier:
Eligibility:
Directional Thesis:
Underlying Thesis Score:
Underlying Completeness:
Underlying Confidence:

OPTIONS SETUP
Contract:
Expiration:
DTE:
Strike:
Delta:
Bid / Ask / Midpoint:
Spread % Mid:
Open Interest:
Volume:
Implied Volatility:
Estimated Premium:
Breakeven:
Options Setup Score:
Options Data Completeness:
Options Decision Confidence:

RISK
Contracts:
Max Premium Risk:
Premium Risk % of Account:
Premium Allocation Dollars:
Premium Allocation % Account:
Max Contractual Loss Dollars:
Max Contractual Loss % Account:
Planned Trade Risk Dollars:
Planned Trade Risk % Account:
Current Open Options Premium Risk:
Post-Proposal Premium Risk:
Correlation Cluster:

ACCOUNT FIT
PASS / FAIL

FINAL CLASSIFICATION
PM_PROPOSAL / SHADOW_ONLY_QUALIFIED / WATCH / TEMP_BLOCK / REJECT

EXECUTION
HYPOTHETICAL PROPOSAL - NOT SUBMITTED.
No live-order review is required for research or shadow tracking. Exact reviewed-order approval is required before any future live execution.
```

If any critical field is missing, output `NO TRADE` or the appropriate blocked/rejected classification.
