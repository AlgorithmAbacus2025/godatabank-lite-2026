# ALIS Core Source/Test Candidate Classification Register v1.0

## 1. Purpose

This register classifies the current modified tracked source/test-adjacent
candidates, untracked backend source candidates, and untracked test candidates
for future ALIS Core source/test baseline review.

This is a planning-only register. It does not authorise staging, commits,
cleanup, deletion, file movement, migration, skeleton creation, import changes,
refactoring, or implementation.

## 2. Source Documents Reviewed

The following source documents were reviewed:

- `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_TEST_BASELINE_REVIEW_PLAN_V1_0.md`
- `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md`
- `docs/reviews/ALIS_CORE_WORKING_TREE_RESOLUTION_PLAN_V1_0.md`

Current repository state was also inspected using read-only source-control and
filesystem checks.

## 3. Current Repository State

Observed state before this register was created:

| Item | Observed state |
| --- | --- |
| Staged files | None |
| Modified tracked files | 13 |
| Modified tracked source/test-adjacent candidates in scope | 6 |
| Untracked paths | 250 |
| Untracked backend paths | 81 |
| Untracked backend Python candidates, excluding `.pyc` | 27 |
| Untracked test paths | 83 |
| Untracked Python test candidates, excluding `.pyc` | 27 |
| Untracked `.pyc` files | 100 |
| Untracked paths under `__pycache__/` | 100 |
| Skeleton folders checked | Not present |

After creation, this register will become an additional untracked documentation
file until a later milestone explicitly reviews and authorises any disposition.

## 4. Classification Principles

The following principles apply:

- Classify source/test candidates only; do not convert generated artifacts into
  source/test candidates.
- Use the ALIS Core Boundary Register as the controlling ownership contract.
- Mark source-registry files and registry tests as blocked pending a Thoth
  authority decision.
- Mark line-ending warning files as blocked pending retention and ownership
  decisions.
- Do not resolve mixed engine boundaries inside this register.
- Do not stage, commit, move, rename, delete, clean, refactor, implement, or
  restructure anything under this register.
- Do not create target skeleton folders or change imports.
- Keep `.pyc`, `__pycache__/`, logs, generated data, and generated reports out
  of any future source/test baseline.

## 5. Classification Taxonomy

This register uses the following taxonomy:

| Classification | Meaning |
| --- | --- |
| Accepted-for-review candidate | Low-risk source/test candidate suitable for detailed review before possible later authorisation. |
| Review-before-decision | Candidate requires human review before acceptance, deferral, or rejection. |
| Boundary-blocked candidate | Candidate crosses or may cross engine/product/shared-service ownership boundaries. |
| Source-registry-blocked candidate | Candidate cannot be accepted until Thoth registry authority and storage policy are decided. |
| Line-ending-blocked candidate | Candidate has line-ending warnings and must wait for retention/ownership decision before line-ending remediation. |
| Generated-artifact excluded | Generated output; not a source/test candidate. |
| Runtime-log excluded | Runtime log; not a source/test candidate. |
| Data/report excluded | Data or report output; not a source/test candidate. |
| Bytecode/cache excluded | Python bytecode or cache folder; not a source/test candidate. |
| Legacy/transitional review | Candidate may be legacy, duplicate, placeholder, or transitional code. |
| Product-layer review | Candidate likely belongs to the GoDataBank product layer or needs product/core split review. |
| Test candidate pending source ownership | Test should not be accepted until matching source ownership is clear. |
| Do-not-stage | Explicitly not authorised for staging by this register. |

## 6. Modified Tracked Candidate Classification Table

