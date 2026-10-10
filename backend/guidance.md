---
area: backend
path: backend/guidance.md
rules: 1
---
### TEST-DBL-001 · `must` · T3 guidance
**Strict Test Double Taxonomy: Prefer Fakes and Stubs Over Interaction Mocks**

Test suites must distinguish between Fakes (lightweight in-memory implementations), Stubs (canned queries), and Mocks (interaction verification). Prefer Fakes and Stubs over brittle interaction Mocks.

How to: Create an InMemoryUserRepository implementing UserRepository for hermetic tests. Use Mocks only to verify unobservable outgoing commands to external boundaries (e.g. email service).

✗ expect(mockRepo.query).toHaveBeenCalledTimes(1); // Brittle interaction verification
✓ const fakeRepo = new InMemoryUserRepository(); const service = new UserService(fakeRepo); expect(await service.getUser(id)).toEqual(expected);

**Why:** Asserting that a specific collaborator method was called exactly N times (mocking) couples the test to procedural call sequences rather than validating final output state.

