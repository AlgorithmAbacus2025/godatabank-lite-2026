# ALIS Core Documentation Governance Preservation Plan v1.0

## 1. Purpose

This document defines a planning-only approach for preserving the remaining
uncommitted ALIS Core governance and review documents before any source/test
baseline planning, artifact cleanup, skeleton creation, migration, or
implementation work proceeds.

The plan does not authorise execution. It does not stage files, commit files,
move files, rename files, delete files, clean generated artifacts, create
skeleton folders, refactor code, change imports, implement engines, restructure
the repository, or modify `.gitignore`.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md`
- `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md`
- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`
- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_AUTHORISATION_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`

Current repository status was also inspected using read-only source-control and
filesystem checks.

## 3. Current Governance-Document State

Observed state before this preservation plan was created:

| Item | Observed state |
| --- | --- |
| Staged files | None |
| Modified tracked files | 13 |
| Untracked paths | 249 |
| Untracked ALIS Core governance/review documents | 3 |
| Target preservation plan file | Not present before creation |
| Skeleton folders checked | Not present |

Untracked ALIS Core governance/review documents observed before this plan:

1. `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
2. `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md`
3. `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md`

After creation, this document will become a fourth untracked ALIS Core
governance document:

4. `docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md`

The prior baseline planning, authorisation, and baseline commit review documents
have already been committed through earlier documentation-only commits. This
plan addresses only the remaining uncommitted ALIS Core governance chain.

## 4. Preservation Principles

Preservation should follow these principles:

- Preserve governance evidence before changing source, tests, artifacts,
  skeleton folders, or repository structure.
- Keep the preservation commit documentation-only.
- Include only ALIS Core governance/review documents needed to maintain the
  source-control decision chain.
- Exclude historical non-ALIS review documents unless separately classified and
  authorised.
- Exclude source code, tests, data, reports, generated artifacts, runtime logs,
  source registry files, `.gitignore`, `.pyc` files, `__pycache__/` folders,
  skeleton folders, migration folders, cleanup work, and implementation work.
- Do not use directory-level staging or glob-based staging in any future
  execution milestone.
- Require an independent authorisation milestone before any staging or commit.

## 5. Documents Recommended for Preservation

The following documents are recommended for preservation in a future narrow
documentation-governance preservation commit, subject to independent review and
separate execution authorisation:

| Document | Recommendation | Reason |
| --- | --- | --- |
| `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md` | Preserve | Defines remaining dirty/untracked repository state and sequencing constraints before source/test/artifact/skeleton work. |
| `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md` | Preserve | Records the authorisation boundary for the one-file baseline commit review preservation commit. |
| `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md` | Preserve | Independently confirms commit `853e498f8170c78de27ecf69c39d9c66385be4eb` matched its one-file scope. |
| `docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md` | Preserve | Records this planning decision before moving to source/test, artifact, skeleton, migration, or implementation planning. |

These four documents form the minimal uncommitted ALIS Core governance chain
remaining after the documentation-only baseline and narrow baseline-review
commits.

## 6. Documents Recommended for Deferred Review

The following document groups should remain deferred:

| Document group | Recommendation | Reason |
| --- | --- | --- |
| Other untracked `docs/reviews/*.md` documents unrelated to the ALIS Core baseline chain | Deferred review | They may be product, deployment, publishing, charting, or historical review evidence and require separate classification. |
| Future source/test baseline planning documents not yet created | Deferred review | They should be created only after the current governance chain is preserved or explicitly deferred. |
| Future artifact-retention, cleanup, skeleton, migration, or implementation authorisations | Deferred review | They are outside the governance preservation scope. |

Deferred review does not mean deletion, movement, staging, or rejection. It only
means those documents are not part of the recommended immediate preservation
commit.

## 7. Documents Explicitly Excluded From Immediate Preservation

The future preservation commit should not include:

- previously committed ALIS Core baseline documents;
- any historical non-ALIS review document under `docs/reviews/`;
- any root-level documentation outside the four files in Section 9;
- any `docs/contracts/` or `docs/governance/` file not separately authorised;
- any future document created after this plan unless independently reviewed and
  authorised.

This exclusion keeps the preservation commit narrow and auditable.

## 8. Proposed Commit Grouping

Recommended future commit grouping:

| Group | Scope | Status |
| --- | --- | --- |
| Group 1 | Preserve the four remaining ALIS Core governance/review documents listed in Section 9 | Recommended for a future narrow authorisation milestone |
| Group 2 | Review other untracked historical `docs/reviews/*.md` documents | Deferred |
| Group 3 | Source/test baseline review documents and accepted source/test candidates | Deferred |
| Group 4 | Artifact-retention and cleanup authorisations | Deferred |
| Group 5 | Skeleton creation and migration planning documents | Deferred |

