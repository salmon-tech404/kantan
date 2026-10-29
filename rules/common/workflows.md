---
area: common
path: rules/common/workflows.md
rules: 1
---
### SWE-REV-001 · `must` · T3 guidance
**Five-Point Code Review Verification Checklist**

Every Pull Request must be audited against 5 criteria before approval: Correctness, Security, Architecture Alignment, Test Coverage, and Readability.

How to: Include a standardized PR template checklist covering all 5 dimensions. Ensure all CI quality gates pass before merge.

✗ Merging PRs with 'LGTM' without verifying tests or security boundaries.
✓ PR checklist verified: [x] Unit/Integration Tests pass [x] No any types [x] Ownership filters verified [x] TSDoc added

**Why:** Ad-hoc reviews devolve into superficial debates over formatting while critical security vulnerabilities, regression risks, and architectural drift go unnoticed.

