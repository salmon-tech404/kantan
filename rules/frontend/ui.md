---
area: frontend
path: rules/frontend/ui.md
rules: 16
---
### UI-STA-001 · `must` · T2 needs review
**Mandatory Five-State Component Anatomy**

Every data-displaying component must explicitly implement all 5 UI states: Empty, Loading/Skeleton, Error (with retry), Success, and Interactive (Hover/Active/Disabled).

How to: Provide dedicated sub-components or branches: if (loading) <Skeleton />; if (error) <ErrorView onRetry={retry} />; if (empty) <EmptyView />.

✗ docs.map(...) directly with no check for docs.length === 0 or error states, rendering an empty white box.
✓ <DocumentList items={docs} renderEmpty={<EmptyUploadPrompt />} />

**Why:** Failing to design for empty and error states creates broken, blank interfaces when network calls fail or when new users have no data.


### UI-A11Y-001 · `must` · T1 critical
**Semantic HTML and ARIA Labeling on Interactive Elements**

Interactive elements must use semantic HTML tags (<button>, <a>, <input>) and provide explicit aria-label attributes when icons lack text labels.

How to: Use <Button size='icon' aria-label='Close Dialog'><XIcon /></Button>.

✗ <div onClick={close} className='cursor-pointer'><XIcon /></div> // Inaccessible div button
✓ <button type='button' aria-label='Close dialog' onClick={close}><XIcon /></button>

**Why:** Using <div onClick=...> prevents screen readers from announcing elements as interactive and disables keyboard activation via Space and Enter.


### UI-LAW-002 · `must` · T1 critical
**Fitts's Law: Minimum Target Size of 44x44px for Interactive Elements**

Interactive touch and click targets (buttons, icon buttons, checkboxes) must have an effective hit area of at least {{touch_target}} CSS pixels with adequate spacing.

How to: For small visual icons (16px), add padding or an invisible bounding box to ensure the clickable area reaches at least 44px (min-h-[44px] min-w-[44px]).

✗ <button className="h-4 w-4 p-0"><XIcon className="h-4 w-4" /></button> // Extremely difficult to click
✓ <button className="p-3 min-h-[44px] min-w-[44px] flex items-center justify-center"><XIcon className="h-4 w-4" /></button>

**Why:** Small, cramped targets increase acquisition time and cause accidental misclicks, particularly on mobile touchscreens or high-DPI displays.

**Parameter:** `{{touch_target}} CSS pixels`


### UI-DLG-001 · `must` · T1 critical
**Focus Trapping and ESC Key Dismissal in Modal Dialogs**

Modal dialogs must trap keyboard focus within the dialog container and dismiss immediately upon pressing the Escape key.

How to: Use Radix UI Dialog primitives (shadcn/ui Dialog) which handle focus trapping, ARIA roles, and Escape listener out of the box.

✗ Building a custom modal with a raw <div> and fixed positioning without focus trapping.
✓ <Dialog><DialogContent>{children}</DialogContent></Dialog> (using Radix primitive)

**Why:** Without focus trapping, keyboard and screen-reader users tab behind the modal into the backdrop, losing their place and rendering the application unusable.


### UI-DLG-002 · `must` · T2 needs review
**Explicit Two-Step Confirmation for Destructive Actions**

Destructive operations (e.g. deleting knowledge bases, revoking keys) must require explicit confirmation with the resource name stated, and default focus must NOT rest on the destructive button.

How to: Style the confirm button in Destructive Red. Focus the Cancel button by default. Require typing the resource name for critical bulk deletes.

✗ Using window.confirm('Are you sure?') or auto-focusing the red Delete button on modal open.
✓ <DestructiveDialog title="Delete Knowledge Base" targetName={kb.name} onConfirm={deleteKb} />

**Why:** Accidental clicks or pressing Enter immediately upon dialog open can permanently destroy user data if default focus is on the Delete action.


### UI-GEN-001 · `must_not` · T1 critical
**Strict Prohibition of Emojis in Production Interface Elements**

Emojis must not be used as interface icons, status badges, buttons, or navigation indicators in production interfaces.

How to: Use curated SVG vector icons from Lucide React (<CheckIcon />, <AlertTriangleIcon />, <TrashIcon />).

✗ <button>🗑️ Delete Item</button> or <span>⚠️ Warning</span>
✓ <Badge variant='destructive'><AlertCircle className='h-3 w-3 mr-1' /> Error</Badge>

**Why:** Emojis render inconsistently across operating systems (Apple, Windows, Android), lack scalable vector styling, and cause screen readers to announce verbose, disruptive descriptions.


### UI-PER-001 · `should` · T2 needs review
**Perceived Performance via Skeleton Loaders (Doherty Threshold)**

Content areas with predictable structure must render layout-matching Skeleton Shimmer loaders instead of spinning loaders during data retrieval.

How to: Render <Skeleton className='h-4 w-full' /> matching the typography and grid layout of arriving cards or tables.

✗ A centered spinning spinner icon in the middle of a blank white screen.
✓ <div className='space-y-2'><Skeleton className='h-4 w-3/4' /><Skeleton className='h-4 w-1/2' /></div>

