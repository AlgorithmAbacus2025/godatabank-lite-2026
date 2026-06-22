# ALIS Core Thoth Registry Narrow Implementation Authorisation Plan v1.0-R1

## 1. Purpose

This document defines a planning-only narrow authorisation plan for a future implementation revision of `backend/alis/source_registry.py`. It decides whether a future implementation milestone may be authorised, but it does not perform or authorise immediate implementation.

---

## 2. Controlling Documents Reviewed

This plan has been developed by reviewing and evaluating the following controlling documents:
* [ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md)
* [ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md)
* [ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md)
* [ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_TEST_CANDIDATE_CLASSIFICATION_REGISTER_V1_0.md)
* [ALIS_CORE_READINESS_GOVERNANCE_CHECKPOINT_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_READINESS_GOVERNANCE_CHECKPOINT_V1_0.md)

---

## 3. Current Governance State

* Codex implementation remains paused.
* Source/test implementation remains paused.
* Registry implementation remains paused.
* Cleanup is not authorised.
* `.gitignore` change is not authorised.
* Skeleton creation is not authorised.
* Migration is not authorised.
* Source edits are not authorised.
* Test edits are not authorised.
* Registry implementation is not authorised.
* No staging or commits are performed in this milestone.

---

## 4. Current Blocked Files

The following files must remain blocked:
* `backend/alis/source_registry.py` (Source file - pending narrow implementation revision)
* `sources/source_registry.json` (Prototype/fixture data - not production canonical state)
* `tests/alis/test_source_registry.py` (Test file - blocked)
* `tests/alis/test_registry_integration.py` (Test file - blocked)

---

## 5. Proposed Future Implementation Target

The only file permitted for edits in a future execution milestone is:
* `backend/alis/source_registry.py`

---

## 6. Authorised Future Implementation Boundary

Any future implementation milestone must remain strictly within the following boundaries:
* Remove dependency on `sources/source_registry.json` as production canonical state.
* Stop describing the JSON file as canonical registry state.
* Introduce or enforce Thoth-owned canonical source IDs.
* Represent source entries using the minimum fields required by the frozen Thoth Registry Design.
* Preserve fail-closed validation behaviour.
* Keep network retrieval and operations out of Thoth.
* Keep policy gate decisions out of Thoth.
* Keep source admission/proposal workflows out of Thoth.
* Keep analytics, rendering, and observability outside Thoth.
* Avoid broad abstractions or plugin systems.

---

## 7. Explicit Non-Authorised Actions

The following actions are strictly **not authorised**:
* Editing test files (e.g., `tests/alis/test_source_registry.py`, `tests/alis/test_registry_integration.py`).
* Editing `sources/source_registry.json`.
* Creating a database or database schema.
* Creating runtime storage or cache areas.
* Creating fixture files.
* Moving files.
* Renaming packages.
* Changing imports outside the target file.
* Editing Aegis, Arya, Hermes, Abacus, Apollo, Argus, or GoDataBank product code.
* Adding external packages or dependencies.
* Changing `.gitignore`.
* Cleaning up workspace directories.
* Creating skeleton folders.
* Performing migrations.
* Executing commits or staging in this milestone.

---

## 8. Minimum Permissible Implementation Changes

Edits to `backend/alis/source_registry.py` must do only the following:
1. Correct documentation and code comments to remove references to `sources/source_registry.json` as canonical production registry state.
2. Remove GoDataBank product-specific vocabulary and align it with ALIS Core Thoth naming conventions.
3. Model a minimal Source Registry Entry entity according to the Thoth Registry Design.
4. Establish fail-closed verification checks for expected registry metadata fields.
5. Defer or stub mutation, provenance, lineage, and checksum logic.

If provenance, lineage, mutation history, or checksum logic is deferred or stubbed, the implementation must label this as incomplete non-production behaviour. The revised helper must not claim full canonical Thoth registry compliance until those elements are implemented and separately reviewed.

---

## 9. Required Acceptance Criteria

A future implementation is acceptable only if:
* The source file `backend/alis/source_registry.py` passes Python syntax compilation using:
  ```powershell
  python -m py_compile backend/alis/source_registry.py
  ```
* No changes occur outside `backend/alis/source_registry.py`.
* All engine boundaries defined in the Boundary Register remain fully respected.
* No policy decision code is added to the registry lookup functionality.

---

## 10. Required Verification Commands for Future Execution

The future execution agent must run the following validation checks:

1. Verify no pre-existing staged files before edits:
   ```powershell
   git diff --cached --name-only
   ```
   If any staged file exists, abort before editing.

2. After the future implementation edit, verify that only this file is modified and/or staged:
   `backend/alis/source_registry.py`

---

## 11. Test Status and Restrictions

* **Tests remain blocked** until a later separate test authorisation milestone.
* No test files are authorised for editing, staging, or execution under this plan.

---

## 12. Registry Data Restrictions

* No database creation, runtime storage deployment, fixture promotion, or modification to JSON files is authorised.
* Registry state must be read-only and memory-only for prototype structures.

---

## 13. Source-Control Restrictions

* Only explicit staging command (e.g. `git add backend/alis/source_registry.py`) is allowed.
* Globbing or directory-level additions (`git add .`) are strictly prohibited.

---

## 14. Overengineering Restrictions

* No broad class hierarchies, factories, plugin systems, service containers, adapters, orchestration layers, or generic abstraction frameworks are permitted. A minimal dataclass, TypedDict, dictionary schema, or equivalent simple structure is permitted only if required to represent the Source Registry Entry specified by the frozen Thoth Registry Design.
* No new frameworks, external dependencies, or complex registry containers are permitted.
* Implement only the minimum code paths required.

---

## 15. Abort Conditions

A future implementation execution must abort immediately if:
* Staged changes exist before execution starts.
* Any edits are attempted on files other than `backend/alis/source_registry.py`.
* External libraries are added.
* Database files or filesystem caches are generated.

---

## 16. Decision

**AUTHORISATION PLAN PASSED — FUTURE NARROW IMPLEMENTATION MAY BE AUTHORISED**

No implementation is authorised by this milestone.

---

## 17. Recommended Next Milestone

The recommended next milestone is:
```text
Thoth Registry Narrow Implementation Execution Authorisation v1.0
```
This next milestone must still be independently reviewed and approved before any source file edits are executed.

---

STATUS: THOTH REGISTRY NARROW IMPLEMENTATION AUTHORISATION PLAN REVISED
REVISION: V1.0-R1
CODEX IMPLEMENTATION: PAUSED
SOURCE IMPLEMENTATION: PAUSED
TEST IMPLEMENTATION: PAUSED
REGISTRY IMPLEMENTATION: PAUSED
STAGING: NOT PERFORMED
COMMITS: NOT PERFORMED
CODE CHANGES: NOT PERFORMED
TEST CHANGES: NOT PERFORMED
REGISTRY CHANGES: NOT PERFORMED
CLEANUP: NOT PERFORMED
GITIGNORE CHANGES: NOT PERFORMED
NEXT RECOMMENDED STEP: Independent Review