| Path | Status | Primary classification | Candidate owner | Reason | Required decision |
| --- | --- | --- | --- | --- | --- |
| `backend/abacus/README.md` | Modified tracked | Line-ending-blocked candidate | Abacus documentation | Abacus-local documentation may need V1.0-R1 alignment and has line-ending review open. | Decide retain/update/reject and then handle line endings separately. |
| `backend/abacus/classifier.py` | Modified tracked | Line-ending-blocked candidate | Abacus | Existing classifier is an Abacus source candidate, but line-ending and source acceptance review remain open. | Decide accepted Abacus baseline source or reject/defer. |
| `backend/abacus/taxonomy.py` | Modified tracked | Line-ending-blocked candidate | Abacus | Taxonomy supports Abacus classification but may need governance review and line-ending review. | Decide accepted Abacus taxonomy source or reject/defer. |
| `backend/validators/README.md` | Modified tracked | Boundary-blocked candidate | Aegis, shared service, or legacy | Transitional validator documentation overlaps Aegis gates, shared schemas, and legacy status. | Decide owner/status before baseline; line endings remain blocked. |
| `backend/validators/schema.py` | Modified tracked | Boundary-blocked candidate | Shared service, Aegis, or legacy | Schema/validator source may be shared contract support, Aegis support, or superseded legacy. | Decide owner/status before baseline; line endings remain blocked. |
| `backend/validators/validator.py` | Modified tracked | Boundary-blocked candidate | Aegis or legacy | Validation source may predate Aegis and overlaps gate behavior. | Decide Aegis candidate, legacy, or rejection; line endings remain blocked. |

No modified tracked candidate is authorised for staging by this register.

## 7. Untracked Backend Source Candidate Classification Table

