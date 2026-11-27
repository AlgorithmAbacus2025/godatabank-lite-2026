# ALIS Core Documentation-Only Baseline Commit Authorisation v1.0

## 1. Purpose

This document authorises the proposed first documentation-only baseline commit
for ALIS Core planning artifacts.

The authorisation is limited to identifying the exact documentation files that
may be staged and committed in a future step after independent review. It does
not stage files, commit files, clean generated artifacts, alter source code,
change tests, create skeleton folders, or modify repository structure.

## 2. Source Documents Reviewed

The following source documents were reviewed for this authorisation:

- `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md`

## 3. Authorisation Boundary

This authorisation permits only a future documentation-only baseline commit,
subject to independent review and explicit human approval before staging.

The authorisation boundary is:

- Include only the approved ALIS Core planning and review documents listed in
  Section 4.
- Exclude all source code, tests, data, reports, generated artifacts, templates,
  scripts, skeleton folders, and source-control configuration changes.
- Do not modify `.gitignore`.
- Do not stage or commit anything as part of this authorisation document.
- Do not use path globs for staging the future commit.

## 4. Exact Files Authorised for Future Staging

Only the following files are authorised for future staging:

| File | Future staging status | Notes |
| --- | --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Authorised after independent review | Governing ALIS Core boundary register. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Authorised after independent review | Repository engineering audit source evidence. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Authorised after independent review | Repository architecture migration plan. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Authorised after independent review | Current file and folder classification register. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md` | Authorised after independent review | Source-control baseline and skeleton planning document. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md` | Authorised after independent review | Disposition register for tracked and untracked path groups. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md` | Authorised after independent review | Source-control baseline commit plan. |
| `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_AUTHORISATION_V1_0.md` | Authorised after independent review | This authorisation document. |

No other file is authorised for future staging by this document.

## 5. Files and Path Groups Explicitly Excluded

The following files and path groups are explicitly excluded from the future
documentation-only baseline commit:

- `backend/`
- `tests/`
- `data/`
- `reports/`
- `sources/`
- `templates/`
- `scripts/`
- `evidence_package_output.json`
- `**/*.pyc`
- `**/__pycache__/`
- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`
- `.gitignore`

These exclusions apply even if some paths contain useful source candidates,
test candidates, fixtures, reports, or planning-relevant evidence. Their
disposition must be handled by later review or separate approval.

## 6. Generated Artifacts Excluded

Generated artifacts are excluded from the future documentation-only baseline
commit.

Excluded generated artifact groups include:

- `**/*.pyc`
- `**/__pycache__/`
- generated logs
- generated reports
- runtime outputs under `reports/`
- generated or runtime data under `data/`
- `evidence_package_output.json`

No generated artifact should be staged, committed, deleted, cleaned, moved, or
archived under this authorisation.

## 7. Source Code Excluded

All source-code paths are excluded from the future documentation-only baseline
commit.

Excluded source-code groups include:

- `backend/`
- `scripts/`
- `sources/`
- `templates/`

This exclusion covers ALIS Core engine candidates, shared service candidates,
GoDataBank product-layer candidates, publishing-layer candidates, validators,
connectors, pipelines, schemas, and transitional source files.

## 8. Tests Excluded

All test paths are excluded from the future documentation-only baseline commit.

Excluded test groups include:

- `tests/`
- `tests/alis_core/`
- `tests/godatabank/`

Test files may be assessed in a later source/test baseline milestone, but they
are not authorised for the documentation-only baseline commit.

## 9. Skeleton Folders Excluded

No target skeleton folders are authorised for creation or staging under this
document.

The following skeleton folders remain excluded:

- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

Skeleton creation remains blocked until after the documentation baseline is
reviewed, approved, and committed through a separately authorised step.

## 10. Forbidden Commands

The following commands and command classes remain forbidden during this
authorisation milestone:

- `git add`
- `git commit`
- `git reset`
- `git checkout --`
- `git clean`
- commands that delete files or folders
- commands that move or rename files or folders
- commands that clean `.pyc` files or `__pycache__/` folders
- commands that modify `.gitignore`
- commands that create `src/`, `artifacts/`, `legacy/`, `docs/migration/`,
  `tests/alis_core/`, or `tests/godatabank/`
- commands that refactor code, change imports, implement engines, or restructure
  the repository

## 11. Required Pre-Staging Checks

Before any future staging occurs, the reviewer or operator must confirm:

- independent review has approved this authorisation document;
- the future staging scope contains exactly the eight files listed in Section 4;
- no source code, tests, generated artifacts, data, reports, templates, scripts,
  skeleton folders, or `.gitignore` changes are included;
- `git diff --cached --name-only` is empty before staging begins;
- the repository has not been cleaned, restructured, or migrated since this
  authorisation was created;
- no skeleton folders have been created;
- no generated artifacts have been deleted or modified as part of the baseline
  commit process;
- line-ending warnings on excluded tracked source/data files are not resolved as
  part of the documentation-only baseline commit;
- the staging commands are run one file at a time, without globs or directory
  adds;
- the resulting staged file list exactly matches Section 4 before commit.

## 12. Exact Future Staging Command Set, But Do Not Run It

The following command set is authorised for future review only. It must not be
run until independent review approves this document and a separate execution
step is authorised.

```text
git add docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md
git add docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md
git add docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md
git add docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md
git add docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md
git add docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_AUTHORISATION_V1_0.md
```

No directory-level `git add` command is authorised.

## 13. Exact Future Commit Message, But Do Not Run It

The following commit message is authorised for future review only. It must not
be used until independent review approves this document and a separate execution
step is authorised.

```text
docs: freeze ALIS Core planning baseline
```

## 14. Abort Conditions

The future documentation-only baseline commit must be aborted if any of the
following conditions apply:

- any file outside Section 4 is staged;
- any source-code, test, generated artifact, data, report, template, script, or
  skeleton path is staged;
- `.gitignore` is modified or staged;
- a directory-level or glob-based staging command is used;
- `git diff --cached --name-only` does not exactly match the eight authorised
  files;
- generated artifacts are cleaned, deleted, moved, or modified;
- skeleton folders are created;
- source code is refactored or imports are changed;
- the repository is restructured or migrated;
- line-ending normalization is attempted on excluded source or data files;
- independent review requires revision before commit execution.

## 15. Final Decision

The first documentation-only baseline commit is authorised for future staging
and commit execution only after independent review.

The authorised future commit scope is exactly the eight documentation files
listed in Section 4. All other files and path groups are excluded from this
documentation-only baseline commit.

STATUS: DOCUMENTATION-ONLY BASELINE COMMIT AUTHORISATION CREATED
AUTHORISATION: PENDING INDEPENDENT REVIEW
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
