# Strategy Research Lab — prospective protocol 1

Production remains v2.0.2, retaining the v2.0.1 selection rules and >=75 qualification gate. This lab is an independent research protocol, not a v2.1 trading release. No scanner changes, additional trade frequency, account-size substitutions, spreads, 0DTE, crypto, short premium, or automatic execution. Existing historical trades are not enrolled retroactively. Never relabel lab results as canonical strategy performance.

## Entry protocol

For every newly qualified canonical directional setup, including account-fit failures, collect the candidate quotes in the same regular-session signal window. Freeze before observing any forward prices. A setup marked WATCH does not qualify. Reference its setup ID and signal-group ID; one experiment per signal group. Keep the canonical setup and shadow unchanged.

| Arm | Frozen expression |
| --- | --- |
| A | Exact production-selected contract, even if outside .45–.55 delta / 35–65 DTE; report target-band match |
| B | Absolute delta .65–.75, exact same expiration as A |
| C | Absolute delta .50–.60, 75–100 calendar DTE |
| D | Lowest predeclared exposure-cost proxy among absolute delta .45–.75 / 35–100 DTE |

Puts use negative signed delta and require independently qualified bearish theses. No puts are added simply to balance the sample. B/C/D require positive bid, noncrossed quotes, spread/mid <=5%, open interest >=100, and explicit event compatibility. These are lab eligibility settings, not production rule changes. Delta proximity then spread then instrument ID breaks B/C ties. Missing arms stay UNAVAILABLE permanently, with the candidate set and rejection reasons preserved. Two arms may select the same instrument; report them as duplicates, not independent trades. A is the actual selected contract, not an invented .50-delta counterfactual.

D minimizes `(ask-bid + 10*max(0,-theta)) / (abs(delta)*spot) * max(1, IV/RV20)`, then instrument ID. Theta is premium dollars per share per calendar day; IV and 20-day annualized realized volatility use decimal units. D is a testable cost proxy, **not** known best expected return. Missing theta or IV/RV leaves that candidate ineligible for D. Freeze the formula with the experiment; never fit its constants to prior outcomes.

Use `templates/research_lab_entry.json`. Set null metrics to null with availability reasons and source references in the raw payload; never estimate provider Greeks or IV history silently. IV rank/percentile require a documented lookback and source, stored in the candidate payload. The lab stores IV, IV/RV20, spread, theta, vega, breakeven distance and premium/spot. No inferred causal attribution to IV contraction: positive underlying return plus negative option return and declining IV is descriptive evidence only.

```bash
python3 scripts/strategy_research_lab.py freeze --input /absolute/path/entry.json
```

Capture must be within five minutes of invocation, setup timestamp and underlying quote, with each option quote no more than five minutes old. Use timezone-aware provider quote timestamps. Same window means a common frozen comparison snapshot, not falsely claiming simultaneous exchange ticks. Save unmodified provider responses separately and reference their paths. If capture is unavailable or stale, report LAB_ENTRY_CAPTURE_FAILED; do not manufacture retrospective entries. Research performed after close must wait for a newly validated regular-session setup. The CLI does not fetch broker data itself.

## Daily prospective capture

Capture **every trading session**, not only 1/5/10/20/30-day checkpoints. Reuse the repository's trading calendar. The due command returns unique option IDs and missed prior sessions. Merge these IDs with canonical due IDs for quote retrieval, while persisting each dataset separately.

```bash
python3 scripts/strategy_research_lab.py due --as-of YYYY-MM-DD
python3 scripts/strategy_research_lab.py observe --input /absolute/path/observation.json
python3 scripts/strategy_research_lab.py report --as-of YYYY-MM-DD --output data/validation_reports/YYYY-MM-DD-research-lab.json
```

Use `templates/research_lab_observation.json`. Capture closing quotes 16:00–16:30 America/New_York, with quote times no earlier than 15:55 and <=30 minutes old. Persist immediately. Supply all active variant quotes together; capture failures remain raw error artifacts and visibly missing sessions. Never replace a missed date with a later quote. Underlying price must be the official same-session close, with its provider timestamp/source retained. Continue recording underlying closes after expiration through day 30. Expiration intrinsic valuation uses the expiration-session underlying close (preceding trading session for weekend expiration) and is flagged separately; missing settlement remains unresolved. This is a cash-payoff simulation, not exercise or stock-delivery modeling.

Evaluate the original frozen technical invalidation condition daily. Set `thesis_valid` true/false with evidence, or null when unavailable. Do not invent a new condition after seeing returns. Null blocks a technical-exit estimate but not price-only policies.

Entries and observations are immutable JSON artifacts under `data/strategy_research_lab/`. Identical retries are no-ops; conflicting retries fail. No observations are overwritten by reports. These files follow the same private-data rules as canonical artifacts.

## Outcomes and interpretation

Returns are fractions (0.25 means +25%). Hold returns use entry/exit midpoint; hypothetical exits use entry ask and observed exit bid, with no threshold-price fill assumption or fees. Freeze all 18 combinations of TP +25/+40/+60%, SL -20/-30/-40%, time stop 5/10 trading sessions, plus a separate technical exit capped at 30 sessions. Each policy exits at its first observed daily trigger. Missing prior prices make a policy indeterminate, not successful. Daily observations cannot identify intraday barrier touches or true intraday MAE/MFE. Excursions include entry zero and are explicitly labeled sampled; incomplete paths are flagged and excluded from bucket excursion averages.

Reports include per-arm 1/5/10/20/30-session outcomes, IV change, theta/vega, sampled option/underlying MAE/MFE, exit results, policy summaries, paired B−A/C−A/D−A return differences and direction-separated 75–79/80–84/85–89/90–94/95–100 score buckets. Buckets show sample count, arithmetic mean observed return (an empirical expectancy estimate), median, win rate, and complete-path excursion averages. Arm counts are not signal counts. Inspect missing-arm/path coverage and pair availability before comparing means. Inspect return differences only at matched horizons for matched signals. Broader volatility diagnosis and entry-pullback hypotheses require evidence, not automatic rule changes.

After 10–20 new independent signals, review feasibility and descriptive variant differences. After 30–50 observations per relevant comparison, review score discrimination; these are review milestones, not proof of an edge. No automated winner selection, threshold tightening, or optimization. Record negative results and revisit the signal engine when underlying performance lacks an edge.

## Bearish candidate evidence

Before qualification, independently score five bearish research features: failed breakout, relative weakness versus benchmark, trend deterioration, confirmed negative catalyst, and weak sector/regime alignment. Use `templates/research_lab_bearish_candidate.json` and `bearish --input ...` to persist the research score. Each feature: 0 = evidence contradicts, 1 = weak, 2 = mixed, 3 = clear, 4 = strong corroboration. Cite dated measurements/sources for each; unavailable is null, never zero. The diagnostic score is `5*sum(components)` only when all five exist. It does not replace the underlying/options scores or authorize a shadow. A declining stock alone is insufficient. Retain rejected candidates and reasons; only production-qualified bearish setups enter A–D.

## Scheduled-run integration

The daily agent must run entry freezing after canonical qualification and persistence, and run daily lab capture alongside canonical checkpoints before analytics. Weekly/monthly agents generate lab reports separately and audit missing entries and observations. A lab failure is reported as `LAB_DEGRADED`, preserving the production decision. Compare newly qualified signal groups with experiment IDs so entry capture failures cannot disappear from denominators. Actual schedules remain managed by Codex; this module is invoked by the repo's agent workflow, not a background service.
