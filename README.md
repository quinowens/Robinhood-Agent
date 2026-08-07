# Quin AI Trading Agent

## Mission

Build and continuously improve an AI-powered tactical options agent grounded in disciplined underlying-equity research.

The agent's primary goal is **capital preservation** and **consistent long-term account growth** through systematic decision-making.

This project is designed for Robinhood's AI Agent platform. In v2.0, equities remain the research substrate and options become the primary proposed trade expression.

---

## Current Version

- **Version:** 2.0
- **Account Type:** Dedicated AI Agent account
- **Execution Mode:** Proposal-only until explicitly upgraded
- **Asset Type:** Options-primary; long calls/long puts only at launch; equities are approved underlyings

---

## Core Principles

1. Capital preservation comes first.
2. Cash is a valid position.
3. Risk management is more important than prediction.
4. The agent should not inherit stale watchlists.
5. The tradable universe should be regenerated systematically.
6. Research and portfolio decisions should be separated.
7. High-quality setups are preferred over high trade frequency.
8. The system should evolve through testing, performance review, and controlled version changes.

---

## Agent Architecture

Version 2.0 integrates Robinhood's expanded Agentic Trading tools for underlying research, options-chain research, account context, simulated order review, validation, and outcome tracking while preserving explicit approval for every account write and live order.

### 1. Research Agent

The Research Agent is responsible for finding qualified option underlyings. It scans a broad equity universe, applies filters, ranks candidates, classifies directional thesis, and produces an Underlying Thesis Score.

It does **not** place trades.

### 2. Portfolio Manager Agent

The Portfolio Manager Agent decides whether a directional thesis should become a defined-risk options proposal. It reviews the underlying, contract, account fit, premium risk, correlation exposure, and execution alerts.

It may only propose trades unless autonomous execution has been explicitly enabled.

### Scanner Engine

The Scanner Engine uses live Robinhood scanner tools to discover candidates from the broader market. Scanner results are research inputs only and do not automatically become trades.

The dynamic pipeline uses multiple scanner types:

- Momentum Candidates
- Options Activity Radar
- Earnings Risk Radar
- Manual / legacy watchlists for testing only

Scanner results are merged, deduplicated, filtered, scored, and routed to the Portfolio Manager only after research validation.

### Options Strategy Layer

Options are the primary proposed trade expression in v2.0, but remain proposal-only / shadow-trading by default. The agent may analyze chains, retrieve quotes, rank long call/put contracts, and review simulated single-leg option orders, but may not place live option orders without explicit approval of the exact reviewed order.


```text
Market Regime
        ↓
Saved Scanners / Discovery
        ↓
Underlying Research Engine
        ↓
Underlying Eligibility + Directional Thesis
        ↓
Options Suitability Gate
        ↓
Options Chain / Contract Research
        ↓
Options Setup Score
        ↓
Portfolio / Risk Manager
        ↓
Hypothetical Options Proposal / Shadow Tracking / No Trade
        ↓
Performance Review
```

---

## Trading Style

- Options-focused tactical expression using single-leg long calls and long puts
- Long equities as underlying research and validation substrate
- Momentum
- Trend following
- Sector rotation
- Quality bias
- Institutional participation
- Market-regime awareness

---

## Risk Parameters

| Parameter | Value |
| --- | --- |
| Maximum open positions | 3 |
| Maximum Tier 1 position size | 15% of account |
| Maximum Tier 2 position size | 10% of account |
| Maximum risk per trade | Premium-risk cap by account stage; never loosened to force trades |
| New entries outside approved universe | Provisional Tier 2 validation or explicit one-off user approval required |
| Watchlist entries | Not eligible for live-quality options proposals |

---

## Repository Structure

