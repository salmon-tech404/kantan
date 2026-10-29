# Backend Standards — [Project Name]

Technology Stack: [e.g., Express.js 5, TypeScript, PostgreSQL]

## Standards by Topic

| Topic | Reference |
|---|---|
| HTTP API, validation, error handling | `standards/kantanda/rules/backend/api.md` |
| Database queries, transactions, access control | `standards/kantanda/rules/backend/database.md` |
| Authentication, authorization, security | `standards/kantanda/rules/backend/security.md` |
| Unit and integration testing | `standards/kantanda/rules/backend/testing.md` |

Architecture rules apply per the style declared in `standards/profile.md` (Architecture section).

## Critical Invariants

1. **Ownership** — every resource query filters by the owner ID.
2. **Input validation** — validate all external input before use.
3. **Safe responses** — never leak internal details in responses.
4. **User content is untrusted** — sanitize all user-generated content.

## Before Submitting Changes

```bash
cd backend && npx tsc --noEmit
```
