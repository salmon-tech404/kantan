---
area: frontend
path: frontend/guidance.md
rules: 4
---
### FE-STA-001 · `must` · T3 guidance
**Strict State Separation (Server vs Global UI vs Form State)**

Frontend state must be strictly partitioned into Server State (caching API data), Global UI State (Zustand: active modal, sidebar), and Form State (React Hook Form).

How to: Never copy server API response lists into Zustand. Keep Zustand lean for client-only UI flags.

✗ Storing documents: Document[] in a global Zustand store and attempting to manually update it on every CRUD operation.
✓ useUIStore: { isSidebarOpen, activeModalId }; useDocuments: fetches and caches server data via API client.

**Why:** Storing server response arrays in global Zustand stores causes cache invalidation nightmares, stale data, and synchronization bugs.


### UI-LAW-001 · `must` · T3 guidance
**Jakob's Law: Conform to Familiar User Interface Mental Models**

Users spend most of their time on other sites; interface layouts, navigation patterns, and iconography must conform to familiar mental models rather than inventing proprietary navigation mechanics.

How to: Place primary navigation on the left sidebar or top header, search prominently in the top bar, and profile/settings in the top-right corner.

✗ Hiding the primary navigation inside an unlabelled floating action button at the bottom left.
✓ Top navbar with Logo on left, Global Search centered, and User Avatar on right.

**Why:** Violating conventional placement (e.g., placing the search bar in the bottom footer) causes cognitive friction and disorientation, driving user abandonment.


### UI-LAW-003 · `should` · T3 guidance
**Hick's Law: Minimize Options to Reduce Decision Latency**

Break down complex choices into distinct progressive steps; menus and selection dialogs should limit initial choices to high-frequency actions.

How to: Highlight recommended presets. Move advanced esoteric settings into a secondary collapsible 'Advanced Settings' accordion.

✗ Presenting 25 unorganized sliders and dropdowns on the primary chat window.
✓ Preset: Standard (8 Chunks), Detailed (12 Chunks). Advanced toggle: customize exact temperature and top-p.

**Why:** Decision time increases logarithmically with the number and complexity of choices. Overwhelming users with 30 options causes choice paralysis.


### UI-LAW-004 · `should` · T3 guidance
**Miller's Law: Chunk Complex Information into 5 to 9 Discrete Units**

Complex interfaces and forms must organize related information into discrete visual chunks containing no more than 7 (+/- 2) elements per group.

How to: Group document metadata into logical visual cards: Document Details, Indexing Metrics, Access Permissions.

✗ A single flat form page containing 28 continuous input fields without visual section headers.
✓ Dividing a long onboarding form into 3 step-by-step wizard tabs, each containing 4 inputs.

**Why:** Human working memory has an average capacity of 7 items. Cluttering an interface with unchunked data leads to cognitive overload and errors.