```text
Robinhood-Agent/
├── README.md                    # Project overview
├── PRIVATE_DATA.md              # Private data and public-release policy
├── Makefile                     # Validation and repo helper targets
├── system_prompt.md             # Master operating instructions
├── research_agent.md            # Research Agent responsibilities and output format
├── portfolio_manager_agent.md   # Portfolio Manager Agent responsibilities and risk decisions
├── strategy.md                  # Trading strategy specification
├── universe.md                  # Universe selection rules + active Current Universe
├── scanner_engine.md            # Robinhood scanner workflow and governance
├── pipeline_config.md           # Active scanner IDs and dynamic pipeline steps
├── tool_policy.md               # Tool catalog, permissions, freshness, and order lifecycle
├── performance_metrics.md       # Metrics and monthly review framework
├── changelog.md                 # Version history and roadmap
├── templates/                   # Reusable report templates
├── docs/                        # Artifact, contribution, and branch-protection guidance
├── scripts/                     # Validation and maintenance tooling
├── data/                        # Structured manifests, snapshots, research records, and outcomes
├── research_logs/               # Live scanner dry runs and research reports
├── state/                       # Persistent universe, thesis, and rejection memory
└── backtests/                   # Monthly reviews and archived universes
```

---

## Operating Modes

### Mode 1 — Research Only

The agent scans, ranks, and reports. No trade proposals.

### Mode 2 — Proposal Only

The agent may produce trade proposals but cannot submit orders.

### Mode 3 — Confirm-Before-Trade

The agent may prepare orders but must receive explicit approval before submission.

### Mode 4 — Autonomous Execution

Not enabled by default. Requires proven performance, stable logs, clean rule compliance, and explicit user approval.

---

## Version 2.0 Status

Version 2.0 is the current source of truth.

The system is now an **options-primary tactical pipeline**:

- Robinhood saved scanners discover candidates.
- `pipeline_config.md` defines which scanners run and how results are routed.
- `scanner_engine.md` defines scanner behavior and guardrails.
- `research_agent.md` scores and validates underlyings, direction, and options suitability.
- `options_strategy.md` scores and ranks contracts separately from the underlying thesis.
- `portfolio_manager_agent.md` applies account, premium-risk, correlation, and exact-order constraints.
- `system_prompt.md` remains the master behavior file.
- `tool_policy.md` maps the expanded Robinhood tool surface to permissions and safe call sequences.
- Universe membership is separate from temporary entry eligibility.
- Universe refreshes require a run manifest, at least 90% terminal coverage, and complete critical data for Tier 1 and Tier 2.
- Structured templates preserve raw scanner rows, underlying research, options setup records, shadow options trades, and forward outcomes.

The **Current Universe** remains the Approved Underlying Universe. It governs which equities are high enough quality to serve as option underlyings.

Options remain proposal-only / shadow-trading by default and are not autonomous.

Live dry-run reports should be stored in `research_logs/` and should follow `templates/daily_research_log.md` when possible. Backtests and month-end historical reviews should remain in `backtests/`. Persistent machine-readable memory should live in `state/`.

---

## Repository Safety

This repository is private by default. Review `PRIVATE_DATA.md` before sharing it or changing repository visibility.

Run validation before pushing:

```bash
make validate
```

If Apple command-line developer tools are not installed, run the validator directly:

```bash
python3 scripts/validate_repo.py
```

Useful maintenance targets:

```bash
make status
make scan-sensitive
make daily-log DATE=2026-08-06
make analyze-outcomes
make validation-report MONTH=2026-08
```

Generated research artifacts are currently tracked for reproducibility. The policy for what should remain tracked lives in `docs/ARTIFACT_POLICY.md`.

Scheduled daily, weekly, and monthly scan behavior is documented in `docs/SCHEDULED_SCANS.md`.

---

## Roadmap

### v1.9

- Validation release: shadow portfolio, signal outcome tracking, score-bucket performance, scanner-source alpha, and rule opportunity-cost analysis
- Market regime scoring with VIX, breadth, trend, and sector participation components
- Correlation-cluster checks before serious funding
- Monthly answer to: "If we had followed this agent for the last 30/60/90 days exactly as written, what would have happened?"

### v2.0

- Tactical options pivot
- Long calls and long puts only at launch
- Separate Underlying Thesis Score and Options Setup Score
- Options setup, shadow-trade, and outcome records
- Account fit separated from setup quality

### v2.1

- Call debit spreads and put debit spreads, after validation
- Sector rotation model
- Correlation model
- Sector exposure optimizer
- Automated research logs
- Automated trade logs
- Monthly universe refresh automation
