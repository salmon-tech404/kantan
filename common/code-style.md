---
area: common
path: common/code-style.md
rules: 3
---
### SWE-STY-001 · `must` · T1 critical
**Automated Formatting and Style Guides as Common Law**

Code formatting must be entirely delegated to automated deterministic tools (Prettier, ESLint). Style debates must never take place in manual code reviews.

How to: Enforce prettier --check and eslint in CI. Reject PRs with unformatted code automatically.

✗ A code review comment: 'Please add a newline between line 14 and 15.'
✓ Configuring .prettierrc with singleQuote: true, trailingComma: 'all', and running pre-commit auto-formatting.

**Why:** Human code reviewers wasting time discussing tabs, spaces, semicolons, and trailing commas burns cognitive energy that should be focused on architectural correctness and security.


### CODE-FUN-002 · `must` · T1 critical
**Small Function Size and Guard Clause Early Returns**

Functions should not exceed {{max_fn_lines}} lines of logic and must use guard clauses (early returns) to maintain a cyclomatic nesting depth of {{max_depth}} or less.

How to: Check preconditions at the top of the function and return immediately on failure. Avoid else blocks after returns.

✗ if (user) { if (hasAccess(user)) { ... } else { ... } } else { ... } // Arrow anti-pattern
✓ if (!user) return null; if (!hasAccess(user)) throw new ForbiddenError(); return execute(user);

**Why:** Deeply nested if-else ladders increase cognitive complexity exponentially, leading to missed edge cases and maintenance dread.

**Parameter:** `exceed {{max_fn_lines}} lines`, `depth of {{max_depth}} or less`


### CODE-DEM-001 · `must` · T2 needs review
**Law of Demeter (Principle of Least Knowledge)**

A method must only invoke methods on: (1) its own object, (2) objects passed in as arguments, (3) objects it instantiates, and (4) its direct collaborators. Deep chaining of accessors is strictly forbidden.

How to: Follow the 'Tell, Don't Ask' principle: user.getOrganizationTier() rather than user.getOrganization().getSettings().getTier().

✗ const tier = req.user.profile.company.billing.subscription.planTier; // Deep train wreck chaining
✓ const tier = req.user.getBillingTier();

**Why:** Chaining accessors (e.g. req.user.profile.organization.settings.tier) leaks structural internals, creating high coupling where a schema change in an inner object breaks distant callers.

