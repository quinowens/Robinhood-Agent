# v1.9 Validation Release

Version 1.9 should prove whether the existing rules work before adding more discretionary rules.

The central question is:

> If the agent had been followed exactly as written over the last 30, 60, and 90 trading days, what would have happened?

## Evidence Priorities

Track:

- Forward returns by research score bucket.
- Alpha versus `SPY` and `QQQ` by score bucket.
- Scanner-source alpha.
- Rejection opportunity cost.
- NO TRADE 5/10/20-day outcomes by block reason.
- Options Activity confirmation lift.
- Earnings-block opportunity value.
- Shadow-portfolio return, drawdown, and R-multiple distribution.
- Market-health score versus subsequent opportunity quality.
- Correlation-cluster concentration among approved candidates.
- Tier threshold calibration against actual score distributions.
- Primary-vs-secondary blocking rule attribution.

## Do Not Loosen Rules Prematurely

An empty Tier 1 is valid. A NO TRADE decision after many scanner hits is valid. Conservative behavior should only be loosened after outcome data shows the rule is costing more than it protects.

## Minimum Useful Sample

Do not promote a rule change from a tiny sample. Use the smallest applicable threshold below:

| Analysis | Minimum sample |
| --- | ---: |
| Score bucket forward return | 20 candidates per bucket |
| Scanner-source alpha | 30 candidates from the scanner |
| Options confirmation lift | 20 confirmed and 20 unconfirmed comparable candidates |
| Earnings-block opportunity value | 20 blocked candidates |
| Shadow portfolio performance | 20 qualified hypothetical trades |

Below those counts, label conclusions as directional only.

## Monthly Output

Save validation summaries to `data/validation_reports/YYYY-MM-validation-summary.json` and a human-readable month-end review in `backtests/YYYY-MM-review.md`.

The summary should answer:

1. Did higher scores outperform lower scores?
2. Did the agent outperform `SPY` and `QQQ` in the shadow portfolio?
3. Which scanner sources produced positive alpha?
4. Which rejection or temporary-block rules saved losses?
5. Which rules created costly missed opportunities?
6. Did options activity add measurable value?
7. Did market-health score improve or reduce entry quality?
8. Did correlation clustering create hidden concentration?
9. Are Tier 1 and Tier 2 thresholds predictive and reachable under the current scoring model?
10. Which primary blocking rules created the largest missed-winner or avoided-loser effects?
