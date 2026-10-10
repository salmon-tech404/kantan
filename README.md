# Kantanda Engineering Standards

A shared set of engineering standards for multiple projects. Clone it, create three `AGENTS.md` files, customize `profile.md` → ready to use.

---

## Table of Contents

- [Introduction](#introduction)
- [Quick Start](#quick-start)
- [Project Setup](#project-setup)
- [Understanding Standards](#understanding-standards)
- [Customization](#customization)
- [Contributing](#contributing)

---

## Introduction

Kantanda — A unified standard for every project.
As the number of projects and team members grows, maintaining standards becomes difficult to control: guidelines get repeated, standards diverge, and onboarding takes longer. Kantanda solves this by building a single source of truth, where every project can inherit and apply standards consistently from the start.

### Why Kantanda?

- **Unified Standards**: One set of rules for all projects
- **Project-Specific Customization**: Override or extend rules when needed
- **LLM-Friendly**: AI agents automatically discover standards
- **No Repetition**: Clone once, customize per context
- **Built-In Quality**: Security, performance, and maintainability are pre-configured

### What's Included

| Area | Standards | Reference |
|------|-----------|-----------|
| **Frontend** | Component design, styling, state management, testing | `frontend/` |
| **Backend** | API design, database patterns, authentication, security | `backend/` |
| **Architecture** | Module boundaries, system design, ADR | `architecture/` |
| **Common** | Code style, version control, testing strategy | `common/` |
| **Guides** | Documentation, technical writing | `guide/` |

---

## Quick Start

### Step 1: Clone Kantanda

```bash
git clone <kantanda-repository> my-project
cd my-project
```

### Step 2: Create Three AGENTS.md Files

Three `AGENTS.md` files are navigation maps. They list all standards applicable to each area (frontend, backend, or organization-wide).

#### Frontend — `frontend/AGENTS.md`

Create `frontend/AGENTS.md` with:

```markdown
# Frontend Standards — [Project Name]

Technology Stack: [e.g., Next.js 16, React 19, Tailwind CSS v4]

## Standards by Topic

| Topic | Reference Document |
|-------|-------------------|
| Component Design, UI Patterns, Accessibility | `frontend/ui.md` |
| Project Structure, Server Components, State Management | `frontend/architecture.md` |
| TypeScript Types and Interfaces | `frontend/typescript.md` |
| Rendering User-Generated Content | `frontend/security.md` |
| End-to-End Testing | `frontend/testing.md` |

See `standards/profile.md` for project-specific parameters and overrides.

## Before Submitting Changes

\`\`\`bash
npm run verify
\`\`\`
```

Replace `[Project Name]` with your project's name.

---

#### Backend — `backend/AGENTS.md`

Create `backend/AGENTS.md` with:

```markdown
# Backend Standards — [Project Name]

Technology Stack: [e.g., Express.js 5, TypeScript, PostgreSQL]

## Standards by Topic

| Topic | Reference Document |
|-------|-------------------|
| HTTP API, Validation, Error Handling | `backend/api.md` |
| Database Queries, Transactions, Access Control | `backend/database.md` |
| Authentication, Authorization, Security | `backend/security.md` |
| Unit and Integration Testing | `backend/testing.md` |

See `standards/profile.md` for project-specific parameters and overrides.

## Critical Invariants

1. **Ownership Authentication** — All resource queries must filter by the specified user ID
2. **Input Validation** — Validate all external input before use
3. **Safe Responses** — Never leak internal details in responses
4. **User Content Is Untrusted** — Sanitize all user-generated content

## Before Submitting Changes

\`\`\`bash
cd backend && npx tsc --noEmit
\`\`\`
```

Replace `[Project Name]` with your project's name.

---

#### Source Root — `AGENTS.md` (root)

Create `AGENTS.md` at the repository root:

```markdown
# Standards — [Project Name]

[One-line project description]

Repository structure: `frontend/` · `backend/` · [other directories]

## Standards by Scope

| Scope | Reference |
|-------|-----------|
| **Frontend** | See `frontend/AGENTS.md` |
| **Backend** | See `backend/AGENTS.md` |
| **Architecture, Module Boundaries** | `architecture/boundaries.md` · `architecture/adr.md` |
| **Code Style** | `common/code-style.md` |
| **Version Control** | `common/git.md` |
| **Testing Strategy** | `common/testing.md` |
| **Documentation** | `guide/writing.md` |

To find the full Kantanda: See `AGENTS.md` at the root of Kantanda.

Project configuration: `standards/profile.md`

## Priority Order When Conflicts Arise

\`\`\`
Conventions in this file > standards/profile.md > Kantanda
\`\`\`

Exception: Core security rules (see Kantanda) cannot be overridden.

## Verify

Run verify before committing:

- Frontend: `npm run verify`
- Backend: `npx tsc --noEmit`
```

Replace `[Project Name]` and `[One-line project description]` with your project's information.

---

### Step 3: Configure `standards/profile.md`

This file declares **project-specific configuration**: technology stack, parameters, rule overrides if needed.

**Create `standards/profile.md` using the template below. Replace values in `[...]` with your project information.**

```markdown
---
project: [Your Project Name]
kantanda_version: 3.0.0
updated: [Today]
---

# Project Configuration

## 1. Technology Stack

List the technologies your project uses. This is a reference for new developers to understand the project tech.

| Component | Technology |
|-----------|-----------|
| Frontend | [e.g., Next.js 16, React 19, Tailwind CSS v4] |
| Backend | [e.g., Express.js 5, TypeScript 5] |
| Database | [e.g., PostgreSQL 15] |

**Concrete Example:**
```
| Frontend | Next.js 16.2.6, React 19.2.4, Tailwind CSS v4, Zustand |
| Backend | Express.js 5.2, TypeScript 5.3, Prisma 7.8 |
| Database | PostgreSQL 16 |
```

---

## 2. Required Parameters

Kantanda rules use placeholders `{{...}}`. You need to fill in your project's specific values.

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `ownership_key` | userId, orgId, or tenantId | Which column in the DB to check ownership |
| `max_function_lines` | 40, 50, 100 (varies) | Functions longer than this must be split |
| `max_nesting_depth` | 2, 3, 4 (varies) | Maximum nesting depth for control structures |
| `access_token_ttl` | 15m, 30m, 1h | How long access tokens remain valid |
| `refresh_token_ttl` | 7d, 30d (varies) | How long refresh tokens remain valid |
| `max_upload_size` | 5MB, 10MB, 20MB | Maximum file upload size |

**Concrete Example:**
```
| `ownership_key` | userId | Backend checks queries with `where: { id, userId }` |
| `max_function_lines` | 40 | Functions > 40 lines must be split |
| `max_nesting_depth` | 3 | No more than 3 levels of nesting |
| `access_token_ttl` | 15m | JWT access token valid for 15 minutes |
| `refresh_token_ttl` | 7d | JWT refresh token valid for 7 days |
| `max_upload_size` | 20MB | Only files <= 20MB can be uploaded |
```

---

## 3. Rule Overrides (Optional)

If your project **cannot comply with a Kantanda rule**, document it here. Skip this section if you don't override any rules.

| Rule ID | Standard Rule | Exception | Reason |
|---------|--------------|-----------|--------|
| [e.g., FE-ACT-001] | [What Kantanda says] | [What your project does differently] | [Why compliance isn't possible] |

**Concrete Example:**
```
| FE-ACT-001 | Server Actions for form mutations only | Permit real-time sync | Pages router migration in progress |
| BE-DB-001 | Filter queries by ownership_key | Data refactoring not complete | Legacy code, will fix in Q3 |
```

---

## 4. Project-Specific Rules (Optional)

If your project adds rules beyond Kantanda, document them here. Skip this section if you don't have new rules.

| Rule ID | Tier | Description |
|---------|------|-------|
| [e.g., VX-TEST-001] | T1 or T2 | [Rule description] |

**Concrete Example:**
```
| VX-TEST-001 | T1 | All React components must have `*.test.tsx` snapshot tests. Enforced via Jest. |
| VX-STYLE-001 | T1 | Forbid `console.log`. Use logger service instead. |
```
```

**How to Fill It Out:**
1. Set the project name in `project:`
2. Fill in the stack in Section 1 (actual technologies your project uses)
3. Fill in parameters in Section 2 (required so Kantanda knows the values)
4. Sections 3 & 4 → skip if you don't need overrides or new rules

---

## Project Setup

After completing Quick Start, your repository contains:

```
my-project/
├── README.md                    # Project documentation
├── CLAUDE.md                    # Entry point for AI agents (→ AGENTS.md)
├── AGENTS.md                    # Root navigation map
│
├── frontend/
│   ├── AGENTS.md               # Frontend standards map
│   └── src/
│
├── backend/
│   ├── AGENTS.md               # Backend standards map
│   └── src/
│
└── standards/
    ├── profile.md              # Project configuration
    └── adr/                     # Architecture Decision Records
```

Everything in `standards/profile.md` cascades through the codebase. Developers and AI agents find all applicable standards by reading three AGENTS.md files.

---

## Understanding Standards

### Rule ID

Standards in Kantanda use structured identifiers:

**Format**: `[DOMAIN]-[CATEGORY]-[NUMBER]`

**Examples**:
- `BE-DB-001` → Backend, Database, rule 001 (see `backend/database.md`)
- `FE-SEC-002` → Frontend, Security, rule 002 (see `frontend/security.md`)
- `SEC-AUTH-003` → Security (cross-domain), Authentication, rule 003

When you see a Rule ID, the domain-category prefix tells you exactly which file contains the full definition.

### Enforcement Levels

Each standard has an enforcement level that indicates how to verify it:

| Level | Mechanism | Strictness |
|-------|-----------|-----------|
| **T1 (Automated)** | Linters, type checkers, tests | High. Blocks commits. Error rate <1%. |
| **T2 (Review)** | Code review + automated flagging | Medium. Flags during review. Error rate <10%. |
| **T3 (Guidance)** | Manual reference only | Low. No enforcement. |

---

## Customization

### Add Project-Specific Rule

**Scenario**: Your project requires all React components to have snapshot tests.

**Step 1**: Add to `standards/profile.md` (Project Extensions):

```markdown
| VX-TEST-001 | T1 | All React components must have `*.test.tsx` snapshot tests. Enforced via Jest. |
```

**Step 2**: Add to `frontend/AGENTS.md` (end of file):

```markdown
## Project Extensions

| Rule | Enforcement | Description |
|------|-------------|-------|
| VX-TEST-001 | Automated (T1) | All React components require snapshot tests in `*.test.tsx`. |
```

Developers and AI agents will see this rule when working on frontend.

### Override Kantanda Rule

**Scenario**: Your project uses Server Actions for real-time sync, but Kantanda restricts Server Actions to form mutations.

**Step 1**: Add to `standards/profile.md` (Rule Exceptions):

```markdown
| FE-ACT-001 | Server Actions restricted to form mutations | Permit real-time data sync | Pages router migration in progress. |
```

**Step 2**: Add to `frontend/AGENTS.md` (end of file):

```markdown
## Rule Exceptions

| Rule | Change |
|------|--------|
| FE-ACT-001 | Server Actions may be used for non-form mutations during pages router migration. See `standards/profile.md`. |
```

---

## Detailed Structure

### backend/
- `api.md` — API contracts, endpoint naming, status codes, authentication
- `database.md` — schema, query patterns, N+1 prevention
- `security.md` — SQL injection, authorization, business logic
- `testing.md` — unit test, integration test strategy
- `guidance.md` — recommendations, not rules

### frontend/
- `ui.md` — component API, accessibility, responsive design, animation
- `typescript.md` — type coverage, no `any`, generic naming
- `architecture.md` — state management, server actions vs client
- `security.md` — XSS, CSRF, CSP, sensitive data
- `testing.md` — component testing, E2E testing strategy
- `guidance.md` — recommendations, not rules

### common/
- `code-style.md` — variable naming, function length, complexity
- `git.md` — commit messages, branch naming, PR workflow
- `testing.md` — test file naming, assertion style
- `workflows.md` — onboarding, releases, hotfixes
- `incidents.md` — incident reporting, prevention, post-mortems
- `guidance.md` — recommendations, not rules

### architecture/
- `adr.md` — Architecture Decision Record template + list
- `boundaries.md` — bounded contexts, anti-corruption layers
- `conflicts.md` — 5 resolved conflicts (DRY vs Bounded Context, etc.)
- `frameworks.md` — decision frameworks (database selection, caching strategy)
- `workflows.md` — database migrations, feature flags, deployments
- `guidance.md` — recommendations, not rules

### guide/
- `writing.md` — standards for README, commit messages, ADR, code comments

### _system/
- `profile-template.md` — project template: stack, parameters ({{...}}), overrides
- `evidence.md` — source citations — **not loaded by default**
- `audit-notes.md` — audit notes (version, rules removed, reasons)
- `pruned.md` — 10 removed rules and their reasons
- `tooling/` — ESLint config, Semgrep patterns

---

## Questions & Support

- **New to Kantanda?** See [Quick Start](#quick-start) for 3 simple setup steps
- **Need to customize rules for your project?** See [Customization](#customization) to learn how to override or extend rules
- **Want to contribute new ideas?** See [Contributing](#contributing) to submit a pull request

For detailed understanding of specific standards, refer to files in `frontend/`, `backend/`, `architecture/`, and `common/` directories.

---

## Acknowledgments

Kantanda is not the work of one person, but an accumulation of hundreds of lessons learned from real-world projects. We thank:

- **Engineering Teams** — Those who spent time debating, reviewing, and refactoring code to comply with these standards
- **Airbnb, Google, TypeScript Team** — Pioneering style guides that inspired Kantanda's structure and philosophy
- **OWASP Foundation** — Security standards that protect user data and system integrity
- **Open-Source Community** — The frameworks, tools, and patterns on which Kantanda is built

If Kantanda helps your project, please share feedback or suggestions. If you find issues, don't hesitate to open an issue or submit a pull request. Kantanda will continue evolving with the real-world needs of projects.

---

## License

MIT License — Kantanda is released under the MIT License. You are free to use, modify, distribute, and use for commercial or personal purposes without permission, provided you include a copy of this license.
