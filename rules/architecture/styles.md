---
area: architecture
path: rules/architecture/styles.md
---

Architecture **styles** and which rules apply to which style. Read this before applying any `ARCH-*` or `FE-ARCH-*` rule.

## Why this file exists

Coding rules and architecture are different things.

- A **coding rule** says how to write code inside a place (validate input, name things, never log secrets). It holds under every architecture.
- An **architecture style** says where code lives and which way dependencies point. Styles exclude each other, so a rule written for one style is wrong for another.

Applying a style-specific rule to a project that chose a different style produces false violations. This is why each architecture rule carries `applies_to`.

## Two independent axes

A project picks one value on each axis. They combine freely (a modular monolith may use layers inside each module).

| Axis | Question | Values |
|---|---|---|
| **Partitioning** | How is the top level of the codebase split? | `domain-partitioned` (by feature/domain) · `technical-partitioned` (by layer) |
| **Dependency style** | Which way do dependencies point inside one module? | `layered` (Route → Controller → Service → Repository) · `hexagonal` (domain defines ports, infrastructure implements adapters) |

Other values that appear in `applies_to`:

| Value | Meaning |
|---|---|
| `domain-model` | Business logic uses the Domain Model pattern (aggregates, invariants), not simple CRUD |
| `feature-slice` | Frontend code is colocated per feature under `src/features/<feature>/` |
| `stack:<name>` | Applies only to one framework (e.g. `stack:next-app-router`) |
| `any` | Applies under every style |

> Source for the partitioning axis: *Fundamentals of Software Architecture* (technical vs domain partitioning). The `dependency style` axis is Kantanda's own grouping of layered vs hexagonal and is not a quote from a book.

## Rule → style map

| Rule | Tier | `applies_to` | Machine check today |
|---|---|---|---|
| `ARCH-ADR-001` | T2 | `any` | none |
| `ARCH-DDD-001` | T3 | `any` | n/a |
| `ARCH-DDD-002` | T1 | `any` | ESLint `kantanda/acl` (vendor SDK imports outside adapters) |
| `ARCH-DDD-003` | T3 | `domain-model` | n/a |
| `ARCH-DDD-004` | T3 | `any` | n/a |
| `ARCH-DDD-005` | T1 | `hexagonal` | ESLint `kantanda/hexagonal`, only when `styles` includes `hexagonal` |
| `ARCH-DDD-006` | T3 | `any` | n/a |
| `ARCH-LAY-001` | **T2** | `layered` | none (was T1 without a tool; lowered) |
| `ARCH-SINK-001` | T3 | `layered` | n/a |
| `ARCH-MOD-001` | T3 | `any` | n/a |
| `ARCH-MOD-002` | T1 | `any` | ESLint `kantanda/modularity` |
| `ARCH-MOD-003` | T3 | `any` | n/a |
| `ARCH-MONO-001` | T2 | `domain-partitioned` | none |
| `FE-ARCH-001` | T2 | `stack:next-app-router` | none |
| `FE-ARCH-002` | **T2** | `feature-slice` | none (was T1 without a tool; lowered) |

A rule may only be T1 if a tool in `tooling/` enforces it. Raise `ARCH-LAY-001` or `FE-ARCH-002` back to T1 only after adding that tool.

## How a project declares its style

In `profile.md` (template: `setup/profile-template.md`), section **Architecture**. Declare per package, because a monorepo usually mixes styles (for example a Rust backend and a TypeScript frontend).

```
| Package | Partitioning | Dependency style | Other |
|---|---|---|---|
| crates/ | domain-partitioned | hexagonal | domain-model |
| packages/web | domain-partitioned | — | feature-slice, stack:next-app-router |
```

Loading rule for agents: for the files you are changing, find the nearest package in the profile, then apply the rules whose `applies_to` is `any` or matches one of that package's declared values.

## Choosing a style

Choosing is a structural decision. Record it as an ADR (`rules/architecture/adr.md`). Use `rules/architecture/frameworks.md` to compare options. Do not change style by editing rules; change it in the profile.

## Enforcement is per ecosystem

Dependency direction is checked by different tools per language. Kantanda ships the ESLint (TypeScript) layer. For other stacks, write the equivalent check before marking a rule T1 for that stack.

| Stack | Typical tool |
|---|---|
| TypeScript / JavaScript | ESLint `no-restricted-imports`, dependency-cruiser |
| Rust | one crate per layer, `cargo-deny` `bans` with `wrappers` |
| Python | import-linter |
| Java / Kotlin | ArchUnit |

These are the common tools for each ecosystem; check each tool's own documentation for exact configuration. Kantanda does not yet ship Rust or Python checks.

## Not yet done

- Style packs: per style, the folder layout and a ready-to-use check for each stack. Until they exist, `applies_to` only controls which rules apply; it does not generate checks.
- The vocabulary above (layer, module, port) is not proven sufficient for every style. Test it against a real project before relying on it.
