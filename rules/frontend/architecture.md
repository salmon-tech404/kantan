---
area: frontend
path: rules/frontend/architecture.md
rules: 4
---
### FE-ARCH-001 · `must` · T2 needs review
> applies_to: `stack:next-app-router`
**Server-First Components in Next.js App Router**

React components in the Next.js App Router must be React Server Components (RSC) by default. The 'use client' directive must only be applied at leaf interactive components.

How to: Keep layouts and data-fetching pages as Server Components. Extract buttons, inputs, and modals into leaf Client Components.

✗ Placing 'use client' at the very top of app/documents/page.tsx.
✓ page.tsx (Server Component fetching doc) -> imports <DocumentTable /> (Server) -> imports <DeleteButton /> ('use client')

**Why:** Applying 'use client' at high levels inflates JavaScript client bundles, degrades first contentful paint (FCP), and breaks server streaming advantages.


### FE-ARCH-002 · `must` · T2 needs review
> applies_to: `feature-slice`
**Colocation of Feature Components and Hooks**

Components, hooks, api callers, and types specific to a single feature must be colocated under src/features/<feature>/ rather than scattered into global directories.

How to: Structure code as src/features/chat/ containing ChatWindow.tsx, useChat.ts, chat.api.ts, and chat.types.ts.

✗ Placing 80 custom hooks in global src/hooks/ and 120 components in global src/components/.
✓ src/features/documents/components/DocumentCard.tsx, src/features/documents/hooks/useDocuments.ts

**Why:** Scattering feature code into global components/, hooks/, and types/ creates high coupling and makes features difficult to maintain, delete, or refactor.


### FE-API-001 · `must_not` · T1 critical
**Decoupled API Client Service Layer (No Fetch/Axios in JSX)**

UI components must not call axios or fetch directly in JSX event handlers or useEffect hooks; all calls must be encapsulated in typed API service functions.

How to: Export typed functions from features/<feature>/api/ (e.g. getDocuments(): Promise<Document[]>).

✗ const res = await axios.get('/api/v1/documents'); // Direct Axios call in button onClick handler
✓ const data = await documentApi.list(); setDocuments(data);

**Why:** Scattering HTTP client invocations across components makes global error handling, authentication interceptors, retry logic, and testing impossible.


### FE-STA-002 · `must` · T2 needs review
**URL-as-State for Search Queries, Filters, and Pagination**

State that alters the primary view of data (search terms, filter categories, sorting order, active pagination page) must be synchronized with URL search parameters.

How to: Use useSearchParams() and useRouter().replace() with debounce for text inputs. Read parameters server-side in page.tsx for direct Server Component rendering.

✗ const [page, setPage] = useState(1); const [filter, setFilter] = useState('all'); // State lost on refresh, impossible to bookmark
✓ const searchParams = useSearchParams(); const page = Number(searchParams.get('page')) || 1; function onPageChange(p) { updateUrlParam('page', p); }

**Why:** Storing search and filter state purely in React useState or global stores breaks browser back/forward navigation, makes bookmarking impossible, and impairs link sharing.

