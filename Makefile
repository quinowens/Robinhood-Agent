.PHONY: validate scan-sensitive status daily-log

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
