# ALIS Core Source-Control Baseline Commit Plan v1.0

## 1. Purpose

This document defines a proposed first source-control baseline commit plan for
the current repository state.

It is based on the frozen Source-Control Disposition Register v1.0 and separates
files that may be included in a future baseline commit from files that must be
excluded or deferred. It does not stage, commit, move, rename, delete, clean,
refactor, change imports, create skeleton folders, implement engines, modify
`.gitignore`, or restructure the repository.

The purpose is to make the first baseline commit reviewable before any Git
operation is performed.

## 2. Source Documents Reviewed

| Document | Role |
| --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Governing ALIS Core engine boundary register, revision V1.0-R1. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Target repository architecture and migration plan. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | File and folder classification source. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md` | Baseline and skeleton planning source, revision V1.0-R1. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md` | Frozen disposition source for this commit plan. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Repository audit and technical-debt evidence. |

## 3. Commit-Plan Principles

1. Documentation first: the first baseline commit should preserve reviewed
   architecture, classification, disposition, and planning evidence before code
   movement or skeleton creation.
2. No generated artifact by default: generated logs, reports, data outputs,
   bytecode, and production-candidate artifacts should be excluded unless a
   human approves them as fixtures or evidence.
3. No ambiguous source without review: source candidates with unresolved engine
   ownership should not be staged in the first baseline commit.
4. No skeleton folders: `src/`, `artifacts/`, `legacy/`, `docs/migration/`,
   `tests/alis_core/`, and `tests/godatabank/` must not be created.
5. No import or code changes: baseline commit planning must not modify runtime
   behavior.
6. Line endings must be reviewed before committing any tracked files that Git
   warned may change from LF to CRLF.
7. Staging must be explicit and reviewed. This document is not authorization to
   run `git add` or `git commit`.

## 4. Proposed Baseline Commit Scope

Recommended first baseline commit scope:

```text
Documentation-only baseline commit.
```

The safest first commit should include only approved planning, architecture,
contract, governance, and review documents after human review. It should exclude
all generated artifacts, Python bytecode, runtime logs, generated report output,
raw/validated data, root generated JSON, and unresolved source/test candidates.

Proposed first commit intent:

- preserve the governing ALIS Core boundary register
- preserve repository architecture, classification, baseline, disposition, and
  commit-plan evidence
- preserve approved architecture/contracts/governance/review documentation
- leave source code, tests, generated artifacts, and skeleton creation for later
  reviewed commits

## 5. Files/Path Groups Approved for Commit, Subject to Human Approval

