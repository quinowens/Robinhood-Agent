# Contribution Workflow

This repository is private and currently uses direct pushes to `main`.

## Before Pushing

Run:

```bash
make validate
```

Review:

```bash
git status --short
git diff --stat
```

## Commit Style

Prefer small, descriptive commits:

- `Add daily scanner dry run for 2026-08-07`
- `Update rejected candidate memory`
- `Add repository validation checks`
- `Clarify options proposal guardrails`

## Main Branch Rules

- Keep `main` in a runnable, validated state.
- Do not commit credentials or authentication material.
- Do not commit public-release changes without applying `PRIVATE_DATA.md`.
- Do not mix live trading workflow changes with generated daily artifacts unless one directly explains the other.

## Later Branch Workflow

When the project stabilizes:

1. Create a branch for each change.
2. Run `make validate`.
3. Open a pull request.
4. Merge after review.
