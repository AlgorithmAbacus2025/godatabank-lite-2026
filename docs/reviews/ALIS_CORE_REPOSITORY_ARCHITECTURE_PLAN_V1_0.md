# ALIS Core Repository Architecture Plan v1.0

## 1. Purpose

This document is a planning-only repository architecture migration plan for
aligning the current GoDataBank repository with the ALIS Core Boundary Register
v1.0-R1.

No migration is performed by this plan. No files are moved, renamed, deleted, or
refactored. No engines are implemented. The plan exists to define the target
repository shape, identify current-to-target mappings, and set review gates
before any future repository restructuring begins.

The controlling principle is that repository layout must express the frozen
engine contract:

- one canonical builder per artifact
- engine code separated by responsibility
- shared services separated from engine ownership
- GoDataBank product concerns separated from ALIS Core platform concerns
- generated artifacts separated from source code
- historical reviews preserved as evidence

## 2. Source Documents Reviewed

Reviewed source documents:

| Document | Role in this plan |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing ALIS Core engine boundary register, revision V1.0-R1. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Current repository engineering audit and technical debt assessment. |

Current repository structure was also inspected directly using read-only
directory and file inventory commands.

## 3. Current Repository Structure

The current repository is a functional prototype with ALIS Core, GoDataBank
product, publishing, generated artifact, and review concerns mixed together.

Observed top-level structure:

```text
GoDataBank/
  .agents/
  backend/
  data/
  docs/
  reports/
  scripts/
  sources/
  templates/
  tests/
  README.md
  evidence_package_output.json
```

Observed backend structure:

```text
backend/
  abacus/
  alis/
    connectors/
    mappers/
    pipelines/
    publishing/
    schemas/
    validators/
    visualisation/
  publisher/
  publishing/
    api_routes/
    html_export/
    pdf_export/
    report_builder/
  summary/
  validators/
```

Observed data and output structure:

```text
data/
  classified/
  published/
  publishing/
    candidate_output_v0_1/
    candidate_output_v0_2/
    evidence/
    production_candidate_inputs_v0_1/
    production_candidate_inputs_v0_2/
  raw/
    ons/
    world_bank/
  summaries/
  validated/
reports/
  generated/
templates/
sources/
```

Observed documentation structure:

```text
docs/
  architecture/
  contracts/
  governance/
  reviews/
  root-level milestone and policy documents
```

Observed test structure:

```text
tests/
  abacus/
  alis/
  integration/
```

Current architectural assessment:

- `backend/alis/` is the broadest implementation container and currently holds
  retrieval, registry, schema, validation, mapping, visualisation, publishing,
  production-candidate, and upload-boundary concerns.
- `backend/abacus/` exists by name but is narrower than the Abacus boundary in
  the V1.0-R1 register.
- Arya, Vyasa, Hermes, Thoth, Aegis, Apollo, and Argus do not yet exist as
  explicit repository packages.
- `backend/publisher/`, `backend/publishing/`, and `backend/alis/publishing/`
  overlap in publishing responsibility.
- `backend/validators/`, `backend/alis/validators/`, schemas, and publishing
  validators overlap in validation responsibility.
- generated files, logs, evidence outputs, and production candidates are present
  inside the same tree as source code.

## 4. Proposed Target Repository Structure

The target structure should make ALIS Core a platform layer and GoDataBank a
product layer built on top of that platform.

Proposed future structure:

```text
GoDataBank/
  src/
    alis_core/
      engines/
        abacus/
        arya/
        hermes/
        thoth/
        aegis/
        vyasa/
        apollo/
        argus/
      shared/
        artifacts/
        checksum/
        clock/
        config/
        contracts/
        errors/
        identity/
        logging/
        schemas/
      runtime/
        orchestration/
        adapters/
    godatabank/
      product/
      publishing/
      reports/
      templates/
      web/
  tests/
    alis_core/
      engines/
        abacus/
        arya/
        hermes/
        thoth/
        aegis/
        vyasa/
        apollo/
        argus/
      shared/
      contracts/
    godatabank/
    integration/
  docs/
    architecture/
    contracts/
      alis_core/
      engines/
      artifacts/
    governance/
    reviews/
    migration/
  artifacts/
    generated/
    evidence/
    publishing/
  data/
    source_snapshots/
    local_only/
  legacy/
    backend/
    generated/
  scripts/
  README.md
```

