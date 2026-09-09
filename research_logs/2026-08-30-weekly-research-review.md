# Weekly Research Review - 2026-08-30

Automation: Robinhood Agent Weekly Options Research Review  
Mode: Research-only / proposal-only / shadow-trading  
Review window: 2026-08-24 through 2026-08-30, using available daily scanner artifacts from 2026-08-24, 2026-08-25, 2026-08-26, and 2026-08-28.  
Source path note: source-of-truth policy, strategy, state, validation, and backtests were read from `/Users/quinowens/Desktop/Robinhood-Agent`. The active automation workspace `/Users/quinowens/Desktop/Robinhood-Agent-v1.6` contains this week's spillover logs/data but not the required policy/state files.

## Executive Summary

Decision: NO LIVE TRADE. No `PM_PROPOSAL` was produced, no exact order review was run, and no live order was placed, modified, or canceled.

This week's best options-primary evidence remained long-call only. Several large, liquid contracts reached account-fit failure or watch status, but none became a properly persisted canonical `SHADOW_ONLY_QUALIFIED` shadow trade for this review window. The strongest log-supported candidates were:

| Date | Underlying | Contract | DTE | Bid / Ask / Mid or Mark | Setup Score | Account Fit | Weekly Treatment |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-08-24 | GOOGL | 2026-10-16 350C | 53 | 15.75 / 16.00 / 15.875 | 82 | FAIL | Log-supported shadow-qualified setup, but missing structured setup/shadow/outcome artifacts. |
| 2026-08-26 | MSFT | 2026-10-16 500C | 51 | 18.20 / 19.00 / 18.60 | 72 | FAIL | Structured setup record exists as `QUALIFIED_BUT_NOT_ACCOUNT_FIT`; no shadow trade was opened. |
| 2026-08-28 | AMZN | 2026-10-16 270C | 49 | mark 10.70 / ask 10.80 | 72 | FAIL | Log-only account-fit failure; no structured shadow record. |
| 2026-08-28 | MSFT | 2026-10-16 520C | 49 | mark 17.18 / ask 17.65 | 70 | FAIL | Log-only account-fit failure; no structured shadow record. |
| 2026-08-28 | AAPL | 2026-10-16 320C | 49 | mark 11.98 / ask 12.20 | 68 | FAIL | Log-only account-fit failure; AAPL is not Current Universe Tier 2. |
| 2026-08-28 | DKNG | 2026-10-16 27.5C | 49 | mark 1.11 / ask 1.17 | 55 | FAIL | Watch only; best contract exceeded buying power. |
| 2026-08-28 | DKNG | 2026-10-16 30C | 49 | mark 0.53 / ask 0.61 | 38 | PASS by affordability | Rejected as a cheap low-delta substitution. |

The weekly Portfolio Manager conclusion is unchanged: the Agentic account remains a $100 validation account. High-quality one-contract long calls on approved large-cap underlyings require roughly $1,080 to $1,900+ of premium this week, so account fit failed without using prohibited affordability substitutions.

## Weekly Run Health

Available daily run set:

| Date | Run ID | Status | Scanner Calls | Options Steps | Health Notes |
| --- | --- | --- | ---: | --- | --- |
| 2026-08-24 | `2026-08-24-daily-scanner-dry-run` | Degraded | 3/3 | GOOGL chain/quote/contract scoring completed in log | Missing structured setup, shadow trade, outcome, and manifest in spillover data. |
| 2026-08-25 | `2026-08-25-daily-scanner-dry-run` | Degraded | 3/3 | MSFT chain/instrument lookup only | Correctly stopped before setup qualification because option quote snapshot was missing. |
| 2026-08-26 | `2026-08-26-daily-scanner-dry-run` | Degraded | 3/3 | MSFT chain/quotes completed | One structured options setup record exists; no `SHADOW_ONLY_QUALIFIED` shadow trade was created. |
| 2026-08-28 | `2026-08-28-daily-scanner-dry-run-153353-cdt` | Degraded | 3/3 | AMZN/MSFT/AAPL/DKNG option quotes reviewed in log | No PM proposal, no shadow trade, no order review. |

