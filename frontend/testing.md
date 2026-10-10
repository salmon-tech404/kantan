---
area: frontend
path: frontend/testing.md
rules: 4
---
### TEST-E2E-001 · `must` · T2 needs review
**Page Object Model (POM) for E2E Test Isolation**

Playwright end-to-end tests must encapsulate web page locators and user interactions within Page Object Model (POM) classes.

How to: Create LoginPage, ChatPage, and DocumentPage classes with semantic action methods (e.g. login(email, pass)).

✗ await page.click('div.flex > div > input.sc-12'); await page.click('button.bg-blue-500');
✓ await chatPage.sendMessage('What is the policy?'); expect(await chatPage.getAnswer()).toContain('Policy');

**Why:** Directly hardcoding CSS selectors across dozens of test specs causes widespread test suite breakages whenever UI class names or layouts change.


### TEST-E2E-003 · `should` · T2 needs review
**Visual Regression Testing for Critical Layouts**

High-traffic or layout-sensitive pages (landing page, chat interface, document viewer) must have a Playwright screenshot-comparison test asserting the rendered page matches an approved baseline image.

How to: Generate baselines in the same environment CI runs in (e.g. a Docker container matching the CI OS/browser) to avoid cross-platform pixel diffs causing false failures.

✗ Relying solely on `expect(locator).toBeVisible()` checks for a page redesign with no screenshot baseline.
✓ await page.goto('/dashboard'); await expect(page).toHaveScreenshot('dashboard.png');

**Why:** Functional assertions (element present, correct text) do not catch unintended CSS/layout regressions — a broken grid or overlapping element can pass every functional check while looking visibly broken to real users.


### TEST-E2E-004 · `should` · T2 needs review
**Reuse Authenticated Session State via storageState**

E2E test suites requiring an authenticated session must generate the logged-in browser storage state once (via a setup project/script) and reuse it across tests, rather than performing the UI login flow in every test.

How to: Write a one-time setup script that logs in and calls `context.storageState({ path: 'logged_in_state.json' })`, then reference that file via the `storageState` project option in playwright.config.

✗ test('view dashboard', async ({ page }) => { await page.goto('/login'); await page.fill('#email', ...); await page.fill('#password', ...); await page.click('#submit'); /* repeated in every test file *
✓ await context.storageState({ path: 'logged_in_state.json' }); // generated once; playwright.config.ts references it as `use: { storageState: 'logged_in_state.json' }`

**Why:** Repeating the full login UI flow (navigate, type credentials, submit) in every single test adds up to significant, unnecessary suite runtime and makes every test fragile to login-page changes.


### TEST-E2E-005 · `must` · T1 critical
**Automated Accessibility Scanning with axe-core**

Critical user-facing pages must have an automated Playwright test running an axe-core accessibility scan (via @axe-core/playwright) and asserting zero violations against the project's target WCAG level.

How to: Install @axe-core/playwright, run `new AxeBuilder({ page }).withTags([...]).analyze()` against each critical page, and fail the test if `results.violations.length > 0`. Wire this scan into CI so it runs on every push.

✗ Shipping a redesigned page with only visual/functional tests and no automated accessibility scan.
✓ const results = await new AxeBuilder({ page }).withTags(['wcag2aa', 'section508']).analyze(); expect(results.violations).toEqual([]);

**Why:** Accessibility defects (missing labels, insufficient contrast, broken ARIA roles) are not caught by functional or visual tests and routinely go unnoticed until a legal complaint or a real assistive-technology user is bloc