Target responsibility model:

| Area | Target responsibility |
| --- | --- |
| `src/alis_core/engines/abacus/` | Execution Plans, Analysis Packages, Chart-ready Datasets, statistical checks, and analytical caveats. |
| `src/alis_core/engines/arya/` | Source Proposals, Source Admission Requests, Retrieval Manifests, acquisition logs, and readiness status. |
| `src/alis_core/engines/hermes/` | transport adapters, Raw Transport Artifacts, Retrieved Evidence Packages, receipts, and retry records. |
| `src/alis_core/engines/thoth/` | Source Registry Entries, Provenance Records, Lineage Records, Checksum Records, schema references, and contract version references. |
| `src/alis_core/engines/aegis/` | Validation Reports, Gate Decisions, Validated Evidence Packages, quarantine records, and boundary enforcement. |
| `src/alis_core/engines/vyasa/` | Narrative Packages, Claim-to-Evidence Maps, methodology text, caveat text, and evidence-traceable synthesis. |
| `src/alis_core/engines/apollo/` | Publication Packages, Publication Manifests, rendered pages, chart embeds, and release candidates. |
| `src/alis_core/engines/argus/` | Audit Records, run timelines, health reports, alerts, Incident Timelines, and observability gaps. |
| `src/alis_core/shared/` | shared services only: contracts, schemas, checksum, clock, configuration, identity, logging interfaces, and error taxonomy. |
| `src/godatabank/` | product-specific report surfaces, web/application workflows, product templates, and GoDataBank-specific publishing decisions. |
| `artifacts/` | generated or runtime artifacts that are not source code. |
| `legacy/` | transitional holding area for retired or superseded paths after review, never a default import target. |

The target does not require all folders to be created at once. Empty package
creation, compatibility shims, import rewrites, or file movement must be
separately reviewed and authorised in future milestones.

## 5. Mapping From Existing Folders to Target Folders

The mapping below is a planning map, not a movement instruction.