Missing daily scanner reports for this latest full review window: 2026-08-27, 2026-08-29, and 2026-08-30. The last two dates were weekend dates, but the absence should still be noted because the automation requested a full weekly consolidation.

Run health summary:

| Area | Weekly Result |
| --- | --- |
| Scanner resolution | All recorded manifests/logs show the three configured scanners matched expected names/IDs. |
| Scanner execution | Successful in available runs; no failed scanner calls observed. |
| Account preflight | Complete in daily logs/manifests: Agentic account ending 8691, $100 account value/cash/buying power, no equity positions, no option positions, no open option orders. |
| Tool coverage | Account, portfolio, scanner, quote, tradability, fundamentals, financials, earnings, historicals, indexes, selected option chains/instruments/quotes were available across the week. |
| Missing fields | Full scanner row exports remained unavailable; RUT was restricted and DJI often unresolved; no direct breadth tool; Aug 25 missing option quote; Aug 24 missing structured option artifacts. |
| v2.0 options steps | Correctly progressive. Chains were skipped when no candidate passed direction/suitability. Aug 25 correctly stopped for missing quotes. Aug 24 should have produced structured shadow artifacts but only the daily log was found. |
| Order tools | No `review_option_order`, `place_option_order`, replacement, cancellation, scan write, or watchlist write was recorded. |

## Market / Benchmark Context

Available daily logs described a non-hostile, selective market backdrop. VIX stayed low-to-moderate in the recorded snapshots: 15.45 on Aug 25, 15.21 on Aug 26, and 14.43 on Aug 28. SPX and NDX were constructive enough for selective bullish research, but not enough to override candidate-specific earnings blocks, trend weakness, or account risk.

| Date | SPX | NDX | VIX | Interpretation |
| --- | ---: | ---: | ---: | --- |
| 2026-08-24 | 7652.86 | 29023.18 | N/A | Broad context not hostile; GOOGL was the only clean Tier 2 finalist. |
| 2026-08-25 | 7677.28 | 29209.23 | 15.45 | Constructive enough for selective bullish research; MSFT quotes missing. |
| 2026-08-26 | 7675.70 | 29224.52 | 15.21 | Neutral-to-constructive; same-day earnings dominated blockers. |
| 2026-08-28 | 7711.76 | 29433.43 | 14.43 | Constructive backdrop; account fit and earnings/event risk controlled decisions. |

Material 2026-08-28 scanner/quote context from daily artifacts: AMZN 266.21, MSFT 513.02, AAPL 319.70, GOOGL 346.06, DKNG 25.28. These values are research snapshots, not executable quotes for any future action.

## Scanner Review

| Scanner | Weekly Role | Recorded Matches | Quality Read |
| --- | --- | --- | --- |
| Momentum Candidates | Underlying movement discovery | 399 on Aug 24, 398 on Aug 25, 399 on Aug 26, 399 on Aug 28 | Useful for finding large-cap movement in GOOGL, MSFT, AMZN, AAPL, DKNG, NOW, WDAY, CRWD, PANW, and event names. It remained broad and was not treated as direction by itself. |
| Options Activity Radar | Options context only | 192 on Aug 24, 137 on Aug 25, 109 on Aug 26, 100 on Aug 28 | Useful lower in the list for AMZN/MSFT/AAPL/DKNG/GOOGL/NVDA/META context, but top rows were frequently microcap, penny-stock, or high-IV rejects. |
| Earnings Risk Radar | Event-risk confirmation | 334 on Aug 24, 334 on Aug 25, 337 on Aug 26, 334 on Aug 28 | Valuable as blocker confirmation for NVDA, CRWD, PANW, AVGO, WDAY, CRM, MRVL, AFRM, LULU, and other event names. Direct earnings evidence remained primary. |

