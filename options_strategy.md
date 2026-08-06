# Options Strategy

## Purpose

This file defines how options may be researched, reviewed, and proposed inside the Robinhood Agent system.

Options are powerful but risky. They may create rapid losses, expiration risk, liquidity problems, and behavioral mistakes. For that reason, options are treated as a separate strategy layer with stricter controls than long equities.

---

## Current Options Mode

**Mode:** Proposal-only / review-only

The agent may research option contracts, retrieve chains, retrieve option quotes, review simulated option orders, and present trade proposals.

The agent may **not** place live option orders unless the user explicitly approves the exact reviewed order after seeing:

- Underlying symbol
- Contract type
- Strike
- Expiration
- Premium
- Max premium at risk
- Liquidity / spread notes
- Earnings risk
- Why the option is being used instead of stock
- Pre-trade alerts from the review tool

No standing permission exists for autonomous options execution.

---

## Supported Option Structures

Only single-leg options are allowed in this framework.

Allowed for research and proposal:

- Long calls
- Long puts
- Covered calls, only if the required shares are already held
- Cash-secured puts, only if cash collateral is available and explicitly approved

Not allowed:

- Naked short calls
- Naked short puts without cash-secured intent and manual approval
- Multi-leg spreads
- Iron condors
- Butterflies
- Calendars
- Diagonals
- Straddles
- Strangles
- 0DTE trades unless manually approved for research only
- Earnings lottery trades
- Contracts with poor liquidity or wide bid/ask spreads

---

## Options Philosophy

Options should be used only when they improve the trade structure versus buying or selling stock.

Acceptable reasons to consider options:

- Defined premium risk
- Limited capital deployment
- Strong directional thesis with a clear time window
- Existing equity position hedging
- Covered income strategy on owned shares

Bad reasons to consider options:

- Trying to get rich quickly
- Avoiding proper position sizing
- Chasing unusual options volume
- Gambling around earnings
- Buying cheap contracts because they are cheap
- Trading contracts without understanding expiration risk

---

## Contract Selection Rules

For long calls or puts, prefer:

- Expiration at least 30-90 days out unless manually approved
- Delta generally between 0.35 and 0.70
- Tight bid/ask spread relative to premium
- Sufficient open interest and volume when available
- Clear underlying trend confirmation
- No new long premium entry within 5 trading days before earnings unless manually approved

Avoid:

- Deep out-of-the-money lottery contracts
- Illiquid contracts
- Contracts with extreme implied volatility after a major move
- Contracts expiring within 14 days unless specifically approved

---

## Premium Risk Limits

Options risk is measured by premium at risk, not notional exposure.

Default rules:

| Account Stage | Max Premium Risk Per New Option Trade |
| --- | ---: |
| Testing account | $25 or less preferred |
| Small live account | 0.25% - 0.50% of equity |
| Mature account | 0.50% - 1.00% of equity only with strong justification |

For Quin's current small Agentic account, options should normally be **research-only** unless a very small, manually approved test is being performed.

---

## Required Proposal Format

Every option proposal must include:

```text
UNDERLYING:
CONTRACT:
SIDE:
POSITION EFFECT:
EXPIRATION:
STRIKE:
ESTIMATED PREMIUM:
MAX PREMIUM RISK:
THESIS:
WHY OPTION INSTEAD OF STOCK:
LIQUIDITY NOTES:
EARNINGS DATE / BLACKOUT CHECK:
EXIT PLAN:
INVALIDATION LEVEL:
REVIEW TOOL ALERTS:
FINAL DECISION: PROPOSE / NO TRADE
```

If any required field is missing, output `NO TRADE`.

---

## Exit Rules

Before entering an option, define an exit plan.

Possible exits:

- Underlying trend breaks
- Premium loses 40-50% from entry
- Contract reaches target profit
- Thesis invalidated
- Earnings event approaches
- Time decay becomes unacceptable
- Better risk/reward exists in equity instead

Never hold an option simply because it is down and the user hopes it recovers.

---

## Relationship to Equity Strategy

The equity strategy remains the primary system.

Options are secondary and should usually require stronger evidence than stock trades. A valid equity setup does not automatically mean a valid option setup.

The Portfolio Manager Agent must always ask:

> Is the option structure clearly better than simply buying the stock or staying in cash?

If not, choose stock or no trade.