| Existing path | Proposed target | Classification | Reason |
| --- | --- | --- | --- |
| `backend/abacus/` | `src/alis_core/engines/abacus/` | Move later | Existing named Abacus code belongs under the Abacus engine after contract review. |
| `backend/alis/connectors/` | `src/alis_core/engines/hermes/adapters/` | Move later with review | Connector transport logic is closest to Hermes, but source proposal and admission logic must be separated first. |
| `backend/alis/world_bank_connector.py` | Review before movement | Transitional candidate | Duplicates connector responsibility and may be older than `backend/alis/connectors/world_bank.py`. |
| `backend/alis/ons_connector.py` | Review before movement | Transitional candidate | Duplicates connector responsibility and may be older than `backend/alis/connectors/ons.py`. |
| `backend/alis/source_registry.py` | `src/alis_core/engines/thoth/` | Move later with review | Registry ownership belongs to Thoth, but Arya proposal inputs must be separated from canonical registry state. |
| `sources/source_registry.json` | `artifacts/evidence/` or Thoth-managed registry storage | Review before movement | It may be canonical source registry state or a prototype artifact; ownership must be confirmed. |
| `backend/alis/schemas/` | `src/alis_core/shared/schemas/` and `docs/contracts/artifacts/` | Move later with review | Schemas are shared contracts, but each schema must be assigned to its artifact owner. |
| `backend/alis/pipelines/` | Split across Hermes, Aegis, Thoth, and integration runtime | Review before movement | Pipelines currently combine retrieval, evidence packaging, provenance, and validation handoff concerns. |
| `backend/alis/validators/statistical_gatekeeper.py` | `src/alis_core/engines/abacus/` or `src/alis_core/engines/aegis/` | Review before movement | Statistical checks may be Abacus analysis checks, while gate decisions belong to Aegis. |
| `backend/validators/` | `src/alis_core/engines/aegis/` or legacy | Review before movement | Older validator layer overlaps with Aegis and schemas. |
| `backend/alis/mappers/evidence_to_visualisation.py` | `src/alis_core/engines/abacus/` | Move later with review | Mapping evidence to chart-ready datasets is Abacus-aligned if it produces analytical visualization data, not rendered publication output. |
| `backend/alis/visualisation/chart_spec_export.py` | `src/alis_core/engines/abacus/` or `src/alis_core/engines/apollo/` | Review before movement | Chart specification may be Abacus-owned, while export/rendering may be Apollo-owned. |
| `backend/alis/visualisation/minimal_chart_engine.py` | `src/alis_core/engines/abacus/` or `src/alis_core/engines/apollo/` | Review before movement | Needs split between chart specification generation and rendered artifact production. |
| `backend/alis/visualisation/static_chart_renderer.py` | `src/alis_core/engines/apollo/` | Move later with review | Rendering is Apollo responsibility. |
| `backend/alis/visualisation/html_chart_embedding.py` | `src/alis_core/engines/apollo/` or `src/godatabank/publishing/` | Review before movement | Embedding may be generic Apollo rendering or GoDataBank-specific presentation. |
| `backend/alis/visualisation/svg_export_integration.py` | `src/alis_core/engines/apollo/` | Move later with review | SVG export is rendering/publication output. |
| `backend/alis/publishing/static_report_fragment.py` | `src/alis_core/engines/apollo/` or `src/godatabank/publishing/` | Review before movement | Report fragment logic may contain product-specific layout assumptions. |
| `backend/alis/publishing/static_report_page.py` | `src/alis_core/engines/apollo/` or `src/godatabank/publishing/` | Review before movement | Page assembly is Apollo if generic, GoDataBank if product-specific. |
| `backend/alis/publishing/static_report_index.py` | `src/alis_core/engines/apollo/` or `src/godatabank/publishing/` | Review before movement | Index generation may be product-layer navigation. |
| `backend/alis/publishing/static_manifest_validation.py` | `src/alis_core/engines/aegis/` or `src/alis_core/engines/apollo/` | Review before movement | Manifest creation is Apollo; validation gate ownership is Aegis. |
| `backend/alis/publishing/static_site_assembly.py` | `src/alis_core/engines/apollo/` | Move later with review | Static bundle assembly aligns with Apollo. |
| `backend/alis/publishing/static_publishing_pipeline.py` | Split across Apollo, Aegis, Argus, and product layer | Review before movement | Pipeline likely combines rendering, validation, audit, and product concerns. |
| `backend/alis/publishing/static_site_smoke_test.py` | `src/alis_core/engines/argus/` or tests | Review before movement | Smoke-test evidence may be Argus observability or test-only support. |
| `backend/alis/publishing/production_candidate_static_output.py` | `src/alis_core/engines/apollo/` or `src/godatabank/publishing/` | Review before movement | Production candidate output may be generic publication packaging or product-specific release assembly. |
| `backend/alis/publishing/production_candidate_output_evidence.py` | `src/alis_core/engines/argus/` or `src/alis_core/engines/thoth/` | Review before movement | Evidence capture may be Argus audit output with Thoth lineage references. |
| `backend/alis/publishing/cloudflare_upload_candidate_inspection.py` | `src/alis_core/engines/aegis/` or deployment review tooling | Review before movement | Upload boundary inspection is a governance/release gate concern. |
| `backend/publisher/` | `legacy/backend/publisher/` or `src/alis_core/engines/apollo/` | Review before movement | Older publisher path overlaps with Apollo and may be superseded. |
| `backend/publishing/` | `src/godatabank/publishing/` or legacy | Review before movement | Placeholder structure appears product-facing but must be classified. |
| `backend/summary/` | `src/alis_core/engines/vyasa/` | Move later with review | Summary generation is the closest current candidate for Vyasa narrative synthesis. |
| `backend/alis/config.py` | `src/alis_core/shared/config/` | Move later with review | Configuration is a shared service and must not become an engine owner. |
| `tests/abacus/` | `tests/alis_core/engines/abacus/` | Move later | Existing Abacus tests should follow the Abacus engine target. |
| `tests/alis/` | Split across `tests/alis_core/engines/`, `tests/alis_core/shared/`, and `tests/godatabank/` | Review before movement | Current test namespace reflects prototype layout, not engine ownership. |
| `tests/integration/` | `tests/integration/` | Remain, then expand | Integration tests should remain a separate cross-boundary layer. |
| `docs/architecture/` | `docs/architecture/` | Remain | Architecture docs are already in the correct documentation area. |
| `docs/contracts/` | `docs/contracts/` with future subfolders | Remain, then expand | Existing contracts should stay while future engine/artifact contracts are added. |
| `docs/governance/` | `docs/governance/` | Remain | Governance documents align with Aegis/Thoth but should not be moved without review. |
| `docs/reviews/` | `docs/reviews/` | Remain | Historical review evidence should remain stable. |
| `data/raw/` | `artifacts/evidence/raw/` or external artifact storage | Review before movement | Raw source snapshots are artifacts, not source code. |
| `data/validated/` | `artifacts/evidence/validated/` | Review before movement | Validated evidence ownership must align with Aegis before movement. |
| `data/classified/` | `artifacts/generated/analysis/` | Review before movement | Classified output likely maps to Abacus artifacts. |
| `data/summaries/` | `artifacts/generated/narrative/` | Review before movement | Summaries likely map to Vyasa artifacts. |
| `data/publishing/` | `artifacts/publishing/` | Review before movement | Publishing artifacts should be separated from source after artifact policy approval. |
| `data/published/` | `artifacts/publishing/published/` or external deployment storage | Review before movement | Published artifacts require release and retention policy. |
| `reports/generated/` | `artifacts/publishing/reports/` | Review before movement | Generated report output should not be mixed with source. |
| `reports/manifest.json` | `artifacts/publishing/` or Apollo manifest storage | Review before movement | Manifest ownership should align with Apollo. |
| `templates/` | `src/godatabank/templates/` or `src/alis_core/engines/apollo/templates/` | Review before movement | Templates may be product-specific or generic renderer assets. |
| `scripts/` | `scripts/` or `tools/` | Remain initially | Scripts need usage classification before movement. |
| `README.md` | `README.md` | Remain, update later | Entry-point documentation should be revised after architecture review. |
| `evidence_package_output.json` | `artifacts/evidence/` or removal after review | Review before movement | Root generated artifact should not remain at repository root long-term. |
| `__pycache__/` and `.pyc` files | Excluded generated cache | Review before cleanup | These are generated bytecode, but cleanup requires separate authorization. |

