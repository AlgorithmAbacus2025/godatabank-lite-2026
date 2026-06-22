# ALIS Core Source/Test Baseline Review Plan v1.0

## 1. Purpose

This document defines a planning-only review path for the remaining candidate
source and test files after the ALIS Core documentation governance baseline
commits.

The plan does not authorise staging, commits, cleanup, deletion, file movement,
migration, skeleton creation, import changes, refactoring, or implementation. It
exists to decide how source and test candidates should be reviewed before any
future baseline authorisation is drafted.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_GOVERNANCE_REVIEW_TAIL_PRESERVATION_DECISION_V1_0.md`
- `docs/reviews/ALIS_CORE_NARROW_GOVERNANCE_TAIL_PRESERVATION_COMMIT_REVIEW_V1_0.md`

Current repository status was also inspected using read-only source-control and
filesystem checks.

## 3. Current Repository State

Observed state before this plan was created:

| Item | Observed state |
| --- | --- |
| Staged files | None |
| Modified tracked files | 13 |
| Untracked paths | 249 |
| Untracked backend paths | 81 |
| Untracked backend Python source candidates, excluding `.pyc` | 27 |
| Untracked test paths | 83 |
| Untracked Python test candidates, excluding `.pyc` | 27 |
| Untracked `.pyc` files | 100 |
| Untracked paths under `__pycache__/` | 100 |
| Skeleton folders checked | Not present |

Untracked paths by top-level folder:

| Top-level path | Untracked path count |
| --- | ---: |
| `backend/` | 81 |
| `data/` | 24 |
| `docs/` | 53 |
| `evidence_package_output.json` | 1 |
| `reports/` | 3 |
| `scripts/` | 4 |
| `tests/` | 83 |

After creation, this plan will become an additional untracked documentation file
until a later milestone explicitly reviews and authorises any disposition.

## 4. Review Principles

The source/test baseline review must follow these principles:

- Use the ALIS Core Boundary Register as the controlling contract.
- Review source and tests before any migration, movement, import rewrite, or
  skeleton creation.
- Do not move mixed folders wholesale into ALIS Core.
- Do not allow one source/test baseline commit to hide generated artifacts,
  logs, data files, reports, source registry state, or bytecode.
- Separate ALIS Core engine candidates from shared services, GoDataBank product
  code, and transitional legacy code.
- Resolve source-registry authority before committing registry state or tests.
- Resolve line-ending review only after deciding each file's retention and
  ownership.
- Stage no file under this plan; all future staging requires a separate narrow
  authorisation.

## 5. Modified Tracked Source/Test Candidate Review Plan

The 13 modified tracked files remain unresolved. Only six are direct source or
source-adjacent candidates; the rest are generated artifacts, logs, reports, or
registry blockers.

| Path | Candidate type | Review decision required |
| --- | --- | --- |
| `backend/abacus/README.md` | Abacus documentation candidate | Check against V1.0-R1 Abacus boundary before acceptance. |
| `backend/abacus/classifier.py` | Abacus source candidate | Decide whether current classifier is accepted baseline source. |
| `backend/abacus/taxonomy.py` | Abacus source candidate | Decide whether taxonomy remains Abacus source or needs governance review. |
| `backend/validators/README.md` | Transitional validator documentation | Decide Aegis, shared schema support, legacy, or reject. |
| `backend/validators/schema.py` | Transitional schema/source candidate | Decide shared service, Aegis support, legacy, or superseded. |
| `backend/validators/validator.py` | Transitional validation source candidate | Decide Aegis candidate, legacy, or rejection. |
| `sources/source_registry.json` | Source-registry authority blocker | Do not accept until Thoth registry authority and storage policy are explicit. |
| `data/classified/classified_world_bank_metadata_40107522.json` | Generated data artifact | Exclude from source/test baseline. |
| `data/raw/world_bank/latest_metadata.json` | Generated raw data artifact | Exclude from source/test baseline. |
| `data/raw/world_bank/logs/world_bank_connector.log` | Runtime log | Exclude from source/test baseline. |
| `data/validated/approved_world_bank_metadata_40107522.json` | Generated validated data artifact | Exclude from source/test baseline. |
| `data/validated/validator.log` | Runtime log | Exclude from source/test baseline. |
| `reports/manifest.json` | Generated report/manifest artifact | Exclude from source/test baseline. |

No modified tracked file is authorised for staging by this plan.

## 6. Untracked Backend Source Candidate Review Plan

The untracked backend source review should start from file ownership, not folder
location.

Untracked backend Python source candidates:

```text
backend/alis/connectors/ons.py
backend/alis/connectors/world_bank.py
backend/alis/mappers/evidence_to_visualisation.py
backend/alis/ons_connector.py
backend/alis/pipelines/multi_source_evidence.py
backend/alis/pipelines/multi_source_observation_evidence.py
backend/alis/pipelines/ons_observation_evidence.py
backend/alis/publishing/cloudflare_upload_candidate_inspection.py
backend/alis/publishing/production_candidate_output_evidence.py
backend/alis/publishing/production_candidate_static_output.py
backend/alis/publishing/static_manifest_validation.py
backend/alis/publishing/static_publishing_pipeline.py
backend/alis/publishing/static_report_fragment.py
backend/alis/publishing/static_report_index.py
backend/alis/publishing/static_report_page.py
backend/alis/publishing/static_site_assembly.py
backend/alis/publishing/static_site_smoke_test.py
backend/alis/schemas/evidence_package.py
backend/alis/schemas/visualisation_dataset.py
backend/alis/source_registry.py
backend/alis/validators/statistical_gatekeeper.py
backend/alis/visualisation/chart_spec_export.py
backend/alis/visualisation/html_chart_embedding.py
backend/alis/visualisation/minimal_chart_engine.py
backend/alis/visualisation/static_chart_renderer.py
backend/alis/visualisation/svg_export_integration.py
backend/publisher/html_publisher.py
```

Untracked backend non-Python placeholders and documentation:

```text
backend/publisher/README.md
backend/publishing/README.md
backend/publishing/api_routes/.gitkeep
backend/publishing/html_export/.gitkeep
backend/publishing/pdf_export/.gitkeep
backend/publishing/report_builder/.gitkeep
```

Review approach:

- Review `backend/alis/connectors/` as Hermes candidates.
- Review duplicate connector paths before choosing any canonical adapter.
- Review `backend/alis/pipelines/` as mixed responsibility; do not commit as a
  single engine package.
- Review `backend/alis/publishing/` file by file across Apollo, Aegis, Argus,
  Thoth, and GoDataBank product concerns.
- Review `backend/publisher/` and `backend/publishing/` as transitional legacy
  or product-layer candidates before source baseline acceptance.
- Exclude all backend `__pycache__/` and `.pyc` files.

## 7. Untracked Tests Candidate Review Plan

Untracked Python test candidates:

```text
tests/alis/test_chart_spec_export.py
tests/alis/test_cloudflare_upload_candidate_inspection.py
tests/alis/test_evidence_package_schema.py
tests/alis/test_evidence_to_visualisation_mapper.py
tests/alis/test_html_chart_embedding.py
tests/alis/test_minimal_chart_engine.py
tests/alis/test_multi_source_evidence.py
tests/alis/test_multi_source_observation_evidence.py
tests/alis/test_ons_connector.py
tests/alis/test_ons_observation_evidence.py
tests/alis/test_ons_observations.py
tests/alis/test_production_candidate_output_evidence.py
tests/alis/test_production_candidate_static_output.py
tests/alis/test_registry_integration.py
tests/alis/test_source_registry.py
tests/alis/test_static_chart_renderer.py
tests/alis/test_static_manifest_validation.py
tests/alis/test_static_publishing_pipeline.py
tests/alis/test_static_report_fragment.py
tests/alis/test_static_report_index.py
tests/alis/test_static_report_page.py
tests/alis/test_static_site_assembly.py
tests/alis/test_static_site_smoke_test.py
tests/alis/test_statistical_gatekeeper.py
tests/alis/test_svg_export_integration.py
tests/alis/test_visualisation_dataset_schema.py
tests/alis/test_world_bank_connector.py
```

Untracked test placeholders and documentation:

```text
tests/abacus/.gitkeep
tests/abacus/README.md
tests/integration/.gitkeep
tests/integration/README.md
```

Review approach:

- Do not move tests to `tests/alis_core/` or `tests/godatabank/` yet.
- Map each test to the accepted source owner before committing tests.
- Keep mixed pipeline and publishing tests as integration candidates until
  engine boundaries are explicit.
- Exclude all `tests/**/__pycache__/` and `tests/**/*.pyc` paths.

## 8. Engine Ownership Review Matrix

| Owner | Candidate paths | Review requirement |
| --- | --- | --- |
| Abacus | `backend/abacus/*`, `backend/alis/mappers/evidence_to_visualisation.py`, possible chart-spec files, possible `statistical_gatekeeper.py` | Confirm analysis-only ownership, validated inputs, chart-ready data, and no rendering/release behavior. |
| Arya | No strong current source path; possible future source-admission material | Do not infer implementation from docs alone; identify actual source proposal/admission code before baseline. |
| Hermes | `backend/alis/connectors/*.py`, duplicate connector paths, retrieval portions of pipelines | Confirm transport/retrieval-only behavior and no admission, validation, analysis, or publication decisions. |
| Thoth | `backend/alis/source_registry.py`, `sources/source_registry.json`, registry tests, provenance portions of pipelines | Resolve registry authority, storage policy, and source/provenance ownership before commit. |
| Aegis | `backend/validators/*`, `backend/alis/validators/statistical_gatekeeper.py`, manifest/upload inspection candidates | Separate gate decisions from schemas, analytical checks, and release/audit evidence. |
| Vyasa | No current untracked backend source observed in this inventory; prior summary outputs are generated artifacts | Do not commit generated summaries as source; identify narrative source before baseline. |
| Apollo | static rendering/export files, site assembly, publication package candidates | Confirm rendering/publication-package ownership and approved input requirements. |
| Argus | smoke test, production output evidence, audit/inspection evidence candidates | Separate observability/audit records from gate decisions and release approval. |

## 9. Shared-Service Candidate Review

Shared-service candidates include:

- `backend/alis/schemas/evidence_package.py`
- `backend/alis/schemas/visualisation_dataset.py`
- possible schema-support portions of `backend/validators/schema.py`

Review requirements:

- Confirm whether each schema is a shared support API or an engine-owned
  artifact contract.
- Ensure schema location does not imply canonical artifact ownership.
- Separate evidence package schemas from retrieved, validated, analysed, and
  publication artifact ownership.
- Defer any movement to `src/alis_core/shared/` until skeleton creation and
  migration are separately authorised.

## 10. GoDataBank Product-Layer Candidate Review

Potential GoDataBank product-layer candidates include:

- `backend/alis/publishing/static_report_fragment.py`
- `backend/alis/publishing/static_report_page.py`
- `backend/alis/publishing/static_report_index.py`
- `backend/alis/visualisation/html_chart_embedding.py`
- `backend/publishing/**`
- product-specific templates and generated publishing outputs, which remain
  excluded from source/test baseline staging.

Review requirements:

- Identify product-specific presentation, navigation, and template assumptions.
- Keep product-layer code separate from Apollo generic publication behavior.
- Do not migrate or rename product code under this plan.
- Do not commit generated product output as source.

## 11. Legacy/Transitional Candidate Review

Legacy or transitional candidates include:

- `backend/alis/ons_connector.py`
- possible `backend/alis/world_bank_connector.py` if present in later inventory
- `backend/publisher/**`
- `backend/publishing/**`
- `backend/validators/**`

Review requirements:

- Compare duplicate connectors before choosing canonical Hermes adapters.
- Determine whether old publisher and publishing folders are active, placeholder,
  product-layer, or legacy.
- Determine whether `backend/validators/**` is Aegis source, shared schema
  support, transitional legacy, or superseded.
- Do not delete or move any transitional file under this plan.

## 12. Source-Registry Authority Blocker

Source-registry authority is a blocker for any source/test baseline that touches
registry files.

Affected paths include:

- `sources/source_registry.json`
- `backend/alis/source_registry.py`
- `tests/alis/test_source_registry.py`
- `tests/alis/test_registry_integration.py`
- source-registry `.pyc` files under `__pycache__/`

Open questions:

- Is `sources/source_registry.json` canonical Thoth state, fixture data,
  generated data, or transitional prototype data?
- Should registry state live in source control, artifact storage, fixtures, or a
  runtime data store?
- Which tests verify Thoth registry behavior versus integration behavior?

Do not resolve these questions accidentally inside a broad source/test baseline
commit.

## 13. Line-Ending Review Blocker

Line-ending review remains open for:

- `backend/abacus/README.md`
- `backend/abacus/classifier.py`
- `backend/abacus/taxonomy.py`
- `backend/validators/README.md`
- `backend/validators/schema.py`
- `backend/validators/validator.py`
- `sources/source_registry.json`

Review requirements:

- Do not normalise line endings as part of source acceptance review.
- Do not mix line-ending-only churn with functional source review.
- Decide file retention and ownership before any line-ending remediation.
- Keep `.gitignore` unchanged unless a separate ignore-policy milestone is
  authorised.

## 14. Generated Artifact Exclusion

Generated artifacts must remain excluded from any source/test baseline review
commit.

Excluded generated artifact examples include:

- `evidence_package_output.json`
- generated classified data under `data/classified/`
- generated validated data under `data/validated/`
- generated publishing outputs under `data/publishing/`
- generated reports under `reports/generated/`
- generated manifests under `reports/` and `data/publishing/`

Artifact retention, archival, cleanup, or fixture promotion requires a separate
artifact-retention milestone.

## 15. Runtime Log Exclusion

Runtime logs must remain excluded from source/test baseline staging.

Known log paths include:

- `data/raw/world_bank/logs/world_bank_connector.log`
- `data/raw/ons/logs/ons_connector.log`
- `data/validated/validator.log`

Logs may be reviewed for short-term evidence retention, but they must not enter
a source/test baseline commit.

## 16. Data/Report Exclusion

Data and report outputs must remain excluded from source/test baseline staging.

Excluded groups include:

- `data/raw/**`
- `data/classified/**`
- `data/validated/**`
- `data/summaries/**`
- `data/publishing/**`
- `data/published/**`
- `reports/**`
- `evidence_package_output.json`

Data/report files may later become fixtures or archived evidence only through a
separate review and authorisation.

## 17. .pyc and __pycache__ Exclusion

The current working tree contains 100 untracked `.pyc` files and 100 untracked
paths under `__pycache__/`.

Rules:

- Exclude `**/*.pyc` from source/test baseline commits.
- Exclude `**/__pycache__/` from source/test baseline commits.
- Do not clean or delete these files under this plan.
- Do not modify `.gitignore` under this plan.
- Handle ignore policy and cleanup only through a separate milestone.

## 18. Skeleton-Folder Exclusion

The following target skeleton folders remain absent and must not be created by
this plan:

- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

Skeleton creation remains blocked until source/test ownership, artifact
disposition, source registry authority, line endings, and migration sequencing
are reviewed and separately authorised.

## 19. Proposed Source/Test Review Sequence

Recommended planning sequence:

1. Create a narrow source/test candidate classification register limited to
   source and test candidates, excluding artifacts, logs, data, reports, `.pyc`,
   and `__pycache__/`.
2. Review modified tracked source candidates separately from generated tracked
   artifacts.
3. Resolve source-registry authority before accepting registry data, registry
   source, or registry tests.
4. Review untracked backend source groups by owner: Hermes, Abacus, shared
   services, Apollo, Aegis, Argus, GoDataBank, and legacy.
5. Review test candidates after source owners are assigned.
6. Draft a future source/test baseline authorisation plan only after candidate
   ownership and exclusions are clear.

This sequence does not authorise execution.

## 20. Proposed Future Source/Test Baseline Commit Grouping

Potential future commit groups, subject to later review:

| Group | Possible scope | Status |
| --- | --- | --- |
| Group 1 | Accepted low-risk source candidates with clear ownership, such as isolated Hermes connectors or shared schemas | Future review only |
| Group 2 | Accepted tests matching Group 1 source ownership | Future review only |
| Group 3 | Abacus accepted source candidates and matching tests | Future review only |
| Group 4 | Apollo/product/legacy publishing candidates after boundary review | Future review only |
| Group 5 | Aegis/Argus/Thoth candidates after gate, audit, and registry authority review | Future review only |

No future group should include generated artifacts, logs, data/report outputs,
`.pyc` files, `__pycache__/`, `.gitignore`, skeleton folders, migration, or
implementation changes.

## 21. Files Explicitly Not Authorised for Staging

No files are authorised for staging by this plan.

Explicitly not authorised:

- all 13 modified tracked files;
- all untracked backend source candidates;
- all untracked test candidates;
- `sources/source_registry.json`;
- `backend/alis/source_registry.py`;
- `tests/alis/test_source_registry.py`;
- `tests/alis/test_registry_integration.py`;
- `data/**`;
- `reports/**`;
- `evidence_package_output.json`;
- runtime logs;
- `**/*.pyc`;
- `**/__pycache__/`;
- `.gitignore`;
- `src/`;
- `artifacts/`;
- `legacy/`;
- `docs/migration/`;
- `tests/alis_core/`;
- `tests/godatabank/`;
- this plan document until separately reviewed and authorised.

## 22. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Broad source commit preserves boundary debt | High | Review mixed folders file by file before authorisation. |
| Registry state is treated as canonical too early | High | Resolve Thoth source-registry authority first. |
| Product-specific publishing enters ALIS Core | Medium-high | Split Apollo and GoDataBank presentation concerns before baseline. |
| Generated artifacts enter source history | High | Keep artifacts, logs, reports, data, `.pyc`, and `__pycache__/` excluded. |
| Tests are committed before source ownership is clear | Medium | Map tests after source candidates are classified. |
| Line-ending churn obscures source review | Medium | Keep line-ending remediation separate from source acceptance. |
| Skeleton creation implies migration before review | High | Do not create skeleton folders until blockers are resolved. |

## 23. Abort Conditions

Any future source/test authorisation or execution should abort if:

- files are already staged before an authorised staging step begins;
- source, tests, generated artifacts, logs, data, reports, registry state, and
  documentation are mixed without explicit scope approval;
- any generated artifact, runtime log, `.pyc` file, or `__pycache__/` folder is
  proposed for source/test staging;
- `sources/source_registry.json` is proposed before registry authority is
  resolved;
- directory-level or glob-based staging is proposed for mixed folders;
- `.gitignore` modification is included without separate approval;
- skeleton folders are created;
- files are moved, renamed, deleted, cleaned, refactored, implemented, migrated,
  or restructured;
- imports are changed before migration is authorised;
- independent review requires revision.

## 24. Recommended Next Milestone

Recommended next milestone:

```text
Source/Test Candidate Classification Register v1.0
```

Purpose of the next milestone:

```text
Create a narrow source/test-only classification register for current modified
tracked source candidates, untracked backend source candidates, and untracked
test candidates, with generated artifacts, logs, data, reports, source-registry
state, bytecode, skeleton folders, migration, and implementation explicitly
excluded.
```

That milestone should remain planning-only and must not stage, commit, clean,
delete, move, rename, refactor, implement, migrate, restructure, create skeleton
folders, change imports, or modify `.gitignore`.

STATUS: SOURCE/TEST BASELINE REVIEW PLAN CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
