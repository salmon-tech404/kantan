---
area: common
path: rules/common/guidance.md
rules: 7
---
### CODE-FUN-001 · `must` · T3 guidance
**Single Responsibility Principle (SRP) for Functions**

Every function and method must perform a single, well-defined task and operate at a consistent level of abstraction.

How to: If a function contains 'and' in its informal description (e.g. 'parseAndSaveAndNotify'), split it into distinct composed functions.

✗ function process(buffer) { /* 200 lines doing regex, embedding, db calls, and emails */ }
✓ const text = extractText(buffer); const chunks = splitIntoChunks(text); await storeChunks(chunks);

**Why:** Functions that mix business decisions with data formatting and low-level I/O are difficult to test, impossible to reuse, and attract bugs during changes.


### CODE-NAM-001 · `must` · T3 guidance
**Intent-Revealing, Searchable Identifiers**

Variable and function names must clearly express their intent, domain concept, and unit of measurement without requiring external comments.

How to: Include units in variable names where ambiguous (timeoutMs, maxFileSizeMb). Prefix booleans with is/has/can/should.

✗ const flag = false; const timeout = 5000; const data2 = getData();
✓ const isIndexingCompleted = false; const maxTimeoutMs = 5000;

**Why:** Obscure names (e.g. data, temp, flag, d) force readers to scan entire files to deduce meaning, slowing down debugging and review.


### CODE-DOC-001 · `must` · T3 guidance
**Comments Must Explain 'Why', Never 'What'**

In-line comments must explain technical rationale, non-obvious business requirements, or architectural trade-offs; they must never simply narrate the code.

How to: If code is not obvious, refactor variable and function names. Use comments only for rationale (e.g., // Overlap is set to 50 words to bridge cross-page sentences).

✗ // Split the document into chunks const chunks = split(text);
✓ // 50-word overlap bridges boundary sentences in legal contracts that span page breaks

**Why:** Narrative comments (// increment i by 1) become outdated quickly, pollute the file, and distract from the actual logic.


### TEST-TRUTH-001 · `must` · T3 guidance
**Truth-in-Testing: Prohibition of False Concurrency Claims on In-Memory Fakes**

Pull requests and walkthrough documentation must never claim concurrency locking or race-condition verification based solely on in-memory fake repositories. If a test runs on an in-memory double without real engine locks, the report must state that runtime concurrency is unverified.

How to: Verify real concurrency against PostgreSQL using Testcontainers (TEST-INT-001). If using an in-memory test double, explicitly declare 'Domain business logic verified; runtime concurrency unverified'.

✗ Writing '// Simulates SELECT ... FOR UPDATE' in an in-memory Map and claiming 'Pessimistic Row Locking verified' in the PR summary.
✓ Integration test running concurrent transactions against a real PostgreSQL instance assert that serializable or row-level locks prevent lost updates.

**Why:** In-memory fakes lack database row locking and transaction serialization. Claiming concurrency safety based on in-memory tests creates false confidence and causes lost-update bugs in production.


### TEST-BLD-001 · `should` · T3 guidance
**Object Mother for Reusable Test Fixture Construction**

When arrange-section setup code for a test fixture is duplicated across several tests, extract it into a factory ("Object Mother") method or class with sensible defaults and named overrides for the fields each specific test cares about. Do not build a fluent Test-Data-Builder chain as the default choice.

How to: Write one function per entity (e.g. `createTestUser(overrides = {})`) returning a fully-valid default object merged with the caller's overrides, and call it from every test's arrange section instead of constructing the object inline.

✗ Hand-writing the same 15-field user object literal inline in 20 different test files, each slightly out of sync with the current schema.
✓ const user = createTestUser({ role: 'admin' }); // Object Mother: sensible defaults + named override

**Why:** Duplicated, hand-written fixture setup across many tests makes every test harder to read and turns any shared-schema change into a many-file edit; a single factory method centralizes that cost. A fluent builder achieves 


### TEST-HUM-001 · `should` · T3 guidance
**Humble Object Pattern for Splitting Untestable Code**

When business logic is entangled with a hard-to-test collaborator (a UI framework, an HTTP framework's request/response objects, a raw DB client), extract the business logic into a plain, dependency-free class or function, leaving behind a "humble" thin controller/adapter whose only job is orchestration and is simple enough not to need its own tests.

How to: Move calculation/decision logic out of Express route handlers, React components, or repository classes into pure functions/classes with no framework imports; the route handler or component becomes a thin orchestrator calling that logic.

✗ An Express route handler that inline-computes discount/tax logic mixed with req/res access, making the business rule untestable without mocking Express.
✓ function calculateOrderTotal(order: Order): Money { ... } // pure, unit-tested; route handler just calls it and writes the response

**Why:** Code that mixes business rules with an out-of-process or framework dependency forces every test of that logic to pay the cost (and flakiness) of that dependency. Splitting the logic out lets the business rules be unit-te


### CODE-TDD-001 · `should` · T3 guidance
**Three Laws of TDD (Red-Green-Refactor Sequencing)**

When practicing test-driven development, follow the sequence strictly: (1) write no production code until a failing unit test demands it, (2) write no more of a test than is needed to make it fail (a non-compiling test counts as failing), (3) write no more production code than is needed to make the currently failing test pass.

How to: Keep the red-green-refactor loop tight (seconds to a couple of minutes per cycle): red (failing test) -> green (minimum code to pass) -> refactor (clean up with the safety net of the passing test).

✗ Writing an entire service's implementation first, then bolting on a test suite afterward to hit a coverage number.
✓ // 1. write failing test for calculateDiscount() // 2. write minimal calculateDiscount() to pass it // 3. refactor with the test as a safety net

**Why:** Writing production code ahead of its test tends to produce code shaped by the implementer's assumptions rather than by an observable, verified requirement, and it is the single biggest reason teams end up with large bloc

