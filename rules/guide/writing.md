---
area: guide
path: rules/guide/writing.md
rules: 7
---

Documentation standards: README, technical guides, user guides, runbooks.

This area prescribes **how to write**, not **what to write**. Project documentation lives in the project's repository.

### DOC-AUD-001 · `must` · T3 guidance
**Each document declares its audience on the first line.**

The first line must state who the document is for and what readers should already know.

✗ "This document describes the authentication system."
✓ "For backend engineers new to the project, familiar with JWT but not yet with our refresh token flow."

**Why:** Without knowing the audience, you can't decide detail level, and documentation drifts toward useless middle ground.

### DOC-SRC-001 · `must` · T2 review reminder
**Technical documentation must derive from real code, not memory.**

Every claim about system behavior must trace back to source, config, schema, migration, test, or CI. Don't invent architecture from guesses.

✗ "The system uses Redis for caching." (unverifiable)
✓ "Caching uses Redis — see `src/cache/client.ts:12` and `docker-compose.yml`."

**Why:** Wrong documentation is more dangerous than none, because readers trust it without verification.

### DOC-VER-001 · `must` · T2 review reminder
**Documentation lives next to what it describes.**

Code documentation lives in the same repository as the code, versioned together. Don't place it in external directories or in `.gitignore` locations.

**Why:** External documentation never gets updated when code changes, and links break at the first directory restructure.

### DOC-TIME-001 · `must_not` · T1 automated block
**Never write time-relative information.**

Forbid "currently," "soon," "next month," "new version." Use absolute dates or version numbers.

✗ "Soon we will migrate to v2."
✓ "Planned v2 migration in Q1/2027 — see ADR-0012."

**Why:** Relative information becomes wrong silently, without any error signal.

### DOC-OLD-001 · `should` · T3 guidance
**Deprecated content moves to "Legacy Approach," not deletion.**

Keep historical context in a collapsible section at the end, with the deprecation date.

**Why:** Readers finding old code need to understand why it was once done that way, but that content shouldn't crowd the current approach.

### DOC-TERM-001 · `must` · T2 review reminder
**One concept, one name, throughout the document.**

Pick a term and don't change it. Don't mix "endpoint / route / URL / path" for the same thing.

**Why:** Readers have to guess whether two words mean the same thing, and both humans and AI guess wrong.

### DOC-LEN-001 · `should` · T1 automated block
**Documents longer than 100 lines must have a table of contents at the start.**

**Why:** Both humans and AI skim long files. Without a table of contents, nobody knows whether the section they need exists.
