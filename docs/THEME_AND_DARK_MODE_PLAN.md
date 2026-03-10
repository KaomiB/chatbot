# Plan: Toggleable dark mode and color schemes (Streamlit app)

## Goal

1. **Dark mode** — Users can switch to a dark theme (and back to light).
2. **Optional multiple color schemes** — e.g. “Heal&Save” (current), “Ocean”, “Forest” that users can pick.

Scope: Streamlit app only (HSA Topics, Task Breaker, Trade-Off Tool, AI Chat). “Mainpage” here means the main Streamlit entry (Explore HSA by topic) and the rest of the app.

---

## Part 1: Dark mode (Streamlit-native)

### How Streamlit handles light/dark

- In **`.streamlit/config.toml`** you can set `[theme]` and optionally **`[theme.light]`** and **`[theme.dark]`** with different colors for each.
- Users switch theme via the app’s **Settings** (☰ → Settings) or the **“Use device theme” / “Light” / “Dark”** control in the Streamlit Cloud UI. No extra toggle in our code is required for basic light/dark.

### What to do

1. **Define dark theme in config**
   - Add a **`[theme.dark]`** (and **`[theme.dark.sidebar]`**) section in `.streamlit/config.toml`.
   - Use dark backgrounds (e.g. `#1A2028`, `#2D3748`), light text (e.g. `#E2E8F0`), and adjust primary/accent so they’re visible and on-brand on dark (e.g. keep `#FFB8D1` or slightly brighter, ensure contrast).
   - Keep existing **`[theme]`** / **`[theme.sidebar]`** (and optional **`[theme.light]`**) for the current light look.

2. **Custom CSS that we inject**
   - **HSA_Topics.py:** “Explore” tag (`.m-tag`) and “HSA by Topic” (`.m-title`), plus sidebar “Go to topic” button (Blush `#FFB8D1`).
   - **Task Breaker:** Sticky-note block (yellow background) and any other custom styles.
   - For dark mode these need to stay readable:
     - **Option A:** Use **`prefers-color-scheme: dark`** in a media query and override colors only when the user’s device prefers dark (matches “Use device theme”).
     - **Option B:** If we add an in-app theme toggle (see below), we can add a class to the body (e.g. `data-theme="dark"`) and scope overrides with `[data-theme="dark"] .m-title { ... }`.
   - Decide: rely on device preference (A) or in-app toggle (B). In-app toggle requires storing choice in `session_state` and injecting a small script + CSS that sets `data-theme` and applies dark overrides for our custom components.

3. **Sticky note (Task Breaker)**
   - Light: current yellow `#FDFBD4` and left border.
   - Dark: use a darker “sticky” (e.g. dark gold/amber background and light text) in the dark theme CSS so it doesn’t clash with the dark sidebar.

---

## Part 2: In-app theme toggle (optional)

If we want a **toggle inside the app** (e.g. in the sidebar) instead of relying only on Streamlit’s Settings:

1. **Storage**
   - Store choice in **`st.session_state.theme`** (e.g. `"light"` | `"dark"`).
   - Optional: persist via **`st.query_params`** or **localStorage** (would need a small JS snippet) so the choice survives refresh; otherwise session-only is fine.

2. **UI**
   - Sidebar: e.g. radio or selectbox “Theme: Light / Dark” (and optionally “Use device setting” if we read `prefers-color-scheme` via JS).
   - On change: update `st.session_state.theme` and **rerun**.

3. **Applying the choice**
   - Streamlit’s theme (light/dark) is controlled by the host (Streamlit Cloud / Settings), not by our Python. So we **cannot** switch Streamlit’s built-in light/dark from Python.
   - What we **can** do: inject CSS that **overrides** colors so the app *looks* dark (or light) regardless of Streamlit’s setting. That means:
     - Inject a large block of CSS that sets backgrounds, text, sidebar, inputs, etc. for “our” dark mode.
     - Use a body class or `data-theme="dark"` and scope all overrides under it.
   - Downside: we must maintain a full set of overrides for every element we care about and keep them in sync with Streamlit’s DOM (selectors like `[data-testid="stSidebar"]`, etc.).

**Recommendation:** Prefer **Streamlit’s built-in light/dark** (config + Settings). Add an in-app toggle only if we need to force a look that differs from the user’s Streamlit Settings (e.g. “always Heal&Save dark” vs “always Heal&Save light”).

---

## Part 3: Multiple color schemes (e.g. Heal&Save, Ocean, Forest)

Streamlit **does not** support loading different `config.toml` themes at runtime. So multiple schemes = **custom CSS overrides** driven by app state.

### Approach