| Path | Primary classification | Candidate owner | Reason | Baseline readiness |
| --- | --- | --- | --- | --- |
| `backend/alis/connectors/ons.py` | Accepted-for-review candidate | Hermes | ONS adapter appears to be source retrieval/transport behavior. | Suitable for narrow Hermes review. |
| `backend/alis/connectors/world_bank.py` | Accepted-for-review candidate | Hermes | World Bank adapter appears to be source retrieval/transport behavior. | Suitable for narrow Hermes review. |
| `backend/alis/mappers/evidence_to_visualisation.py` | Accepted-for-review candidate | Abacus | Maps evidence to visualisation-ready analytical data. | Suitable after validated-input check. |
| `backend/alis/ons_connector.py` | Legacy/transitional review | Hermes or legacy | Duplicate connector path may overlap `backend/alis/connectors/ons.py`. | Not suitable until duplicate comparison. |
| `backend/alis/pipelines/multi_source_evidence.py` | Boundary-blocked candidate | Hermes, Thoth, Aegis, or runtime orchestration | Pipeline likely combines retrieval, evidence assembly, provenance, and validation handoffs. | Not suitable until split review. |
| `backend/alis/pipelines/multi_source_observation_evidence.py` | Boundary-blocked candidate | Hermes, Thoth, Aegis, or runtime orchestration | Multi-source observation flow likely crosses engine boundaries. | Not suitable until split review. |
| `backend/alis/pipelines/ons_observation_evidence.py` | Boundary-blocked candidate | Hermes, Thoth, Aegis, or runtime orchestration | ONS evidence path may mix retrieval and evidence packaging. | Not suitable until split review. |
| `backend/alis/publishing/cloudflare_upload_candidate_inspection.py` | Boundary-blocked candidate | Aegis or Argus | Upload inspection may be gate behavior or audit evidence. | Not suitable until gate/audit split. |
| `backend/alis/publishing/production_candidate_output_evidence.py` | Boundary-blocked candidate | Argus or Thoth | Output evidence may be audit record, provenance, or lineage. | Not suitable until evidence ownership review. |
| `backend/alis/publishing/production_candidate_static_output.py` | Product-layer review | Apollo or GoDataBank | Production candidate output may be product-specific publication packaging. | Not suitable until Apollo/product split. |
| `backend/alis/publishing/static_manifest_validation.py` | Boundary-blocked candidate | Aegis or Apollo | Manifest validation may be gate validation or publication-build validation. | Not suitable until owner split. |
| `backend/alis/publishing/static_publishing_pipeline.py` | Boundary-blocked candidate | Apollo, Aegis, Argus, or GoDataBank | Publishing pipeline likely crosses rendering, validation, audit, and product boundaries. | Not suitable until file-level boundary review. |
| `backend/alis/publishing/static_report_fragment.py` | Product-layer review | GoDataBank or Apollo | Report fragments may be product layout rather than generic publication artifact. | Not suitable until product/core split. |
| `backend/alis/publishing/static_report_index.py` | Product-layer review | GoDataBank or Apollo | Report index likely includes product navigation/presentation concerns. | Not suitable until product/core split. |
| `backend/alis/publishing/static_report_page.py` | Product-layer review | GoDataBank or Apollo | Report page assembly may be product-specific presentation. | Not suitable until product/core split. |
| `backend/alis/publishing/static_site_assembly.py` | Review-before-decision | Apollo or GoDataBank | Static site assembly may be generic Apollo packaging or product output. | Needs approved-input and product/core review. |
| `backend/alis/publishing/static_site_smoke_test.py` | Boundary-blocked candidate | Argus or integration test support | Smoke testing may be observability evidence or test support. | Not suitable until Argus/test split. |
| `backend/alis/schemas/evidence_package.py` | Accepted-for-review candidate | Shared service | Schema support candidate for evidence package contracts. | Suitable for narrow shared-schema review. |
| `backend/alis/schemas/visualisation_dataset.py` | Accepted-for-review candidate | Shared service or Abacus contract support | Schema support candidate for visualisation-ready dataset contracts. | Suitable after artifact ownership check. |
| `backend/alis/source_registry.py` | Source-registry-blocked candidate | Thoth | Registry implementation cannot be accepted until registry authority is decided. | Blocked. |
| `backend/alis/validators/statistical_gatekeeper.py` | Boundary-blocked candidate | Abacus or Aegis | Statistical gatekeeping may be analytical checking or governance gate enforcement. | Not suitable until owner split. |
| `backend/alis/visualisation/chart_spec_export.py` | Boundary-blocked candidate | Abacus or Apollo | Chart specification and export/rendering ownership are distinct. | Not suitable until artifact owner decision. |
| `backend/alis/visualisation/html_chart_embedding.py` | Product-layer review | GoDataBank or Apollo | HTML embedding may be product presentation or generic rendering support. | Not suitable until product/core split. |
| `backend/alis/visualisation/minimal_chart_engine.py` | Boundary-blocked candidate | Abacus or Apollo | May combine chart specification and rendering. | Not suitable until artifact owner decision. |
| `backend/alis/visualisation/static_chart_renderer.py` | Accepted-for-review candidate | Apollo | Static chart rendering aligns with Apollo publication responsibilities. | Suitable for narrow Apollo review. |
| `backend/alis/visualisation/svg_export_integration.py` | Accepted-for-review candidate | Apollo | SVG export integration aligns with Apollo rendering/export concerns. | Suitable after approved-input check. |
| `backend/publisher/html_publisher.py` | Legacy/transitional review | Apollo, GoDataBank, or legacy | Older publisher path may be superseded or still active. | Not suitable until active/legacy decision. |
| `backend/publisher/README.md` | Legacy/transitional review | Apollo, GoDataBank, or legacy | Documentation for older publisher path. | Not suitable until active/legacy decision. |
| `backend/publishing/README.md` | Product-layer review | GoDataBank or legacy | Placeholder/product publishing structure has unclear status. | Not suitable until product/legacy decision. |
| `backend/publishing/api_routes/.gitkeep` | Product-layer review | GoDataBank or placeholder | API route placeholder is product-facing or empty structure. | Do not stage until skeleton policy exists. |
| `backend/publishing/html_export/.gitkeep` | Product-layer review | GoDataBank or placeholder | HTML export placeholder may imply future structure. | Do not stage until skeleton policy exists. |
| `backend/publishing/pdf_export/.gitkeep` | Product-layer review | GoDataBank or placeholder | PDF export placeholder may imply future structure. | Do not stage until skeleton policy exists. |
| `backend/publishing/report_builder/.gitkeep` | Product-layer review | GoDataBank or placeholder | Report builder placeholder may imply future structure. | Do not stage until skeleton policy exists. |

