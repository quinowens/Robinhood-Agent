# Outcome Status Migration

Version 2.0.2 adds `forward_{1,5,10,20,30}d_status` and matching observation metadata to canonical option outcomes. Run `scripts/migrate_v202_ids.py` first to add deterministic record IDs, template defaults, and reconstructable manifest references without changing prices, returns, scores, or decisions. Then run `scripts/update_option_outcomes.py --snapshot <snapshot.json>`.

Existing non-null returns are finalized and are never overwritten by a normal update. An intentional correction requires both `--allow-correction` and `--correction-reason`. Records whose stable IDs cannot be inferred from historical content receive deterministic `legacy-*` IDs and `legacy_schema: true`. Pre-v2.0.2 scheduled-ledger status vocabulary is retained as historical evidence and reported once as `LEGACY_LEDGER_FORMAT_GRANDFATHERED`, rather than repeated row-level warnings.

`PENDING` means the horizon is immature as of the updater's source snapshot. `OBSERVED` requires both option and underlying returns plus timestamp/source provenance. `MISSING_SOURCE_DATA` and `UPDATE_FAILED` persist a reason and visibly degrade health. `NOT_APPLICABLE` is reserved for records where the horizon is deliberately outside the record's tracking contract.

This migration changes tracking metadata only. It does not change setup scoring, underlying scoring, tier thresholds, DTE/delta/liquidity/earnings/universe/suitability rules, `NO TRADE`, contract selection, or execution permissions.
