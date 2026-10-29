---
area: architecture
path: rules/architecture/frameworks.md
---

Decision frameworks. Use when you must **choose among multiple valid options**.

No option is default. Read the conditions, choose, document the choice in an ADR if it's a structural decision.

## Database Concurrency and Locking Strategy · `FW-CON-001`

**When:** Choosing between Optimistic Locking, Pessimistic Locking, and In-Memory Sequencing under concurrent writes, while avoiding the Single-Node Distributed Systems Fallacy.

**If:** Low-to-medium contention mutations where conflicts are rare (e.g. editing document title, updating user profile)
**→ Use:** Optimistic Concurrency Control (OCC) with version number
**Trade-off:** Zero lock overhead on reads, high throughput; client must handle retry on OCC conflict.
✗ Do not use SELECT ... FOR UPDATE on low-contention read-heavy endpoints.

**If:** High-contention critical balance/inventory deductions where conflict probability is high (e.g. debiting user credits, reserving ticket)
**→ Use:** Pessimistic Row-Level Locking (SELECT ... FOR UPDATE) inside short database transaction
**Trade-off:** Guarantees sequential correctness without retry storms; locks database rows, latency spikes if transaction is slow.
✗ Never hold external network I/O calls (e.g. Stripe, LLM APIs) while holding a pessimistic row lock.

**If:** Multi-pod backend web services deployed behind a Load Balancer (Single-Node Fallacy)
**→ Use:** Database-Level Locking (SELECT FOR UPDATE / Serializable) or Distributed Lock (Redis Redlock)
**Trade-off:** Guarantees cross-instance consistency across all Kubernetes pods; slight network latency to DB / Redis.
✗ CRITICAL ANTI-PATTERN: Never use an in-memory Node.js Promise Mutex or local Map as a concurrency control mechanism for production multi-instance services. Pod A cannot see Pod B's RAM mutex — this assumption breaks under the book's 11 Fallacies of Distributed Computing (e.g. "the network is reliable," "latency is zero") once state must be shared across independently-deployed pods.

**If:** Ultra-high-frequency real-time event streaming and message matching (High-throughput streaming engines, 10,000+ events/sec)
**→ Use:** Single-Threaded Event Loop with In-Memory Ring Buffer and Async DB Flush
**Trade-off:** Zero database lock contention, sub-millisecond execution; state must be reconstructed from WAL / Domain Events upon crash. Supported by Ch.16 (Space-Based Architecture, data-pump pattern).
✗ Never route high-frequency event-by-event updates through relational database row transactions.

## Bounded Context Boundary & Mapping Strategy · `FW-ARCH-001`

**When:** Determining how two distinct business domains should interact and whether to share code, models, or isolate with adapters.

**If:** Both subsystems evolve together under the same team with identical business lifecycles
**→ Use:** Shared Kernel
**Trade-off:** Avoids mapper boilerplate; changes in the shared kernel require synchronized releases between subsystems.
✗ Shared Kernel across different teams or disparate deployment cadences is acceptable ONLY when Partnership-level coordination (synchronized releases, shared CI) has been ruled out (Ch.4, Integrating Bounded Contexts). Do not default to it; prefer Partnership first.

**If:** One subsystem depends on a foreign third-party API or legacy system with unstable/messy schemas
**→ Use:** Anti-Corruption Layer (ACL)
**Trade-off:** Insulates internal domain models completely from external churn; requires maintenance of a one-directional, consumer-owned DTO mapper (a cheap stateless translation proxy, or a costlier stateful aggregating layer when the upstream model diverges significantly).
✗ Do not expose foreign schema properties inside internal domain services.

**If:** Subsystems belong to different business subdomains (e.g. Ingestion/RAG vs User Billing)
**→ Use:** Autonomous Bounded Contexts with Duplicate DTOs (Separate Ways)
**Trade-off:** Guarantees 100% independent deployability and zero hidden coupling; violates strict DRY across domain boundaries. The book warns Separate Ways should be avoided when integrating core subdomains — verify neither subsystem is a core subdomain before choosing this.
✗ Do not attempt to unify User and Customer into a single monolithic entity class.

## Idempotency and Message Deduplication Strategy · `FW-IDEM-001`

**When:** Choosing the appropriate idempotency deduplication architecture across short-lived caching, transactional relational storage, and distributed event streams. NOTE: only the general HTTP-method safety/idempotence concept traces to its claimed source, "Design and Build Great Web APIs" (BOOK-API-WEB), Chapter 2, "Safe and Idempotent" — which defines idempotency as an intrinsic property of the HTTP method (PUT/GET/DELETE are idempotent, POST is not) and illustrates it with "use PUT instead of POST for a bank transfer." The book never mentions an Idempotency-Key header, Redis, distributed locks, TTL caching, database unique constraints, message queues, or the Transactional Outbox/Idempotent Consumer patterns.