Scanner frequency was not treated as bullish or bearish evidence. Options Activity Radar was used only as context and never as direction.

## Underlying Queue

| Priority | Symbol | Weekly Evidence | Decision / Next Action |
| ---: | --- | --- | --- |
| 1 | MSFT | Tier 2; Aug 25 and Aug 26 strongest approved-name options path; Aug 26 500C had acceptable liquidity/delta but failed account fit. | Research queue lead. Recheck trend/RS and quote quality; no live proposal unless account fit changes. |
| 2 | AMZN | Tier 2; recovered into Aug 28 momentum/options overlap; Aug 28 270C was high-quality enough for account-fit review but unaffordable. | Watch for persistent trend recovery; track prior AMZN 2026-10-16 265C shadow outcome from Aug 19. |
| 3 | GOOGL | Tier 2; Aug 24 350C scored 82 and failed account fit; later weakened/no fresh edge. | Needs structured artifact backfill only if repo policy authorizes repair; fresh options research only on renewed direction. |
| 4 | NVDA | Tier 2; recurring options context, but Aug 24-26 earnings block and Aug 28 post-earnings weakness/no directional edge. | Post-earnings review after complete trading session; failed bullish setup is not bearish evidence. |
| 5 | CRWD | Tier 2; same 2026-08-26 PM earnings block dominated. | Post-earnings review before any new option research. |
| 6 | PANW | Tier 2; recurring earnings risk, verified 2026-09-01 PM report. | Keep temporarily blocked through earnings window. |
| 7 | AVGO | Tier 2; options activity plus verified 2026-09-02 PM report. | Keep temporarily blocked through earnings window. |
| 8 | META | Tier 2; post-earnings confidence penalty and choppy trend; no clean fresh setup. | Watch only until structure improves. |
| 9 | AAPL | Strong Aug 28 setup context, but not Current Universe Tier 2. | No proposal without provisional Tier 2 evidence or explicit one-off approval. |
| 10 | DKNG | Momentum/options overlap and affordable alternative existed, but best contract exceeded buying power and cheaper 30C was low-delta substitution. | Watch only; do not force cheap contract. |
| 11 | HOOD / SMCI / AMD / NOW / WDAY / CRM / MRVL / AFRM / LULU | Recurring scanner names or event movers. | Require complete provisional Tier 2 path, and event names need post-earnings review. |

## Directional Thesis Review

Bullish thesis candidates:

| Symbol | Directional Classification | Confidence Read | Weekly Decision |
| --- | --- | --- | --- |
| GOOGL | Bullish on Aug 24, then neutral/no fresh edge later | Moderate on Aug 24 only | Log-supported options research; artifact gap prevents canonical shadow classification for weekly analytics. |
| MSFT | Bullish on Aug 25/26/28 | Moderate | Contract evidence existed on Aug 26/28, but account fit failed and no PM proposal was appropriate. |
| AMZN | Neutral/weak early, bullish by Aug 28 | Moderate-low to moderate | Account fit failed on Aug 28; prior Aug 19 canonical shadow remains the cleanest AMZN record. |
| AAPL | Bullish context on Aug 28 | Lower confidence for this repo because not Current Universe Tier 2 | No Current Universe/provisional eligibility for a repo-quality proposal. |
| DKNG | Bullish scanner context | Low | Watch/reject due contract quality and affordability-substitution guardrail. |

Neutral or unsupported: NVDA after earnings, GOOGL on Aug 25/26, AMZN on Aug 26, META through the week, WDAY/CRM/MRVL/AFRM around earnings. No bearish thesis reached options proposal quality. The workflow correctly avoided converting failed bullish evidence into long puts.

## Options Setup Review

Serious selected contract evidence:

| Underlying | Contract | Type | DTE Bucket | Delta | Spread / Liquidity | Premium / Breakeven | Score | Completeness / Confidence |
| --- | --- | --- | --- | ---: | --- | --- | ---: | --- |
| GOOGL | 2026-10-16 350C | Long call | 46-60 | 0.523 | 1.57% spread; OI 3,576; vol 491 | mid $15.875, about $1,587.50; breakeven not persisted in structured data | 82 | Log complete enough, but missing structured setup/shadow/outcome artifacts. |
| MSFT | 2026-10-16 500C | Long call | 46-60 | 0.509 | 4.30% spread to mark; OI 23,355; vol 604 | ask $19.00, mark $18.60; breakeven $518.60 | 72 | High / medium in daily record. |
| AMZN | 2026-10-16 270C | Long call | 46-60 | 0.492 | OI 14,274; vol 9,844 | mark $10.70, ask $10.80 | 72 | 0.82 / 0.64 in daily log. |
| MSFT | 2026-10-16 520C | Long call | 46-60 | 0.487 | OI 7,463; vol 861 | mark $17.18, ask $17.65 | 70 | 0.82 / 0.62 in daily log. |
| AAPL | 2026-10-16 320C | Long call | 46-60 | 0.536 | OI 11,820; vol 3,380 | mark $11.98, ask $12.20 | 68 | 0.82 / 0.58 in daily log. |
| DKNG | 2026-10-16 27.5C | Long call | 46-60 | 0.372 | OI 379; vol 294 | mark $1.11, ask $1.17 | 55 | 0.76 / 0.43 in daily log. |
| DKNG | 2026-10-16 30C | Long call | 46-60 | 0.214 | OI 1,093; vol 2,293 | mark $0.53, ask $0.61 | 38 | Rejected low-delta affordability substitute. |

All option structures stayed inside v2.0 launch scope: single-leg long calls only. No puts qualified this week. No 0DTE, option selling, cash-secured puts, covered calls, spreads, or margin-driven structures appeared.

## Account-Fit / Shadow-Only Review

The account-fit result was decisive:

| Account Field | Weekly State |
| --- | --- |
| Account ending | 8691 |
| Account type | Cash |
| Broker options level | Level 2 / option_level_2 |
| Strategy-enabled options | `LONG_CALL`, `LONG_PUT` only |
| Account value | $100 |
| Cash / buying power / option buying power | $100 / $100 / $100 |
| Equity positions | 0 |
| Option positions | 0 |
| Open option orders | 0 |

Qualified or near-qualified large-cap contracts exceeded the account by a large margin:

| Setup | One-Contract Premium Basis | Account-Fit Result |
| --- | ---: | --- |
| GOOGL 350C | about $1,587.50 midpoint | FAIL |
| MSFT 500C | about $1,900 ask | FAIL |
| AMZN 270C | about $1,080 ask | FAIL |
| MSFT 520C | about $1,765 ask | FAIL |
| AAPL 320C | about $1,220 ask | FAIL |

The account fit failure must not be solved by selecting lower-quality contracts. The DKNG 30C was affordable but rejected because it was a low-delta affordability substitute, not the best expression of the thesis.

Weekly shadow-accounting conclusion: there were log-supported account-fit failures, but no new canonical `data/option_shadow_trades/` record was found for Aug 24-30. Aug 24 GOOGL is the strongest candidate for a future artifact repair pass because the daily report explicitly named `option_setup_id`, `option_shadow_trade_id`, and the selected instrument ID, but this weekly review does not backfill state or shadow files without explicit repository authorization.

## Options Outcome Review

No new canonical option shadow trade was opened this week, so no new matured Aug 24-30 shadow outcomes exist.

Prior canonical shadow records from earlier August remain the relevant outcome set:

