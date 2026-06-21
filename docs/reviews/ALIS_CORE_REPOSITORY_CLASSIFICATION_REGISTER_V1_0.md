# ALIS Core Repository Classification Register v1.0

## 1. Purpose

This register classifies the current GoDataBank repository at folder and file
level against the ALIS Core Boundary Register v1.0-R1 and the repository
architecture migration plan.

This is a classification review only. It does not move, rename, delete, refactor
or clean any file. It does not change imports, implement engines, restructure
the repository, or remove generated artifacts.

The purpose is to make future migration safer by identifying the likely owner,
future location, movement status, and risk for each relevant current path.

## 2. Source Documents Reviewed

| Document | Role |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing engine boundary register, revision V1.0-R1. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Target repository structure and migration planning source. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Current repository audit, technical debt assessment, and inventory evidence. |

Repository inventory was inspected using read-only file listing. No tests were
run for this classification milestone.

## 3. Classification Taxonomy

Allowed classifications:

| Classification | Meaning |
| --- | --- |
| ALIS Core engine candidate | Existing path appears to belong to one ALIS Core engine after review. |
| ALIS Core shared service candidate | Existing path appears to provide shared contracts, schemas, config, utilities, or runtime support rather than engine-owned behavior. |
| GoDataBank product layer | Existing path appears product-specific: report presentation, product templates, public pages, local publishing surfaces, or GoDataBank-specific workflows. |
| Contract or governance document | Existing path records architecture, contracts, policy, source admission, citation, exclusion, or governance rules. |
| Review or audit evidence | Existing path records milestone reviews, audit findings, freeze evidence, or planning evidence. |
| Generated artifact | Existing path is runtime output, report output, generated data, log output, bytecode cache, or production-candidate artifact. |
| Fixture or test data | Existing path is a test, test README, or data used to verify behavior. |
| Transitional legacy | Existing path appears superseded, duplicated, placeholder, or older implementation that must be reviewed before migration. |
| Deletion candidate requiring separate approval | Existing path appears generated or obsolete enough to be cleaned later, but must not be deleted without explicit approval. |
| Unknown / requires human review | Existing path cannot be confidently classified from documentation and static inventory alone. |

Movement statuses:

| Movement status | Meaning |
| --- | --- |
| Remain | Keep in place for now and potentially long term. |
| Move later | Likely future move after approval, import planning, and tests. |
| Review before movement | Do not move until ownership, imports, and behavior are reviewed. |
| Do not move | Must remain in place or must not be migrated as part of architecture work. |
| Deletion candidate requiring approval | Do not delete now; review and approve separately before cleanup. |

Confidence levels:

| Confidence | Meaning |
| --- | --- |
| High | Ownership is clear from path, current behavior, and boundary register. |
| Medium | Ownership is plausible but needs code-level or import-level confirmation. |
| Low | Ownership is ambiguous or path may combine several responsibilities. |

## 4. File/Folder Classification Table

