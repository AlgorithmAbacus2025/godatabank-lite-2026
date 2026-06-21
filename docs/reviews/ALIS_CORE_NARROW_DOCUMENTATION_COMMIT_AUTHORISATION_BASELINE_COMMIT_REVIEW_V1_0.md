# ALIS Core Narrow Documentation Commit Authorisation for Baseline Commit Review v1.0

## 1. Purpose

This document authorises a future one-file documentation commit for the ALIS
Core baseline commit review document only.

The authorisation is narrow by design. It exists to preserve the independent
review of the documentation-only baseline commit without including working tree
resolution planning, source code, tests, generated artifacts, skeleton folders,
repository configuration, cleanup, migration, or implementation work.

This document does not authorise execution. It does not stage files, commit
files, move files, rename files, delete files, clean generated artifacts, create
skeleton folders, refactor code, change imports, implement engines, restructure
the repository, or modify `.gitignore`.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_AUTHORISATION_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md`

## 3. Authorisation Boundary

This authorisation is limited to a future one-file documentation commit.

The future commit may include only:

- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`

The future commit must not include:

- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
- this authorisation document;
- any other documentation file;
- any source code;
- any test file;
- any generated artifact;
- any runtime log;
- any source registry file;
- any skeleton folder;
- `.gitignore`.

No directory-level staging command and no glob-based staging command is
authorised.

## 4. Exact One-File Future Staging Scope

The exact future staging scope is:

| File | Future staging status | Notes |
| --- | --- | --- |
| `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md` | Authorised after independent review | The only file authorised for the future one-file documentation commit. |

No other file or path group is authorised for future staging by this document.

## 5. Explicit Exclusions

The following files and path groups are explicitly excluded from the future
one-file documentation commit:

- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
- any other file under `docs/`
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

These exclusions apply even if a file or path later appears useful for source
baseline review, evidence retention, cleanup planning, or migration planning.
Separate review and authorisation are required for any excluded item.

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
- commands that stage `backend/`, `tests/`, `data/`, `reports/`, `sources/`,
  `templates/`, `scripts/`, `.gitignore`, `.pyc` files, or `__pycache__/`
  folders
- commands that move, rename, delete, or clean files
- commands that create `src/`, `artifacts/`, `legacy/`, `docs/migration/`,
  `tests/alis_core/`, or `tests/godatabank/`
- commands that refactor code, change imports, implement engines, or restructure
  the repository

The exact future staging command in Section 8 is listed for review only and must
not be run under this milestone.

## 7. Required Pre-Staging Checks

Before any future execution milestone stages the authorised file, the operator
must confirm:

- independent review has approved this authorisation document;
- `git diff --cached --name-only` is empty before staging begins;
- the future staging scope is exactly
  `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`;
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md` is not staged;
- this authorisation document is not staged;
- no other documentation file is staged;
- no source code, tests, generated artifacts, runtime logs, source registry
  files, `.gitignore` changes, or skeleton folders are staged;
- no directory-level or glob-based staging command is used;
- no cleanup, deletion, movement, rename, import change, implementation, or
  migration has been performed as part of the execution.

## 8. Exact Future Staging Command, Listed as Text Only

The following command is listed as text only for future review. It must not be
run until a separate execution milestone is authorised.

```text
git add docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md
```

## 9. Exact Future Commit Message, Listed as Text Only

The following commit message is listed as text only for future review. It must
not be used until a separate execution milestone is authorised.

```text
docs: record ALIS Core baseline commit review
```

## 10. Abort Conditions

Any future execution milestone must abort if:

- files are already staged before execution begins;
- any file other than
  `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`
  is staged;
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md` is staged;
- this authorisation document is staged;
- any other documentation file is staged;
- any excluded path from Section 5 is staged;
- a directory-level or glob-based staging command is used;
- `.gitignore` is modified or staged;
- `.pyc` files or `__pycache__/` folders are staged, deleted, or cleaned;
- skeleton folders are created;
- source code, tests, generated artifacts, runtime logs, source registry files,
  or data/report outputs are staged;
- files are moved, renamed, deleted, cleaned, refactored, implemented, migrated,
  or restructured.

## 11. Final Decision

The future one-file documentation commit is authorised for review only.

The only file authorised for future staging is:

```text
docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md
```

No other file is authorised.

## 12. Recommended Next Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Narrow Documentation Commit Authorisation for Baseline Commit Review v1.0
```

If approved, a later execution milestone may stage and commit only the one file
listed in Section 4 using the exact command and commit message listed in
Sections 8 and 9.

STATUS: NARROW DOCUMENTATION COMMIT AUTHORISATION CREATED
AUTHORISATION: PENDING INDEPENDENT REVIEW
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
