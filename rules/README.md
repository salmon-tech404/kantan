# Rules

All Kantanda rules live here, grouped by area. **107 rules**: 39 T1, 43 T2, 25 T3. This index is generated from the rule files; if it disagrees with a rule file, the rule file wins.

Agents: do not read this tree. Use the task table in the root [`AGENTS.md`](../AGENTS.md) to pick one file.

## Summary

| Area | Folder | Rules | T1 | T2 | T3 | T1 with a check in `tooling/` |
|---|---|---:|---:|---:|---:|---:|
| Common | `common/` | 17 | 5 | 4 | 8 | 1 / 5 |
| Frontend | `frontend/` | 31 | 12 | 15 | 4 | 4 / 12 |
| Backend | `backend/` | 28 | 16 | 11 | 1 | 11 / 16 |
| Architecture | `architecture/` | 13 | 3 | 3 | 7 | 3 / 3 |
| Guide | `guide/` | 7 | 2 | 3 | 2 | 0 / 2 |
| Optional modules | `backend/` (rag, ml) | 11 | 1 | 7 | 3 | 0 / 1 |
| **Total** | | **107** | **39** | **43** | **25** | **19 / 39** |

> **T1 means a tool can catch the rule.** The last column counts T1 rules whose ID appears in `tooling/eslint.config.mjs` or `tooling/semgrep.yml`. The other T1 rules may be enforced by tools outside Kantanda (CI, commit lint, `npm audit`) or not enforced yet; that has not been classified.

## Not rules, but also here

| File | What |
|---|---|
| `architecture/styles.md` | Architecture styles and which rule applies to which style (`applies_to`) |
| `architecture/frameworks.md` | 5 decision frameworks: pick one option among several, with conditions |
| `architecture/conflicts.md` | 5 resolved conflicts between two correct principles |
| `common/incidents.md` | Real incidents, each linked to the rule that would have prevented it |
| `*/guidance.md` | Recommendations (T3). Read when weighing trade-offs; never a reason to block a change |

## Index

<details>
<summary><b>Common</b> · 17 rules</summary>

Naming, function size, git and CI gates, testing strategy, code review, incident log.

| ID | Rule | Tier | File | Check |
|---|---|:---:|---|---|
| `SWE-STY-001` | Automated Formatting and Style Guides as Common Law | T1 | [common/code-style.md](common/code-style.md) | — |
| `CODE-FUN-002` | Small Function Size and Guard Clause Early Returns | T1 | [common/code-style.md](common/code-style.md) | ESLint |
| `CODE-DEM-001` | Law of Demeter (Principle of Least Knowledge) | T2 | [common/code-style.md](common/code-style.md) | — |
| `GIT-CMT-001` | Conventional Commits v1.0.0 Specification | T1 | [common/git.md](common/git.md) | — |
| `CD-GAT-001` | Automated Pre-Commit and CI Quality Gates | T1 | [common/git.md](common/git.md) | — |
| `SWE-DEP-001` | Deterministic Dependency Pinning and Vulnerability Auditing | T1 | [common/git.md](common/git.md) | — |
| `CODE-FUN-001` | Single Responsibility Principle (SRP) for Functions | T3 | [common/guidance.md](common/guidance.md) | — |
| `CODE-NAM-001` | Intent-Revealing, Searchable Identifiers | T3 | [common/guidance.md](common/guidance.md) | — |
| `CODE-DOC-001` | Comments Must Explain 'Why', Never 'What' | T3 | [common/guidance.md](common/guidance.md) | — |
| `TEST-TRUTH-001` | Truth-in-Testing: Prohibition of False Concurrency Claims on In-Memory Fakes | T3 | [common/guidance.md](common/guidance.md) | — |
| `TEST-BLD-001` | Object Mother for Reusable Test Fixture Construction | T3 | [common/guidance.md](common/guidance.md) | — |
| `TEST-HUM-001` | Humble Object Pattern for Splitting Untestable Code | T3 | [common/guidance.md](common/guidance.md) | — |
| `CODE-TDD-001` | Three Laws of TDD (Red-Green-Refactor Sequencing) | T3 | [common/guidance.md](common/guidance.md) | — |
| `SWE-TST-001` | Hermetic Test Isolation and Explicit Test Sizing | T2 | [common/testing.md](common/testing.md) | — |
| `TEST-RACE-001` | Mandatory Concurrent Execution Testing for Concurrency and Locking Claims | T2 | [common/testing.md](common/testing.md) | — |
| `TEST-IDEM-001` | Mandatory Behavioral Idempotency Deduplication Testing | T2 | [common/testing.md](common/testing.md) | — |
| `SWE-REV-001` | Five-Point Code Review Verification Checklist | T3 | [common/workflows.md](common/workflows.md) | — |