## 6. Folders and Files That Should Remain Unchanged

The following should remain unchanged during the next planning and review
milestones:

| Path | Reason |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing boundary register for this plan. Changes require boundary-register review. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Source audit evidence for this plan. |
| `docs/reviews/` historical review files | Preserve milestone evidence and decision history. |
| `docs/contracts/` existing files | Existing contracts should remain until replacement contracts are reviewed. |
| `docs/governance/` | Governance source material should remain stable until Aegis/Thoth documents are formalised. |
| `tests/` | Tests should not be moved until import boundaries and target packages are approved. |
| `data/`, `reports/`, `sources/`, `templates/` | These contain evidence, generated output, registry, and template material that requires classification before movement. |
| `.git/` | Repository metadata must not be altered by architecture planning. |

## 7. Folders and Files That Should Be Moved Later

These paths appear directionally clear, but movement should occur only after an
approved migration milestone, import-impact review, and test plan:

| Existing path | Later target |
| --- | --- |
| `backend/abacus/` | `src/alis_core/engines/abacus/` |
| `backend/alis/connectors/` | `src/alis_core/engines/hermes/adapters/` |
| `backend/alis/source_registry.py` | `src/alis_core/engines/thoth/` |
| `backend/alis/mappers/evidence_to_visualisation.py` | `src/alis_core/engines/abacus/` |
| `backend/alis/visualisation/static_chart_renderer.py` | `src/alis_core/engines/apollo/` |
| `backend/alis/visualisation/svg_export_integration.py` | `src/alis_core/engines/apollo/` |
| `backend/alis/publishing/static_site_assembly.py` | `src/alis_core/engines/apollo/` |
| `backend/summary/summary_generator.py` | `src/alis_core/engines/vyasa/` |
| `tests/abacus/` | `tests/alis_core/engines/abacus/` |

