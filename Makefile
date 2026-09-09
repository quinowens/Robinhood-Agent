.PHONY: validate scan-sensitive status daily-log analyze-outcomes strategy-diagnostics validation-report integrity-audit update-option-outcomes migrate-v202-ids

PYTHON ?= python3

validate:
	$(PYTHON) scripts/validate_repo.py

scan-sensitive:
	$(PYTHON) scripts/validate_repo.py --scan-sensitive-only

status:
	git status --short --branch

daily-log:
	@test -n "$(DATE)" || (echo "Usage: make daily-log DATE=YYYY-MM-DD" && exit 2)
	@test -f "research_logs/$(DATE)-daily-scanner-dry-run.md" || (echo "Missing research_logs/$(DATE)-daily-scanner-dry-run.md" && exit 1)
	@sed -n '1,80p' "research_logs/$(DATE)-daily-scanner-dry-run.md"

analyze-outcomes:
	$(PYTHON) scripts/analyze_outcomes.py

strategy-diagnostics:
	$(PYTHON) scripts/generate_strategy_diagnostics.py $(if $(OUTPUT),--output "$(OUTPUT)",)

validation-report:
	@test -n "$(MONTH)" || (echo "Usage: make validation-report MONTH=YYYY-MM" && exit 2)
	$(PYTHON) scripts/analyze_outcomes.py --month "$(MONTH)" --output "data/validation_reports/$(MONTH)-validation-summary.json"

integrity-audit:
	$(PYTHON) scripts/data_integrity.py $(if $(AS_OF),--as-of "$(AS_OF)",) $(if $(OUTPUT),--output "$(OUTPUT)",)

update-option-outcomes:
	@test -n "$(SNAPSHOT)" || (echo "Usage: make update-option-outcomes SNAPSHOT=path/to/snapshot.json" && exit 2)
	$(PYTHON) scripts/update_option_outcomes.py --snapshot "$(SNAPSHOT)"
	$(PYTHON) scripts/analyze_outcomes.py $(if $(MONTH),--month "$(MONTH)",) $(if $(OUTPUT),--output "$(OUTPUT)",)

migrate-v202-ids:
	$(PYTHON) scripts/migrate_v202_ids.py $(if $(DRY_RUN),--dry-run,)
