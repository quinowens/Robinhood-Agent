# Trading Strategy

## Strategy Name

**Institutional Momentum Equity Rotation**

---

## Objective

Generate consistent long-term account growth by investing in high-quality equities exhibiting strong momentum, institutional participation, and favorable market conditions.

The system should avoid low-quality speculation, stale watchlists, forced trades, and emotional entries.

---

## Market Philosophy

The market rewards strength.

The agent should focus on stocks demonstrating:

- Relative strength
- Strong volume
- Positive momentum
- Healthy trend structure
- Institutional participation
- Quality fundamentals
- Durable business narratives

The goal is **not** to predict the future. The goal is to align with existing trends while maintaining disciplined risk management.

If conditions are unclear, the correct action is usually **no trade**.

Version 1.9 should focus on evidence, not more discretionary rules. The system should prove which scanner sources, score buckets, temporary blocks, and portfolio constraints add value before any thresholds are loosened.

---

## Two-Agent Strategy Model

### Research Agent

The Research Agent answers:

> What stocks deserve attention?

It scans a broad candidate universe, applies objective filters, scores candidates, and produces a ranked list.

### Portfolio Manager Agent

The Portfolio Manager Agent answers:

> Should this idea become a position in Quin's account?

It reviews the Research Agent output, checks current account constraints, calculates sizing, evaluates risk, and decides whether to propose a trade.

Research quality and portfolio risk are intentionally separated to prevent a good stock idea from automatically becoming a bad portfolio decision.

---

## Trading Universe

The set of tradable equities is **generated dynamically** from objective filters and ranking logic. It is not based on an old manual watchlist.

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

Sector leadership should be earned through data, not assumed.

---

## Entry Requirements

Before entering a position:

1. The stock must be in Tier 1 or Tier 2 of the Current Universe.
2. Market trend must be constructive.
3. Sector must show relative strength.
4. Stock must demonstrate above-average volume or clear institutional participation.
5. Price structure must be constructive.
6. Risk/reward must be favorable.
7. Position must have a defined stop-loss.
8. Earnings risk must be acceptable.
9. Portfolio concentration rules must pass.
10. Correlation-cluster exposure must not create hidden concentration.

Universe membership and current entry eligibility are separate. A Tier 1 or Tier 2 member may remain in the Current Universe while temporarily blocked by earnings, extension, market regime, trend damage, or portfolio constraints.

---

## Exit Requirements

Exit or reduce exposure when:

- Stop-loss is triggered.
- Trend structure breaks.
- Relative strength materially deteriorates.
- Market conditions materially worsen.
- Earnings risk becomes unacceptable.
- The position thesis is invalidated.
- A better opportunity exists and portfolio capacity is limited.

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
- Enter trades outside the Current Universe without explicit user approval

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

## Options Overlay

Options are not the core strategy. They are a secondary tactical layer used only when they provide a clearly better risk/reward structure than buying stock or staying in cash.

Options are proposal-only by default. See `options_strategy.md` for contract selection, premium risk limits, forbidden structures, and required proposal format.

---

## Scanner Overlay

The agent may use Robinhood scanner tools to identify live market candidates. Scanner hits must still pass the Research Agent process and Portfolio Manager risk checks.

See `scanner_engine.md` for scanner workflow and governance.