| Path or path group | Category | Proposed first baseline action | Human approval required | Notes |
| --- | --- | --- | --- | --- |
| `docs/architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md` | Approved documentation commit candidate | Include after review approval. | Approve as governing V1.0-R1 boundary contract. | Blocks skeleton until committed or otherwise baselined. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ENGINEERING_AUDIT_V1_0.md` | Approved documentation commit candidate | Include after review approval. | Approve as audit evidence. | Source for later planning docs. |
| `docs/reviews/ALIS_CORE_REPOSITORY_ARCHITECTURE_PLAN_V1_0.md` | Approved documentation commit candidate | Include after review approval. | Approve as architecture planning evidence. | Defines target structure. |
| `docs/reviews/ALIS_CORE_REPOSITORY_CLASSIFICATION_REGISTER_V1_0.md` | Approved documentation commit candidate | Include after review approval. | Approve as classification evidence. | Supports file ownership review. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_AND_SKELETON_PLAN_V1_0.md` | Approved documentation commit candidate | Include after review approval. | Approve revised V1.0-R1 plan. | Defines baseline and skeleton constraints. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_DISPOSITION_REGISTER_V1_0.md` | Approved documentation commit candidate | Include after review approval. | Approve disposition register. | Frozen source for this commit plan. |
| `docs/reviews/ALIS_CORE_SOURCE_CONTROL_BASELINE_COMMIT_PLAN_V1_0.md` | Approved documentation commit candidate | Include only after independent review. | Approve this commit plan. | This file is not self-approving. |
| Other `docs/reviews/*.md` | Approved documentation commit candidate | Include as a separate docs-evidence group if approved. | Confirm the full historical review set is intentional. | Avoid mixing with source or generated artifacts. |
| `docs/contracts/**` | Approved documentation commit candidate | Include if approved. | Confirm current vs historical contract status. | May need later indexing, but should be preserved. |
| `docs/governance/**` | Approved documentation commit candidate | Include if approved. | Confirm governance documents are approved baseline evidence. | Supports Aegis/Thoth policy context. |
| Root-level `docs/*.md` policy/review files | Deferred documentation candidate | Include only after document-by-document review. | Decide current policy vs historical evidence. | Some may be stale or workspace-specific. |

## 6. Files/Path Groups Excluded From Commit

| Path or path group | Reason for exclusion | Future action |
| --- | --- | --- |
| `**/__pycache__/` | Generated Python cache folders. | Ignore and delete later only with approval. |
| `**/*.pyc` | Generated Python bytecode; 100 untracked files observed. | Ignore and delete later only with approval. |
| Runtime logs under `data/**/logs/` | Generated operational logs. | Artifact-retention review, then archive/delete/ignore decision. |
| `data/validated/validator.log` | Generated validation log. | Artifact-retention review. |
| `reports/generated/**/*.html` | Generated report output. | Archive-later or fixture approval. |
| `reports/manifest.json` | Generated publication manifest. | Archive-later or fixture approval. |
| `evidence_package_output.json` | Root generated evidence artifact. | Archive/delete-later decision with approval. |
| `data/publishing/**` | Generated publication candidates, evidence, and staged inputs. | Artifact-retention review. |
| `data/raw/**/*.json` | Raw source retrieval snapshots. | Evidence-retention review. |
| `data/validated/**/*.json` | Validated output snapshots. | Evidence-retention review. |
| `data/classified/**/*.json` | Generated analytical output. | Fixture/evidence review. |
| `data/summaries/**/*.json` | Generated narrative output. | Fixture/evidence review. |

## 7. Files/Path Groups Deferred for Later Review

| Path or path group | Deferred category | Reason | Required review |
| --- | --- | --- | --- |
| `backend/abacus/README.md` | Source-code commit candidate requiring human approval | Modified tracked Abacus documentation with line-ending warning. | Confirm content and line endings before staging. |
| `backend/abacus/classifier.py` | Source-code commit candidate requiring human approval | Modified tracked Abacus source with line-ending warning. | Confirm source change and line endings before staging. |
| `backend/abacus/taxonomy.py` | Source-code commit candidate requiring human approval | Modified tracked Abacus source with line-ending warning. | Confirm source change, taxonomy governance, and line endings. |
| `backend/validators/**` | Review-before-decision files | Modified tracked validation source/docs with ambiguous ownership. | Decide Aegis, shared schema, legacy, or reject. |
| `backend/alis/connectors/*.py` | Source-code commit candidate requiring human approval | Hermes connector candidates. | Confirm accepted connector source and duplicate connector status. |
| `backend/alis/world_bank_connector.py` | Review-before-decision files | Duplicate World Bank connector path. | Compare with package connector. |
| `backend/alis/ons_connector.py` | Review-before-decision files | Duplicate ONS connector path. | Compare with package connector. |
| `backend/alis/source_registry.py` | Source-code commit candidate requiring human approval | Thoth registry candidate. | Confirm registry ownership and storage semantics. |
| `backend/alis/schemas/*.py` | Source-code commit candidate requiring human approval | Shared schema candidates. | Confirm artifact schema ownership. |
| `backend/alis/mappers/evidence_to_visualisation.py` | Source-code commit candidate requiring human approval | Abacus mapping candidate. | Confirm no rendering or unvalidated evidence dependency. |
| `backend/alis/validators/statistical_gatekeeper.py` | Review-before-decision files | Ambiguous Abacus vs Aegis responsibility. | Decide statistical check vs gate ownership. |
| `backend/alis/pipelines/*.py` | Review-before-decision files | Cross-boundary orchestration risk. | Split owner by artifact and handoff. |
| `backend/alis/visualisation/*.py` | Review-before-decision files | Mixed chart-spec/rendering responsibilities. | Assign Abacus, Apollo, product, or integration support. |
| `backend/alis/publishing/*.py` | Review-before-decision files | Mixed Apollo, Aegis, Argus, Thoth, and product concerns. | File-level ownership review. |
| `backend/publisher/**` | Review-before-decision files | Older publisher path may be legacy. | Determine active status. |
| `backend/publishing/**` | Review-before-decision files | Product/legacy placeholder ambiguity. | Determine product or legacy status. |
| `backend/summary/**` | Source-code commit candidate requiring human approval | Vyasa candidate. | Confirm evidence-traceable summary behavior. |
| `scripts/**` | Review-before-decision files | Tooling or orchestration ambiguity. | Decide developer tool, fixture, or legacy. |
| `templates/report_template.html` | Review-before-decision files | Apollo template vs GoDataBank product template ambiguity. | Decide owner. |
| `sources/source_registry.json` | Review-before-decision files | Possible canonical Thoth registry or fixture data, with line-ending warning. | Decide registry authority and line endings. |
| `tests/alis/*.py` | Test commit candidate requiring human approval | Test source should be baselined if accepted. | Accept tests and map later to owners. |
| `tests/abacus/README.md`, `tests/integration/README.md`, `tests/**/.gitkeep` | Test commit candidate requiring human approval | Test docs/placeholders. | Confirm placeholder policy. |
| `docs/architecture/SYSTEM_ARCHITECTURE.md` | Review-before-decision files | Older architecture model may conflict with V1.0-R1. | Mark historical, revise later, or approve as context. |

## 8. Generated Artifacts Excluded From Commit

| Path or path group | Exclusion type | Reason |
| --- | --- | --- |
| `**/*.pyc` | Ignore/delete-later-with-approval | Generated bytecode. |
| `**/__pycache__/` | Ignore/delete-later-with-approval | Generated cache folders. |
| `data/raw/ons/**` | Archive-later | Raw ONS retrieval artifacts and logs. |
| `data/raw/world_bank/**` generated JSON/log paths | Archive-later or delete-later for logs | Raw World Bank retrieval artifacts and logs. |
| `data/validated/**` generated JSON/log paths | Archive-later or delete-later for logs | Validated artifacts and runtime logs. |
| `data/classified/**` | Archive-later | Generated classified/analysis output. |
| `data/summaries/**` | Archive-later | Generated summary/narrative output. |
| `data/publishing/**` | Archive-later or delete-later with approval | Generated publication candidates, evidence, and inputs. |
| `reports/generated/**` | Archive-later | Generated HTML reports. |
| `reports/manifest.json` | Archive-later | Generated publication manifest. |
| `evidence_package_output.json` | Delete-later-with-approval or archive-later | Root generated evidence artifact. |

## 9. Line-Ending Review Requirements

Git reported LF-to-CRLF warnings for these tracked files. They should not be
included in a baseline commit until line-ending policy is reviewed:

| Path | Proposed action |
| --- | --- |
| `backend/abacus/README.md` | Review line endings before staging. |
| `backend/abacus/classifier.py` | Review line endings before staging. |
| `backend/abacus/taxonomy.py` | Review line endings before staging. |
| `backend/validators/README.md` | Review line endings before staging. |
| `backend/validators/schema.py` | Review line endings before staging. |
| `backend/validators/validator.py` | Review line endings before staging. |
| `sources/source_registry.json` | Review line endings before staging. |

Recommended policy decision before staging:

- decide whether to introduce `.gitattributes` in a later reviewed milestone
- decide whether to normalize tracked text files before baseline source commit
- do not allow line-ending churn to hide behavioral source changes

This milestone does not modify `.gitattributes` or line endings.

## 10. Proposed Commit Grouping Strategy

Recommended grouping, subject to human approval:

| Commit group | Include | Exclude | Reason |
| --- | --- | --- | --- |
| Group 1: Core planning documentation baseline | Boundary register, audit, architecture plan, classification register, baseline/skeleton plan, disposition register, baseline commit plan. | Source code, tests, generated artifacts, skeleton folders. | Establishes governance and planning source of truth. |
| Group 2: Historical docs/contracts/governance baseline | Approved `docs/reviews/*.md`, `docs/contracts/**`, `docs/governance/**`, selected root-level docs. | Stale or conflicting docs not yet reviewed. | Preserves milestone evidence after document review. |
| Group 3: Accepted source baseline | Accepted backend source candidates only. | Generated artifacts, ambiguous source groups, pycache. | Requires human owner review before staging. |
| Group 4: Accepted test baseline | Accepted test source/docs only. | Test pycache. | Requires test mapping approval before staging. |
| Group 5: Artifact fixture baseline, if approved | Only generated artifacts explicitly approved as fixtures/evidence. | Runtime logs and generated caches by default. | Requires artifact-retention approval. |

The first approved baseline commit should normally be Group 1 only.

## 11. Human Approval Checklist Before Staging

Before any future staging command, a human reviewer must confirm:

- the reviewed commit group is approved
- the exact paths to stage are listed
- no generated cache files are included
- no runtime logs are included unless explicitly approved
- no generated data or reports are included unless approved as fixtures/evidence
- no line-ending warning files are included without a line-ending decision
- no `src/`, `artifacts/`, `legacy/`, `docs/migration/`,
  `tests/alis_core/`, or `tests/godatabank/` folders are created
- no source-code commit candidates are included in a documentation-only commit
- no review-before-decision files are included without their decision recorded
- no `.gitignore` change is included unless separately requested
- no import paths or runtime code are modified

## 12. Commands That Remain Forbidden

These commands or action categories remain forbidden by this milestone:

- `git add`
- `git commit`
- `git reset`
- `git checkout --`
- `git clean`
- file deletion commands
- file move or rename commands
- generated artifact cleanup
- `.gitignore` modification
- skeleton folder creation
- import rewrites
- code refactoring
- engine implementation
- repository restructuring

Read-only Git inspection remains acceptable, but this document does not require
further command execution.

## 13. Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Documentation commit accidentally includes generated artifacts | High | Stage only explicit approved documentation paths in a later authorised action. |
| Source code enters baseline before ownership review | High | Keep source-code candidates deferred until human approval. |
| Tests are committed with pycache | High | Exclude `tests/**/__pycache__/` and `tests/**/*.pyc`. |
| Line-ending churn obscures source changes | Medium-high | Resolve line-ending policy before staging tracked source files. |
| Generated evidence is lost by exclusion | Medium-high | Exclude from commit now, but require archive/retention review before cleanup. |
| Stale docs become authoritative | Medium | Mark older docs as historical or review-before-decision before inclusion. |
| Skeleton creation starts prematurely | High | Keep target skeleton folders forbidden until post-baseline review. |
| `.gitignore` remains unchanged | Medium | This is intentional for this milestone; ignore policy should be separate. |

## 14. Abort Conditions

Abort any future baseline commit action if:

- the action would stage files not listed in an approved commit group
- generated `.pyc` or `__pycache__` files are included
- runtime logs are included without explicit artifact-retention approval
- generated data or reports are included without fixture/evidence approval
- tracked line-ending warning files are staged before line-ending review
- source files are staged during a documentation-only commit
- review-before-decision files are staged without recorded human decision
- `.gitignore` modification is included without explicit request
- skeleton folders are created or staged
- imports, code behavior, or repository structure would change
- any deletion, cleanup, move, or rename is required

## 15. Recommended Next Milestone

Recommended next milestone:

```text
Independent Review of ALIS Core Source-Control Baseline Commit Plan v1.0
```

The review should approve or revise the documentation-only first commit scope,
then separately authorize the exact staging command set if a baseline commit is
approved. No staging or commit should occur until that independent review is
complete.

STATUS: SOURCE-CONTROL BASELINE COMMIT PLAN CREATED
BASELINE: NOT CHANGED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
SKELETON: NOT CREATED
MIGRATION: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
DELETIONS: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