</details>

<details>
<summary><b>Frontend</b> · 31 rules</summary>

UI and accessibility, TypeScript, structure and state, rendering untrusted content, end-to-end tests.

| ID | Rule | Tier | File | Check |
|---|---|:---:|---|---|
| `FE-ARCH-001` | Server-First Components in Next.js App Router | T2 | [frontend/architecture.md](frontend/architecture.md) | — |
| `FE-ARCH-002` | Colocation of Feature Components and Hooks | T2 | [frontend/architecture.md](frontend/architecture.md) | — |
| `FE-API-001` | Decoupled API Client Service Layer (No Fetch/Axios in JSX) | T1 | [frontend/architecture.md](frontend/architecture.md) | ESLint + Semgrep |
| `FE-STA-002` | URL-as-State for Search Queries, Filters, and Pagination | T2 | [frontend/architecture.md](frontend/architecture.md) | — |
| `FE-STA-001` | Strict State Separation (Server vs Global UI vs Form State) | T3 | [frontend/guidance.md](frontend/guidance.md) | — |
| `UI-LAW-001` | Jakob's Law: Conform to Familiar User Interface Mental Models | T3 | [frontend/guidance.md](frontend/guidance.md) | — |
| `UI-LAW-003` | Hick's Law: Minimize Options to Reduce Decision Latency | T3 | [frontend/guidance.md](frontend/guidance.md) | — |
| `UI-LAW-004` | Miller's Law: Chunk Complex Information into 5 to 9 Discrete Units | T3 | [frontend/guidance.md](frontend/guidance.md) | — |
| `SEC-AI-002` | Output Sanitization of LLM Generated Content | T1 | [frontend/security.md](frontend/security.md) | Semgrep |
| `TEST-E2E-001` | Page Object Model (POM) for E2E Test Isolation | T2 | [frontend/testing.md](frontend/testing.md) | — |
| `TEST-E2E-003` | Visual Regression Testing for Critical Layouts | T2 | [frontend/testing.md](frontend/testing.md) | — |
| `TEST-E2E-004` | Reuse Authenticated Session State via storageState | T2 | [frontend/testing.md](frontend/testing.md) | — |
| `TEST-E2E-005` | Automated Accessibility Scanning with axe-core | T1 | [frontend/testing.md](frontend/testing.md) | — |
| `FE-TS-001` | Strict Zero-Any Policy in TypeScript | T1 | [frontend/typescript.md](frontend/typescript.md) | ESLint |
| `FE-TS-002` | Discriminated Unions for Representing State | T2 | [frontend/typescript.md](frontend/typescript.md) | — |
| `UI-STA-001` | Mandatory Five-State Component Anatomy | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-A11Y-001` | Semantic HTML and ARIA Labeling on Interactive Elements | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-LAW-002` | Fitts's Law: Minimum Target Size of 44x44px for Interactive Elements | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-DLG-001` | Focus Trapping and ESC Key Dismissal in Modal Dialogs | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-DLG-002` | Explicit Two-Step Confirmation for Destructive Actions | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-GEN-001` | Strict Prohibition of Emojis in Production Interface Elements | T1 | [frontend/ui.md](frontend/ui.md) | ESLint |
| `UI-PER-001` | Perceived Performance via Skeleton Loaders (Doherty Threshold) | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-SEL-001` | One Non-Color Cue for Selected State — No Stacked Signals | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `UI-STB-001` | Interactions Must Not Shift Unrelated Layout | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `DS-BTN-001` | Button Loading State and Disabled Accessibility | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `DS-BTN-003` | Single Primary Button Per Visual Area | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `DS-INP-001` | Explicit Label and Accessible Error Association | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `DS-INP-002` | Persistent Focus Rings | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `DS-TST-001` | Accessible Toast Notifications with Polite Live Regions | T1 | [frontend/ui.md](frontend/ui.md) | — |
| `FE-FRM-001` | React Hook Form Combined with Zod Schema Resolver | T2 | [frontend/ui.md](frontend/ui.md) | — |
| `FE-ACT-001` | Server Actions Mutation Lifecycle with useActionState and useOptimistic | T2 | [frontend/ui.md](frontend/ui.md) | — |

</details>

<details>
<summary><b>Backend</b> · 28 rules</summary>

HTTP API and errors, input validation, database access control, authentication and security, backend tests.

| ID | Rule | Tier | File | Check |
|---|---|:---:|---|---|
| `BE-ERR-001` | Centralized AppError Exception Hierarchy | T1 | [backend/api.md](backend/api.md) | ESLint |
| `BE-ERR-002` | Never Expose Internal Stack Traces in Production | T1 | [backend/api.md](backend/api.md) | ESLint + Semgrep |
| `BE-API-001` | RESTful Plural Nouns and Kebab-Case Endpoints | T1 | [backend/api.md](backend/api.md) | — |
| `BE-API-002` | Uniform API Response Envelope | T2 | [backend/api.md](backend/api.md) | — |
| `BE-VAL-001` | Boundary Request Validation via Zod Schemas | T1 | [backend/api.md](backend/api.md) | — |
| `BE-VAL-002` | Strict Rejection of Unknown Request Fields | T1 | [backend/api.md](backend/api.md) | ESLint |
| `BE-IDEM-001` | Active Idempotency Deduplication Execution | T2 | [backend/api.md](backend/api.md) | — |
| `BE-DB-001` | Mandatory Tenant and User Scoping on Database Queries | T1 | [backend/database.md](backend/database.md) | Semgrep |
| `SEC-BOLA-002` | Defense-in-Depth Anti-BOLA: Opaque IDs, 403/404 Strategy, and Automated Testing | T2 | [backend/database.md](backend/database.md) | — |
| `BE-DB-002` | Atomic Transactions for Multi-Table Writes | T2 | [backend/database.md](backend/database.md) | Semgrep |
| `TEST-DBL-001` | Strict Test Double Taxonomy: Prefer Fakes and Stubs Over Interaction Mocks | T3 | [backend/guidance.md](backend/guidance.md) | — |
| `SEC-AUTH-001` | Dual-Token Architecture (15m Memory Access + 7d HttpOnly Cookie Refresh) | T2 | [backend/security.md](backend/security.md) | — |
| `SEC-AUTH-002` | Two-Factor Authentication (2FA) for Sensitive Administrative Operations | T2 | [backend/security.md](backend/security.md) | — |
| `SEC-AUTH-003` | Mandatory Role and Permission Enforcement at Route Boundaries (Anti-BFLA) | T1 | [backend/security.md](backend/security.md) | Semgrep |
| `SEC-JWT-001` | Strict Verification of JWT Issuer, Audience, Expiry, and Algorithm | T1 | [backend/security.md](backend/security.md) | Semgrep |
| `SEC-UPL-001` | Magic Bytes File Signature Verification on Uploads | T1 | [backend/security.md](backend/security.md) | Semgrep |
| `SEC-UPL-002` | Strict File Size Limits and Memory Quotas | T1 | [backend/security.md](backend/security.md) | — |
| `SEC-SSRF-001` | Allowlist-First URL Validation with Denylist Defense-in-Depth (Anti-SSRF) | T1 | [backend/security.md](backend/security.md) | Semgrep |
| `SEC-RAT-001` | Strict Rate Limiting on Authentication and AI Generation Endpoints | T1 | [backend/security.md](backend/security.md) | — |
| `SEC-LOG-001` | Automated PII and Credential Masking in Structured Logs | T1 | [backend/security.md](backend/security.md) | Semgrep |
| `SEC-AI-001` | Isolation and Demarcation Against Prompt Injections | T2 | [backend/security.md](backend/security.md) | — |
| `SEC-AI-003` | Least-Privilege Execution and Confirmation for Tool-Calling Agents | T2 | [backend/security.md](backend/security.md) | — |
| `SEC-AI-004` | Sandboxed Execution for LLM-Generated Code | T2 | [backend/security.md](backend/security.md) | — |
| `TEST-INT-001` | Integration Tests with Real Database State Rollback | T1 | [backend/testing.md](backend/testing.md) | — |
| `TEST-MCK-001` | Restrict Mocking to Out-of-Process Unmanaged Dependencies | T1 | [backend/testing.md](backend/testing.md) | ESLint |
| `TEST-MCK-002` | Verify State and Output, Never Interaction Counts on Internals | T2 | [backend/testing.md](backend/testing.md) | ESLint |
| `TEST-AAA-001` | Standardized Arrange-Act-Assert (AAA) Test Structure | T2 | [backend/testing.md](backend/testing.md) | — |
| `TEST-ANT-001` | Unit Testing Anti-Patterns: Never Test Private Methods or Mock Concrete Classes | T1 | [backend/testing.md](backend/testing.md) | ESLint |

</details>

<details>
<summary><b>Architecture</b> · 13 rules</summary>

Architecture styles, module boundaries, ADRs, decision frameworks, resolved conflicts.

| ID | Rule | Tier | File | Check |
|---|---|:---:|---|---|
| `ARCH-ADR-001` | Mandatory Architectural Decision Records (ADR) for Structural Decisions | T2 | [architecture/adr.md](architecture/adr.md) | — |
| `ARCH-DDD-002` | Anti-Corruption Layer (ACL) for External Services | T1 | [architecture/boundaries.md](architecture/boundaries.md) | ESLint |
| `ARCH-DDD-005` | Ports & Adapters (Hexagonal) Architecture for Domain-Model Business Logic | T1 | [architecture/boundaries.md](architecture/boundaries.md) | ESLint |
| `ARCH-LAY-001` | Layer Isolation: Requests Flow Through the Defined Layers | T2 | [architecture/boundaries.md](architecture/boundaries.md) | — |
| `ARCH-MOD-002` | Low Coupling and Explicit Module Contracts | T1 | [architecture/boundaries.md](architecture/boundaries.md) | ESLint |
| `ARCH-MONO-001` | Modular Monolith Domain-Driven Partitioning | T2 | [architecture/boundaries.md](architecture/boundaries.md) | — |
| `ARCH-DDD-001` | Explicit Definition of Bounded Contexts | T3 | [architecture/guidance.md](architecture/guidance.md) | — |
| `ARCH-DDD-003` | Aggregate Root Invariant Encapsulation and Transactional Boundary | T3 | [architecture/guidance.md](architecture/guidance.md) | — |
| `ARCH-DDD-004` | Domain Events and Transactional Outbox for Asynchronous Decoupling | T3 | [architecture/guidance.md](architecture/guidance.md) | — |
| `ARCH-SINK-001` | Avoid Architecture Sinkhole Anti-Pattern | T3 | [architecture/guidance.md](architecture/guidance.md) | — |
| `ARCH-MOD-001` | High Cohesion within Domain Modules | T3 | [architecture/guidance.md](architecture/guidance.md) | — |
| `ARCH-MOD-003` | Eliminate Connascence of Execution Order | T3 | [architecture/guidance.md](architecture/guidance.md) | — |
| `ARCH-DDD-006` | EventStorming for Cross-Team Domain Discovery | T3 | [architecture/workflows.md](architecture/workflows.md) | — |

</details>

<details>
<summary><b>Guide</b> · 7 rules</summary>

How to write READMEs, technical guides and user documentation.

| ID | Rule | Tier | File | Check |
|---|---|:---:|---|---|
| `DOC-AUD-001` | Each document declares its audience on the first line. | T3 | [guide/writing.md](guide/writing.md) | — |
| `DOC-SRC-001` | Technical documentation must derive from real code, not memory. | T2 | [guide/writing.md](guide/writing.md) | — |
| `DOC-VER-001` | Documentation lives next to what it describes. | T2 | [guide/writing.md](guide/writing.md) | — |
| `DOC-TIME-001` | Never write time-relative information. | T1 | [guide/writing.md](guide/writing.md) | — |
| `DOC-OLD-001` | Deprecated content moves to "Legacy Approach," not deletion. | T3 | [guide/writing.md](guide/writing.md) | — |
| `DOC-TERM-001` | One concept, one name, throughout the document. | T2 | [guide/writing.md](guide/writing.md) | — |
| `DOC-LEN-001` | Documents longer than 100 lines must have a table of contents at the start. | T1 | [guide/writing.md](guide/writing.md) | — |

</details>

<details>
<summary><b>Optional modules</b> · 11 rules</summary>

Read only when the project profile enables them: `rag-pgvector` (RAG, embeddings, vector search) and `python-ml` (loading ML models).

| ID | Rule | Tier | File | Check |
|---|---|:---:|---|---|
| `SEC-AI-005` | Safe Model File Deserialization (No Pickle for AI Model Loading) | T3 | [backend/ml.md](backend/ml.md) | — |
| `SEC-AI-006` | Feature/Label Poisoning Resistance for In-House ML Classifiers | T3 | [backend/ml.md](backend/ml.md) | — |
| `RAG-CHK-001` | Deterministic Word Window Chunking with Overlap | T2 | [backend/rag.md](backend/rag.md) | — |
| `RAG-ING-002` | Streaming / Bounded-Buffer Parsing for Large Document Ingestion | T2 | [backend/rag.md](backend/rag.md) | — |
| `RAG-CIT-001` | Verifiable Source Grounding and Citation Metadata | T1 | [backend/rag.md](backend/rag.md) | — |
| `RAG-PRM-001` | Strict Contextual Framing and Anti-Hallucination Prompting | T3 | [backend/rag.md](backend/rag.md) | — |
| `RAG-ASY-001` | Asynchronous Background Processing for Multi-Page Document Ingestion | T2 | [backend/rag.md](backend/rag.md) | — |
| `RAG-EVL-001` | Automated Groundedness and Faithfulness Evaluation | T2 | [backend/rag.md](backend/rag.md) | — |
| `RAG-VEC-001` | Normalized High-Dimensional Cosine Similarity Search | T2 | [backend/rag.md](backend/rag.md) | — |
| `RAG-VEC-002` | Tuned HNSW Index Parameters for pgvector | T2 | [backend/rag.md](backend/rag.md) | — |
| `RAG-VEC-003` | Embedding Model Version Pinning and Re-Index-on-Change | T2 | [backend/rag.md](backend/rag.md) | — |

</details>

## Rule format

Each rule is one block: `ID · modality · tier`, a one-line title, the requirement, **How to**, a wrong example (✗), a right example (✓) and **Why**. Architecture rules also carry `applies_to`.

Modality words: `must`, `must_not`, `should`, `should_not`. Tiers are explained in the root [README](../README.md#core-ideas).
