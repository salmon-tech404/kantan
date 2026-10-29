---
area: backend
path: rules/backend/testing.md
rules: 5
---
### TEST-INT-001 · `must` · T1 critical
**Integration Tests with Real Database State Rollback**

Integration tests must execute against a real PostgreSQL instance with pgvector enabled, rolling back transactions after each test to ensure state cleanliness.

How to: Use a dedicated test container or test database. Wrap tests in a rollback transaction or run truncate migrations in beforeEach.

✗ Mocking the entire PrismaClient object in an integration test.
✓ await prisma.document.create(...); const res = await request(app).get('/api/v1/documents'); expect(res.status).toBe(200);

**Why:** In-memory fake databases (SQLite, Mock Prisma) do not support pgvector syntax, JSON operators, or PostgreSQL-specific constraint violations, masking critical production bugs.


### TEST-MCK-001 · `must` · T1 critical
**Restrict Mocking to Out-of-Process Unmanaged Dependencies**

Only mock external, out-of-process unmanaged dependencies that you do not own (e.g., Gemini API, DeepSeek API, Nodemailer). Do not mock internal classes, helpers, or managed databases.

How to: Use real domain classes and in-process collaborators in unit tests. Mock only network boundaries with third-party servers.

✗ vi.mock('../utils/math-helper'); // Anti-pattern: mocking internal pure helper function
✓ const mockGemini = { generateEmbedding: vi.fn().mockResolvedValue([0.1, 0.2]) };

**Why:** Over-mocking internal classes couples tests to private implementation details, creating brittle tests that break on every refactor without catching real bugs.


### TEST-MCK-002 · `must_not` · T2 needs review
**Verify State and Output, Never Interaction Counts on Internals**

Tests must not assert internal method invocation counts (e.g. expect(internalHelper).toHaveBeenCalledTimes(1)) on internal components.

How to: Assert the observable return value or the resulting database/state change.

✗ expect(chunker['splitWords']).toHaveBeenCalledTimes(3); // Brittle interaction testing
✓ const result = chunker.process(text); expect(result).toHaveLength(3);

**Why:** Asserting how many times internal sub-routines are called binds tests to exact line-by-line coding choices, causing false test failures during refactoring.


### TEST-AAA-001 · `must` · T2 needs review
**Standardized Arrange-Act-Assert (AAA) Test Structure**

Every test case must follow the Arrange-Act-Assert (AAA) pattern with clearly separated phases, containing only a single Act invocation.

How to: Structure each test with 3 distinct comment blocks or visual whitespace: // Arrange, // Act, // Assert.

✗ const u = makeUser(); auth(u); u.name = 'x'; update(u); expect(u).toBe(...); delete(u); expect(u).toBeNull();
✓ // Arrange: const user = makeUser(); // Act: const res = auth(user); // Assert: expect(res.token).toBeDefined();

**Why:** Interweaving setup, multiple acts, and repeated assertions turns tests into confusing multi-step scripts, making it difficult to pinpoint failure causes.


### TEST-ANT-001 · `must_not` · T1 critical
**Unit Testing Anti-Patterns: Never Test Private Methods or Mock Concrete Classes**

Unit tests must only verify observable public behavior; tests must never inspect or invoke private methods, expose internal state for testing, or mock concrete business classes.

How to: If a private method feels too complex to test through the public API, refactor it into a separate collaborator class with its own public interface.

✗ (service as any).privateCalculateHash(); // Testing private methods directly via casting
✓ const result = await service.register(input); expect(result.id).toBeDefined(); // Testing observable public contract

**Why:** Testing private methods couples tests tightly to implementation details, causing tests to break during harmless internal refactoring and producing false positive failures.