## 8. Untracked Test Candidate Classification Table

| Path | Primary classification | Candidate owner | Reason | Baseline readiness |
| --- | --- | --- | --- | --- |
| `tests/alis/test_chart_spec_export.py` | Test candidate pending source ownership | Abacus or Apollo | Source owner for chart spec/export is unresolved. | Not suitable until source owner decision. |
| `tests/alis/test_cloudflare_upload_candidate_inspection.py` | Test candidate pending source ownership | Aegis or Argus | Upload inspection may be gate or audit behavior. | Not suitable until source owner decision. |
| `tests/alis/test_evidence_package_schema.py` | Test candidate pending source ownership | Shared service | Schema source candidate is likely shared service. | Suitable after schema ownership check. |
| `tests/alis/test_evidence_to_visualisation_mapper.py` | Test candidate pending source ownership | Abacus | Matches Abacus mapper candidate. | Suitable after mapper source review. |
| `tests/alis/test_html_chart_embedding.py` | Product-layer review | GoDataBank or Apollo | HTML embedding may be product presentation. | Not suitable until product/core split. |
| `tests/alis/test_minimal_chart_engine.py` | Test candidate pending source ownership | Abacus or Apollo | Minimal chart engine ownership is unresolved. | Not suitable until source owner decision. |
| `tests/alis/test_multi_source_evidence.py` | Test candidate pending source ownership | Integration or mixed engines | Multi-source evidence crosses Hermes, Thoth, Aegis, and runtime boundaries. | Not suitable until split review. |
| `tests/alis/test_multi_source_observation_evidence.py` | Test candidate pending source ownership | Integration or mixed engines | Observation evidence likely crosses multiple engine boundaries. | Not suitable until split review. |
| `tests/alis/test_ons_connector.py` | Test candidate pending source ownership | Hermes | Matches ONS connector candidates. | Suitable after duplicate connector review. |
| `tests/alis/test_ons_observation_evidence.py` | Test candidate pending source ownership | Hermes, Thoth, Aegis, or integration | Evidence flow ownership is mixed. | Not suitable until split review. |
| `tests/alis/test_ons_observations.py` | Test candidate pending source ownership | Hermes or integration | Observation retrieval may be connector or integration behavior. | Suitable only after source owner decision. |
| `tests/alis/test_production_candidate_output_evidence.py` | Test candidate pending source ownership | Argus or Thoth | Evidence output source ownership is unresolved. | Not suitable until owner decision. |
| `tests/alis/test_production_candidate_static_output.py` | Product-layer review | GoDataBank or Apollo | Production candidate output may be product publication. | Not suitable until product/core split. |
| `tests/alis/test_registry_integration.py` | Source-registry-blocked candidate | Thoth or integration | Registry authority and integration boundary are unresolved. | Blocked. |
| `tests/alis/test_source_registry.py` | Source-registry-blocked candidate | Thoth | Registry source and storage policy are unresolved. | Blocked. |
| `tests/alis/test_static_chart_renderer.py` | Test candidate pending source ownership | Apollo | Matches Apollo static renderer candidate. | Suitable after renderer source review. |
| `tests/alis/test_static_manifest_validation.py` | Test candidate pending source ownership | Aegis or Apollo | Manifest validation owner is unresolved. | Not suitable until owner decision. |
| `tests/alis/test_static_publishing_pipeline.py` | Test candidate pending source ownership | Integration or mixed engines | Publishing pipeline crosses product/core/gate/audit boundaries. | Not suitable until split review. |
| `tests/alis/test_static_report_fragment.py` | Product-layer review | GoDataBank or Apollo | Static report fragment may be product presentation. | Not suitable until product/core split. |
| `tests/alis/test_static_report_index.py` | Product-layer review | GoDataBank or Apollo | Static report index may be product navigation. | Not suitable until product/core split. |
| `tests/alis/test_static_report_page.py` | Product-layer review | GoDataBank or Apollo | Static report page may be product presentation. | Not suitable until product/core split. |
| `tests/alis/test_static_site_assembly.py` | Test candidate pending source ownership | Apollo, GoDataBank, or integration | Site assembly ownership is unresolved. | Not suitable until owner decision. |
| `tests/alis/test_static_site_smoke_test.py` | Test candidate pending source ownership | Argus or integration | Smoke testing may be observability or test-only. | Not suitable until owner decision. |
| `tests/alis/test_statistical_gatekeeper.py` | Test candidate pending source ownership | Abacus or Aegis | Statistical gatekeeper source ownership is unresolved. | Not suitable until owner decision. |
| `tests/alis/test_svg_export_integration.py` | Test candidate pending source ownership | Apollo or integration | SVG export aligns with Apollo but may be integration. | Suitable after source owner decision. |
| `tests/alis/test_visualisation_dataset_schema.py` | Test candidate pending source ownership | Shared service or Abacus | Visualisation dataset schema ownership must be confirmed. | Suitable after schema owner decision. |
| `tests/alis/test_world_bank_connector.py` | Test candidate pending source ownership | Hermes | Matches World Bank connector candidate. | Suitable after connector source review. |
| `tests/abacus/.gitkeep` | Do-not-stage | Test placeholder | Placeholder could imply target structure before skeleton policy. | Do not stage under this register. |
| `tests/abacus/README.md` | Review-before-decision | Abacus test documentation | Existing test documentation may need boundary alignment. | Review before any test baseline. |
| `tests/integration/.gitkeep` | Do-not-stage | Test placeholder | Placeholder could imply structure before test migration policy. | Do not stage under this register. |
| `tests/integration/README.md` | Review-before-decision | Integration test documentation | Integration test policy is not yet defined. | Review before any test baseline. |

