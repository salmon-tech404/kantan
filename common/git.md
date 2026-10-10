---
area: common
path: common/git.md
rules: 3
---
### GIT-CMT-001 · `must` · T1 critical
**Conventional Commits v1.0.0 Specification**

Git commit messages must strictly adhere to the Conventional Commits specification: <type>(<scope>): <short description> in lowercase.

How to: Valid types: feat, fix, refactor, test, docs, chore, perf. Scope should match the affected module.

✗ git commit -m 'fix bug' or 'update code'
✓ feat(rag): add excel multi-sheet extraction support

**Why:** Standardized commit messages allow automated semantic versioning, changelog generation, and immediate comprehension of change impact.


### CD-GAT-001 · `must` · T1 critical
**Automated Pre-Commit and CI Quality Gates**

Git commits and CI builds must enforce automated quality gates: ESLint (zero errors), TypeScript type-check (tsc --noEmit), and automated unit tests.

How to: Configure Husky with lint-staged for pre-commit. Configure GitHub Actions to run lint, typecheck, and test on every PR.

✗ Committing with git commit -n (--no-verify) to bypass failing type checks.
✓ npx lint-staged (running eslint --fix && prettier --write) on staged files prior to commit.

**Why:** Allowing broken types or unlinted code into the main branch blocks team velocity and leads to broken deployments.


### SWE-DEP-001 · `must` · T1 critical
**Deterministic Dependency Pinning and Vulnerability Auditing**

Package dependencies must be strictly committed with lockfiles (package-lock.json). CI must execute npm audit / security vulnerability scans on every build.

How to: Use npm ci in CI pipelines. Run npm audit --audit-level=high in quality gates.

✗ npm install with wildcards (*) and omitting package-lock.json from version control.
✓ npm ci (strictly installing exact versions verified by package-lock.json).

**Why:** Unpinned or loose dependency ranges (^1.2.0) allow upstream compromises or breaking sub-dependency releases to break production builds unexpectedly.

