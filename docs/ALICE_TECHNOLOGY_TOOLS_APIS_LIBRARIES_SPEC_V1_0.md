# Alice — Technology, Tools, APIs and Library Specification

**Document ID:** ALICE-TECH-001  
**Version:** 1.0 (proposed technology baseline)  
**Date:** 27 November 2026  
**Milestone:** M06  
**Status:** Documentation-only recommendation; pending approval.  
**Dependencies:** M01–M05 (stacked PRs #1–5, pending adoption).

## 1. Purpose and controlling documents

Alice is an Adaptive, Objective-Oriented Research, Analysis and Discovery Agent. Technology must support the agreed purpose, not determine it.

- [Founding Constitution](ALICE_FOUNDING_CONSTITUTION_V1_0.md)
- [System Definition](ALICE_SYSTEM_DEFINITION_V1_0.md)
- [System Requirements Specification (SRS)](ALICE_SYSTEM_REQUIREMENTS_SPECIFICATION_V1_0.md)
- [Research Formulation Engine (RFE)](ALICE_RESEARCH_FORMULATION_SPEC_V1_0.md)
- [ALIS Core architectural audit](ALICE_ALIS_CORE_ARCHITECTURAL_AUDIT_AND_EVOLUTION_V1_0.md)
- [ALIS Core Boundary Register](architecture/ALIS_CORE_BOUNDARY_REGISTER_V1_0.md)

M05 audited main commit 054114b3d0d711eecca005bfcce708b86b0e616b and identified legacy validator/schema, registry format and execution-order issues (F01–F03). These remain unresolved. Nothing in this specification authorises legacy repair, migration, test execution, dependency installation, credential creation, live research, external data transfer, spending or publication. Historical local assets have not been reconciled.

## 2. Selection method and constraints

Mandatory selection gates: supports the required capability and platform; compatible licence/terms and security policy; bounded external effects; replaceable behind a public contract; testable failure modes. Failure on a mandatory gate blocks adoption.

Compare remaining candidates by functional fit (30%), testability and maintainability (25%), privacy/security (20%), runtime footprint and latency (15%), and total cost (10%). These weights are proposed evaluation criteria; no fabricated comparative scores. Measure representative workloads and record rejected alternatives before freezing versions.

Reported development environment: Windows 11 Pro workstation, i9-14900KF, RTX 4090 with 24 GB VRAM, 128 GB system RAM, NVMe storage, VS Code, GitHub and LM Studio. These are operator-reported resources, not a current inspected inventory. Confirm Python, drivers, installed model IDs, quantisations, LM Studio version, disk availability and local server configuration before execution. No new hardware purchase recommended.

## 3. Release-specific stack

| ID | Technology | Phase / disposition | Requirement mapping | Alternative and reason |
| --- | --- | --- | --- | --- |
| T01 | Python 3.12 candidate baseline; venv, pip, pyproject.toml | P0; retain language, confirm supported patch | NFR-004,010 | Reuse a supported existing Python version if compatibility is better; no need for a second language in backend |
| T02 | Python enum, dataclasses, typing, graphlib, collections | P0; standard library | RFE-006–009, ORC-001,009 | Custom graph algorithms or external workflow framework unnecessary for small explicit state graph |
| T03 | Pydantic v2 | P0; provisional | RFE-003–012, NFR-004 | Dataclasses plus manual checks or jsonschema; Pydantic offers typed models and schema generation; independently validate semantic rules |
| T04 | FastAPI + Uvicorn | P0; provisional | RFE-005,010–012, NFR-001,008 | Flask or Streamlit; FastAPI separates API/controller from presentation; Streamlit can still serve a disposable UX experiment |
| T05 | HTML/CSS and vanilla JavaScript, locally served | P0; provisional | RFE-005,007,010, NFR-008 | HTMX or React if justified; avoid npm build chain initially |
| T06 | sqlite3 (SQLite) | P0; provisional | RFE-012, NFR-005 | JSON files useful for fixtures/exports; transactional state and revision checks favour SQLite; PostgreSQL deferred |
| T07 | LM Studio local inference | P0; reuse subject to inspection | RFE-003,004,015, NFR-006 | Ollama or llama.cpp server as later comparable adapter; do not install another runtime without measured need |
| T08 | HTTPX | P0 local inference; P1 controlled research transport | ORC-006,011, NFR-004 | Existing urllib.request adequate for simple fetch; HTTPX supports timeouts, limits and mock transport. Preserve legacy module |
| T09 | json, hashlib, datetime, uuid, decimal, logging, time | P0; standard library | RFE-008,011,012, NFR-005,007 | No external event bus, log SaaS, crypto SDK or serialisation framework needed at P0 |
| T10 | pytest | P0/P1; reuse test style | M04 F01–F20, NFR-009 | unittest available; pytest already appears in committed registry test module; do not modify/run frozen legacy tests without scope |
| T11 | Git/GitHub and VS Code | P0; retain existing tooling | NFR-004,010 | No additional IDE or hosted development subscription required |
| T12 | Python statistics/math; NumPy, pandas as need arises | P1 | ANA-001–003 | Initial simple statistics can use standard library; use arrays/dataframes only when a real analytical task requires them |
| T13 | SciPy, statsmodels, SymPy, openpyxl | P1/P2; conditional | ANA-001–003, EXT-001 | Add only for approved statistical, forecasting, symbolic or spreadsheet methods; not mandatory for basic GDP demonstration |
| T14 | Matplotlib or Plotly | P1/P2; conditional | OUT-001, ANA-001 | Existing HTML templates or native SVG initially; charts must reflect approved chart-ready datasets |
| T15 | Full-text search (SQLite FTS5), document parsing, embeddings/RAG | P1/P2; conditional | EVD-001–003, SYN-001 | Filter/search structured datasets first; vector database not necessary for P0; benchmark retrieval relevance before adding |
| T16 | Hosted model API, MCP, LangGraph, smolagents or other orchestration SDK | P1/P2; deferred/optional | ORC-011, EXT-001, NFR-010 | Native state machine remains authoritative; no automatic hosted fallback or unreviewed tool exposure |

The proposed minimal direct runtime packages are pydantic, fastapi, uvicorn and httpx. pytest is a development dependency. FastAPI dependencies are transitive; verify full resolved tree rather than claiming five packages total. No external database server, agent framework, vector database, container orchestrator or paid API needed for P0. No package is installed or version locked by this document.

## 4. Model architecture and benchmark

A model is an interchangeable inference component, not Alice's identity, memory, decision authority or sole state machine.

Logical ModelAdapter request: task ID, mission/revision, schema ID, bounded contextual fields, prompt template version, model configuration, deadline and token limit. Result: structured proposal or typed failure, model/runtime identifier, timing, token counts when reported and trace reference. All outputs are validated independently against typed contracts and current mission state. No model may call the execution facade directly.

Adapter candidates:
1. Recorded deterministic responses: mandatory for controller and error-path tests; zero live inference.
2. LM Studio local server: preferred first real inference candidate, loopback binding, authenticated if supported/configured, explicit endpoint and model ID, JSON Schema structured output through supported chat endpoint.
3. Optional second local runtime or hosted provider: later compatibility test for ORC-011. Hosted usage requires separate privacy, billing, credential and external transfer approval; no automatic fallback.

LM Studio documents JSON Schema structured outputs via its OpenAI-compatible chat completions endpoint [S1]. This does not guarantee correct content or universal support across models/quantisations; independently reject malformed, out-of-scope or inconsistent proposals. Verify schema subset and model-specific support. Local mode is an operational policy, not a guarantee of zero telemetry: check runtime configuration, network behaviour and model provenance.

### 4.1 Candidate local models

Start with existing installed instruct models if suitable (inventory unverified). For a controlled comparison, Qwen3-4B and Qwen3-8B are documented Apache-2.0 model candidates [S6–S7]; select exact approved instruct variant, quantisation source, licence and digest before download. Do not treat these as the latest or objectively best models. Compare larger existing models only if smaller ones fail intent or schema targets.

Approximate weights-only lower-bound at 4 bits/parameter: 4B = 2 GB; 8B = 4 GB; 14B = 7 GB; 35B = 17.5 GB (decimal units). Actual quantised formats, auxiliary tensors, context/KV cache, CUDA/runtime buffers and OS usage increase memory. Mixture-of-experts total parameters, not merely active parameters, affect resident weights. CPU offloading can increase latency. Neither fit nor response speed has been measured on this workstation.

Benchmark:
- M04 30 synthetic intents across at least three domain profiles; three repetitions of model-dependent cases.
- Compare installed/small candidates against deterministic template and single-pass baselines.
- Record exact model artifact, quantisation, prompt, context length, output cap, settings, runtime, CPU/GPU utilisation, warm/cold latency, format success, intent fidelity, redundancy and failure rate.
- SRS targets: median <=3 s, p95 <=10 s per refinement interaction, >=90% intent fidelity on labelled cases and no silently contradicted explicit hard constraints in the release suite.
- Choose smallest model meeting reviewed criteria; if none passes, revise prompt/schema or evaluate a stronger approved model, not an uncontrolled escalation.

## 5. P0 operational arrangement

```text
Local browser
  -> FastAPI application (loopback only)
  -> authenticated operator / request validation
  -> deterministic mission controller + versioned SQLite store
  -> question planner / local model adapter (structured proposals)
  -> schema and semantic validation / dependency invalidation
  -> editable review snapshot + explicit version-bound approval
  -> simulated capability catalogue / execution adapter
  -> recorded simulated result and audit events
```

RFE and policy controller remain separate from the model. Server-side validation applies even when the browser hides/disables a button. All P0 research tools are simulated; local inference is distinct from live research. No access to legacy pipelines, source-registry writes, arbitrary shell/code, filesystem outside approved storage, publication, or network research. Deny by default; do not use arbitrary model-produced URLs as tool endpoints. Store only necessary mission events and synthetic test content. No user credentials, tokens or personal data in repository, fixture or logs.

SQLite design candidate: mission, revision, event, review_snapshot, approval, capability_decision and run tables; foreign keys and explicit transactions; optimistic revision guard, idempotency event key and immutable approved snapshots. A digest identifies content but does not grant authority. Stable canonical serialisation must be specified, validated and frozen under G1; do not invent an implicit encoding. SQLite files are local runtime state, not Thoth production registry or Git-tracked evidence. Define retention, backups and permissions before operational data.

Loopback is not complete authentication. Bind approved hosts, use operator session/identity, origin and CSRF safeguards as appropriate, validate payloads, enforce sizes, cancel/timeout safely, and reject stale or forged approvals. No LAN/public exposure by default.

## 6. ALIS Core technology responsibilities

| Engine | Retain/reuse | Proposed additions, only after relevant gate |
| --- | --- | --- |
| Arya | Source admission rule and source plans | Versioned source proposal and retrieval manifest schemas; approved endpoint catalogue |
| Hermes | urllib World Bank connector primitives | HTTPX controlled transport; timeout, retry, rate limit, pagination, byte limits, immutable raw evidence |
| Thoth | Frozen source registry helper | Reviewed metadata storage, canonical IDs, checksums, lineage, reference verification; no silent promotion |
| Aegis | Validator rules and governing policy | Explicit policy/gate schemas and deterministic checks; separately repair F01–F03 |
| Abacus | Existing classification/taxonomy and workbench calculation candidates | Versioned method registry, standard-library calculations, approved quantitative libraries as justified |
| Vyasa | Controlled summary templates | Claim-to-evidence map; optionally constrained synthesis adapter consuming approved inputs |
| Apollo | Static HTML reports/templates | Deterministic rendering and manifests; optional chart library; release remains separately authorised |
| Argus | Existing timestamped logs | Structured event contracts, run/mission correlation, redaction, failure metrics and incident records |

These are logical ownership assignments, not permission to move files or replace existing implementations. Existing canonical artifact owners and gate sequence remain unchanged. No new ninth ALIS engine.

## 7. Research API catalogue (candidate, not admitted)

Only one approved read-only connector is needed for P1. Prefer a reviewed World Bank Indicators fixture/connector mission, separate from the Documents & Reports metadata endpoint. Existing GoDataBank source admission rules apply to every product output. An official API or a discovery index is not proof of admission, claim support, current endpoint availability or redistribution rights.

| Candidate | Domain / purpose | Phase and disposition | Access and policy check |
| --- | --- | --- | --- |
| World Bank Documents & Reports API | Publication metadata | Legacy path; preserve; do not expose directly to Alice | Existing source record scoped to that endpoint; fix F01–F03 before integration |
| World Bank Indicators API v2 | Economic/social indicator series | Preferred P1 candidate; fixture first | Public documented API [S8]; independently review specific dataset, access terms, metadata, definitions and provenance |
| ONS developer API | UK official economic, population and social statistics | Alternative P1 or P2 | Official catalogue [S9]; verify current endpoints, editions, versions, licences and dataset availability |
| NCBI E-utilities / PubMed | Biomedical literature discovery | P2 scientific profile | Documented service [S10]; rate limits, metadata vs full-text permissions, underlying source review |
| Crossref REST API | DOI and scholarly metadata discovery | P2 scientific profile | Documented metadata API [S11]; Crossref metadata is discovery, not proof of results or permission to access article full text |
| UK official public datasets, regulators and government feeds | Policy, market and engineering context | P2 candidates to scope individually | Endpoint, terms, issuer and exact data availability unverified here; no connector selection yet |
| Primary survey collection | User-authorised research data | P2; separate design | Consent, recruitment, sampling, retention, privacy and ethics; no third-party survey service selected |
| Commercial, news, web search, scholarly aggregators and other non-GoDataBank sources | Broader research discovery | Deferred, not admitted | New research-only policy and isolated artifacts required before use; existing GoDataBank exclusions remain |

For each future connector require owner/source identity, endpoint and parameters, allowed HTTP methods/hosts, authentication reference, documented quotas, access terms/licence, source admission decision, version/edition, schema, pagination and rate-limit behaviour, checksum and citation metadata, failure handling, cost and test fixtures. Source discovery is distinct from approval and evidence retrieval. Do not interpret model training knowledge as a source. No current API rate, price or data licence is assumed without checking the relevant endpoint and date.

## 8. Analytical capability catalogue

Abacus methods must declare purpose, input schema, units, missing-data handling, formula/method version, preconditions, uncertainty and output schema. Alice proposes methods; Abacus owns canonical analytical execution plans and packages. No model arithmetic is canonical.

| Capability | Proposed tool | Stage |
| --- | --- | --- |
| Counts, extrema, mean, median, ratios, percentage change | Python math/statistics/decimal, reviewed pure functions | P1 |
| Data filtering, joins and time-series alignment | Python, pandas/NumPy when required | P1 |
| Distributions, confidence intervals, tests | SciPy stats [S12] | Conditional P1/P2 |
| Regression and time-series modelling | statsmodels [S13] | P2 after backtesting, assumptions and validation |
| Symbolic engineering calculations | SymPy | Conditional P2; unit validation separate |
| XLSX ingest | openpyxl or existing reviewed reader | Conditional P1/P2 |
| Charts and reporting | Reviewed template, Matplotlib/Plotly if needed | Conditional P1/P2; approved datasets only |
| Research discovery and idea assessment | Structured model proposals plus cited evidence and explicit validation steps | P1/P2; no unsupported factual or commercial success claims |

Scientific inference, causal analysis, forecasts and surveys require approved methods and independent tests. Do not infer causal effects from correlation; preserve series definitions, nominal/real distinctions, sampling limitations and uncertainty.

## 9. Cost, privacy, licences and maintenance

P0 incremental procurement target: GBP 0 for hardware, hosted inference and paid research API charges; electricity, time and existing licences are not zero. No paid requests or new subscriptions authorised. Software packages proposed are generally permissively licensed: Pydantic and FastAPI MIT, Uvicorn and HTTPX BSD-style, pytest MIT, SQLite public domain [S14–S19]. Confirm licence of exact version, all dependencies, bundled assets, model weights and applicable LM Studio terms before installation/distribution; this is not a legal clearance or a complete SBOM.

Local electricity cost = measured average power in kW * operating hours * tariff GBP/kWh. Measure wall power if useful rather than treating GPU TDP as whole-system consumption.

If hosted models are later approved: estimated usage cost = input tokens/1e6 * input tariff + output tokens/1e6 * output tariff + any tool/storage/network fees. Track currency, tax and pricing date. OpenAI documents structured outputs and usage pricing [S20–S21]; no specific hosted model or price assumed. Existing chat subscription does not establish API credits. No external API key is needed for P0. Use explicit budgets, no unlimited automatic retries and no default cross-provider transfer. Set policy to deny if total call cost cannot be bounded.

Freeze compatible Python/runtime/model versions after actual tests. Record dependency lock, hashes where practical, direct/transitive licences, vulnerability review, update cadence, rollback procedure and model provenance. Use synthetic fixtures and no secrets in GitHub. Dependency changes require regression tests and review. Separate local storage from public repository content. Avoid proprietary or hosted lock-in by using model, state and transport interfaces.

## 10. M07 readiness and proposed work packages

Before code: review M01–M06 stacked PRs; reconcile local and remote baseline (M05 G0); determine isolated prototype physical location; resolve G1 executable schema, field attribution, canonical serialisation, approval and blocked-preview semantics, policy authority and test scope. Existing freeze continues. The P0 simulated research adapter does not bypass ALIS Core or modify legacy source.

Proposed M07 work packages, subject to explicit implementation authorisation:
- WP1: executable contracts, typed field registry and validation tests.
- WP2: deterministic state reducer, revision guards, question dependency invalidation and capability resolver.
- WP3: transactional local mission storage and audit.
- WP4: recorded model adapter then approved LM Studio adapter with structured output and bounded retry.
- WP5: local browser interface, adaptive questions, editable review and authorisation.
- WP6: simulated research execution and visible terminal states.
- WP7: execute applicable M04 F01–F20 under approved test scope and benchmark SRS targets; record limitations.
- WP8: review and freeze P0 before separately approved P1 legacy remediation and one research connector.

P0 acceptance: no live research access; deterministic negative tests pass; no stale authorisation; traceable state revisions; appropriate adaptive questions; benchmark results reported honestly. Do not mark P0 accepted merely because a model returns JSON. No hardware purchase or hosted model requirement justified.

## 11. Primary technical references

Documentation checked 27 November 2026; links describe capabilities, not observed performance or guaranteed deployment compatibility. Verify exact versions and terms again before use.

- S1: [LM Studio structured output](https://lmstudio.ai/docs/developer/openai-compat/structured-output); [local server](https://lmstudio.ai/docs/developer/core/server).
- S2: [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/).
- S3: [FastAPI features](https://fastapi.tiangolo.com/features/).
- S4: [HTTPX documentation](https://www.python-httpx.org/).
- S5: [Python SQLite interface](https://docs.python.org/3.12/library/sqlite3.html); [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html).
- S6: [Qwen3-4B model card](https://huggingface.co/Qwen/Qwen3-4B).
- S7: [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B).
- S8: [World Bank Indicators API documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation); [basic call structures](https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures).
- S9: [ONS Developer Hub](https://developer.ons.gov.uk/).
- S10: [NCBI E-utilities introduction](https://www.ncbi.nlm.nih.gov/books/NBK25497/?report=printable).
- S11: [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).
- S12: [SciPy statistical methods](https://docs.scipy.org/doc/scipy/reference/stats.html).
- S13: [statsmodels API reference](https://www.statsmodels.org/stable/api).
- S14: [Pydantic licence](https://github.com/pydantic/pydantic/blob/main/LICENSE).
- S15: [FastAPI licence](https://github.com/fastapi/fastapi/blob/master/LICENSE).
- S16: [HTTPX licence](https://github.com/encode/httpx/blob/master/LICENSE.md).
- S17: [Uvicorn licence](https://github.com/Kludex/uvicorn/blob/main/LICENSE.md).
- S18: [pytest licence](https://github.com/pytest-dev/pytest/blob/main/LICENSE).
- S19: [SQLite copyright](https://www.sqlite.org/copyright.html).
- S20: [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs).
- S21: [OpenAI API pricing](https://developers.openai.com/api/docs/pricing).

## 12. Decision and limitations

Proposed local-first stack: Python, native deterministic state machine, Pydantic, FastAPI/Uvicorn, browser HTML/CSS/JS, SQLite, HTTPX, LM Studio and pytest. All choices subject to feasibility, licence and security checks. The exact model, dependencies, deployment, benchmark outcomes and live connectors remain unverified. No exhaustive vendor comparison, runtime benchmark, code changes, schema generation, test execution, purchase, model download, API key creation or merge occurred. This milestone does not resolve the M05 legacy defects or supersede governance.

M06 prepares M07; it does not authorise implementation. Any change must reference affected requirement IDs, document trade-offs and receive scoped approval.
