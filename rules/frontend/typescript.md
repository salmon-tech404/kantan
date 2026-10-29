---
area: frontend
path: rules/frontend/typescript.md
rules: 2
---
### FE-TS-001 · `must_not` · T1 critical
**Strict Zero-Any Policy in TypeScript**

The 'any' keyword is strictly prohibited in application code. Use unknown, generics, or explicit narrowing types.

How to: Enable @typescript-eslint/no-explicit-any: 'error'. Use type guards (if (typeof x === 'string')) to narrow unknown.

✗ function parse(input: any): any { return input.name; } // Type-unsafe
✓ function parse(input: unknown): string { if (typeof input === 'string') return input; throw new Error(); }

**Why:** Using 'any' silently disables the TypeScript type checker, propagating unsafety across callers and causing preventable runtime crashes.


### FE-TS-002 · `must` · T2 needs review
**Discriminated Unions for Representing State**

Asynchronous UI states must be modeled using Discriminated Unions with a common literal discriminator property ('status') to make impossible states unrepresentable.

How to: type State = { status: 'idle' } | { status: 'loading' } | { status: 'success'; data: T } | { status: 'error'; error: string };

✗ if (isLoading && !isError && data) ... // Error-prone boolean permutation checks
✓ switch (state.status) { case 'loading': return <Skeleton />; case 'success': return <View data={state.data} />; }

**Why:** Using independent booleans (isLoading: boolean, isError: boolean, data: T | null) allows contradictory states like { isLoading: true, isError: true }.