## 8. Folders and Files That Need Review Before Movement

These paths have ambiguous ownership, duplication, product coupling, or
generated-artifact risk:

| Path | Review question |
| --- | --- |
| `backend/alis/world_bank_connector.py` | Is this superseded by `backend/alis/connectors/world_bank.py`, or does it preserve required behaviour? |
| `backend/alis/ons_connector.py` | Is this superseded by `backend/alis/connectors/ons.py`, or does it preserve required behaviour? |
| `backend/alis/pipelines/` | Which parts are Hermes retrieval, Aegis validation, Thoth lineage, or orchestration-only? |
| `backend/alis/schemas/` | Which schemas are shared contracts, and which belong to a specific artifact owner? |
| `backend/alis/validators/statistical_gatekeeper.py` | Is this Abacus analytical checking or Aegis gate enforcement? |
| `backend/validators/` | Is this legacy validation, Aegis candidate code, or superseded code? |
| `backend/alis/visualisation/chart_spec_export.py` | Is chart specification an Abacus output or Apollo rendering support? |
| `backend/alis/visualisation/minimal_chart_engine.py` | Does it produce chart-ready analytical specification, rendered output, or both? |
| `backend/alis/visualisation/html_chart_embedding.py` | Is it generic Apollo rendering or GoDataBank product presentation? |
| `backend/alis/publishing/` | Must be split across Apollo, Aegis, Argus, Thoth, and GoDataBank product responsibilities. |
| `backend/publisher/` | Determine whether it is legacy, superseded, or Apollo candidate code. |
| `backend/publishing/` | Determine whether it is intended product layer, placeholder structure, or legacy. |
| `tests/alis/` | Tests must be assigned to engine, shared-service, product, or integration ownership. |
| `data/` | Classify as source snapshots, generated artifacts, canonical evidence, logs, or local-only output. |
| `reports/` | Classify as generated publication output or product source material. |
| `templates/` | Classify as generic Apollo templates or GoDataBank product templates. |
| `sources/source_registry.json` | Determine whether it is canonical Thoth registry state or transitional fixture data. |
| `scripts/` | Determine whether scripts are developer tools, product workflows, or engine orchestration. |
| `__pycache__/` and `.pyc` files | Confirm cleanup policy before removal. |

## 9. Risks

| Risk | Severity | Explanation | Mitigation |
| --- | --- | --- | --- |
| Moving code before ownership is settled | High | Several modules combine multiple engine responsibilities. | Require file-level ownership review before movement. |
| Breaking imports | High | Tests currently reference prototype paths under `backend/alis/`. | Create an import migration plan and run tests after each later movement phase. |
| Misplacing validation logic | High | Validation can mean schema validation, statistical checking, gate approval, or manifest validation. | Assign each validator to Aegis, Abacus, Apollo, or shared schema contracts before movement. |
| Product/core coupling persists | High | Publishing and production candidate logic may contain GoDataBank-specific assumptions. | Separate generic Apollo rendering from GoDataBank presentation templates. |
| Generated artifacts treated as source | Medium-high | Logs, reports, evidence files, pycache, and candidate outputs are mixed into the tree. | Approve artifact policy before moving or deleting generated files. |
| Duplicate connectors diverge | Medium-high | Old and new ONS/World Bank connector paths both exist. | Compare behaviour before designating canonical Hermes adapters. |
| Historical review evidence is disturbed | Medium | Docs preserve milestone decisions and must remain auditable. | Keep review docs stable and add new review docs rather than rewriting history. |
| Boundary register drift | Medium | Repository layout could imply different ownership from V1.0-R1. | Check every movement against the canonical artifact ownership table. |
| Dirty worktree confuses provenance | Medium | The audit records many modified and untracked files. | Establish a source-control baseline before migration work. |
| Deployment risk from publishing moves | Medium | Publishing paths relate to release candidates and Cloudflare upload reviews. | Keep deployment/promotion gated by Aegis and independent review. |

