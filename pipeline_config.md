# Pipeline Config

## Purpose

This file defines the active dynamic research pipeline. It is the operational map the agent should follow when running daily market discovery.

---

## Pipeline Version

- **Version:** 2.0
- **Mode:** Research-only / Proposal-only
- **Primary Asset:** Tactical long options
- **Underlyings:** Equity Current Universe / provisional Tier 2
- **Options:** Long calls and long puts only at launch; no autonomous execution

---

## Active Scanners

```yaml
scanners:
  - name: Momentum Candidates
    scan_id: 26cdeb14-da13-493f-b0c6-783468971a16
    role: primary_underlying_movement_discovery
    run_frequency: daily
    priority: high

  - name: Options Activity Radar
    scan_id: 7068db65-2a47-470c-bde9-94d66f36b806
    role: options_context_and_attention_signal
    run_frequency: daily
    priority: medium
    mode: research_only

  - name: Earnings Risk Radar
    scan_id: 737924f1-e94f-4ad4-ba98-6c12fcaafaa9
    role: risk_filter
    run_frequency: daily
    priority: high
```

---

## Pipeline Steps

```yaml
steps:
  - run_preflight_checks
  - create_run_manifest
  - read_account_state
  - read_positions_and_open_orders
  - read_realized_pnl_and_trade_history
  - build_broad_seed_universe
  - list_and_resolve_saved_scans
  - run_active_scanners
  - persist_raw_scanner_snapshots
  - normalize_results
  - deduplicate_symbols
  - tag_scanner_sources
  - apply_permanent_membership_filters
  - pull_fundamentals
  - pull_reported_financials
  - pull_quotes
  - verify_tradability
  - pull_historicals
  - pull_earnings_results_and_calendar
  - pull_index_context
  - validate_trend
  - calculate_component_scores
  - normalize_scores_across_population
  - score_candidates
  - assign_tiers
  - apply_temporary_entry_blocks
  - classify_directional_thesis
  - evaluate_options_suitability
  - pull_option_chains_for_qualified_finalists
  - filter_option_expirations
  - pull_option_instruments
  - filter_option_contracts
  - pull_option_quotes
  - pull_option_historicals_when_needed
  - rank_option_contracts
  - calculate_options_setup_score
  - validate_options_completeness
  - evaluate_account_fit
  - validate_run_completeness
  - publish_or_mark_degraded
  - send_option_setup_to_portfolio_manager
  - refresh_account_state
  - review_exact_order_if_requested
  - produce_proposal_report
  - record_option_setup_record
  - record_option_shadow_trade_when_qualified
  - record_unaffordable_qualified_setup_in_options_shadow_portfolio
  - schedule_forward_outcome_tracking_for_all_terminal_candidates
  - schedule_option_outcome_tracking
```

Same-day reruns, repairs, and schema backfills must not create new independent observations. Every options setup, option shadow trade, and option signal outcome must persist `signal_group_id`, `supersedes_setup_id`, and `is_canonical`. Analytics must use only canonical records; non-canonical repair/rerun rows may remain for audit but must not affect win rates, average returns, funding requirements, or conversion statistics.

---

## Candidate Status Values

```yaml
statuses:
  - rejected
  - watch_only
  - research_further
  - portfolio_review
  - proposal_candidate
  - provisional_tier_2
  - options_research
  - stock_thesis_only
  - no_directional_edge
  - pm_proposal
  - shadow_only_qualified
  - blocked_by_earnings
  - blocked_by_risk
```

---

## Default Eligibility Rules

### Permanent Membership Rejection Filters

Reject before scoring when any of these are true:

- OTC security
- Penny stock or low-quality microcap
- Not active or not regular-hours tradable
- Leveraged or inverse ETF
- Structurally insufficient liquidity for safe entry/exit
- Unresolved critical data quality issue

### Temporary Entry Blocks

Retain an otherwise qualified candidate in its assigned tier, but mark it ineligible for a new entry when any of these are true:

- Earnings inside the five-trading-day blackout window
- Extreme one-day move without follow-through
- Weak or defensive market regime
- Temporary trend damage
- Portfolio risk, concentration, or buying-power constraint

Every block must include `eligibility`, `blocked_reason`, `primary_blocking_rule`, and `eligible_after` or `next_review_date`. Secondary applicable blocks belong in `secondary_blocking_rules`. A temporary block must not erase a high-quality candidate from the Current Universe.

### Scoring / Penalty Filters

Apply penalties instead of automatic rejection for:

- Market cap below $10B
- Volume below 2M shares
- Below 200-day SMA
- Weak relative strength versus `SPY`
- Missing or incomplete fundamentals
- Extreme one-day move without follow-through

### Run Completeness Gate

The pipeline must not publish a refresh as complete unless:

- A run manifest exists.
- At least 90% of the deduplicated seed universe has a terminal result: scored, permanently rejected, or explicitly incomplete.
- All Tier 1 and Tier 2 candidates have verified tradability, price, liquidity, earnings date, and historical trend data.
- `SPY` and `QQQ` benchmark histories are available for the scoring dates.
- Failed calls, retries, and missing fields are recorded.

If any requirement fails, preserve collected records, set the manifest status to `degraded` or `failed`, and do not overwrite the last valid Current Universe.

### Universe Constraint

Scanner candidates remain research candidates until validated. When the Current Universe is officially populated, a daily scanner candidate may become `provisional_tier_2` until the next monthly refresh if it meets Tier 2 standards, has complete critical data, and has no active temporary block. Outside-universe names below those standards require explicit user approval before any one-off review.

### Options Data Constraint

Do not retrieve option chains for every scanner hit. Option-chain work begins only after the underlying passes permanent filters, has enough data to classify a directional thesis, and passes the Options Suitability Gate.

---

## Output Requirement

Every pipeline run must produce:

1. Market context.
2. Scanner summary.
3. Top candidates.
4. Rejected / blocked reasons.
5. Portfolio Manager action recommendation.
6. Clear statement of whether any real order is being proposed.
7. A structured run manifest and run-health summary.
8. Raw scanner snapshots and structured research records.
9. A completeness percentage and publish/degrade decision.
10. Forward outcome tracking records for every terminal candidate, including NO TRADE, blocked, rejected, Watchlist, and proposal candidates.
11. Primary blocking-rule attribution for every blocked, rejected, Watchlist, or NO TRADE candidate.
12. Options setup records, option shadow trades, and option outcome tracking when an underlying reaches options research.

Daily dry-run reports should follow `templates/daily_research_log.md` when possible and should be saved to `research_logs/YYYY-MM-DD-description.md`.

Daily option research should evaluate up to `shadow_options_research_top_n: 3` qualified finalists before stopping for account-fit failures. Keep `shadow_research_limit`, `live_proposal_limit`, and `live_position_limit` separate.

`WATCH` and `SHADOW_ONLY_QUALIFIED` are intentionally different:

- `WATCH` means the underlying, timing, direction, or option setup is not currently qualified.
- `SHADOW_ONLY_QUALIFIED` means the underlying and selected option setup are good enough that the Portfolio Manager would take the setup if account/risk constraints allowed it.

Every `SHADOW_ONLY_QUALIFIED` setup must be added to the dedicated Options Shadow Portfolio, not to a normal watchlist. The record must freeze the exact setup selected at decision time: underlying, direction, option instrument ID when available, expiration, strike, type, side, position effect, DTE, bid, ask, midpoint/mark, delta, IV, open interest, volume, breakeven, underlying price, option setup score, account snapshot, account-fit failure reasons, premium risk, and planned exit/stop/target rules. Do not later replace that frozen contract with a cheaper, farther-OTM, shorter-DTE, or hindsight-improved contract.

Default live-execution output is **NO TRADE** unless a candidate passes underlying research, options suitability, contract scoring, account-fit review, exact reviewed-order review, and exact user approval. Research output is separate: a setup that qualifies but fails account fit is `SHADOW_ONLY_QUALIFIED` and is not forced into a lower-quality contract.

Required account-dependent records must include `account_snapshot_id`, `account_snapshot_as_of`, `setup_quality_status`, `account_fit_status`, and `final_decision`. Material account-state changes during a run invalidate downstream account-fit decisions and require recomputation from the newest account snapshot.

For each `SHADOW_ONLY_QUALIFIED` setup, schedule option outcome tracking for 1, 5, 10, 20, and 30 trading days. Tracking must preserve option premium return, underlying return, excess return versus `SPY` and `QQQ`, maximum favorable and adverse excursion for option and underlying, whether the planned premium stop would have triggered, whether the target would have hit, whether the underlying thesis stayed valid, whether the option expired worthless, and whether the underlying thesis was right but contract selection was poor.

Run manifests must include UTC lifecycle fields `started_at`, `first_tool_call_at`, `last_tool_call_at`, and `completed_at`. `completed_at` must be null while status is `RUNNING`, then set after outputs and validation finish. Manifests must also record `run_trigger`, `session_context`, and `intended_workflow`.
