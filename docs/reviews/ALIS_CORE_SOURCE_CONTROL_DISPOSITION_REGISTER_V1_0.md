# ALIS Core Source-Control Disposition Register v1.0

## 1. Purpose

This register assigns a proposed source-control disposition to the modified
tracked file groups and untracked path groups identified in the source-control
baseline plan.

This is a disposition register only. It does not stage, commit, move, rename,
delete, clean, refactor, change imports, create skeleton folders, implement
engines, or restructure the repository.

The purpose is to decide what kind of human decision is required before any
baseline commit, cleanup, skeleton creation, or migration can begin.

## 2. Source Documents Reviewed

| Document | Role |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing ALIS Core engine boundary register, revision V1.0-R1. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Target repository architecture and skeleton planning source. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Path classification and ownership source. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md` | Source-control baseline and skeleton plan, revision V1.0-R1. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Repository engineering audit and technical-debt evidence. |

Observed baseline facts from the source-control plan:

- 13 modified tracked files
- 250 untracked paths before the source-control baseline plan file was created
- 100 untracked `.pyc` files
- no staged files
- branch `main`, upstream `origin/main`, HEAD `0ba1ccf`

The source-control baseline plan and this disposition register are additional
untracked review documents created after that baseline count.

## 3. Disposition Taxonomy

| Disposition | Meaning |
| --- | --- |
| Commit candidate | May be included in a future baseline commit after human approval. |
| Ignore candidate | Should normally be excluded from source control through ignore policy, without deleting in this milestone. |
| Archive-later candidate | Should be preserved outside or apart from source code after artifact-retention review. |
| Delete-later-with-approval candidate | May be deleted only in a later authorised cleanup milestone. |
| Review-before-decision | Requires human review before deciding commit, ignore, archive, or delete. |
| Do-not-touch | Must not be staged, moved, deleted, cleaned, or otherwise altered as part of migration planning. |

Field meanings used in tables:

| Field | Meaning |
| --- | --- |
| May be baseline commit | Whether the item may be committed later after approval. |
| Must exclude | Whether the item should be excluded from source control unless a specific exception is approved. |
| Artifact review | Whether artifact-retention or evidence-retention review is required. |
| Line-ending review | Whether line-ending review is required before commit. |
| Blocks skeleton | Whether unresolved disposition blocks target skeleton creation. |

## 4. Modified Tracked File Disposition Table

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `backend/abacus/README.md` | Modified tracked | Review-before-decision | Existing Abacus candidate documentation changed; must be checked against V1.0-R1. | Medium | Accept as Abacus documentation, revise later, or reject. | Yes, if accepted | No | No | Yes | Yes |
| `backend/abacus/classifier.py` | Modified tracked | Review-before-decision | Existing Abacus source changed; migration requires clean accepted source baseline. | High | Accept source change as current Abacus candidate or reject separately. | Yes, if accepted | No | No | Yes | Yes |
| `backend/abacus/taxonomy.py` | Modified tracked | Review-before-decision | Existing Abacus taxonomy source changed; taxonomy may also need governance review. | High | Accept as Abacus candidate source or require further review. | Yes, if accepted | No | No | Yes | Yes |
| `backend/validators/README.md` | Modified tracked | Review-before-decision | Transitional validator documentation changed; ownership is ambiguous. | Medium | Decide legacy, Aegis candidate, shared schema support, or reject. | Yes, if accepted | No | No | Yes | Yes |
| `backend/validators/schema.py` | Modified tracked | Review-before-decision | Transitional validator/schema source changed; could overlap Aegis and shared schemas. | High | Decide whether this remains source, becomes legacy, or is superseded. | Yes, if accepted | No | No | Yes | Yes |
| `backend/validators/validator.py` | Modified tracked | Review-before-decision | Transitional validator source changed; validation ownership is unresolved. | High | Decide Aegis candidate, legacy, or rejection before migration. | Yes, if accepted | No | No | Yes | Yes |
| `data/classified/classified_world_bank_metadata_40107522.json` | Modified tracked | Archive-later candidate | Generated classified analytical output should not be treated as source without fixture approval. | Medium | Decide fixture/evidence retention or archive outside source. | Only if approved as fixture | No | Yes | No | Yes |
| `data/raw/world_bank/latest_metadata.json` | Modified tracked | Archive-later candidate | Raw retrieval output is generated evidence, not source code. | Medium | Decide evidence fixture, external archive, or ignore policy. | Only if approved as evidence fixture | No | Yes | No | Yes |
| `data/raw/world_bank/logs/world_bank_connector.log` | Modified tracked | Delete-later-with-approval candidate | Runtime log is generated and should not normally be source-controlled. | Medium | Decide retain as audit evidence, archive, or delete later. | Only by explicit exception | Yes | Yes | No | Yes |
| `data/validated/approved_world_bank_metadata_40107522.json` | Modified tracked | Archive-later candidate | Validated output is generated evidence and may be historical fixture. | Medium | Decide Aegis-era evidence fixture, archive, or exclude. | Only if approved as fixture | No | Yes | No | Yes |
| `data/validated/validator.log` | Modified tracked | Delete-later-with-approval candidate | Runtime validation log is generated and should not normally be committed. | Medium | Decide retain as audit evidence, archive, or delete later. | Only by explicit exception | Yes | Yes | No | Yes |
| `reports/manifest.json` | Modified tracked | Archive-later candidate | Publication manifest is generated Apollo-like artifact, not source. | Medium | Decide publication fixture, archive, or exclude. | Only if approved as fixture | No | Yes | No | Yes |
| `sources/source_registry.json` | Modified tracked | Review-before-decision | Could be canonical Thoth registry state or transitional fixture data. | High | Decide canonical registry, fixture, generated artifact, or archive. | Yes, if accepted as registry/fixture | No | Yes | Yes | Yes |

## 5. Untracked Source/Test Disposition Table

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `backend/alis/connectors/*.py` | Untracked | Commit candidate | Hermes connector candidates are source files and must be baselined before migration if accepted. | High | Accept as Hermes transport candidates or reject as superseded. | Yes, if accepted | No | No | No | Yes |
| `backend/alis/world_bank_connector.py` | Untracked | Review-before-decision | Duplicate connector path may be legacy or still required. | High | Compare with `backend/alis/connectors/world_bank.py`. | Maybe | No | No | No | Yes |
| `backend/alis/ons_connector.py` | Untracked | Review-before-decision | Duplicate connector path may be legacy or still required. | High | Compare with `backend/alis/connectors/ons.py`. | Maybe | No | No | No | Yes |
| `backend/alis/source_registry.py` | Untracked | Commit candidate | Thoth source registry candidate should be versioned if accepted. | High | Accept as Thoth candidate or require registry redesign. | Yes, if accepted | No | No | No | Yes |
| `backend/alis/mappers/evidence_to_visualisation.py` | Untracked | Commit candidate | Abacus mapping candidate should be baselined if accepted. | Medium | Confirm it produces chart-ready data without rendering or unvalidated input. | Yes, if accepted | No | No | No | Yes |
| `backend/alis/schemas/*.py` | Untracked | Commit candidate | Shared schema candidates should be versioned if accepted. | Medium | Confirm artifact schema ownership and names. | Yes, if accepted | No | No | No | Yes |
| `backend/alis/validators/statistical_gatekeeper.py` | Untracked | Review-before-decision | Ambiguous Abacus statistical check vs Aegis gate behavior. | High | Decide owner before committing. | Maybe | No | No | No | Yes |
| `backend/alis/pipelines/*.py` | Untracked | Review-before-decision | Pipelines likely cross Hermes, Thoth, Aegis, and orchestration boundaries. | High | Split ownership decision before baseline commit. | Maybe | No | No | No | Yes |
| `backend/alis/visualisation/*.py` | Untracked | Review-before-decision | Mixed Abacus chart specification and Apollo rendering responsibilities. | High | Assign each file to Abacus, Apollo, product, or integration support. | Maybe | No | No | No | Yes |
| `backend/alis/publishing/*.py` | Untracked | Review-before-decision | Mixed Apollo, Aegis, Argus, Thoth, and GoDataBank product concerns. | High | File-level owner decision before commit. | Maybe | No | Some files yes | No | Yes |
| `backend/publisher/*` | Untracked | Review-before-decision | Older publisher path may be legacy or Apollo candidate. | Medium | Determine active vs superseded status. | Maybe | No | No | No | Yes |
| `backend/publishing/**` | Untracked | Review-before-decision | Placeholder/product publishing structure with unclear status. | Medium | Decide product layer, legacy, or placeholder disposition. | Maybe | No | No | No | Yes |
| `scripts/*` | Untracked | Review-before-decision | Scripts may be tooling, examples, or old orchestration with imports/external calls. | Medium | Decide developer tool, fixture, or legacy status. | Maybe | No | No | No | Yes |
| `tests/alis/*.py` | Untracked | Commit candidate | Test source should be baselined if accepted; needed for future movement. | High | Accept and later map tests to engine/product/integration owners. | Yes, if accepted | No | No | No | Yes |
| `tests/abacus/README.md` and `tests/integration/README.md` | Untracked | Commit candidate | Test documentation/placeholders support future test structure. | Low | Accept as test docs or revise later. | Yes, if accepted | No | No | No | No |
| `tests/**/.gitkeep` | Untracked | Review-before-decision | Existing placeholders may be useful but require policy. | Low | Decide whether placeholders are allowed in current tree. | Maybe | No | No | No | No |

## 6. Documentation Disposition Table

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Untracked | Commit candidate | Governing V1.0-R1 boundary register must be baselined before migration. | High | Approve boundary register as current governing contract. | Yes | No | No | No | Yes |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Untracked | Commit candidate | Audit baseline is required planning evidence. | High | Approve as audit evidence. | Yes | No | No | No | Yes |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Untracked | Commit candidate | Architecture migration plan is required planning evidence. | High | Approve as planning evidence. | Yes | No | No | No | Yes |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Untracked | Commit candidate | Classification register is required planning evidence. | High | Approve as planning evidence. | Yes | No | No | No | Yes |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md` | Untracked | Commit candidate | Baseline and skeleton plan is required planning evidence. | High | Approve revised V1.0-R1 baseline plan. | Yes | No | No | No | Yes |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md` | Untracked after creation | Commit candidate | This disposition register should be committed only after independent review. | High | Approve this register. | Yes | No | No | No | Yes |
| Other `docs/reviews/*.md` | Untracked | Commit candidate | Historical milestone review evidence should generally be preserved. | Medium | Confirm review evidence set is intentional. | Yes, if accepted | No | No | No | No |
| `docs/contracts/**` | Untracked | Commit candidate | Existing contracts are source-of-truth or historical contract evidence. | Medium | Confirm whether contracts are current or historical. | Yes | No | No | No | Yes |
| `docs/governance/**` | Untracked | Commit candidate | Governance documents support Aegis/Thoth policy context. | Medium | Confirm governance docs are approved evidence. | Yes | No | No | No | Yes |
| `docs/architecture/SYSTEM_ARCHITECTURE.md` | Untracked | Review-before-decision | Older architecture document may conflict with eight-engine model. | Medium | Decide current, historical, or revise-later status. | Maybe | No | No | No | No |
| Root-level `docs/*.md` review/policy files | Mixed tracked/untracked | Review-before-decision | Mix of policies, workspace rules, and older reviews. | Medium | Classify current policy vs historical evidence. | Maybe | No | No | Maybe | No |
| `docs/**/.gitkeep` | Untracked | Review-before-decision | Existing placeholders are low risk but should follow placeholder policy. | Low | Decide whether current placeholder files are kept. | Maybe | No | No | No | No |

## 7. Generated Artifact Disposition Table

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `**/__pycache__/` | Untracked | Ignore candidate | Generated Python cache folders should not be source-controlled. | Low | Approve ignore policy; cleanup later only with approval. | No | Yes | No | No | Yes |
| `**/*.pyc` | Untracked | Delete-later-with-approval candidate | 100 generated bytecode files observed. | Low | Approve cleanup milestone; do not delete now. | No | Yes | No | No | Yes |
| `data/raw/ons/**` | Untracked | Archive-later candidate | Raw ONS retrieval snapshots/logs are generated evidence. | Medium | Decide fixture, archive, ignore, or delete-later policy. | Only by exception | No | Yes | No | Yes |
| `data/raw/world_bank/archive/**` | Untracked | Archive-later candidate | Raw World Bank archive snapshot is generated evidence. | Medium | Decide fixture or archive policy. | Only by exception | No | Yes | No | Yes |
| Modified `data/raw/world_bank/latest_metadata.json` | Modified tracked | Archive-later candidate | Raw generated source snapshot. | Medium | Decide fixture or archive policy. | Only by exception | No | Yes | No | Yes |
| `data/raw/*/logs/*.log` | Mixed tracked/untracked | Delete-later-with-approval candidate | Runtime logs are generated and normally excluded. | Medium | Decide audit retention before cleanup. | Only by exception | Yes | Yes | No | Yes |
| `data/validated/**/*.json` | Mixed tracked/untracked | Archive-later candidate | Validated output may be historical evidence or fixture. | Medium | Decide evidence fixture or archive status. | Only by exception | No | Yes | No | Yes |
| `data/validated/*.log` | Modified tracked | Delete-later-with-approval candidate | Runtime validation log is generated. | Medium | Decide audit retention before cleanup. | Only by exception | Yes | Yes | No | Yes |
| `data/classified/**/*.json` | Mixed tracked/untracked | Archive-later candidate | Generated classified analysis outputs. | Medium | Decide fixture/evidence/ignore status. | Only by exception | No | Yes | No | Yes |
| `data/summaries/**/*.json` | Untracked | Archive-later candidate | Generated summary/narrative output. | Medium | Decide fixture/evidence/ignore status. | Only by exception | No | Yes | No | Yes |
| `data/publishing/candidate_output_v0_1/**` | Untracked | Delete-later-with-approval candidate | Older candidate output flagged as failed/superseded candidate. | Medium | Confirm whether historical evidence must be retained. | Only by exception | Yes | Yes | No | Yes |
| `data/publishing/candidate_output_v0_2/**` | Untracked | Archive-later candidate | Current production-candidate output may be release evidence. | High | Decide release evidence retention and storage policy. | Only by exception | No | Yes | No | Yes |
| `data/publishing/evidence/**` | Untracked | Archive-later candidate | Production candidate evidence may be audit evidence. | High | Decide evidence retention. | Only by exception | No | Yes | No | Yes |
| `data/publishing/production_candidate_inputs_v*/**` | Untracked | Archive-later candidate | Staged/generated publication inputs. | Medium | Decide fixture or artifact archive policy. | Only by exception | No | Yes | No | Yes |
| `data/published/**` | Untracked | Review-before-decision | Published area includes placeholders/docs and may not be true output. | Medium | Decide artifact, docs, or placeholder disposition. | Maybe | No | Yes | No | Yes |
| `reports/generated/*.html` | Untracked | Archive-later candidate | Generated HTML reports are publication artifacts. | Medium | Decide publication artifact retention. | Only by exception | No | Yes | No | Yes |
| `reports/manifest.json` | Modified tracked | Archive-later candidate | Generated publication manifest. | Medium | Decide fixture or archive status. | Only by exception | No | Yes | No | Yes |
| `evidence_package_output.json` | Untracked | Delete-later-with-approval candidate | Root generated evidence artifact should not remain as source by default. | Medium | Decide retain/archive/delete later. | Only by exception | Yes | Yes | No | Yes |

## 8. Ignore Candidates

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `**/__pycache__/` | Untracked | Ignore candidate | Python cache folders are generated. | Low | Approve ignore policy. | No | Yes | No | No | Yes |
| `**/*.pyc` | Untracked | Ignore candidate | Python bytecode is generated and platform/runtime-specific. | Low | Approve ignore policy and later cleanup. | No | Yes | No | No | Yes |
| Runtime logs under `data/**/logs/` | Mixed | Ignore candidate | Logs should not be committed by default. | Medium | Decide audit exceptions before ignoring tracked logs. | Only by exception | Yes | Yes | No | Yes |

## 9. Archive-Later Candidates

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `data/raw/**/*.json` | Mixed | Archive-later candidate | Raw source snapshots may be evidence. | Medium | Decide fixture vs external archive. | Only by exception | No | Yes | No | Yes |
| `data/validated/**/*.json` | Mixed | Archive-later candidate | Validated data may be evidence. | Medium | Decide fixture vs external archive. | Only by exception | No | Yes | No | Yes |
| `data/classified/**/*.json` | Mixed | Archive-later candidate | Generated analysis output. | Medium | Decide fixture vs external archive. | Only by exception | No | Yes | No | Yes |
| `data/summaries/**/*.json` | Untracked | Archive-later candidate | Generated narrative output. | Medium | Decide fixture vs external archive. | Only by exception | No | Yes | No | Yes |
| `reports/generated/**/*.html` | Untracked | Archive-later candidate | Generated publication output. | Medium | Decide publication evidence retention. | Only by exception | No | Yes | No | Yes |
| `data/publishing/candidate_output_v0_2/**` | Untracked | Archive-later candidate | May be current production candidate evidence. | High | Decide release evidence retention. | Only by exception | No | Yes | No | Yes |

## 10. Delete-Later-With-Approval Candidates

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `**/*.pyc` | Untracked | Delete-later-with-approval candidate | Generated bytecode has no source value. | Low | Approve cleanup. | No | Yes | No | No | Yes |
| `**/__pycache__/` | Untracked | Delete-later-with-approval candidate | Generated cache folders have no source value. | Low | Approve cleanup. | No | Yes | No | No | Yes |
| `data/raw/*/logs/*.log` | Mixed | Delete-later-with-approval candidate | Runtime logs should be retained only by evidence policy. | Medium | Approve archive or deletion. | Only by exception | Yes | Yes | No | Yes |
| `data/validated/validator.log` | Modified tracked | Delete-later-with-approval candidate | Runtime validation log. | Medium | Approve archive or deletion. | Only by exception | Yes | Yes | No | Yes |
| `data/publishing/candidate_output_v0_1/**` | Untracked | Delete-later-with-approval candidate | Older candidate output may be superseded. | Medium | Confirm not required as historical evidence. | Only by exception | Yes | Yes | No | Yes |
| `evidence_package_output.json` | Untracked | Delete-later-with-approval candidate | Root generated artifact should not remain by default. | Medium | Confirm not needed as fixture/evidence. | Only by exception | Yes | Yes | No | Yes |

## 11. Review-Before-Decision Candidates

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `backend/validators/**` | Modified tracked | Review-before-decision | Transitional validator ownership is unresolved. | High | Decide Aegis, shared schema, legacy, or reject. | Maybe | No | No | Yes | Yes |
| `backend/alis/pipelines/**` | Untracked | Review-before-decision | Mixed orchestration and artifact-builder responsibilities. | High | Decide per-file owner before commit. | Maybe | No | No | No | Yes |
| `backend/alis/publishing/**` source files | Untracked | Review-before-decision | Mixed Apollo, Aegis, Argus, Thoth, and product concerns. | High | Decide per-file owner before commit. | Maybe | No | Some files yes | No | Yes |
| `backend/alis/visualisation/chart_spec_export.py` and `minimal_chart_engine.py` | Untracked | Review-before-decision | Ambiguous Abacus chart spec vs Apollo rendering. | High | Decide artifact owner. | Maybe | No | No | No | Yes |
| `backend/publisher/**` | Untracked | Review-before-decision | Older publisher may be legacy or Apollo candidate. | Medium | Determine active status. | Maybe | No | No | No | Yes |
| `backend/publishing/**` | Untracked | Review-before-decision | Placeholder/product/legacy status unclear. | Medium | Determine product or legacy status. | Maybe | No | No | No | Yes |
| `scripts/**` | Untracked | Review-before-decision | Scripts may encode old flows or external calls. | Medium | Decide tool, example, fixture, or legacy. | Maybe | No | No | No | Yes |
| `sources/source_registry.json` | Modified tracked | Review-before-decision | Could be canonical Thoth registry or fixture data. | High | Decide registry authority and storage policy. | Yes, if accepted | No | Yes | Yes | Yes |
| `templates/report_template.html` | Untracked | Review-before-decision | Could be Apollo generic template or GoDataBank product template. | Medium | Decide template owner. | Maybe | No | No | No | Yes |
| `docs/architecture/SYSTEM_ARCHITECTURE.md` | Untracked | Review-before-decision | Older architecture model may conflict with V1.0-R1. | Medium | Mark historical, revise later, or approve as context. | Maybe | No | No | No | No |

## 12. Do-Not-Touch Items

| Path or path group | Tracked status | Proposed disposition | Reason | Risk | Required human decision before action | May be baseline commit | Must exclude | Artifact review | Line-ending review | Blocks skeleton |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `.git/` | Repository metadata | Do-not-touch | Git metadata must not be modified manually. | High | None; never alter through migration planning. | No | Yes | No | No | No |
| `src/` | Not present | Do-not-touch | Target skeleton root must not be created yet. | High | Create only in authorised skeleton milestone. | No | No | No | No | Yes |
| `artifacts/` | Not present | Do-not-touch | Artifact root requires retention policy first. | High | Create only after artifact policy approval. | No | No | Yes | No | Yes |
| `legacy/` | Not present | Do-not-touch | Legacy holding area requires legacy policy first. | High | Create only after legacy policy approval. | No | No | No | No | Yes |
| `docs/migration/` | Not present | Do-not-touch | Migration docs folder is skeleton work. | Medium | Create only after skeleton approval. | No | No | No | No | Yes |
| `tests/alis_core/` and `tests/godatabank/` | Not present | Do-not-touch | Target test skeleton requires test mapping first. | Medium | Create only after test mapping approval. | No | No | No | No | Yes |
| Any file movement target path | Not present or current tree | Do-not-touch | Migration is not authorised. | High | Requires future migration milestone. | No | No | No | No | Yes |

## 13. Skeleton Creation Blockers

Skeleton creation is blocked until these dispositions are resolved:

| Blocker | Reason | Required resolution |
| --- | --- | --- |
| 13 modified tracked files | Migration must not start from unreviewed tracked changes. | Accept, reject, archive, or otherwise disposition each group. |
| 250 baseline untracked paths | Untracked source/test/docs/artifacts make provenance unclear. | Approve commit/ignore/archive/delete disposition by group. |
| 100 untracked `.pyc` files | Generated cache files must not enter baseline. | Approve ignore and later cleanup policy. |
| `__pycache__/` folders | Generated cache folders must not enter baseline. | Approve ignore and later cleanup policy. |
| Generated logs | May be audit evidence but should not be committed by default. | Artifact-retention decision. |
| Generated reports and publication outputs | Product/release evidence may need archive, not source commit. | Publication artifact-retention decision. |
| Raw and validated data | Evidence may be fixture or archive material. | Evidence-retention decision. |
| `evidence_package_output.json` | Root generated artifact. | Decide archive/delete-later/fixture status. |
| `sources/source_registry.json` | Possible Thoth registry state. | Human decision on canonical registry authority. |
| Untracked backend source candidates | Source must be accepted or rejected before migration. | Commit accepted source candidates or reject separately. |
| Untracked tests | Tests must be accepted and mapped before movement. | Commit accepted tests after review. |
| Planning/review docs under `docs/reviews/` | Planning baseline should be preserved if approved. | Commit approved review docs. |
| Line-ending warnings | Seven tracked files may churn on commit. | Line-ending policy review. |

## 14. Risks

| Risk | Severity | Evidence | Mitigation |
| --- | --- | --- | --- |
| Premature commit of generated artifacts | High | Generated data, logs, reports, and caches are present. | Commit only after artifact-retention review. |
| Loss of audit evidence through cleanup | High | Logs and production-candidate evidence may be historical records. | Archive or retain before any deletion. |
| Skeleton creation from unstable baseline | High | Modified and untracked paths are unresolved. | Resolve dispositions before skeleton creation. |
| Wrong engine ownership enters baseline | High | Pipelines, validators, publishing, visualisation, and registry paths are ambiguous. | Human owner review before commit. |
| `.pyc` files pollute repository history | Medium | 100 untracked bytecode files observed. | Ignore and delete later only with approval. |
| Line-ending normalization obscures real changes | Medium | Git reported LF-to-CRLF warnings for seven tracked files. | Review line-ending policy before commit. |
| Product code enters ALIS Core | Medium | Templates and publishing paths may be product-specific. | Product/core boundary review before commit or migration. |
| Review documents remain uncommitted | Medium | Key planning docs are untracked. | Commit approved docs before migration. |

## 15. Recommended Next Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Source-Control Disposition Register v1.0
```

The review should approve or revise this register before any staging, commit,
cleanup, skeleton creation, migration, or engine implementation. After review,
the next actionable milestone should be a source-control baseline commit plan
that specifies the exact approved file groups to stage and the groups to exclude
or defer.

STATUS: SOURCE-CONTROL DISPOSITION REGISTER CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