## 10. Migration Phases

### Phase 0: Independent Review of This Plan

Objective: confirm that the target structure and mapping align with the ALIS
Core Boundary Register V1.0-R1.

Allowed work:

- review this plan
- mark required revisions
- approve or reject target folder names
- confirm whether `src/` is the preferred future source root

No files should be moved in this phase.

### Phase 1: Repository Classification Register

Objective: create a file-level classification register before movement.

Each source file, test file, generated artifact, and documentation group should
be classified as one of:

- ALIS Core engine
- ALIS Core shared service
- GoDataBank product layer
- contract or governance document
- generated artifact
- fixture
- transitional legacy
- deletion candidate requiring separate approval

No production code should be changed in this phase.

### Phase 2: Contract and Test Boundary Planning

Objective: define engine-specific contracts and test destinations before moving
implementation files.

Required outputs:

- artifact contract list by canonical builder
- public API contract list by engine
- test mapping from current `tests/alis/` files to target test folders
- import-risk report

No engine implementation should begin in this phase.

### Phase 3: Create Target Skeletons

Objective: create reviewed empty target folders and documentation placeholders
only after Phase 2 approval.

Permitted later work:

- create target source and test folders
- create package-level README files
- create no-op contract documentation placeholders

Forbidden later work in this phase:

- moving implementation code
- rewriting imports
- changing runtime behaviour

### Phase 4: Move Low-Risk Engine Code

Objective: move files with clear ownership and low coupling.

Likely first candidates:

- `backend/abacus/` to Abacus
- clearly generic Hermes connector adapters
- clearly generic Apollo renderer modules
- clearly Vyasa-aligned summary generator

Each movement should be reviewed independently and followed by targeted tests.

### Phase 5: Split Mixed Responsibility Modules

Objective: handle files that combine engine, shared-service, product, or
generated-artifact responsibilities.

This phase is high risk and should not start until simple movements are stable.

Expected work:

- split publishing pipeline responsibilities
- separate Aegis gates from Apollo manifest creation
- separate Argus evidence capture from Thoth lineage records
- separate Abacus chart-ready data from Apollo rendering
- separate GoDataBank templates and page composition from generic publication packaging

### Phase 6: Product Layer Separation

Objective: make GoDataBank an application/product layer on top of ALIS Core.

Expected work:

- move product-specific templates, routes, reports, and web presentation code
- define product-to-core interfaces
- keep GoDataBank from importing internal engine APIs

### Phase 7: Artifact and Legacy Cleanup

Objective: remove or relocate generated artifacts and legacy folders after
classification and approval.

Expected work:

- move approved generated artifacts to `artifacts/` or external storage
- remove bytecode caches only after cleanup approval
- archive or delete superseded legacy code only after dead-code review
- update README and architecture index

## 11. Abort Conditions

Any future migration phase should stop immediately if one of these conditions is
met:

- a proposed movement conflicts with the canonical artifact ownership table
- source files require behavioural refactoring to move safely
- import paths cannot be mapped without changing runtime behaviour
- tests fail for reasons not understood before proceeding
- generated artifacts cannot be distinguished from source artifacts
- duplicate connector, validator, or publisher paths cannot be classified
- Aegis gate ownership becomes ambiguous
- Thoth provenance or registry ownership becomes ambiguous
- GoDataBank product assumptions are found inside a proposed ALIS Core engine path
- source-control state is not baselined before migration
- reviewers do not approve the phase scope
- a migration step would require deployment, external service access, or production data mutation

## 12. Next Recommended Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Repository Architecture Plan v1.0
```

The review should decide whether this target repository structure is acceptable
and whether the next planning artifact should be a file-level repository
classification register.

No repository migration should begin until this plan has been independently
reviewed and either approved or revised.

STATUS: REPOSITORY ARCHITECTURE PLAN CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
