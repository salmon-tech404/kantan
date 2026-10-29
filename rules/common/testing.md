---
area: common
path: rules/common/testing.md
rules: 3
---
### SWE-TST-001 · `must` · T2 needs review
**Hermetic Test Isolation and Explicit Test Sizing**

Tests must be explicitly categorized by size (Small/Unit, Medium/Integration, Large/E2E). Small tests must be hermetic, running in-memory with zero disk, network, or external process access.

How to: Small tests execute in milliseconds. Medium tests use local database containers. Large tests run full browser workflows.

✗ A 'unit test' that makes real HTTP fetch calls to a live external API server.
✓ Small test: pure math chunking test in Vitest (<10ms). Medium test: Supertest + test database (<500ms).

**Why:** Non-hermetic unit tests that make network calls or rely on external state are flaky, slow down feedback loops, and fail intermittently in CI environments.


### TEST-RACE-001 · `must` · T2 needs review
**Mandatory Concurrent Execution Testing for Concurrency and Locking Claims**

Any code asserting race-condition prevention, optimistic locking, or pessimistic locking must include at least one automated test executing N concurrent requests via Promise.all asserting exact fulfilled/rejected counts and balance invariant preservation.

How to: Execute 10 concurrent transfers with Promise.all on an account with balance sufficient for only 3. Assert fulfilled == 3, rejected == 7, and final balance == initial - 600,000.

✗ Testing a financial transfer service with only sequential 1-by-1 transfers and declaring it race-condition safe.
✓ const results = await Promise.all(requests); expect(fulfilled.length).toBe(3); expect(rejected.length).toBe(7);

**Why:** Sequential tests cannot verify mutexes or row locks. Race conditions only manifest when concurrent threads attempt conflicting mutations simultaneously.


### TEST-IDEM-001 · `must` · T2 needs review
**Mandatory Behavioral Idempotency Deduplication Testing**

Any endpoint or service accepting an Idempotency-Key must include at least one automated test executing two consecutive requests with the identical key, asserting that the second call returns the original result without secondary balance or state mutations.

How to: Issue transfer request with idempotencyKey 'key-1'. Verify balance deducted once. Issue identical request with 'key-1'. Assert HTTP 200, identical transaction reference, and assert source balance remained unchanged.

✗ Only testing that Zod schema rejects malformed UUID idempotency keys without testing duplicate call behavior.
✓ await service.transfer(dto); const res2 = await service.transfer(dto); expect(account.balance).toBe(initialBalance - dto.amount);

**Why:** Unit tests that merely verify Zod schema validation pass falsely while leaving the actual deduplication logic completely unimplemented. Behavioral double-call tests are mandatory to guarantee double-spend prevention.

