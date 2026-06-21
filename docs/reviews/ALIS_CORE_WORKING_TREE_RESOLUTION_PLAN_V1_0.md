# ALIS Core Working Tree Resolution Plan v1.0

## 1. Purpose

This document defines a review-only plan for resolving the remaining dirty and
untracked working tree state after the documentation-only baseline commit
`b16410d0291111528bd6682b15873d882b8d5d1d`.

The plan does not authorise execution. It does not stage files, commit files,
move files, rename files, delete files, clean generated artifacts, create
skeleton folders, refactor code, change imports, implement engines, restructure
the repository, or modify `.gitignore`.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_AUTHORISATION_V1_0.md`
- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`

The current working tree was also inspected using read-only source-control
status commands.

## 3. Current Working Tree State

Observed state before this resolution plan was created:

| Item | Observed state |
| --- | --- |
| Current baseline commit | `b16410d0291111528bd6682b15873d882b8d5d1d` |
| Staged files | None |
| Modified tracked files | 13 |
| Untracked paths | 247 |
| Previously reported untracked paths after baseline commit | 246 |
| Additional untracked path after commit review | `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md` |
| Untracked `.pyc` files | 100 |
| Untracked paths under `__pycache__/` | 100 |

The 247 untracked paths were grouped as follows:

| Top-level path | Untracked path count |
| --- | ---: |
| `backend/` | 81 |
| `data/` | 24 |
| `docs/` | 51 |
| `evidence_package_output.json` | 1 |
| `reports/` | 3 |
| `scripts/` | 4 |
| `tests/` | 83 |

After this plan is created, the plan itself will become an additional untracked
documentation file until a later milestone explicitly reviews and authorises any
disposition.

## 4. Resolution Principles

The following principles govern the remaining working tree resolution:

- Preserve the documentation-only baseline commit as an already completed
  baseline.
- Do not mix source code, tests, generated artifacts, runtime logs, data files,
  and governance documents in one commit.
- Do not stage untracked files by directory or glob.
- Do not clean, delete, or ignore generated artifacts without a separate
  approval milestone.
- Do not resolve line endings while source, data, or registry ownership is still
  undecided.
- Do not create skeleton folders until all blockers are reviewed and the
  working tree has an approved disposition.
- Treat mixed-responsibility folders as review-before-decision, especially
  `backend/alis/pipelines/`, `backend/alis/publishing/`,
  `backend/alis/validators/`, `backend/validators/`, and
  `sources/source_registry.json`.
- Use the frozen boundary register as the controlling contract for any later
  source/test baseline or migration plan.

## 5. Modified Tracked Files Resolution Plan

The 13 modified tracked files must remain unstaged until a later source-control
authorisation decides their disposition.

| Path | Current resolution recommendation | Reason |
| --- | --- | --- |
| `backend/abacus/README.md` | Review before decision | Abacus documentation candidate; may need alignment with V1.0-R1. |
| `backend/abacus/classifier.py` | Review before source baseline | Abacus source candidate; do not commit until accepted as current source. |
| `backend/abacus/taxonomy.py` | Review before source baseline | Abacus taxonomy source candidate; may also need governance review. |
| `backend/validators/README.md` | Review before decision | Transitional validator documentation; Aegis/shared-schema/legacy ownership unresolved. |
| `backend/validators/schema.py` | Review before source baseline | Transitional schema/validator source; ownership unresolved. |
| `backend/validators/validator.py` | Review before source baseline | Transitional validation source; Aegis or legacy status unresolved. |
| `data/classified/classified_world_bank_metadata_40107522.json` | Artifact-retention review | Generated classified analysis output. |
| `data/raw/world_bank/latest_metadata.json` | Artifact-retention review | Raw retrieved data output. |
| `data/raw/world_bank/logs/world_bank_connector.log` | Runtime-log review | Generated connector log; not a source candidate. |
| `data/validated/approved_world_bank_metadata_40107522.json` | Artifact-retention review | Validated/approved data output; Aegis artifact status unresolved. |
| `data/validated/validator.log` | Runtime-log review | Generated validation log. |
| `reports/manifest.json` | Generated-report review | Publication manifest output; Apollo or legacy artifact status unresolved. |
| `sources/source_registry.json` | Source-registry authority review | Possible Thoth registry state, fixture data, generated artifact, or transitional data. |

None of these files should be included in a documentation-only commit. Any
future commit involving them must be preceded by file-level human review and an
explicit staging authorisation.

## 6. Untracked Source-Code Candidates Resolution Plan

Untracked source-code candidates should be reviewed as a separate source/test
baseline workstream, not as cleanup and not as migration.