| Signal | Latest Available Outcome Snapshot |
| --- | --- |
| NVDA 2026-09-18 230C from 2026-08-07 | 1D option -32.99%, 5D option -12.53%, 10D option -58.06%; 10D underlying -4.36%. |
| META 2026-09-18 610C from 2026-08-11 | 1D option -47.26%, 5D option -82.22%; 5D underlying -9.26%. |
| NVDA 2026-09-18 220C from 2026-08-11 | 1D option +26.79%, 5D option -5.58%; 5D underlying +1.03%. |
| NVDA 2026-09-18 225C from 2026-08-12 | 1D option +10.22%, 5D option -33.17%; 5D underlying -2.64%. |
| META 2026-10-16 600C from 2026-08-13 | 1D option -3.01%, 5D option -54.58%; 5D underlying -7.31%. |
| AMZN 2026-10-16 265C from 2026-08-19 | 1D option -21.21%; 1D underlying -2.33%; later horizons not yet mature in the read snapshot. |

Outcome interpretation: early long-call shadow evidence is weak-to-negative for premium performance, especially in META and post-signal NVDA, but mature 20D/30D samples are not available. Classifications remain pending or insufficient; do not recalibrate rules from this small, incomplete sample.

Call vs put result: current canonical sample is all calls. No put performance conclusion is available.  
DTE result: observed setups are mainly 30-45 and 46-60 DTE. Samples are too small.  
Delta result: most canonical qualified setups clustered near 0.46-0.55 delta; the affordable DKNG 0.214-delta substitute was correctly rejected.  
Spread/liquidity result: liquidity quality was generally acceptable for mega-cap contracts; account size, not spreads, was the decisive live blocker.

## Current Universe Review

Current Universe remains populated by the 2026-08-03 official broad catch-up refresh. No weekly evidence authorizes rewriting `state/current_universe.json`.

| Bucket | Names | Weekly Implication |
| --- | --- | --- |
| Tier 1 | None | Still empty; no evidence justifies lowering the 85+ threshold. |
| Tier 2, strengthening/watch | MSFT, AMZN, GOOGL | Produced the main options research candidates, but account fit failed and/or direction was not persistent. |
| Tier 2, event/post-event caution | NVDA, CRWD, PANW, AVGO | Earnings risk dominated. NVDA also needed post-earnings reassessment after Aug 28 weakness. |
| Tier 2, weaker trend | META | Post-earnings confidence penalty and choppy structure kept it watch-only. |
| Watchlist / provisional candidates | AMD, NOW, HOOD, SMCI, DKNG, WDAY, CRM, MRVL, AFRM, LULU | Need complete provisional Tier 2 evidence and clean event timing before option-chain escalation. |
| Permanent/noisy rejects | FNGR, IGC, RFL, INVZ, CMCM, KZIA, LYEL, LX, BNC, KROS, CRDL, NMG, FLD, IMMP, YQ | Options Activity high-IV top tail remains mostly low-quality scanner noise. |

No monthly refresh action was performed. A normal month-end refresh can consider whether MSFT/AMZN/GOOGL remain Tier 2 leaders and whether watchlist scanner repeats deserve full scoring, but this weekly review should not rewrite universe membership.

## Primary Blocking-Rule Analysis

Structured and log-supported primary blocks, counted by decisive layer:

Underlying / research layer:

| Primary Rule Group | Observed Count | Representative Symbols | Interpretation |
| --- | ---: | --- | --- |
| Earnings or post-earnings block | 20 | NVDA, CRWD, PANW, AVGO, OKTA, CRM, NTNX, MRVL, ADSK, WDAY, AFRM, DELL, SNOW, GAP, LULU | Earnings Risk Radar did its job; direct earnings/event checks controlled final decisions. |
| Permanent microcap/penny/high-IV reject | 7+ | FNGR, IGC, CRDL, NMG, FLD, IMMP, YQ | Options Activity top rows remain noisy and should be filtered before expensive enrichment. |
| No fresh directional edge / weak tape | 3+ | GOOGL, AMZN, NVDA | Neutral or failed bullish evidence correctly stopped option proposals. |
| Outside Current Universe / no provisional promotion | 4+ | ANET, TTMI, SMTC, AAPL, HOOD, SMCI, AMD, DKNG | Scanner strength did not bypass universe governance. |
| Post-earnings confidence or trend penalty | 2+ | META, SMTC | Repair mode/watch classification was appropriate. |

