# Standards — [Project Name]

[One-line project description]

Repository structure: `frontend/` · `backend/` · [other directories]

Kantanda is vendored at `standards/kantanda/`. Project configuration: `standards/profile.md`.

## Standards by Scope

| Scope | Reference |
|---|---|
| **Frontend** | `frontend/AGENTS.md` |
| **Backend** | `backend/AGENTS.md` |
| **Architecture style, module boundaries** | `standards/kantanda/rules/architecture/styles.md` · `.../boundaries.md` · `.../adr.md` |
| **Code style** | `standards/kantanda/rules/common/code-style.md` |
| **Version control** | `standards/kantanda/rules/common/git.md` |
| **Testing strategy** | `standards/kantanda/rules/common/testing.md` |
| **Documentation** | `standards/kantanda/rules/guide/writing.md` |

Full Kantanda index: `standards/kantanda/AGENTS.md`.

## Priority Order When Conflicts Arise

```
Conventions in this file > standards/profile.md > Kantanda
```

Exception: Non-Negotiable rules (see Kantanda `AGENTS.md`) cannot be overridden.

## Verify

Run verify before committing:

- Frontend: `npm run verify`
- Backend: `npx tsc --noEmit`