Only Group 1 is recommended as the next reviewable commit scope. This plan does
not authorise staging or commit execution.

## 9. Exact Files Proposed for a Future Documentation-Governance Preservation Commit

The exact files proposed for a future documentation-governance preservation
commit are:

1. `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
2. `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_AUTHORISATION_BASELINE_COMMIT_REVIEW_V1_0.md`
3. `docs/reviews/ALIS_CORE_NARROW_DOCUMENTATION_COMMIT_REVIEW_BASELINE_COMMIT_REVIEW_V1_0.md`
4. `docs/reviews/ALIS_CORE_DOCUMENTATION_GOVERNANCE_PRESERVATION_PLAN_V1_0.md`

No other file is proposed for the future preservation commit.

## 10. Files Explicitly Excluded From That Future Commit

The future documentation-governance preservation commit must exclude:

- any file not listed in Section 9;
- all other `docs/reviews/*.md` files;
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

## 11. Source Code Exclusion

No source code is proposed for preservation.

Excluded source-code groups include:

- `backend/`
- `scripts/`
- `sources/`
- `templates/`

Source-code candidates must remain under source/test baseline review and must
not be mixed into a documentation-governance preservation commit.

## 12. Tests Exclusion

No tests are proposed for preservation.

Excluded test groups include:

- `tests/`
- `tests/alis_core/`
- `tests/godatabank/`

Test candidates must remain deferred until source ownership and engine/product
mapping are reviewed.

## 13. Generated Artifact Exclusion

No generated artifacts are proposed for preservation.

Excluded generated artifact groups include:

- generated data under `data/`
- generated reports under `reports/`
- runtime logs
- `evidence_package_output.json`
- `**/*.pyc`
- `**/__pycache__/`

Artifact retention, archival, cleanup, or deletion decisions require a separate
milestone.

## 14. .gitignore Exclusion

`.gitignore` is explicitly excluded from the future preservation commit.

No ignore-policy change is proposed by this plan, even though `.pyc` files and
`__pycache__/` folders remain clear ignore candidates. Ignore-policy work should
be handled through a separate authorisation if needed.

## 15. Skeleton-Folder Exclusion

No skeleton folders are proposed for creation or preservation.

The following folders remain excluded and must not be created under this plan:

- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

Skeleton creation remains blocked until dirty source/data/artifact/test state
and governance preservation are resolved through separate milestones.

## 16. Required Pre-Staging Checks

Before any future preservation execution is authorised, the operator must
confirm:

- independent review has approved this preservation plan;
- a separate future authorisation document explicitly lists the same Section 9
  file set;
- `git diff --cached --name-only` is empty before staging begins;
- all proposed files are documentation files under `docs/reviews/`;
- the staged file list exactly matches Section 9 and contains no extras;
- no directory-level or glob-based `git add` is used;
- no source code, tests, generated artifacts, data, reports, logs, source
  registry files, `.gitignore`, `.pyc` files, or `__pycache__/` folders are
  staged;
- no skeleton folders have been created;
- no cleanup, deletion, movement, rename, import change, refactor,
  implementation, migration, or repository restructuring has occurred.

## 17. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Over-broad documentation commit captures unrelated historical review docs | Medium | Stage only exact Section 9 files after a separate authorisation. |
| Source/test baseline proceeds without preserving governance chain | Medium | Preserve the four-document governance chain first, or explicitly defer it by review. |
| Generated artifacts or bytecode enter a documentation commit | High | Exclude all data, reports, `.pyc`, and `__pycache__/` paths. |
| Working Tree Resolution Plan becomes stale before preservation | Medium | Re-check status before future authorisation and note any delta. |
| This plan is mistaken for execution approval | Medium | Require a separate narrow authorisation milestone before staging. |

## 18. Abort Conditions

Any future preservation execution must abort if:

- files are already staged before execution begins;
- the staged file list differs from the future approved authorisation scope;
- any file outside Section 9 is staged;
- a directory-level or glob-based staging command is used;
- source code, tests, generated artifacts, runtime logs, source registry files,
  `.gitignore`, `.pyc` files, or `__pycache__/` folders are staged;
- skeleton folders are created;
- files are moved, renamed, deleted, cleaned, refactored, implemented,
  migrated, or restructured;
- independent review requires revision before preservation.

## 19. Recommended Next Milestone

Recommended next milestone:

```text
Narrow Documentation Governance Preservation Commit Authorisation v1.0
```

Purpose of the next milestone:

```text
Create a narrow authorisation document for a future documentation-governance
preservation commit limited to the four files listed in Section 9.
```

That milestone should remain authorisation-only and must not stage, commit,
clean, delete, move, rename, refactor, implement, migrate, restructure, create
skeleton folders, or modify `.gitignore`.

STATUS: DOCUMENTATION GOVERNANCE PRESERVATION PLAN CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