Options / Portfolio Manager layer:

| Primary Rule Group | Observed Count | Representative Setups | Interpretation |
| --- | ---: | --- | --- |
| Account premium risk exceeds cap | 4 log/structured selected setups | GOOGL 350C, MSFT 500C, AMZN 270C, MSFT 520C, AAPL 320C | High-quality long calls are not compatible with the $100 account. |
| Missing option quote snapshot | 1 | MSFT on 2026-08-25 | Correctly prevented setup scoring/shadow freeze. |
| Weak setup / affordability substitution | 2 | DKNG 27.5C / 30C | Best contract was unaffordable; cheaper low-delta contract was correctly rejected. |
| Options Suitability Gate not passed | Multiple no-chain candidates | Aug 25/26/28 non-finalists | Progressive option-chain guardrail generally worked. |

Secondary blocks were retained as context only and not double-counted.

## Score And Options Threshold Calibration

Official Current Universe score distribution from `state/current_universe.json`:

| Metric | Underlying Thesis Score |
| --- | ---: |
| Count | 8 Tier 2 names |
| Highest | 82 |
| Median | 79 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 75 | 8 |
| Count >= 85 | 0 |

Aug 28 daily compatibility scores, which were explicitly non-canonical because source scoring files were absent from the spillover workspace:

| Metric | Score |
| --- | ---: |
| Count | 13 |
| Highest | 74 |
| Median | 51 |
| 90th percentile | 73 |
| 95th percentile | 74 |
| Count >= 65 | 3 |
| Count >= 75 | 0 |
| Count >= 85 | 0 |

Selected options setup-score distribution for this week, using log/structured selected contracts only:

| Metric | Options Setup Score |
| --- | ---: |
| Count | 7 |
| Highest | 82 |
| Median | 70 |
| 90th percentile | 82 |
| 95th percentile | 82 |
| Count >= 70 | 4 |
| Count >= 75 | 1 |
| Count >= 80 | 1 |

Calibration observation: the official Tier 1 threshold remains unreachable in August evidence, but this is still a small and immature sample with no complete 20D/30D options outcome set. Do not change Underlying Thesis Score or Options Setup Score thresholds from this weekly review.

## State Decisions

- `state/current_universe.json`: unchanged.
- `state/open_theses.json`: unchanged; no open theses were present.
- `state/rejected_candidates.json`: unchanged; recurring microcap rejects were recognized but not added from this degraded weekly pass.
- No `research_logs/YYYY-MM-DD-research-agent-candidate-review.md` was created because this run consolidated existing daily artifacts rather than performing a new full candidate scoring pass.
- No option shadow-trade backfill was written. The Aug 24 GOOGL artifact gap should be handled as a separate repair task if authorized.

## Next Research Actions

1. Repair or explicitly mark the Aug 24 GOOGL 2026-10-16 350C artifact gap: the daily log says it should have setup, shadow, and outcome records, but no matching structured files were found.
2. Continue outcome tracking for prior canonical NVDA, META, and AMZN shadow records at 10D/20D/30D horizons.
3. Recheck MSFT and AMZN early next week if momentum persists; both are research leaders but remain account-fit failures at current account size.
4. Keep PANW and AVGO blocked through their verified Sep 1 and Sep 2 earnings windows. Review only after a complete post-event session.
5. Reassess NVDA and CRWD post-earnings; do not treat options activity or failed bullish price action as independent bearish evidence.
6. Evaluate AAPL, DKNG, HOOD, SMCI, AMD, NOW, WDAY, CRM, MRVL, AFRM, and LULU only through the provisional Tier 2 path before any options proposal.

## Execution Statement

No live orders were placed, modified, or canceled. Any options proposal is hypothetical and requires exact reviewed-order user approval before live execution.