1. **Define schemes in code**
   - Create a small **theme module** (e.g. `theme_schemes.py`) that holds 2–3 named schemes. Each scheme is a dict or dataclass of CSS variable names and values, or a full CSS string (e.g. `:root { --bg: ...; --text: ...; }` and overrides for Streamlit selectors).
   - Example keys: `primaryColor`, `backgroundColor`, `secondaryBackgroundColor`, `textColor`, `sidebarBg`, `accentSticky`, etc., mapped to CSS custom properties or to concrete selectors we override.

2. **Apply a scheme**
   - Store **`st.session_state.color_scheme`** (e.g. `"heal&save"` | `"ocean"` | `"forest"`).
   - On every run, if we use “scheme-driven” styling, inject **one** `<style>` block that:
     - Sets CSS variables and/or
     - Overrides Streamlit’s main areas (main container, sidebar, headers, buttons, inputs) using the selected scheme’s colors.
   - Streamlit’s own theme (from config) stays as the “base” (e.g. light); our CSS overrides it for the chosen scheme. For a dark variant of a scheme we’d either:
     - Add a “Dark” variant per scheme (e.g. “Heal&Save Dark”) and define dark colors in that scheme, or
     - Combine “color scheme” with “light/dark” (scheme + theme) and have 2×N combinations in the theme module.

3. **UI**
   - Sidebar (or a shared component): dropdown or pills “Color scheme: Heal&Save | Ocean | Forest”.
   - On change: set `st.session_state.color_scheme`, then **rerun** so the new CSS is injected.

4. **Where to inject**
   - **Option A:** One shared place (e.g. a small “theme loader” snippet in `HSA_Topics.py` and in each page) that reads `session_state.color_scheme` and injects the corresponding CSS.
   - **Option B:** A single **`layout.py`** or **`theme.py`** that every page calls at the top (e.g. `theme.apply_scheme()`) so we don’t duplicate the injection logic.

5. **Config vs CSS**
   - Keep **`.streamlit/config.toml`** as the default (e.g. Heal&Save light and dark). Our “schemes” can override that default when the user picks “Ocean” or “Forest” so we don’t need to change config per scheme.

---

## Part 4: “Mainpage” (clarification)

If “mainpage” means a **separate static or non-Streamlit landing page** (e.g. marketing site, docs):

- That would be a different codebase (HTML/CSS/JS or another framework). The plan above does **not** cover that.
- If “mainpage” is only the **Streamlit main page** (Explore HSA by topic), then it’s already covered: same config + custom CSS (`.m-tag`, `.m-title`, etc.) and, if we add schemes, the same theme module and injector.

---

## Suggested order of work

1. **Dark mode**
   - Add **`[theme.dark]`** (and **`[theme.dark.sidebar]`**) to **`.streamlit/config.toml`** with a full dark palette.
   - Add dark-mode overrides for **custom components** (`.m-tag`, `.m-title`, Blush button, sticky note) using **`prefers-color-scheme: dark`** (and optionally a body class if we add an in-app toggle later).
   - Test: switch theme in Streamlit Settings (or device theme) and confirm main page, sidebar, Task Breaker sticky note, and AI Chat all look correct.

2. **Optional in-app theme toggle**
   - Only if we want to force light/dark regardless of Streamlit Settings: add sidebar control, `session_state.theme`, and CSS injection with `[data-theme="dark"]` (and maybe a tiny script to set `data-theme` from session_state).

3. **Multiple color schemes**
   - Add **`theme_schemes.py`** with 2–3 schemes (e.g. Heal&Save, Ocean, Forest) as color dicts or CSS strings.
   - Add a shared “apply scheme” helper that injects `<style>` from the chosen scheme.
   - Add sidebar selector on the main page (and optionally on others) and `session_state.color_scheme`.
   - Ensure each scheme has a light (and optionally dark) variant so it works with Streamlit’s light/dark toggle.

---

## Files to touch (summary)

| Item | File(s) |
|------|--------|
| Dark theme config | `.streamlit/config.toml` — add `[theme.dark]`, `[theme.dark.sidebar]` |
| Custom components dark | `HSA_Topics.py`, `pages/1_Task_Breaker.py` — extend `<style>` with `prefers-color-scheme: dark` or `[data-theme="dark"]` overrides |
| Theme schemes (if we do multiple) | New `theme_schemes.py`; optional `theme.py` with `apply_scheme()` |
| Scheme selector UI | Sidebar in `HSA_Topics.py` (and optionally other pages) |
| Sticky note dark | `pages/1_Task_Breaker.py` — dark variant in the same or extended `<style>` block |

---

## References

- Streamlit theming: [Theming](https://docs.streamlit.io/develop/concepts/configuration/theming), [Customize colors and borders](https://docs.streamlit.io/develop/concepts/configuration/theming-customize-colors-and-borders).
- Config structure: `[theme]`, `[theme.light]`, `[theme.dark]`, `[theme.sidebar]`, etc. in `config.toml`.