| Path group | Candidate classification | Resolution recommendation |
| --- | --- | --- |
| `backend/alis/connectors/*.py` | Hermes adapter candidates | Review duplicate connector behavior and transport-only boundaries before source baseline. |
| `backend/alis/ons_connector.py` | Transitional Hermes candidate | Compare with `backend/alis/connectors/ons.py`; do not select canonical path yet. |
| `backend/alis/source_registry.py` | Thoth candidate | Review against `sources/source_registry.json` and registry authority rules. |
| `backend/alis/pipelines/*.py` | Mixed responsibility | Split responsibility review across Hermes, Aegis, Thoth, and runtime orchestration before any baseline. |
| `backend/alis/schemas/*.py` | Shared service candidate | Review as shared schema/contracts support; schema ownership must not imply artifact ownership. |
| `backend/alis/validators/statistical_gatekeeper.py` | Abacus or Aegis candidate | Decide whether it is analytical checking or gate enforcement. |
| `backend/alis/mappers/evidence_to_visualisation.py` | Abacus candidate | Review for validated-input assumptions and chart-ready artifact ownership. |
| `backend/alis/visualisation/*.py` | Abacus/Apollo/product candidates | Split chart specification, rendering, embedding, and export responsibilities. |
| `backend/alis/publishing/*.py` | Mixed Apollo/Aegis/Argus/GoDataBank candidates | Do not move or commit wholesale; perform file-level boundary review. |
| `backend/publisher/**` | Transitional legacy or Apollo candidate | Compare with active publishing paths before retention or archival decision. |
| `backend/publishing/**` | Transitional legacy or GoDataBank product layer | Review placeholders and product-facing intent before any baseline. |
| `scripts/**` | Tooling or transitional operational scripts | Review separately; scripts may run pipelines or create artifacts. |

No source-code candidate is authorised for staging by this plan.

## 7. Untracked Test Candidates Resolution Plan

The untracked test area includes 83 untracked paths under `tests/`, including
27 Python test files and generated `.pyc` files under `tests/alis/__pycache__/`.

Resolution recommendations:

- Treat `tests/alis/*.py` as test candidates requiring source/test baseline
  review.
- Keep `tests/abacus/` and `tests/integration/` placeholders under review; do
  not move them to target skeleton paths yet.
- Exclude all `tests/**/__pycache__/` and `tests/**/*.pyc` files from any future
  test baseline.
- Map tests only after source ownership is settled, because several tests span
  mixed engine boundaries: pipelines, publishing, visualisation, source
  registry, validation, and production candidate output.
- Do not create `tests/alis_core/` or `tests/godatabank/` until a separate
  skeleton creation milestone is authorised.

## 8. Documentation/Review Files Resolution Plan

Untracked documentation under `docs/reviews/` contains 40 existing review
documents before this plan, including:

- `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`
- prior Cloudflare, static publishing, charting, evidence package, production
  candidate, and deployment review documents.

Resolution recommendations:

- The safest next operational step is a narrowly scoped authorisation for
  committing `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`
  only.
- Do not include legacy or non-ALIS-Core review documents in that narrow commit.
- Treat this working tree resolution plan as untracked until it receives its own
  independent review or a later documentation disposition milestone.
- Keep all other untracked review documents in review-before-decision status
  until their product, deployment, or artifact relevance is confirmed.

## 9. Generated Artifact Resolution Plan

Generated artifact candidates include data outputs, report outputs, root-level
evidence output, generated HTML, manifests, and Python bytecode.

Resolution recommendations:

- Do not stage generated artifacts in a source/test baseline.
- Do not delete generated artifacts until a separate artifact-retention review
  decides retain, archive-later, fixture, or delete-later-with-approval status.
- Treat `evidence_package_output.json` as a delete-later-with-approval candidate
  unless reviewed and reclassified as retained evidence or fixture data.
- Treat generated publication outputs under `data/publishing/**` and
  `reports/generated/**` as archive-later or generated-artifact candidates, not
  source code.
- Treat generated classified, validated, raw, and summary data as artifacts that
  may map to Abacus, Aegis, Hermes, or Vyasa outputs only after ownership review.

## 10. Runtime Log Resolution Plan

Runtime logs currently include tracked modified logs and untracked logs:

- `data/raw/world_bank/logs/world_bank_connector.log`
- `data/raw/ons/logs/ons_connector.log`
- `data/validated/validator.log`

Resolution recommendations:

- Do not stage logs in source, test, or documentation commits.
- Review whether logs need short-term artifact retention for evidence, audit, or
  debugging before any cleanup.
- If retained, store them under a future artifact policy rather than source
  paths.
- If not retained, delete only under a separate cleanup authorisation.

## 11. Source Registry Resolution Plan

The source registry requires a dedicated review because the boundary register
assigns source registry and provenance responsibility to Thoth, while source
admission and gate behavior remain separate concerns.

Paths requiring registry review:

- modified tracked `sources/source_registry.json`
- untracked `backend/alis/source_registry.py`
- untracked source-registry tests under `tests/alis/test_source_registry.py`
- generated bytecode under source-registry `__pycache__/` paths

Resolution recommendations:

- Decide whether `sources/source_registry.json` is canonical Thoth registry
  state, fixture data, generated artifact, or transitional prototype data.
- Do not commit `sources/source_registry.json` until its authority and storage
  policy are explicit.
- Do not combine source registry code, registry data, and registry tests in one
  commit without a narrow authorisation.
- Exclude source-registry `.pyc` files from source control.

## 12. Line-Ending Resolution Plan

