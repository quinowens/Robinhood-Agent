# Trading Strategy

## Strategy Name

**Institutional Momentum Tactical Options System**

---

## Objective

Generate disciplined tactical exposure by identifying high-quality directional underlyings and expressing qualified theses through liquid, defined-risk option contracts when the options setup itself is attractive.

The system should avoid low-quality speculation, stale watchlists, forced trades, and emotional entries.

---

## Market Philosophy

The market rewards strength, weakness, timing, and risk control.

The agent should focus on underlyings demonstrating:

- Relative strength
- Strong volume
- Positive momentum
- Healthy trend structure
- Institutional participation
- Quality fundamentals
- Durable business narratives

The goal is **not** to predict the future. The goal is to align with directional evidence while maintaining disciplined premium risk management.

If conditions are unclear, the correct action is usually **no trade**.

Version 2.0 should preserve the validation mindset. The system must measure underlying thesis quality, contract-selection quality, account fit, and option outcomes separately before changing thresholds.

---

## Two-Agent Strategy Model

### Underlying Research Agent

The Research Agent answers:

> Which underlyings deserve directional exposure?

It scans a broad candidate universe, applies objective filters, scores candidates, classifies directional thesis, and produces a ranked list.

### Portfolio Manager Agent

The Portfolio Manager Agent answers:

> Should this directional thesis become a defined-risk options position in Quin's account?

It reviews the underlying thesis, candidate contract, account constraints, premium risk, correlation exposure, and simulated order alerts before deciding whether to produce a hypothetical options proposal.

Research quality and portfolio risk are intentionally separated to prevent a good stock idea from automatically becoming a bad portfolio decision.

---

## Trading Universe

The set of approved underlyings is **generated dynamically** from objective filters and ranking logic. It is not based on an old manual watchlist.

See `universe.md` for:

- Seed universe definition
- Permanent Membership Rejection Filters
- Ranking formula
- Tier construction
- Current Universe
- Mid-month exception rules

---

## Sector Focus

The agent may favor sectors with strong momentum, institutional interest, and durable earnings narratives, including but not limited to:

- Artificial intelligence
- Semiconductors
- Cloud infrastructure
- Software
- Cybersecurity
- Automation
- Data centers
- Defense technology
- Financial technology
- Healthcare innovation
- High-quality broad-market ETFs

Sector leadership should be earned through data, not assumed. A strong sector or theme does not automatically justify buying calls; the contract must pass options suitability and setup scoring.

---

## Directional Thesis Model

After an underlying passes research, classify the thesis:

- `bullish`: may proceed to long-call research.
- `bearish`: may proceed to long-put research.
- `neutral`: no options proposal.

Direction must be supported by underlying evidence. Options Activity Radar may confirm options context, but it may not create direction by itself. A failed bullish setup is not automatically a bearish setup.

---

## Options Entry Requirements

Before producing a live-quality options proposal:

1. The underlying must be Tier 1, Tier 2, or validated provisional Tier 2.
2. The underlying must have `eligibility: eligible`.
3. Directional thesis must be `bullish` for a call or `bearish` for a put.
4. Directional confidence and thesis horizon must be explicit.
5. Options Suitability Gate must return `OPTIONS_RESEARCH`.
6. Contract must have acceptable DTE, strike, delta, liquidity, spread, premium, and event timing.
7. Options Setup Score, options completeness, and options confidence must be recorded separately from the underlying score.
8. Account fit must pass for `PM_PROPOSAL`, or the setup must be marked `SHADOW_ONLY_QUALIFIED` / `QUALIFIED_BUT_NOT_ACCOUNT_FIT`.
9. Earnings risk must be acceptable.
10. Portfolio and correlation-cluster exposure must remain reasonable.
11. Exit and invalidation plan must be defined before entry.

Universe membership and current entry eligibility are separate. A Tier 1 or Tier 2 member may remain in the Current Universe while temporarily blocked by earnings, extension, market regime, trend damage, or portfolio constraints.

---

## Exit Requirements

Exit or reduce option exposure when:

- Premium stop is triggered.
- Underlying invalidation level is hit.
- Trend structure breaks against the thesis.
- Relative strength materially deteriorates.
- Market conditions materially worsen.
- Earnings risk becomes unacceptable.
- The position thesis is invalidated.
- Time stop or minimum remaining DTE rule triggers.

---

## Forbidden Behavior

The agent may not:

- Revenge trade
- Average down
- Chase parabolic moves
- Trade low-volume securities
- Trade penny stocks
- Trade based on emotion
- Ignore risk controls
- Treat stale watchlists as approved universes
- Add to losing positions without explicit user approval
- Enter trades outside the Current Universe unless validated as provisional Tier 2 or explicitly approved as a one-off exception
- Enable 0DTE
- Buy cheap far-OTM contracts solely for affordability
- Treat high options activity as direction
- Convert every bullish stock into a call
- Convert every failed bullish setup into a put

---

## Daily Review Process

At the end of each trading day:

1. Review current market regime.
2. Review all open positions.
3. Review any trade proposals or executed trades.
4. Measure performance.
5. Identify mistakes or rule violations.
6. Record lessons learned.
7. Recommend improvements.

---

## Monthly Review Process

At month-end, the system should:

1. Rebuild the universe.
2. Archive the old universe.
3. Review performance versus `SPY` and `QQQ`.
4. Identify best and worst signals.
5. Review rule violations.
6. Recommend controlled changes.
7. Update `changelog.md` only when strategy behavior changes.

---

## Options Primary Expression

Options are the primary proposed trade expression in v2.0, but only after underlying research and contract research both pass.

Options are proposal-only / shadow-trading by default. See `options_strategy.md` for long-call/long-put scope, contract selection, premium risk limits, forbidden structures, setup scoring, and required proposal format.

---

## Scanner Overlay

The agent may use Robinhood scanner tools to identify live market candidates. Scanner hits must still pass the Research Agent process and Portfolio Manager risk checks.

See `scanner_engine.md` for scanner workflow and governance.
