---
area: architecture
path: rules/architecture/workflows.md
rules: 1
---
### ARCH-DDD-006 · `should` · T3 guidance
> applies_to: `any`
**EventStorming for Cross-Team Domain Discovery**

Before modeling a new or poorly-understood business process that spans multiple roles (engineering, product, domain experts), facilitate an EventStorming workshop — a collaborative, sticky-note-based timeline of domain events — before writing bounded-context or aggregate design documents for it.

How to: Gather a diverse group (engineers, domain experts, product owners, testers — capped at roughly 10 participants) in a room with a large modeling surface and sticky notes, and model the process as a timeline of domain events before any bounded-context or aggregate design work begins for that process.

✗ An engineer alone reverse-engineers a new cross-department workflow from an existing ticket and starts writing the domain model without validating the process with the actual domain experts.
✓ Run a 2-4 hour EventStorming session with engineering + product + domain experts, producing a sticky-note event timeline, before drafting the ADR or bounded-context design for that process.

**Why:** Design decisions made without first building a shared, cross-functional understanding of how a business process actually works tend to encode one team's incomplete or incorrect mental model into code, which then has to b

