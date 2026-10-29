# Legacy (pre-3.0, not functional)

Moved here during the structure refactor. Kept for history; nothing here is used by current Kantanda.

- `compiler/` — built `dist/kantanda-manifest.json` from `*.rules.xml`, `taxonomy.xml`, `frameworks/`, `conflicts/`, `incidents/`. Those XML sources no longer exist (rules are Markdown now), so the compiler cannot run. `compile_brain.py` and `query_brain.py` are thin wrappers around the other two.
- `dist/kantanda-manifest.json` — last generated manifest (v2.0.0, 110 rules). Stale.
- `profiles/*.profile.xml` — v2 example profiles. They reference a removed rule (`CODE-DES-001`) and XML conflict files. Replaced by `setup/profile-template.md`.
- `tooling/.eslintrc.js`, `tooling/kantanda-security.yml` — older copies of the ESLint and Semgrep checks. Replaced by `tooling/eslint.config.mjs` and `tooling/semgrep.yml`.

Delete this folder once nobody needs the history (git keeps it anyway).