Line-ending review must remain separate from source/test/data disposition.

Line-ending warning files previously identified for remaining non-baseline
review include:

- `backend/abacus/README.md`
- `backend/abacus/classifier.py`
- `backend/abacus/taxonomy.py`
- `backend/validators/README.md`
- `backend/validators/schema.py`
- `backend/validators/validator.py`
- `sources/source_registry.json`

Resolution recommendations:

- Do not normalise line endings as part of this plan.
- Do not combine line-ending-only changes with source behavior review.
- Resolve line endings only after deciding whether each file is retained,
  rejected, archived, or migrated.
- Keep `.gitignore` unchanged unless a separate ignore-policy milestone is
  authorised.

## 13. .pyc and __pycache__ Resolution Plan

The current working tree contains 100 untracked `.pyc` files, all under
`__pycache__/` paths.

Resolution recommendations:

- Treat `**/*.pyc` as ignore candidates and delete-later-with-approval
  candidates.
- Treat `**/__pycache__/` as generated cache folders that must not be committed.
- Do not delete or clean them in this milestone.
- Do not modify `.gitignore` in this milestone.
- Approve cleanup only through a separate generated-artifact cleanup
  authorisation after any retention concerns are closed.

## 14. Skeleton Creation Blockers

The following blockers remain before target skeleton folders can be created:

- 13 modified tracked files remain unresolved.
- 247 untracked paths remain before this plan is counted.
- The new commit-review document remains untracked.
- This resolution plan will also be untracked after creation.
- 100 `.pyc` files and `__pycache__/` paths remain present.
- Source-code candidates have not been accepted or rejected.
- Test candidates have not been mapped to final engine/product ownership.
- Generated artifacts and runtime logs have not received retention decisions.
- `sources/source_registry.json` has no final Thoth registry authority decision.
- Line-ending review remains open for tracked source and registry files.

The following skeleton folders remain absent and must not be created yet:

- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

## 15. Proposed Resolution Sequence

Recommended sequence:

1. Independently review this working tree resolution plan.
2. Create a narrowly scoped authorisation for committing
   `docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md`
   only, if the reviewer confirms it should be preserved as baseline review
   evidence.
3. Re-check staged files and working tree status after any authorised
   documentation-review commit.
4. Create a source/test baseline review plan for source-code and test
   candidates, excluding generated artifacts, logs, `.pyc` files, and
   `__pycache__/` folders.
5. Create a separate artifact-retention and cleanup authorisation for generated
   artifacts, runtime logs, root evidence output, and Python cache files.
6. Create a source-registry authority decision document before staging
   `sources/source_registry.json` or registry implementation/tests.
7. Only after the above decisions, authorise target skeleton creation in a
   separate milestone.

This sequence is advisory only and does not authorise execution.

## 16. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Accidentally committing source code with documentation review files | High | Use one-file staging authorisations for documentation follow-ups. |
| Preserving mixed engine boundary debt | High | Review mixed folders file by file before source baseline. |
| Committing generated artifacts or bytecode | High | Exclude `.pyc`, `__pycache__/`, logs, and generated outputs from all baseline commits. |
| Losing useful evidence by premature cleanup | Medium | Require artifact-retention review before deletion. |
| Treating `sources/source_registry.json` as canonical too early | High | Require Thoth registry authority decision before staging. |
| Product-specific publishing code entering ALIS Core | Medium | Split Apollo, Aegis, Argus, and GoDataBank responsibilities before migration. |
| Line-ending changes obscuring functional review | Medium | Keep line-ending changes separate from source acceptance decisions. |

## 17. Abort Conditions

Any future resolution execution should abort if:

- files are already staged before an authorised staging step begins;
- a proposed staging list includes paths outside the authorised scope;
- a directory-level or glob-based `git add` is proposed for mixed folders;
- `.pyc` files, `__pycache__/` folders, logs, or generated artifacts are staged
  without explicit artifact authorisation;
- `.gitignore` changes are included without an ignore-policy authorisation;
- skeleton folders are created before blockers are resolved;
- source code, tests, data, and documentation are combined in one baseline
  commit without explicit approval;
- source registry authority remains unresolved but registry data is proposed for
  commit;
- cleanup, deletion, movement, refactoring, import changes, implementation, or
  repository restructuring is attempted under a review-only milestone.

## 18. Recommended Next Milestone

Recommended next milestone:

```text
Narrow Documentation Commit Authorisation for ALIS Core Baseline Commit Review v1.0
```

Purpose of the next milestone:

```text
Authorise, if independently approved, a one-file documentation commit for
docs/reviews/ALIS_CORE_DOCUMENTATION_ONLY_BASELINE_COMMIT_REVIEW_V1_0.md only.
```

If independent review decides that preserving the commit-review document is less
urgent than source/test disposition, the safer alternative is:

```text
Source/Test Baseline Review Plan v1.0
```

That alternative should remain planning-only and must continue excluding
generated artifacts, runtime logs, `.pyc` files, `__pycache__/` folders,
skeleton folders, migration, cleanup, and code changes.

STATUS: WORKING TREE RESOLUTION PLAN CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