## 9. Engine Ownership Classification Summary

| Owner | Candidate status summary |
| --- | --- |
| Abacus | `backend/abacus/*`, mapper source, and matching mapper/chart/statistical tests require Abacus review; Abacus tracked files are line-ending-blocked. |
| Arya | No direct source candidate is accepted; source admission behavior is not explicit in current backend candidates. |
| Hermes | Connector package candidates are the clearest accepted-for-review group; duplicate connector paths and connector tests need comparison. |
| Thoth | Registry implementation, registry data, and registry tests are source-registry-blocked. |
| Aegis | Validator, gate, upload inspection, and manifest validation candidates are boundary-blocked until gate responsibilities are separated. |
| Vyasa | No source candidate is accepted in this scoped inventory; generated summaries remain excluded artifacts. |
| Apollo | Static renderer and SVG export are accepted-for-review; chart-spec, chart-engine, site assembly, and publishing candidates need boundary/product review. |
| Argus | Smoke test and output-evidence candidates require audit/observability versus gate/product split review. |

## 10. Shared-Service Candidate Summary

Shared-service accepted-for-review candidates:

- `backend/alis/schemas/evidence_package.py`
- `backend/alis/schemas/visualisation_dataset.py`, pending artifact ownership check

Shared-service review-before-decision candidate:

- `backend/validators/schema.py`, because it may be shared schema support,
  Aegis support, or transitional legacy.

No shared-service candidate is authorised for staging.

## 11. GoDataBank Product-Layer Candidate Summary

Product-layer review candidates include:

- `backend/alis/publishing/static_report_fragment.py`
- `backend/alis/publishing/static_report_index.py`
- `backend/alis/publishing/static_report_page.py`
- `backend/alis/publishing/production_candidate_static_output.py`
- `backend/alis/visualisation/html_chart_embedding.py`
- `backend/publishing/**`
- related static report, HTML embedding, and production output tests.

These candidates are not suitable for ALIS Core baseline until product-specific
presentation concerns are separated from Apollo generic publication behavior.

## 12. Legacy/Transitional Candidate Summary

Legacy/transitional candidates include:

- `backend/alis/ons_connector.py`
- `backend/publisher/html_publisher.py`
- `backend/publisher/README.md`
- `backend/publishing/**` placeholders, if not product-layer candidates
- `backend/validators/**`, if not accepted as Aegis/shared-service candidates

These candidates require active-vs-superseded review before any baseline
authorisation.

## 13. Source-Registry Blocked Candidates

The following candidates are blocked pending a Thoth source-registry authority
decision:

- `sources/source_registry.json`
- `backend/alis/source_registry.py`
- `tests/alis/test_source_registry.py`
- `tests/alis/test_registry_integration.py`
- any registry-related `.pyc` files under `__pycache__/`

Open authority questions:

- Is `sources/source_registry.json` canonical Thoth state, fixture data,
  generated artifact, or transitional prototype data?
- Should registry state be source-controlled, stored as fixture data, or stored
  outside source control?
- Which tests prove Thoth registry behavior versus cross-engine integration?

No registry candidate is authorised for staging.

## 14. Line-Ending Blocked Candidates

Line-ending review remains blocked for:

- `backend/abacus/README.md`
- `backend/abacus/classifier.py`
- `backend/abacus/taxonomy.py`
- `backend/validators/README.md`
- `backend/validators/schema.py`
- `backend/validators/validator.py`
- `sources/source_registry.json`

Line endings must not be remediated until each file's retention, ownership, and
baseline disposition are decided.

## 15. Generated Artifact Exclusions

Generated artifacts are excluded from this source/test classification scope.

Excluded examples include:

- `evidence_package_output.json`
- `data/classified/**`
- `data/validated/**`
- `data/publishing/**`
- `data/published/**`
- generated manifests
- generated HTML reports

Generated artifacts require a separate artifact-retention or cleanup review.

## 16. Runtime Log Exclusions

Runtime logs are excluded from source/test candidate classification.

Known excluded logs include:

- `data/raw/world_bank/logs/world_bank_connector.log`
- `data/raw/ons/logs/ons_connector.log`
- `data/validated/validator.log`

Runtime logs must not enter any source/test baseline commit.

## 17. Data/Report Exclusions

Data and report outputs are excluded from this register except as explicit
do-not-stage exclusions.

Excluded groups include:

- `data/raw/**`
- `data/classified/**`
- `data/validated/**`
- `data/summaries/**`
- `data/publishing/**`
- `data/published/**`
- `reports/**`
- `evidence_package_output.json`

These paths may be reviewed later as fixtures, retained evidence, generated
artifacts, archive-later candidates, or delete-later-with-approval candidates.

## 18. .pyc and __pycache__ Exclusions

The current working tree includes 100 untracked `.pyc` files and 100 untracked
paths under `__pycache__/`.

Classification:

- `**/*.pyc`: Bytecode/cache excluded.
- `**/__pycache__/`: Bytecode/cache excluded.

These paths must not be staged, committed, cleaned, or deleted under this
register. Ignore policy and cleanup require separate approval.

## 19. Skeleton-Folder Exclusions

The following skeleton folders remain excluded and were not present during this
review:

- `src/`
- `artifacts/`
- `legacy/`
- `docs/migration/`
- `tests/alis_core/`
- `tests/godatabank/`

This register does not authorise skeleton creation.

## 20. Candidate Groups Suitable for Later Narrow Review

The following groups are suitable for later narrow review, not execution:

