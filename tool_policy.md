# Robinhood Tool Policy — Version 1.8

This file maps Robinhood's available Agentic Trading tools to the safest, most useful workflow for this project. Tool output is evidence, not permission to trade.

## Read-Only Tools

Read-only calls may be made without additional approval when they are relevant to the user's request or an active research run.

| Workflow | Tools | Required use |
| --- | --- | --- |
| Account preflight | `get_accounts`, `get_portfolio`, `get_equity_positions`, `get_equity_orders`, `get_option_positions`, `get_option_orders` | Establish account, buying power, positions, and pending exposure before portfolio decisions. |
| Performance and risk | `get_realized_pnl`, `get_pnl_trade_history`, `get_equity_tax_lots` | Measure drawdown and realized outcomes; inspect lots before proposing a sale. Tax lots inform the proposal but do not constitute tax advice. |
| Discovery | `get_scans`, `get_scanner_filter_specs`, `run_scan`, `search`, `get_popular_watchlists` | Resolve saved scans dynamically and discover candidates. Popular lists are leads only. |
| Equity research | `get_equity_fundamentals`, `get_financials`, `get_equity_historicals`, `get_equity_quotes`, `get_equity_tradability` | Validate quality, price, liquidity, trend, and eligibility. |
| Market context | `get_indexes`, `get_index_quotes`, `get_equity_technical_indicators` | Check index regime and independently verify computed indicators against raw history when decisions depend on them. |
| Event risk | `get_earnings_results`, `get_earnings_calendar` | Replace inferred or scanner-only earnings dates with direct event data. |
| Execution quality | `get_equity_price_book` | Optional for timing and spread/depth checks; never use Level 2 alone as a directional signal. Maximum 4 stocks per call. |
| Options research | `get_option_level_upgrade_info`, `get_option_chains`, `get_option_instruments`, `get_option_quotes`, `get_option_historicals` | Use only under `options_strategy.md`; access links do not authorize options trading. |
| Watchlist reads | `get_watchlists`, `get_watchlist_items`, `get_option_watchlist` | Organizational context only; watchlist membership never grants universe or trade eligibility. |

Use `get_equity_quotes` in batches of no more than 20 symbols and `get_equity_price_book` in batches of no more than 4 symbols. Prefer batched calls where supported, but do not request data that the workflow will not use.

## Account Writes

The following mutate Robinhood state and require the user's explicit approval of the target and intended change:

- `create_watchlist`, `update_watchlist`, `follow_watchlist`, `unfollow_watchlist`
- `add_to_watchlist`, `remove_from_watchlist`
- `add_option_to_watchlist`, `remove_option_from_watchlist`
- `create_scan`, `update_scan_filters`, `update_scan_config`

Approval to create or change one watchlist or scan does not grant standing permission for later changes. Before changing a scan, call `get_scanner_filter_specs`, show the proposed filters and sorting, and identify the saved scan to be changed.

## Order Actions

`review_equity_order` and `review_option_order` are simulations and must precede any corresponding live order. Display all warnings and the exact reviewed payload. A review does not authorize placement.

`place_equity_order` and `place_option_order` are live financial actions. They require the operating mode and exact-order approval required by `system_prompt.md`. Never silently alter symbol, side, quantity, order type, limit price, time in force, option contract, or position effect after approval; material changes require a new review and approval.

`cancel_equity_order` and `cancel_option_order` also change account state. Confirm the exact open order and obtain explicit user approval unless the user has already issued a clear cancellation instruction identifying it.

After a placement or cancellation attempt, query order history and report the actual status. Never infer that an order filled or was canceled from the submission response alone.

## Failure and Freshness Rules

- Record tool name, timestamp, symbols or resource IDs, success/failure, and retry count in the run manifest.
- Do not fabricate a replacement for missing tool output.
- Retry transient read failures conservatively; do not automatically retry a live order submission when its outcome is ambiguous. Query order history first.
- Quotes, books, buying power, positions, open orders, and order reviews must be refreshed immediately before an approved live action.
- Historical, fundamental, financial, technical, and earnings inputs must record their as-of time or reporting period.
- Conflicting data lowers completeness and confidence. A conflict affecting eligibility, sizing, earnings risk, or order terms means `NO TRADE` until resolved.