**If:** Stateless HTTP APIs with short mutation windows (e.g. payment checkout, external webhook ingesters)
**→ Use:** Redis Distributed Lock + TTL Caching (24-48 hours) with Request Body Hash Comparison
**Trade-off:** Sub-millisecond deduplication checks, automatic memory reclamation; in rare Redis crash scenarios, key may be lost unless Redis AOF persistence is enabled.
✗ Never store idempotency keys in local in-memory Node.js Maps in production; keys must be shared across all pods via Redis.

**If:** Mission-critical financial ledger, core banking transfers, and billing record creation
**→ Use:** Database Unique Constraint on idempotency_key inside Transaction Table + In-Transaction Double Check
**Trade-off:** Guarantees ACID atomicity with zero chance of lost keys; slight database query overhead on initial check.
✗ Never treat idempotencyKey as a decorative DTO field without querying the database for existing records before execution.

**If:** Asynchronous Event-Driven Microservices and Message Queues (Kafka / RabbitMQ)
**→ Use:** Idempotent Consumer Pattern with Transactional Outbox and Message Deduplication Table
**Trade-off:** At-least-once delivery safely converted into exactly-once processing semantics; requires maintenance of message log cleanup jobs.
✗ Never rely on messaging brokers alone to guarantee exactly-once delivery without consumer-side deduplication.

## Frontend State Architecture Selection Matrix · `FW-STA-001`

**When:** Selecting the appropriate state storage tier when introducing new stateful logic in React / Next.js applications.

**If:** State alters the primary visual dataset, requires bookmarking, browser back/forward, or link sharing (e.g. search keywords, active filters, pagination page, tab selection)
**→ Use:** URL Search Parameters (useSearchParams + useRouter)
**Trade-off:** State survives page refresh and is 100% shareable; serialized as string, requires debounce on high-frequency text input.
✗ Never store page numbers or active tab IDs purely in React useState.

**If:** State represents asynchronous data fetched from server APIs that needs caching, deduplication, background polling, or optimistic updates
**→ Use:** Server State (TanStack Query or React Server Components)
**Trade-off:** Automates garbage collection and revalidation; asynchronous, requires explicit 5-state UI handling.
✗ Never duplicate server lists or entities into global Zustand stores.

**If:** State represents purely ephemeral user input being validated before submission
**→ Use:** Form State (React Hook Form with Zod Resolver)
**Trade-off:** Zero re-renders on keystroke, isolated component state; local to form lifecycle.
✗ Do not lift form input field values into global app state.

**If:** State represents global client-only UI flags (e.g. sidebar collapse, active theme, global command palette open/close)
**→ Use:** Global Client Store (Zustand)
**Trade-off:** Instant synchronous access across any client component with zero boilerplate; lost on hard refresh unless explicitly synced with localStorage.
✗ Do not use Zustand for tabular server data.

## Multi-Tier Testing Strategy Framework · `FW-TST-001`

**When:** Determining the testing depth, isolation boundary, and test double approach for a specific software component.

**If:** Pure algorithmic calculations, data transformations, chunking logic, and business rules without external I/O
**→ Use:** Isolated Unit Tests (AAA Pattern) with Zero Doubles
**Trade-off:** Executes in microseconds, 100% deterministic, indestructible; does not verify database connectivity.
✗ Never introduce Mocks or Stubs when testing pure functions.

**If:** Service layer touching the database (a managed dependency)
**→ Use:** Do NOT fake the repository. Extract pure business logic into a Functional-Core (unit-tested, no DB) and push DB access into a thin Imperative-Shell layer tested only via real-DB integration tests (Ch.8.4.2, Ch.10.3.3).
**Trade-off:** Unit tests on the functional core remain sub-millisecond fast with zero doubles; the thin DB shell is verified against real PostgreSQL, avoiding false confidence from unfaithful fakes; requires disciplined separation of pure logic from DB access code.
✗ Hand-rolled in-memory fake repositories reimplementing query semantics (e.g. pgvector's <=> operator) cannot be faithfully emulated — CONF-004 itself admits this. Never mock database client methods like prisma.user.findFirst directly, and never substitute a hand-rolled fake for the real database engine on a managed dependency.

**If:** Critical end-to-end user journeys (authentication login, document upload and vector search)
**→ Use:** Playwright E2E Tests with Page Object Model (POM)
**Trade-off:** Validates full browser stack, CSS layout, and network integration; slower execution, requires test database seeding.
✗ Do not write E2E tests for visual edge cases that can be verified via unit tests.