| Candidate group | Rationale |
| --- | --- |
| Hermes connector package candidates | `backend/alis/connectors/ons.py` and `world_bank.py` have clear retrieval/transport alignment, pending duplicate comparison. |
| Shared schema candidates | `backend/alis/schemas/*.py` are narrow and likely shared support, pending artifact ownership check. |
| Abacus mapper candidate | `backend/alis/mappers/evidence_to_visualisation.py` has a plausible Abacus role, pending validated-input check. |
| Apollo renderer/export candidates | `static_chart_renderer.py` and `svg_export_integration.py` have plausible Apollo roles, pending approved-input check. |
| Matching narrow tests | Connector, schema, mapper, renderer, and SVG tests may be reviewed after matching source ownership is accepted. |

These groups still require independent review and later authorisation before
any staging.

## 21. Candidate Groups Not Suitable for Baseline Yet

The following groups are not suitable for baseline yet:

- all source-registry candidates;
- all line-ending-blocked tracked source/test-adjacent candidates;
- `backend/alis/pipelines/**`;
- most `backend/alis/publishing/**`;
- product-layer static report/page/index/HTML embedding candidates;
- `backend/validators/**`;
- duplicate or legacy connector/publisher paths;
- mixed publishing, production-output, gate, audit, and integration tests;
- test placeholders and skeleton-like `.gitkeep` files.

These groups require boundary, ownership, source-registry, product/legacy, or
line-ending decisions before any source/test baseline authorisation.

## 22. Files Explicitly Not Authorised for Staging

No files are authorised for staging by this register.

Explicitly not authorised:

- all modified tracked source/test-adjacent candidates;
- all untracked backend source candidates;
- all untracked test candidates;
- all source-registry candidates;
- all generated artifacts;
- all runtime logs;
- all data/report outputs;
- all `.pyc` files;
- all `__pycache__/` folders;
- `.gitignore`;
- `src/`;
- `artifacts/`;
- `legacy/`;
- `docs/migration/`;
- `tests/alis_core/`;
- `tests/godatabank/`;
- this register document until separately reviewed and authorised.

## 23. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Boundary-blocked code is accepted too early | High | Require file-level ownership review before baseline authorisation. |
| Source registry authority is resolved accidentally | High | Keep registry candidates blocked pending Thoth authority decision. |
| Line-ending churn hides source changes | Medium | Keep line-ending remediation separate from retention/ownership review. |
| Product-layer code enters ALIS Core | Medium-high | Split GoDataBank presentation from Apollo generic publication behavior. |
| Generated artifacts or bytecode enter source history | High | Keep artifacts, logs, data, reports, `.pyc`, and `__pycache__/` excluded. |
| Tests are baselined before source ownership is clear | Medium | Review tests after matching source candidates are accepted. |

## 24. Abort Conditions

Any future source/test review, authorisation, or execution should abort if:

- files are already staged before an authorised staging step begins;
- a proposed baseline includes files outside its explicit authorisation scope;
- generated artifacts, logs, data, reports, `.pyc`, or `__pycache__/` paths are
  proposed for staging;
- source-registry candidates are proposed before Thoth authority is decided;
- line-ending remediation is mixed with source acceptance;
- directory-level or glob-based staging is proposed for mixed folders;
- skeleton folders are created;
- files are moved, renamed, deleted, cleaned, refactored, implemented, migrated,
  or restructured;
- imports are changed;
- `.gitignore` is modified without separate approval;
- independent review requires revision.

## 25. Recommended Next Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Source/Test Candidate Classification Register v1.0
```

After independent review, the next planning milestone should be one of:

```text
Source-Registry Authority Decision v1.0
```

or:

```text
Low-Risk Source/Test Baseline Authorisation Plan v1.0
```

Both options must remain planning or authorisation only until a separate
execution milestone is explicitly approved.

STATUS: SOURCE/TEST CANDIDATE CLASSIFICATION REGISTER CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
