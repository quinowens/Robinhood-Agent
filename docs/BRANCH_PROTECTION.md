# Branch Protection Plan

The repository currently allows direct pushes to `main` while the workflow is still being shaped.

When the project reaches a stable state, enable branch protection for `main` in GitHub settings:

1. Require pull requests before merging.
2. Require `make validate` to pass before merge.
3. Require branches to be up to date before merge.
4. Dismiss stale approvals when new commits are pushed.
5. Restrict force pushes and branch deletion.

Recommended migration:

1. Continue direct `main` commits while core repo structure is changing quickly.
2. Add validation and keep it passing.
3. Use short-lived branches for the first few non-urgent changes.
4. Enable protection once branches feel routine.

Until branch protection is enabled, run `make validate` before every push to `main`.