**Why:** Skeleton screens reduce perceived loading latency by previewing the arriving content layout, satisfying the Doherty Threshold for user cognitive engagement.


### UI-SEL-001 · `must` · T2 needs review
**One Non-Color Cue for Selected State — No Stacked Signals**

A selected option (card, chip, segmented choice, list row) must be distinguishable by exactly one non-color cue in addition to color, with at least 3:1 contrast against adjacent colors, and must expose its state to assistive tech (aria-pressed / aria-checked / aria-selected). Do not stack redundant signals (tinted background + colored border + checkmark) on the same element.

How to: Default cue = thicker outline in the brand color via ring/outline (unselected: 1px neutral border; selected: brand border + 1px ring = 2px). A checkmark is an acceptable alternative cue only when the outline cannot change (e.g. dense lists) — then do not also tint the background.

✗ className={selected ? "border-brand bg-brand/10 ring-1 ring-brand" : "border-line"} plus <CheckIcon /> inside the card // three signals for one state
✗ className={selected ? "border-brand" : "border-line"} with the same 1px width // color is the only cue (fails WCAG 1.4.1)
✓ className={selected ? "border-brand ring-1 ring-brand" : "border-line ring-1 ring-transparent"} aria-pressed={selected}

**Why:** WCAG 1.4.1 forbids color as the only cue and 1.4.11 requires 3:1 contrast for state indicators; beyond that, every extra signal adds visual weight without adding information, making option grids look noisy and the selected item harder to scan.


### UI-STB-001 · `must` · T2 needs review
**Interactions Must Not Shift Unrelated Layout**

Hovering, selecting or toggling an element must not resize it or move content around it. Text that appears conditionally (hints, AI rationales, validation messages, samples) must live in space reserved for it, and state styles must not change box dimensions.

How to: Keep helper/rationale lines always rendered in a fixed slot (show the field description when there is no specific message); clamp dynamic text to a fixed number of lines; switch border emphasis with ring/outline/box-shadow, never with border-width or padding changes.

✗ {isSuggested && <p>{reason}</p>} above an option grid — the grid jumps when the user picks another option
✓ <p className="min-h-[1lh]">{reason ?? description}</p> rendered regardless of the current selection

**Why:** Content that jumps under the cursor breaks the user's spatial model and causes mis-clicks; web.dev treats layout shift as a core UX failure and advises reserving space up front rather than inserting content after the fact.


### DS-BTN-001 · `must` · T1 may chan
**Button Loading State and Disabled Accessibility**

While an asynchronous action is executing, buttons must display an inline spinner, maintain their exact layout width to prevent content reflow, and have aria-busy='true' and disabled attributes set.


### DS-BTN-003 · `must` · T2 review nhac
**Single Primary Button Per Visual Area**

Each view or modal card must present at most one primary solid-color call-to-action button to eliminate visual competition and cognitive friction.


### DS-INP-001 · `must` · T1 may chan
**Explicit Label and Accessible Error Association**

Every form input must be linked to an explicit <label htmlFor={id}> and point to its validation error message via aria-describedby when invalid.


### DS-INP-002 · `must` · T1 may chan
**Persistent Focus Rings**

Input focus rings must never be removed with outline-none without replacing with an accessible high-contrast focus ring (e.g. project focus-ring token).

**Parameter:** `project focus-ring token`


### DS-TST-001 · `must` · T1 may chan
**Accessible Toast Notifications with Polite Live Regions**

Non-critical status notifications must use aria-live='polite' and role='status'; critical errors must use role='alert'. Auto-dismissing toasts must pause on hover and keyboard focus.


### FE-FRM-001 · `must` · T2 needs review
**React Hook Form Combined with Zod Schema Resolver**

All forms must be managed with React Hook Form and validated against a shared Zod schema using @hookform/resolvers/zod.

How to: useForm({ resolver: zodResolver(schema) }). Disable submit button while formState.isSubmitting is true.

✗ Managing 10 separate useState hooks for form inputs with manual regex checks in an onSubmit handler.
✓ const { register, handleSubmit, formState } = useForm({ resolver: zodResolver(loginSchema) });

**Why:** Manual useState form management causes unnecessary re-renders on every keystroke and leads to duplicate validation logic between client and server.


### FE-ACT-001 · `must` · T2 needs review
**Server Actions Mutation Lifecycle with useActionState and useOptimistic**

Mutations executed via Next.js Server Actions must be managed in the UI using React 19's useActionState and useOptimistic to provide immediate user feedback and progressive enhancement.

How to: Define 'use server' actions that return typed state { success, error, data }. In the client component, bind the action using const [state, formAction, isPending] = useActionState(serverAction, initialState).

✗ const [loading, setLoading] = useState(false); const handleSubmit = async () => { setLoading(true); await serverAction(); setLoading(false); };
✓ const [state, formAction, isPending] = useActionState(deleteDocumentAction, null); const [optimisticDocs, setOptimistic] = useOptimistic(docs, updateFn);

**Why:** Manual async state tracking with multiple useState and useEffect hooks creates race conditions and fails to leverage React 19 concurrent transition boundaries.