| Current path | Proposed classification | Proposed future location, if known | Confidence | Reason for classification | Movement status | Risk notes |
| --- | --- | --- | --- | --- | --- | --- |
| `.agents/` | Unknown / requires human review | TBD | Low | Local agent configuration is outside ALIS Core runtime boundaries. | Do not move | Moving could affect local tooling. |
| `.git/` | Unknown / requires human review | Not applicable | High | Repository metadata, not architecture source. | Do not move | Must not be touched by migration planning. |
| `README.md` | Unknown / requires human review | `README.md` | Medium | Project entrypoint is reported as outdated and needs later source-of-truth alignment. | Remain | Updating too early could misrepresent approved architecture. |
| `backend/` | Transitional legacy | `src/alis_core/`, `src/godatabank/`, or `legacy/backend/` | Medium | Current backend mixes ALIS Core, product, publishing, validation, and legacy candidates. | Review before movement | Moving the whole folder would violate engine boundaries. |
| `backend/abacus/` | ALIS Core engine candidate | `src/alis_core/engines/abacus/` | High | Existing named Abacus folder maps to Abacus engine. | Move later | Imports and tests must be updated only in a future migration. |
| `backend/abacus/classifier.py` | ALIS Core engine candidate: Abacus | `src/alis_core/engines/abacus/classifier.py` | High | Classification behavior is analytical and Abacus-owned. | Move later | Confirm no hidden dependency on current path. |
| `backend/abacus/taxonomy.py` | ALIS Core engine candidate: Abacus | `src/alis_core/engines/abacus/taxonomy.py` | High | Taxonomy supports classification and analytical organization. | Move later | Taxonomy governance may later need Aegis review. |
| `backend/abacus/README.md` | Contract or governance document | `src/alis_core/engines/abacus/README.md` or `docs/contracts/engines/abacus/` | Medium | Engine-local documentation for existing Abacus candidate. | Review before movement | May be outdated relative to V1.0-R1. |
| `backend/alis/` | Transitional legacy | Split across `src/alis_core/engines/`, `src/alis_core/shared/`, and `src/godatabank/` | High | Audit confirms this folder contains several engine and product responsibilities. | Review before movement | Must not be moved wholesale. |
| `backend/alis/README.md` | Transitional legacy | `docs/migration/` or engine README after review | Low | Placeholder or broad ALIS documentation predates V1.0-R1 boundaries. | Review before movement | May conflict with engine-specific ownership. |
| `backend/alis/config.py` | ALIS Core shared service candidate | `src/alis_core/shared/config/` | Medium | Configuration is a shared service in the boundary register. | Move later | Must not become a hidden cross-engine control plane. |
| `backend/alis/source_registry.py` | ALIS Core engine candidate: Thoth | `src/alis_core/engines/thoth/` | Medium | Canonical source registry ownership belongs to Thoth. | Review before movement | Must separate source admission inputs from canonical registry state. |
| `backend/alis/world_bank_connector.py` | Transitional legacy | Review against `src/alis_core/engines/hermes/adapters/` | Low | Duplicates newer connector package path. | Review before movement | May contain older metadata/archive behavior still needed. |
| `backend/alis/ons_connector.py` | Transitional legacy | Review against `src/alis_core/engines/hermes/adapters/` | Low | Duplicates newer connector package path. | Review before movement | May contain older metadata/archive behavior still needed. |
| `backend/alis/connectors/` | ALIS Core engine candidate: Hermes | `src/alis_core/engines/hermes/adapters/` | High | Connectors execute external source retrieval and transport. | Move later | Ensure source admission stays with Arya and validation stays with Aegis. |
| `backend/alis/connectors/world_bank.py` | ALIS Core engine candidate: Hermes | `src/alis_core/engines/hermes/adapters/world_bank.py` | High | World Bank adapter is transport/retrieval behavior. | Move later | Must not encode admission, validation, or analysis decisions. |
| `backend/alis/connectors/ons.py` | ALIS Core engine candidate: Hermes | `src/alis_core/engines/hermes/adapters/ons.py` | High | ONS adapter is transport/retrieval behavior. | Move later | Must not encode admission, validation, or analysis decisions. |
| `backend/alis/pipelines/` | Unknown / requires human review | Split across engines and `src/alis_core/runtime/orchestration/` | Low | Pipelines likely combine retrieval, packaging, provenance, and validation handoffs. | Review before movement | High risk of moving mixed responsibilities into one engine. |
| `backend/alis/pipelines/multi_source_evidence.py` | Unknown / requires human review | Hermes/Aegis/Thoth/runtime split | Low | Multi-source evidence assembly may combine transport, evidence package creation, and provenance. | Review before movement | Could violate single-builder artifact ownership. |
| `backend/alis/pipelines/multi_source_observation_evidence.py` | Unknown / requires human review | Hermes/Aegis/Thoth/runtime split | Low | Observation evidence pipeline likely crosses multiple engine boundaries. | Review before movement | Requires artifact-by-artifact ownership review. |
| `backend/alis/pipelines/ons_observation_evidence.py` | Unknown / requires human review | Hermes/Aegis/Thoth/runtime split | Low | ONS observation evidence path may combine retrieval and evidence packaging. | Review before movement | Needs separation of Hermes Retrieved Evidence Package and Aegis Validated Evidence Package. |
| `backend/alis/schemas/` | ALIS Core shared service candidate | `src/alis_core/shared/schemas/` and `docs/contracts/artifacts/` | Medium | Schemas are shared contracts but each artifact still has a canonical builder. | Review before movement | Schema location must not imply artifact ownership. |
| `backend/alis/schemas/evidence_package.py` | ALIS Core shared service candidate | `src/alis_core/shared/schemas/evidence_package.py` and `docs/contracts/artifacts/` | Medium | Evidence package schema supports Hermes/Aegis/Thoth boundaries. | Review before movement | Must distinguish Retrieved Evidence Package from Validated Evidence Package. |
| `backend/alis/schemas/visualisation_dataset.py` | ALIS Core shared service candidate | `src/alis_core/shared/schemas/visualisation_dataset.py` or Abacus contract schema | Medium | Visualisation-ready data is likely Abacus output schema. | Review before movement | Could incorrectly pull rendering concerns into Abacus. |
| `backend/alis/validators/` | ALIS Core engine candidate | `src/alis_core/engines/abacus/` or `src/alis_core/engines/aegis/` | Low | Statistical gatekeeping may be analytical checking or governance gate enforcement. | Review before movement | Validation term is overloaded. |
| `backend/alis/validators/statistical_gatekeeper.py` | ALIS Core engine candidate: Abacus or Aegis | TBD after review | Low | Statistical checks align with Abacus, but gatekeeping language aligns with Aegis. | Review before movement | Misclassification could blur analysis and approval gates. |
| `backend/alis/mappers/` | ALIS Core engine candidate: Abacus | `src/alis_core/engines/abacus/` | Medium | Mapping evidence to chart-ready data appears analytical transformation. | Move later | Confirm it does not render or publish. |
| `backend/alis/mappers/evidence_to_visualisation.py` | ALIS Core engine candidate: Abacus | `src/alis_core/engines/abacus/evidence_to_visualisation.py` | Medium | Produces visualisation-ready analytical data from evidence. | Move later | Must avoid consuming unvalidated evidence. |
| `backend/alis/visualisation/` | ALIS Core engine candidate | Split between Abacus and Apollo | Low | Contains chart specification and rendering/export behavior. | Review before movement | Chart specification and rendered artifacts have different owners. |
| `backend/alis/visualisation/chart_spec_export.py` | ALIS Core engine candidate: Abacus or Apollo | TBD after review | Low | Could be chart specification output or rendering/export support. | Review before movement | Needs split by artifact owner. |
| `backend/alis/visualisation/minimal_chart_engine.py` | ALIS Core engine candidate: Abacus or Apollo | TBD after review | Low | May produce chart spec and/or rendered chart output. | Review before movement | Could mix analysis artifact and publication artifact generation. |
| `backend/alis/visualisation/static_chart_renderer.py` | ALIS Core engine candidate: Apollo | `src/alis_core/engines/apollo/` | High | Static chart rendering is publication/rendering responsibility. | Move later | Must only render approved artifacts. |
| `backend/alis/visualisation/html_chart_embedding.py` | GoDataBank product layer or ALIS Core engine candidate: Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | HTML embedding may be generic rendering or product presentation. | Review before movement | Product template assumptions may be hidden. |
| `backend/alis/visualisation/svg_export_integration.py` | ALIS Core engine candidate: Apollo | `src/alis_core/engines/apollo/` | Medium | SVG export integrates rendered publication artifacts. | Move later | Must not validate or alter analysis. |
| `backend/alis/publishing/` | Unknown / requires human review | Split across Apollo, Aegis, Argus, Thoth, and GoDataBank | Low | Publishing folder contains rendering, validation, evidence capture, upload inspection, and product output. | Review before movement | Highest product/core coupling risk. |
| `backend/alis/publishing/static_report_fragment.py` | GoDataBank product layer or ALIS Core engine candidate: Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | Report fragments may be product-specific layout or generic publication components. | Review before movement | Hidden GoDataBank assumptions likely. |
| `backend/alis/publishing/static_report_page.py` | GoDataBank product layer or ALIS Core engine candidate: Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | Report page assembly may be product page composition. | Review before movement | Must not alter analytical findings or caveats. |
| `backend/alis/publishing/static_report_index.py` | GoDataBank product layer | `src/godatabank/publishing/` | Medium | Report index likely product navigation/presentation. | Review before movement | Could contain generic Apollo manifest behavior. |
| `backend/alis/publishing/static_manifest_validation.py` | ALIS Core engine candidate: Aegis or Apollo | TBD after review | Low | Manifest validation may be Aegis gate behavior; manifest creation belongs to Apollo. | Review before movement | Must separate validation from publication building. |
| `backend/alis/publishing/static_site_assembly.py` | ALIS Core engine candidate: Apollo | `src/alis_core/engines/apollo/` | Medium | Static site assembly creates publication bundles. | Move later | Product-specific site structure must be checked. |
| `backend/alis/publishing/static_publishing_pipeline.py` | Unknown / requires human review | Split across Apollo, Aegis, Argus, and product layer | Low | Pipeline likely crosses rendering, validation, audit, and release concerns. | Review before movement | Moving as-is would preserve boundary debt. |
| `backend/alis/publishing/static_site_smoke_test.py` | ALIS Core engine candidate: Argus or Fixture or test data | `src/alis_core/engines/argus/` or `tests/` | Low | Smoke testing can be observability evidence or test support. | Review before movement | Do not confuse audit evidence with release approval. |
| `backend/alis/publishing/production_candidate_static_output.py` | GoDataBank product layer or ALIS Core engine candidate: Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | Production candidate output may be product-specific publication packaging. | Review before movement | Release gate and product assumptions require review. |
| `backend/alis/publishing/production_candidate_output_evidence.py` | ALIS Core engine candidate: Argus or Thoth | `src/alis_core/engines/argus/` or `src/alis_core/engines/thoth/` | Low | Evidence capture may be audit record, provenance, or lineage. | Review before movement | Must not invent audit or lineage data. |
| `backend/alis/publishing/cloudflare_upload_candidate_inspection.py` | ALIS Core engine candidate: Aegis or Argus | `src/alis_core/engines/aegis/` or `src/alis_core/engines/argus/` | Low | Upload inspection is governance/release gate and audit-adjacent. | Review before movement | Deployment approval must remain explicit. |
| `backend/publisher/` | Transitional legacy | `legacy/backend/publisher/` or Apollo after review | Low | Older publisher layer overlaps with current ALIS publishing. | Review before movement | May be superseded but not proven dead. |
| `backend/publisher/html_publisher.py` | Transitional legacy | `legacy/backend/publisher/html_publisher.py` or Apollo | Low | Older HTML publisher candidate. | Review before movement | Dead-code status must be proven before deletion. |
| `backend/publisher/README.md` | Transitional legacy | `legacy/backend/publisher/README.md` | Low | Documentation for older publisher candidate. | Review before movement | May be stale. |
| `backend/publishing/` | Transitional legacy or GoDataBank product layer | `src/godatabank/publishing/` or `legacy/backend/publishing/` | Low | Placeholder or product-facing publishing structure. | Review before movement | Empty/placeholder folders can mislead target architecture. |
| `backend/publishing/README.md` | Transitional legacy | `legacy/backend/publishing/README.md` | Low | Audit identifies this as placeholder or transitional. | Review before movement | Must not be treated as authoritative contract. |
| `backend/publishing/api_routes/` | GoDataBank product layer | `src/godatabank/web/` or `src/godatabank/publishing/` | Low | API routes are product/application surface, not ALIS Core engine. | Review before movement | Need code inventory before target is final. |
| `backend/publishing/html_export/` | GoDataBank product layer or Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | HTML export may be product output or generic renderer. | Review before movement | Same publication boundary risk as ALIS publishing. |
| `backend/publishing/pdf_export/` | GoDataBank product layer or Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | PDF export may be product output or generic renderer. | Review before movement | Must only use approved publication packages. |
| `backend/publishing/report_builder/` | GoDataBank product layer or Apollo | `src/godatabank/publishing/` or `src/alis_core/engines/apollo/` | Low | Report builder may combine product layout and publication assembly. | Review before movement | Risk of mixing narrative, analysis, and rendering responsibilities. |
| `backend/summary/` | ALIS Core engine candidate: Vyasa | `src/alis_core/engines/vyasa/` | Medium | Summary generation is closest to narrative synthesis. | Move later | Must enforce claim-to-evidence and approved-analysis inputs. |
| `backend/summary/summary_generator.py` | ALIS Core engine candidate: Vyasa | `src/alis_core/engines/vyasa/summary_generator.py` | Medium | Produces narrative-style summary output. | Move later | Must not calculate metrics or invent claims. |
| `backend/summary/README.md` | Contract or governance document | `src/alis_core/engines/vyasa/README.md` or `docs/contracts/engines/vyasa/` | Low | Existing summary documentation may be pre-boundary. | Review before movement | May need rewrite to match Vyasa contract. |
| `backend/validators/` | Transitional legacy or ALIS Core engine candidate: Aegis | `src/alis_core/engines/aegis/` or `legacy/backend/validators/` | Low | Older validation layer overlaps with schemas, Aegis, and ALIS validators. | Review before movement | Validation ownership is ambiguous. |
| `backend/validators/validator.py` | Transitional legacy or ALIS Core engine candidate: Aegis | TBD after review | Low | Existing validator may predate Aegis gate model. | Review before movement | Could conflict with Aegis or shared schema validation. |
| `backend/validators/schema.py` | ALIS Core shared service candidate or Aegis candidate | `src/alis_core/shared/schemas/` or Aegis after review | Low | Schema code may be shared contract, not gate implementation. | Review before movement | Must not imply Aegis owns all schemas. |
| `backend/validators/README.md` | Transitional legacy | `legacy/backend/validators/README.md` or docs after review | Low | Older validator documentation. | Review before movement | May contradict current boundary model. |
| `docs/` | Contract or governance document | `docs/` | High | Documentation area should remain source-of-truth evidence. | Remain | Requires later index cleanup, not movement. |
| `docs/architecture/` | Contract or governance document | `docs/architecture/` | High | Architecture documents belong in docs architecture area. | Remain | Older architecture docs may be stale but still evidence. |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Contract or governance document | `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | High | Governing boundary register for this classification. | Do not move | Contract changes require separate review. |
| `docs/architecture/SYSTEM_ARCHITECTURE.md` | Contract or governance document | `docs/architecture/` | Medium | Existing architecture document, but audit reports drift from eight-engine model. | Remain | Must not be treated as current source of truth without revision. |
| `docs/contracts/` | Contract or governance document | `docs/contracts/` with future subfolders | High | Explicit contract documents. | Remain | Existing ALIS/Abacus contracts may be superseded by V1.0-R1. |
| `docs/contracts/ALIS_ENGINE_CONTRACT.md` | Contract or governance document | `docs/contracts/` | Medium | Historical ALIS engine contract. | Remain | Conflicts with current broad `backend/alis/` implementation and newer eight-engine register. |
| `docs/contracts/ABACUS_ENGINE_CONTRACT.md` | Contract or governance document | `docs/contracts/` | Medium | Historical Abacus contract. | Remain | Needs comparison against V1.0-R1 Abacus boundary. |
| `docs/contracts/PIPELINE_CONTRACT.md` | Contract or governance document | `docs/contracts/` | Medium | Pipeline contract documentation. | Remain | Pipeline ownership may change under engine split. |
| `docs/governance/` | Contract or governance document | `docs/governance/` | High | Governance docs align with Aegis/Thoth policy material. | Remain | Could later be indexed under Aegis/Thoth governance references. |
| `docs/governance/ALIS_RETRIEVAL_VALIDATION_PROTOCOL.md` | Contract or governance document | `docs/governance/` | High | Retrieval validation protocol supports governance. | Remain | Must align with Aegis Evidence Validation Gate later. |
| `docs/governance/ALIS_EVIDENCE_PACKAGE_SCHEMA_V0_1.md` | Contract or governance document | `docs/governance/` or `docs/contracts/artifacts/` | Medium | Evidence package schema document. | Remain | Must distinguish retrieved vs validated evidence packages. |
| `docs/reviews/` | Review or audit evidence | `docs/reviews/` | High | Historical milestone reviews and audits. | Remain | Do not rewrite history. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Review or audit evidence | `docs/reviews/` | High | Source audit for this classification. | Do not move | Must remain stable review evidence. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Review or audit evidence | `docs/reviews/` | High | Source architecture plan for this classification. | Do not move | Must remain stable review evidence. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Review or audit evidence | `docs/reviews/` | High | This classification register. | Remain | Future revisions should be new reviewed documents or explicit amendments. |
| `docs/reviews/*_REVIEW.md` | Review or audit evidence | `docs/reviews/` | High | Milestone review and freeze evidence. | Remain | Some content may be historical, not current contract. |
| `docs/*.md` root-level milestone and policy documents | Contract or governance document or Review or audit evidence | `docs/` or later indexed subfolders | Medium | Root docs include policy, milestone reviews, and older architecture material. | Review before movement | Need document-by-document classification before reorganizing docs. |
| `docs/SOURCE_ADMISSION_RULE.md` | Contract or governance document | `docs/governance/` or `docs/contracts/engines/arya-aegis/` | Medium | Source admission rule maps to Arya/Aegis gate context. | Review before movement | Must separate source proposal from Aegis gate decision. |
| `docs/CITATION_POLICY.md` | Contract or governance document | `docs/governance/` | High | Citation policy supports provenance and narrative governance. | Remain | Needs mapping to Thoth/Vyasa/Aegis later. |
| `docs/EXCLUSION_POLICY.md` | Contract or governance document | `docs/governance/` | High | Policy likely supports Aegis gate behavior. | Remain | Must not be embedded in engine code prematurely. |
| `scripts/` | Unknown / requires human review | `scripts/` or `tools/` | Low | Scripts may be developer utilities, workflow runners, or examples. | Review before movement | Could encode old imports. |
| `scripts/run_world_bank_pipeline.py` | Unknown / requires human review | `scripts/` or runtime orchestration after review | Low | Pipeline runner may combine Hermes, Thoth, Aegis, and Abacus steps. | Review before movement | Running or moving may create artifacts or network calls. |
| `scripts/alis_integration_example.py` | Fixture or test data or Unknown / requires human review | `scripts/examples/` or tests fixtures | Low | Example integration script, not engine implementation. | Review before movement | May reference old broad ALIS namespace. |
| `scripts/README.md` | Contract or governance document | `scripts/README.md` | Medium | Script documentation. | Remain | May need update after migration. |
| `scripts/WINDOWS_COPY_GUIDE.md` | Contract or governance document | `scripts/` or docs after review | Low | Local operational guide. | Review before movement | Could be obsolete after target layout. |
| `tests/` | Fixture or test data | Split under `tests/alis_core/`, `tests/godatabank/`, and `tests/integration/` | Medium | Test tree verifies prototype behavior. | Review before movement | Test locations currently reinforce broad ALIS namespace. |
| `tests/abacus/` | Fixture or test data | `tests/alis_core/engines/abacus/` | High | Abacus test area maps to Abacus engine. | Move later | Contains README only in current inventory. |
| `tests/abacus/README.md` | Fixture or test data | `tests/alis_core/engines/abacus/README.md` | Medium | Test placeholder/readme. | Move later | May need update with actual test plan. |
| `tests/integration/` | Fixture or test data | `tests/integration/` | High | Integration tests should remain cross-boundary. | Remain | Future tests must avoid internal API coupling. |
| `tests/integration/README.md` | Fixture or test data | `tests/integration/README.md` | Medium | Integration test documentation. | Remain | May need update after architecture migration. |
| `tests/alis/` | Fixture or test data | Split across target test folders | Low | Contains tests for connectors, schemas, validation, mapping, visualization, publishing, audit, and upload inspection. | Review before movement | Must split by engine/product ownership. |
| `tests/alis/test_world_bank_connector.py` | Fixture or test data | `tests/alis_core/engines/hermes/` | Medium | Tests World Bank connector behavior. | Review before movement | May depend on live or mocked source behavior. |
| `tests/alis/test_ons_connector.py` | Fixture or test data | `tests/alis_core/engines/hermes/` | Medium | Tests ONS connector behavior. | Review before movement | Must verify network isolation. |
| `tests/alis/test_ons_observations.py` | Fixture or test data | `tests/alis_core/engines/hermes/` or integration | Low | Observation retrieval may be connector or pipeline behavior. | Review before movement | Could cross Hermes and evidence packaging boundaries. |
| `tests/alis/test_multi_source_evidence.py` | Fixture or test data | Integration or split engine tests | Low | Multi-source evidence crosses multiple engine responsibilities. | Review before movement | Could hide single-builder violations. |
| `tests/alis/test_multi_source_observation_evidence.py` | Fixture or test data | Integration or split engine tests | Low | Multi-source observation evidence likely crosses Hermes, Thoth, and Aegis. | Review before movement | Requires artifact ownership review. |
| `tests/alis/test_ons_observation_evidence.py` | Fixture or test data | Integration or split engine tests | Low | ONS evidence package flow is cross-boundary. | Review before movement | Distinguish retrieved and validated evidence. |
| `tests/alis/test_evidence_package_schema.py` | Fixture or test data | `tests/alis_core/shared/schemas/` or contracts | Medium | Tests shared evidence package schema. | Review before movement | Schema owner must not imply artifact owner. |
| `tests/alis/test_visualisation_dataset_schema.py` | Fixture or test data | `tests/alis_core/shared/schemas/` or Abacus contracts | Medium | Tests chart-ready/visualisation dataset schema. | Review before movement | Confirm Abacus vs shared schema ownership. |
| `tests/alis/test_source_registry.py` | Fixture or test data | `tests/alis_core/engines/thoth/` | Medium | Tests source registry behavior. | Review before movement | Must separate Arya source requests from Thoth registry. |
| `tests/alis/test_registry_integration.py` | Fixture or test data | `tests/integration/` or `tests/alis_core/engines/thoth/` | Low | Registry integration may cross source, provenance, and evidence flows. | Review before movement | Could mix engine and integration tests. |
| `tests/alis/test_statistical_gatekeeper.py` | Fixture or test data | Abacus or Aegis tests after review | Low | Statistical gatekeeping has ambiguous owner. | Review before movement | Must distinguish analysis checks from approval gates. |
| `tests/alis/test_evidence_to_visualisation_mapper.py` | Fixture or test data | `tests/alis_core/engines/abacus/` | Medium | Tests analytical mapping to chart-ready data. | Review before movement | Must ensure inputs are validated evidence. |
| `tests/alis/test_chart_spec_export.py` | Fixture or test data | Abacus or Apollo tests after review | Low | Chart spec export may be analytical or publication output. | Review before movement | Needs artifact ownership split. |
| `tests/alis/test_minimal_chart_engine.py` | Fixture or test data | Abacus or Apollo tests after review | Low | Tests chart engine that may combine spec and rendering. | Review before movement | Boundary ambiguity. |
| `tests/alis/test_static_chart_renderer.py` | Fixture or test data | `tests/alis_core/engines/apollo/` | Medium | Static chart rendering is Apollo-aligned. | Review before movement | Must use approved inputs. |
| `tests/alis/test_svg_export_integration.py` | Fixture or test data | `tests/alis_core/engines/apollo/` or integration | Medium | SVG export tests rendering integration. | Review before movement | Could be cross-component integration. |
| `tests/alis/test_html_chart_embedding.py` | Fixture or test data | `tests/godatabank/` or Apollo tests | Low | HTML embedding may be product presentation. | Review before movement | Product/core ambiguity. |
| `tests/alis/test_static_report_fragment.py` | Fixture or test data | `tests/godatabank/` or Apollo tests | Low | Report fragments may be product-specific. | Review before movement | Product assumptions likely. |
| `tests/alis/test_static_report_page.py` | Fixture or test data | `tests/godatabank/` or Apollo tests | Low | Static page generation may be product-specific. | Review before movement | Must not rewrite findings. |
| `tests/alis/test_static_report_index.py` | Fixture or test data | `tests/godatabank/` | Medium | Report index likely product navigation. | Review before movement | Could include Apollo manifest assumptions. |
| `tests/alis/test_static_manifest_validation.py` | Fixture or test data | Aegis or Apollo tests after review | Low | Manifest validation may be gate or build validation. | Review before movement | Aegis/Apollo ambiguity. |
| `tests/alis/test_static_site_assembly.py` | Fixture or test data | `tests/alis_core/engines/apollo/` or `tests/godatabank/` | Low | Site assembly may be generic or product-specific. | Review before movement | Publication package ownership must be clear. |
| `tests/alis/test_static_publishing_pipeline.py` | Fixture or test data | Integration tests | Low | Publishing pipeline likely crosses Apollo, Aegis, Argus, and product. | Review before movement | Should remain integration until split. |
| `tests/alis/test_static_site_smoke_test.py` | Fixture or test data | `tests/alis_core/engines/argus/` or integration | Low | Smoke testing may be observability or test-only. | Review before movement | Do not treat as approval gate. |
| `tests/alis/test_cloudflare_upload_candidate_inspection.py` | Fixture or test data | `tests/alis_core/engines/aegis/` or Argus tests | Low | Upload inspection is governance/audit-adjacent. | Review before movement | Deployment gate risk. |
| `tests/alis/test_production_candidate_static_output.py` | Fixture or test data | `tests/godatabank/` or Apollo tests | Low | Production candidate output may be product publication. | Review before movement | Release behavior must remain gated. |
| `tests/alis/test_production_candidate_output_evidence.py` | Fixture or test data | Argus or Thoth tests after review | Low | Evidence capture may be audit or lineage. | Review before movement | Audit events must not be invented. |
| `data/` | Generated artifact | `artifacts/` or external artifact storage after policy approval | Medium | Contains raw snapshots, validated outputs, summaries, candidate outputs, logs. | Review before movement | Some data may be fixtures or canonical evidence. |
| `data/raw/` | Generated artifact | `artifacts/evidence/raw/` or external storage | Medium | Raw source retrieval snapshots and logs. | Review before movement | Retention and provenance policy required. |
| `data/raw/world_bank/latest_metadata.json` | Generated artifact | `artifacts/evidence/raw/world_bank/` | Medium | Latest raw World Bank metadata output. | Review before movement | Could be fixture or live snapshot. |
| `data/raw/world_bank/archive/*.json` | Generated artifact | `artifacts/evidence/raw/world_bank/archive/` | Medium | Archived raw World Bank retrievals. | Review before movement | Preserve provenance if retained. |
| `data/raw/world_bank/logs/world_bank_connector.log` | Generated artifact | `artifacts/logs/` or external logs | High | Runtime connector log. | Deletion candidate requiring approval | Logs may contain operational evidence. |
| `data/raw/ons/latest_metadata.json` | Generated artifact | `artifacts/evidence/raw/ons/` | Medium | Latest raw ONS metadata output. | Review before movement | Could be fixture or live snapshot. |
| `data/raw/ons/archive/*.json` | Generated artifact | `artifacts/evidence/raw/ons/archive/` | Medium | Archived raw ONS retrieval. | Review before movement | Preserve provenance if retained. |
| `data/raw/ons/logs/ons_connector.log` | Generated artifact | `artifacts/logs/` or external logs | High | Runtime connector log. | Deletion candidate requiring approval | Logs may contain operational evidence. |
| `data/validated/` | Generated artifact | `artifacts/evidence/validated/` | Medium | Contains approved validated evidence outputs and validator log. | Review before movement | Must align with Aegis Validated Evidence Package ownership. |
| `data/validated/approved_world_bank_metadata_40107522.json` | Generated artifact | `artifacts/evidence/validated/` | Medium | Validated/approved output. | Review before movement | Confirm whether Aegis-owned or pre-Aegis legacy artifact. |
| `data/validated/approved_ons_metadata_regional-gdp-by-year.json` | Generated artifact | `artifacts/evidence/validated/` | Medium | Validated/approved output. | Review before movement | Confirm whether Aegis-owned or pre-Aegis legacy artifact. |
| `data/validated/validator.log` | Generated artifact | `artifacts/logs/` or external logs | High | Runtime validation log. | Deletion candidate requiring approval | May be needed for audit trail. |
| `data/classified/` | Generated artifact | `artifacts/generated/analysis/` | Medium | Classified outputs are generated analytical artifacts. | Review before movement | Abacus ownership must be confirmed. |
| `data/classified/*.json` | Generated artifact | `artifacts/generated/analysis/` | Medium | Generated classification outputs. | Review before movement | Could be fixtures if used by tests. |
| `data/summaries/` | Generated artifact | `artifacts/generated/narrative/` | Medium | Summary JSON outputs map to narrative artifacts. | Review before movement | Vyasa ownership should be confirmed. |
| `data/summaries/*.json` | Generated artifact | `artifacts/generated/narrative/` | Medium | Generated summary artifacts. | Review before movement | Could be fixtures if used by tests. |
| `data/publishing/` | Generated artifact | `artifacts/publishing/` | High | Candidate outputs, publication inputs, and evidence. | Review before movement | Product/release artifacts need retention policy. |
| `data/publishing/candidate_output_v0_1/` | Generated artifact | `artifacts/publishing/candidates/` | High | Older publication candidate output. | Deletion candidate requiring approval | Audit flags as retained failed/superseded candidate. |
| `data/publishing/candidate_output_v0_2/` | Generated artifact | `artifacts/publishing/candidates/` | High | Current local publication candidate output. | Review before movement | May be needed as release evidence. |
| `data/publishing/evidence/production_candidate_output_evidence_v0_2.json` | Generated artifact | `artifacts/publishing/evidence/` | High | Production candidate evidence capture. | Review before movement | Preserve if used for audit. |
| `data/publishing/production_candidate_inputs_v0_1/` | Generated artifact | `artifacts/publishing/inputs/` | Medium | Generated or staged publication inputs. | Review before movement | May include source report fixtures. |
| `data/publishing/production_candidate_inputs_v0_2/` | Generated artifact | `artifacts/publishing/inputs/` | Medium | Generated or staged publication inputs. | Review before movement | May include source report fixtures. |
| `data/published/` | Generated artifact | `artifacts/publishing/published/` or external deployment storage | Medium | Published artifact area. | Review before movement | Deployment state must be clear before moving. |
| `data/published/README.md` | Contract or governance document | `data/published/README.md` or docs after review | Medium | Documentation inside artifact area. | Review before movement | Decide whether docs remain with data or move to docs. |
| `reports/` | Generated artifact | `artifacts/publishing/reports/` | High | Report outputs and manifest are publication artifacts. | Review before movement | Some files may be product release evidence. |
| `reports/generated/` | Generated artifact | `artifacts/publishing/reports/generated/` | High | Generated HTML report output. | Review before movement | Must not be treated as source templates. |
| `reports/generated/*.html` | Generated artifact | `artifacts/publishing/reports/generated/` | High | Generated static report pages. | Review before movement | Preserve if used in evidence chain. |
| `reports/manifest.json` | Generated artifact | `artifacts/publishing/` or Apollo manifest store | Medium | Publication manifest output. | Review before movement | Apollo ownership likely, but current artifact may be legacy. |
| `templates/` | GoDataBank product layer or ALIS Core engine candidate: Apollo | `src/godatabank/templates/` or `src/alis_core/engines/apollo/templates/` | Low | Template ownership depends on generic vs product-specific use. | Review before movement | Moving without review could couple product into Apollo. |
| `templates/report_template.html` | GoDataBank product layer or Apollo template | `src/godatabank/templates/report_template.html` or Apollo templates | Low | Report template may be product presentation. | Review before movement | Product styling/layout assumptions likely. |
| `sources/` | ALIS Core engine candidate: Thoth or Fixture or test data | `src/alis_core/engines/thoth/` storage contract or `artifacts/evidence/` | Low | Source registry data may be canonical registry state or fixture/prototype data. | Review before movement | Must not corrupt canonical source registry ownership. |
| `sources/source_registry.json` | ALIS Core engine candidate: Thoth or Fixture or test data | Thoth-managed registry storage after review | Low | Registry JSON aligns with Thoth but may be transitional data. | Review before movement | Human review required before treating as canonical. |
| `evidence_package_output.json` | Generated artifact | `artifacts/evidence/` or deletion after approval | High | Root-level generated evidence artifact. | Deletion candidate requiring approval | Root generated artifact should not remain long-term, but may be evidence. |
| `**/__pycache__/` | Deletion candidate requiring separate approval | Excluded from source tree after cleanup approval | High | Generated Python bytecode cache folders. | Deletion candidate requiring approval | Must not clean in this milestone. |
| `**/*.pyc` | Deletion candidate requiring separate approval | Excluded from source tree after cleanup approval | High | 100 generated bytecode files observed. | Deletion candidate requiring approval | Cleanup requires explicit approval and hygiene policy. |

## 5. Engine Candidate Mapping

| Engine | Current path candidates | Confidence | Movement status | Notes |
| --- | --- | --- | --- | --- |
| Abacus | `backend/abacus/`, `backend/alis/mappers/evidence_to_visualisation.py`, possible `backend/alis/validators/statistical_gatekeeper.py`, possible chart-spec files | Medium | Review before movement | Abacus owns execution plans, analysis packages, chart-ready datasets, statistical checks, and caveats. Statistical gatekeeping and chart specification need review before assignment. |
| Arya | No strong current implementation path; possible source admission docs under `docs/SOURCE_ADMISSION_RULE.md` | Low | Review before movement | Arya source proposal/request/manifest behavior is not explicit by package name. |
| Hermes | `backend/alis/connectors/`, possible retrieval portions of `backend/alis/pipelines/`, duplicate `backend/alis/*_connector.py` paths | Medium | Review before movement | Hermes owns transport, Raw Transport Artifacts, and Retrieved Evidence Packages. Duplicate connectors must be resolved before migration. |
| Thoth | `backend/alis/source_registry.py`, `sources/source_registry.json`, schema/provenance-adjacent docs, possible evidence lineage portions of pipelines | Medium | Review before movement | Thoth owns source registry, provenance, lineage, checksums, schema references, and contract version references. |
| Aegis | `backend/validators/`, possible `backend/alis/validators/`, `backend/alis/publishing/static_manifest_validation.py`, `backend/alis/publishing/cloudflare_upload_candidate_inspection.py`, governance policies | Low | Review before movement | Aegis owns gates and validation decisions. Existing validation code must be split from schema contracts and analytical checks. |
| Vyasa | `backend/summary/summary_generator.py`, `data/summaries/` as generated outputs | Medium | Move later after review | Vyasa owns narrative packages and claim-to-evidence maps. Current summary code must be checked for unsupported claims or calculations. |
| Apollo | `backend/alis/visualisation/static_chart_renderer.py`, `backend/alis/visualisation/svg_export_integration.py`, much of `backend/alis/publishing/`, possible `backend/publisher/`, templates if generic | Medium | Review before movement | Apollo owns publication packages, manifests, rendering, and release candidates, but product-specific presentation must be separated. |
| Argus | `backend/alis/publishing/static_site_smoke_test.py`, `backend/alis/publishing/production_candidate_output_evidence.py`, possible upload inspection evidence, logs | Low | Review before movement | Argus owns audit records, incident timelines, observability gaps, and health signals. Existing tests/evidence must not be confused with gate decisions. |

## 6. Shared Service Candidate Mapping

| Shared service candidate | Current paths | Proposed future location | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Schemas and artifact contracts | `backend/alis/schemas/`, `docs/governance/ALIS_EVIDENCE_PACKAGE_SCHEMA_V0_1.md`, `docs/contracts/` | `src/alis_core/shared/schemas/`, `docs/contracts/artifacts/` | Medium | Schemas should support engine contracts without owning artifacts. |
| Configuration | `backend/alis/config.py` | `src/alis_core/shared/config/` | Medium | Configuration must not bypass Aegis gates. |
| Contract registry references | `docs/contracts/`, `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | `docs/contracts/`, future `src/alis_core/shared/contracts/` | Medium | Runtime contract registry does not yet exist. |
| Error taxonomy | No explicit current implementation found | `src/alis_core/shared/errors/` | Low | Boundary register requires shared error taxonomy later. |
| Clock service | No explicit current implementation found | `src/alis_core/shared/clock/` | Low | Current timestamps appear in artifacts/logs, not a service. |
| Checksum service | Possible checksum behavior in publishing/evidence modules | `src/alis_core/shared/checksum/` | Low | Needs code review before extracting. |
| Logging interface | Runtime logs under `data/raw/*/logs` and `data/validated/validator.log` | `src/alis_core/shared/logging/` and external artifact/log storage | Low | Existing logs are artifacts, not a logging service. |
| Identity/permission service | No explicit current implementation found | `src/alis_core/shared/identity/` | Low | Required by boundary register but not present as code. |

## 7. GoDataBank Product-Layer Mapping

| Product-layer candidate | Current paths | Proposed future location | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Product report templates | `templates/report_template.html` | `src/godatabank/templates/` unless proven generic Apollo template | Low | Template ownership depends on product-specific layout assumptions. |
| Product report pages and navigation | `backend/alis/publishing/static_report_page.py`, `static_report_index.py`, `static_report_fragment.py` | `src/godatabank/publishing/` or Apollo after review | Low | Report UI and navigation may be product-specific. |
| Product static output | `data/publishing/candidate_output_*`, `reports/generated/` | `artifacts/publishing/` and/or `src/godatabank/reports/` for source templates only | Medium | Generated product output should not live with source. |
| Product publishing placeholder | `backend/publishing/` | `src/godatabank/publishing/` or legacy | Low | Current folder appears product-facing but may be placeholder. |
| Product API surfaces | `backend/publishing/api_routes/` | `src/godatabank/web/` | Low | Need file-level code review; inventory shows folder but not substantive implementation. |
| Product README/entrypoint | `README.md` | `README.md` | Medium | Should remain top-level but later align with approved architecture. |

## 8. Generated Artifact and Data Classification

| Generated/data path | Classification | Proposed future location | Confidence | Movement status | Risk notes |
| --- | --- | --- | --- | --- | --- |
| `data/raw/` | Generated artifact | `artifacts/evidence/raw/` or external storage | Medium | Review before movement | May include canonical retrieval evidence. |
| `data/validated/` | Generated artifact | `artifacts/evidence/validated/` | Medium | Review before movement | Must align with Aegis Validated Evidence Package ownership. |
| `data/classified/` | Generated artifact | `artifacts/generated/analysis/` | Medium | Review before movement | Likely Abacus output but may be fixture. |
| `data/summaries/` | Generated artifact | `artifacts/generated/narrative/` | Medium | Review before movement | Likely Vyasa output but may be fixture. |
| `data/publishing/` | Generated artifact | `artifacts/publishing/` | High | Review before movement | Contains production-candidate output and evidence. |
| `data/published/` | Generated artifact | `artifacts/publishing/published/` or deployment storage | Medium | Review before movement | Requires release/deployment policy. |
| `reports/generated/` | Generated artifact | `artifacts/publishing/reports/generated/` | High | Review before movement | Generated HTML reports, not source. |
| `reports/manifest.json` | Generated artifact | `artifacts/publishing/` | Medium | Review before movement | Publication manifest ownership likely Apollo. |
| `evidence_package_output.json` | Generated artifact | `artifacts/evidence/` or deletion after approval | High | Deletion candidate requiring approval | Root generated artifact should be removed only after evidence review. |
| `data/raw/*/logs/*.log` | Generated artifact | `artifacts/logs/` or external logs | High | Deletion candidate requiring approval | Logs may be audit evidence. |
| `data/validated/validator.log` | Generated artifact | `artifacts/logs/` or external logs | High | Deletion candidate requiring approval | Validation log may be audit evidence. |
| `**/__pycache__/` | Deletion candidate requiring separate approval | Excluded from source tree after cleanup | High | Deletion candidate requiring approval | Generated caches should not be source, but cleanup is not authorised here. |
| `**/*.pyc` | Deletion candidate requiring separate approval | Excluded from source tree after cleanup | High | Deletion candidate requiring approval | 100 bytecode files observed. |

## 9. Legacy and Deletion-Candidate Register

| Path | Register type | Confidence | Required review before action | Reason |
| --- | --- | --- | --- | --- |
| `backend/alis/world_bank_connector.py` | Transitional legacy | Medium | Compare against `backend/alis/connectors/world_bank.py` and tests. | Duplicate connector path. |
| `backend/alis/ons_connector.py` | Transitional legacy | Medium | Compare against `backend/alis/connectors/ons.py` and tests. | Duplicate connector path. |
| `backend/publisher/` | Transitional legacy | Medium | Import tracing and behavior comparison against `backend/alis/publishing/`. | Older publisher path. |
| `backend/publishing/` | Transitional legacy or product placeholder | Low | Confirm intended role and usage. | Placeholder/product-facing publishing structure. |
| `backend/validators/` | Transitional legacy | Medium | Compare against schemas, Aegis candidates, and ALIS validators. | Older validation path. |
| `data/publishing/candidate_output_v0_1/` | Deletion candidate requiring separate approval | Medium | Confirm whether retained as historical evidence. | Audit flags as failed/superseded candidate output. |
| `evidence_package_output.json` | Deletion candidate requiring separate approval | High | Confirm whether artifact is needed as evidence or fixture. | Root generated artifact. |
| `data/raw/*/logs/*.log` | Deletion candidate requiring separate approval | Medium | Confirm log retention and audit requirements. | Runtime logs in source tree. |
| `data/validated/validator.log` | Deletion candidate requiring separate approval | Medium | Confirm validation evidence requirements. | Runtime log in source tree. |
| `**/__pycache__/` | Deletion candidate requiring separate approval | High | Approve generated artifact cleanup. | Generated cache folders. |
| `**/*.pyc` | Deletion candidate requiring separate approval | High | Approve generated artifact cleanup. | Generated bytecode. |

No deletion is authorised by this register.

## 10. Unknown / Human-Review-Required Register

| Path | Human review question | Why classification is uncertain |
| --- | --- | --- |
| `backend/alis/pipelines/` | Which parts are Hermes retrieval, Aegis validation, Thoth lineage, or orchestration-only? | Pipelines can cross engine boundaries and single-builder ownership. |
| `backend/alis/validators/statistical_gatekeeper.py` | Is this Abacus statistical checking or Aegis gate enforcement? | Name and likely behavior straddle analysis and governance. |
| `backend/alis/visualisation/chart_spec_export.py` | Is the output an Abacus chart specification or Apollo export artifact? | Chart specification and rendering/export are separate responsibilities. |
| `backend/alis/visualisation/minimal_chart_engine.py` | Does it calculate chart-ready data, generate chart specs, or render output? | Different outputs have different canonical builders. |
| `backend/alis/visualisation/html_chart_embedding.py` | Is HTML embedding generic Apollo rendering or GoDataBank presentation? | Product-specific assumptions may be embedded. |
| `backend/alis/publishing/` | How should the folder split across Apollo, Aegis, Argus, Thoth, and GoDataBank? | Folder contains mixed publishing, validation, audit, release, and product code. |
| `backend/publishing/` | Is this active product code, placeholder structure, or legacy? | Inventory suggests placeholder folders, but intent is not explicit. |
| `sources/source_registry.json` | Is this canonical Thoth registry state, fixture data, or transitional prototype data? | Source registry ownership is Thoth, but storage policy is not defined. |
| `templates/report_template.html` | Is the template generic Apollo renderer material or GoDataBank product presentation? | Target location depends on generic/product distinction. |
| `scripts/run_world_bank_pipeline.py` | Is this developer tooling, orchestration, or legacy workflow runner? | It may encode broad ALIS flow and external source behavior. |
| `scripts/alis_integration_example.py` | Is this example, fixture, or obsolete integration path? | It may reference old imports and mixed responsibilities. |
| `README.md` | What should be the current entrypoint after boundary register and architecture plan? | Audit reports it is outdated. |
| `docs/architecture/SYSTEM_ARCHITECTURE.md` | Should this remain historical or be revised as current architecture? | It predates the eight-engine boundary model. |

## 11. Risks

| Risk | Severity | Evidence | Mitigation |
| --- | --- | --- | --- |
| False ownership assignment | High | Many current modules combine responsibilities now separated by V1.0-R1. | Require code review and tests before any movement. |
| Preserving boundary debt by moving folders wholesale | High | `backend/alis/` and `backend/alis/publishing/` are mixed containers. | Split by artifact ownership before migration. |
| Misclassifying validation | High | Validation appears in schemas, validators, statistical checks, manifest checks, and upload inspection. | Separate schema validation, statistical checking, gate decisions, and release inspection. |
| Treating generated artifacts as source | Medium-high | Data, reports, logs, and pycache exist in the repository tree. | Approve artifact policy before cleanup or relocation. |
| Breaking test provenance | Medium-high | Tests are concentrated under `tests/alis/` and map to several future owners. | Create test movement plan before import changes. |
| Losing audit evidence | Medium-high | Logs, candidate outputs, and review docs may be historical evidence. | Preserve until retention policy is approved. |
| Duplicate connectors diverge | Medium | Both root connector files and connector package files exist. | Compare behavior before selecting canonical Hermes adapters. |
| Product assumptions entering ALIS Core | Medium | Static report and template code may be product-specific. | Separate generic Apollo publishing from GoDataBank product presentation. |
| Stale documentation becoming source of truth | Medium | Older ALIS/ABACUS/Publisher docs remain. | Add architecture index in a later milestone after review. |

## 12. Recommended Next Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Repository Classification Register v1.0
```

The review should confirm or revise:

- engine assignments for ambiguous files
- shared-service schema and config ownership
- GoDataBank product-layer boundaries
- generated artifact retention policy
- deletion-candidate approval process
- test mapping before import migration

No file movement, cleanup, import change, or engine implementation should begin
until this register is independently reviewed.

STATUS: REPOSITORY CLASSIFICATION REGISTER CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
