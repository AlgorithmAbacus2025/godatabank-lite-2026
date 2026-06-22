# ALIS Core Thoth Registry Narrow Implementation Execution Authorisation v1.0

## 1. Purpose

This document defines a planning-only narrow execution authorisation for a future narrow implementation edit to `backend/alis/source_registry.py`. It does not perform or authorise immediate implementation edits to source code in this milestone.

---

## 2. Controlling Documents Reviewed

This plan has been developed by reviewing and evaluating the following controlling documents:
* [ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/architecture/ALIS_CORE_THOTH_REGISTRY_DESIGN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_IMPLEMENTATION_REVISION_PLAN_INDEPENDENT_REVIEW_V1_0.md)
* [ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_AUTHORISATION_PLAN_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_THOTH_REGISTRY_NARROW_IMPLEMENTATION_AUTHORISATION_PLAN_V1_0.md)
* [ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_NARROW_THOTH_REGISTRY_IMPLEMENTATION_CANDIDATE_REVIEW_V1_0.md)
* [ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md](file:///C:/Users/kmudh/Documents/GoDataBank/docs/reviews/ALIS_CORE_SOURCE_REGISTRY_AUTHORITY_DECISION_V1_0.md)
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

## 4. Future Implementation Target

The only file permitted for edits in a future execution milestone is:
* `backend/alis/source_registry.py`

---

## 5. Exact Authorised Edit Boundary

The future implementation may only:
* Remove dependency on `sources/source_registry.json` as production canonical state.
* Stop describing the JSON file as canonical registry state.
* Introduce or enforce Thoth-owned canonical source IDs.
* Represent source entries using the minimum fields required by the frozen Thoth Registry Design.
* Preserve fail-closed validation behaviour.
* Keep network retrieval and operations out of Thoth.
* Keep policy gate decisions out of Thoth.
* Keep source admission/proposal workflows out of Thoth.
* Keep analytics, rendering, publication, and observability outside Thoth.
* Use only a minimal dataclass, TypedDict, dictionary schema, or equivalent simple structure if required.
* Label deferred provenance, lineage, mutation history, and checksum logic as incomplete non-production behaviour.

---

## 6. Explicitly Prohibited Edits

The future implementation must **not**:
* Edit test files (e.g., `tests/alis/test_source_registry.py`, `tests/alis/test_registry_integration.py`).
* Edit `sources/source_registry.json`.
* Create a database or database schema.
* Create runtime storage.
* Create fixture files.
* Move files.
* Rename packages.
* Change imports outside `backend/alis/source_registry.py`.
* Edit Aegis, Arya, Hermes, Abacus, Apollo, Argus, or GoDataBank product code.
* Add external packages or dependencies.
* Change `.gitignore`.
* Clean up workspace files.
* Create skeleton folders.
* Perform migrations.
* Claim full canonical Thoth registry compliance if provenance, lineage, mutation history, or checksum logic remains incomplete.

---

## 7. Minimum Permitted Code Changes

* Decouple the registry helper from local JSON parsing.
* Implement a minimal representation of the Source Registry Entry model.
* Limit functions to metadata retrieval, and label all deferred design features explicitly as non-canonical stubs.

---

## 8. Required Future Verification Steps

1. Before editing:
   ```powershell
   git diff --cached --name-only
   ```
   If any staged file exists, abort before editing.

2. After editing:
   Verify only `backend/alis/source_registry.py` is modified and/or staged.

3. Syntax check:
   ```powershell
   python -m py_compile backend/alis/source_registry.py
   ```

4. Before commit:
   ```powershell
   git diff --cached --name-only
   ```
   The staged file list must contain exactly:
   `backend/alis/source_registry.py`

---

## 9. Required Future Staging Commands

Future staging command must be exactly:
```powershell
git add backend/alis/source_registry.py
```

---

## 10. Required Future Commit Message

Future commit message must be exactly:
```text
feat(thoth): revise source registry helper boundary
```

---

## 11. Acceptance Criteria

A future implementation is acceptable only if:
* The source file `backend/alis/source_registry.py` passes Python syntax compilation using:
  ```powershell
  python -m py_compile backend/alis/source_registry.py
  ```
* No changes occur outside `backend/alis/source_registry.py`.
* All engine boundaries defined in the Boundary Register remain fully respected.
* No policy decision code is added to the registry lookup functionality.

---

## 12. Abort Conditions

A future implementation execution must abort immediately if:
* Staged changes exist before execution starts.
* Any edits are attempted on files other than `backend/alis/source_registry.py`.
* External libraries are added.
* Database files or filesystem caches are generated.

---

## 13. Decision

**EXECUTION AUTHORISATION PASSED — FUTURE NARROW IMPLEMENTATION MAY PROCEED AFTER INDEPENDENT REVIEW**

---

## 14. Recommended Next Milestone

The recommended next milestone is:
```text
Independent Review of Thoth Registry Narrow Implementation Execution Authorisation v1.0
```
This execution authorisation must be independently reviewed and approved before any source file edits are performed.

---

STATUS: THOTH REGISTRY NARROW IMPLEMENTATION EXECUTION AUTHORISATION CREATED
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
