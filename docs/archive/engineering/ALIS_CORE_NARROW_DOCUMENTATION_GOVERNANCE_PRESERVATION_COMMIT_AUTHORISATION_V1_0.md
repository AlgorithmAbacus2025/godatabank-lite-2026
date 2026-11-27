# ALIS Core Narrow Documentation Governance Preservation Commit Authorisation v1.0

## 1. Purpose

This document authorises, at planning level only, a future narrow
documentation-governance preservation commit for the remaining ALIS Core
governance review chain.

The authorisation is limited to defining the exact future staging scope and
commit message for later independent review. It does not authorise execution.
It does not stage files, commit files, move files, rename files, delete files,
clean generated artifacts, create skeleton folders, refactor code, change
imports, implement engines, restructure the repository, or modify `.gitignore`.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md`
- `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md`

## 3. Authorisation Boundary

This authorisation is limited to a future documentation-governance preservation
commit containing exactly four files.

The future commit may include only:

1. `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
2. `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md`
3. `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md`
4. `docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md`

The future commit must not include this authorisation document:

```text
docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_GOVERNANCE_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md
```

The future commit must not include any other documentation file, source code,
test file, generated artifact, runtime log, source registry file, `.gitignore`
change, skeleton folder, migration folder, cleanup work, or implementation work.

No directory-level staging command and no glob-based staging command is
authorised.

## 4. Exact Four-File Future Staging Scope

The exact future staging scope is:

| File | Future staging status | Reason |
| --- | --- | --- |
| `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md` | Authorised after independent review | Preserves the post-baseline working tree resolution plan. |
| `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md` | Authorised after independent review | Preserves the one-file baseline commit review authorisation boundary. |
| `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md` | Authorised after independent review | Preserves the independent review of commit `853e498f8170c78de27ecf69c39d9c66385be4eb`. |
| `docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md` | Authorised after independent review | Preserves the governance preservation planning decision. |

No other file is authorised for future staging by this document.

## 5. Explicit Exclusions

The following files and path groups are explicitly excluded from the future
documentation-governance preservation commit:

- `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_GOVERNANCE_PRESERVATION_COMMIT_AUTHORISATION_V1_0.md`
- all other `docs/reviews/*.md` files
- all `docs/contracts/` files unless separately authorised
- all `docs/governance/` files unless separately authorised
- `backend/`
- `tests/`
- `data/`
- `reports/`
- `sources/`
- `templates/`
- `scripts/`
- `evidence_package_output.json`
- `.gitignore`
- `**/*.pyc`
- `**/__pycache__/`
- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

These exclusions remain in force even if a file or path is later found to be
useful for source/test baseline review, artifact retention, cleanup planning,
skeleton planning, migration, or implementation.

## 6. Forbidden Commands

The following commands and command classes remain forbidden during this
authorisation milestone:

- `git add`
- `git commit`
- `git reset`
- `git checkout --`
- `git clean`
- directory-level `git add`
- glob-based `git add`
- commands that stage this authorisation document
- commands that stage files outside the four-file future scope in Section 4
- commands that stage `backend/`, `tests/`, `data/`, `reports/`, `sources/`,
  `templates/`, `scripts/`, `evidence_package_output.json`, `.gitignore`,
  `.pyc` files, or `__pycache__/` folders
- commands that move, rename, delete, or clean files
- commands that create `src/`, `artifacts/`, `legacy/`, `docs/migration/`,
  `tests/alis_core/`, or `tests/godatabank/`
- commands that refactor code, change imports, implement engines, migrate files,
  or restructure the repository

The exact future staging commands in Section 8 are listed as text only and must
not be run under this milestone.

## 7. Required Pre-Staging Checks

Before any future execution milestone stages the authorised files, the operator
must confirm:

- independent review has approved this authorisation document;
- `git diff --cached --name-only` is empty before staging begins;
- all four files listed in Section 4 still exist;
- the future staging scope is exactly the four files listed in Section 4;
- this authorisation document is not staged;
- no other documentation file is staged;
- no source code, tests, generated artifacts, runtime logs, source registry
  files, `.gitignore` changes, `.pyc` files, or `__pycache__/` folders are
  staged;
- no directory-level or glob-based staging command is used;
- no skeleton folders have been created;
- no cleanup, deletion, movement, rename, import change, refactor,
  implementation, migration, or repository restructuring has occurred.

After staging in a future execution milestone, the staged file list must exactly
match Section 4 and contain no additional paths.

## 8. Exact Future Staging Commands, Listed as Text Only

The following commands are listed as text only for future review. They must not
be run until a separate execution milestone is authorised.

```text
git add docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md
git add docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md
git add docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md
```

No directory-level `git add` command is authorised.

## 9. Exact Future Commit Message, Listed as Text Only

The following commit message is listed as text only for future review. It must
not be used until a separate execution milestone is authorised.

```text
docs: preserve ALIS Core governance review chain
```

## 10. Abort Conditions

Any future execution milestone must abort if:

- files are already staged before execution begins;
- any file outside the four-file future scope in Section 4 is staged;
- this authorisation document is staged;
- any other documentation file is staged;
- any excluded path from Section 5 is staged;
- a directory-level or glob-based staging command is used;
- `.gitignore` is modified or staged;
- `.pyc` files or `__pycache__/` folders are staged, deleted, or cleaned;
- source code, tests, generated artifacts, runtime logs, source registry files,
  or data/report outputs are staged;
- skeleton folders are created;
- files are moved, renamed, deleted, cleaned, refactored, implemented, migrated,
  or restructured;
- independent review requires revision before execution.

## 11. Final Decision

The future documentation-governance preservation commit is authorised for review
only.

The only files authorised for future staging are the four files listed in
Section 4. This authorisation document and all other files are excluded.

## 12. Recommended Next Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Narrow Documentation Governance Preservation Commit Authorisation v1.0
```

If approved, a later execution milestone may stage and commit only the four
files listed in Section 4 using the exact commands and commit message listed in
Sections 8 and 9.

STATUS: NARROW DOCUMENTATION GOVERNANCE PRESERVATION COMMIT AUTHORISATION CREATED
AUTHORISATION: PENDING INDEPENDENT REVIEW
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
