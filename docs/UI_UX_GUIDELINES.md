# VNEXIFY Creator OS UI/UX Design Guidelines

- Version: v0.1
- Creation Date: 2026-08-06
- Status: Draft / Design System Specification
- Author: Product Manager / Lead UX Architect, VNEXIFY Creator OS

---

## Table of Contents

- [1. Design Philosophy](#1-design-philosophy)
- [2. Color System](#2-color-system)
  - [Dark Mode Palette (Default)](#dark-mode-palette-default)
  - [Light Mode Palette](#light-mode-palette)
  - [Brand \& Accent Primaries](#brand--accent-primaries)
  - [Semantic Status Colors](#semantic-status-colors)
- [3. Typography](#3-typography)
  - [Font Families](#font-families)
  - [Modular Type Scale](#modular-type-scale)
- [4. Spacing \& Grid System](#4-spacing--grid-system)
- [5. Icons](#5-icons)
- [6. Buttons](#6-buttons)
- [7. Forms \& Inputs](#7-forms--inputs)
- [8. Tables](#8-tables)
- [9. Cards](#9-cards)
- [10. Navigation Architecture](#10-navigation-architecture)
- [11. Dashboard Layout](#11-dashboard-layout)
- [12. Dark Mode Specification](#12-dark-mode-specification)
- [13. Light Mode Specification](#13-light-mode-specification)
- [14. Accessibility (a11y)](#14-accessibility-a11y)
- [15. Responsive Layout Rules](#15-responsive-layout-rules)
- [16. Animations \& Motion](#16-animations--motion)
- [17. Loading States](#17-loading-states)
- [18. Empty States](#18-empty-states)
- [19. Notifications \& Toast System](#19-notifications--toast-system)
- [20. Related Documentation Cross-References](#20-related-documentation-cross-references)

---

# 1. Design Philosophy

VNEXIFY Creator OS is an intelligent, local-first desktop workspace designed specifically for digital content creators, solopreneurs, and media desks. The user interface design is guided by four foundational design principles:

1. **Distraction-Free Flow State**: Content creation requires deep mental concentration. The interface prioritizes content above app chrome. Secondary tools, sidebars, and panels remain accessible without invading the primary creative canvas.
2. **Local-First Instantaneous Feel**: The interface MUST deliver instant visual feedback (<100ms response time). Layouts utilize optimistic rendering, smooth micro-interactions, and zero cumulative layout shifts to mirror native desktop performance.
3. **High Utility Density with Visual Hierarchy**: Creator workflows demand data-dense views (analytics, content tables, calendars) balanced with clean visual hierarchy, standardized container borders, and intentional whitespace.
4. **Modern Dark-First Aesthetics**: Designed with a sleek, dark-mode-first visual signature featuring subtle glassmorphism overlays, vibrant accent gradients, crisp borders, and high contrast typography.

> [!NOTE]
> This document is a formal **UI/UX Design Specification**. It contains design tokens, layout rules, and component state definitions. It does NOT contain React component code or CSS stylesheets.

---

# 2. Color System

The VNEXIFY Creator OS color system relies on structured design tokens defined in both HSL and Hex formats to support dynamic theme switching between Dark Mode (Default) and Light Mode.

### Dark Mode Palette (Default)
- **Surface Page Background**: `#0D0F12` (`hsl(216, 19%, 6%)`) - Deep slate black.
- **Surface Card / Container**: `#16191E` (`hsl(218, 15%, 10%)`) - Card container background.
- **Surface Elevated / Hover**: `#1F232B` (`hsl(220, 16%, 15%)`) - Active item & modal background.
- **Surface Border Default**: `#262B35` (`hsl(220, 16%, 18%)`) - Subdued container dividers.
- **Text Primary**: `#F8FAFC` (`hsl(210, 40%, 98%)`) - High-contrast body & heading text.
- **Text Secondary**: `#94A3B8` (`hsl(215, 16%, 47%)`) - Supportive metadata text.
- **Text Muted**: `#64748B` (`hsl(215, 16%, 40%)`) - Labels and disabled text.

### Light Mode Palette
- **Surface Page Background**: `#F8FAFC` (`hsl(210, 40%, 98%)`) - Off-white canvas.
- **Surface Card / Container**: `#FFFFFF` (`hsl(0, 0%, 100%)`) - Pure white cards.
- **Surface Elevated / Hover**: `#F1F5F9` (`hsl(210, 40%, 96%)`) - Hover container tint.
- **Surface Border Default**: `#E2E8F0` (`hsl(214, 32%, 91%)`) - Clean light gray borders.
- **Text Primary**: `#0F172A` (`hsl(222, 47%, 11%)`) - Deep charcoal main text.
- **Text Secondary**: `#475569` (`hsl(215, 25%, 27%)`) - Secondary body text.
- **Text Muted**: `#94A3B8` (`hsl(215, 16%, 47%)`) - Form placeholders and labels.

### Brand & Accent Primaries
- **Electric Violet (Primary)**: `#7C3AED` (`hsl(263, 84%, 61%)`) - Primary buttons, active states, focus rings.
- **Vivid Cyan (Secondary)**: `#06B6D4` (`hsl(189, 94%, 43%)`) - Interactive highlights, stats indicators.
- **Brand Gradient Accent**: `linear-gradient(135deg, #7C3AED 0%, #06B6D4 100%)` - Header highlights, primary CTA buttons.

### Semantic Status Colors
- **Success (Published / Completed)**: `#10B981` (`hsl(160, 84%, 39%)`) - Emerald green.
- **Warning (Review / Scheduled)**: `#F59E0B` (`hsl(38, 92%, 50%)`) - Amber orange.
- **Error (Failed / Overdue)**: `#EF4444` (`hsl(0, 84%, 60%)`) - Rose red.
- **Info / Neutral (Idea / Draft)**: `#0EA5E9` (`hsl(199, 89%, 48%)`) - Sky blue.

---

# 3. Typography

The typography system prioritizes legibility across dense data tables and long-form markdown editing views, following standard scales defined in [CODING_STANDARD.md](CODING_STANDARD.md).

### Font Families
- **Primary Body & UI Font**: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Monospace Code & Prompt Font**: `'JetBrains Mono', 'Fira Code', 'Courier New', monospace` (used for code blocks, AI prompt inputs, and system ID tokens).

### Modular Type Scale

| Role / Scale | Size (px / rem) | Line Height | Font Weight | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- |
| **Display Title (H1)** | `32px / 2.0rem` | `1.2` | `700 (Bold)` | `-0.02em` |
| **Page Header (H2)** | `24px / 1.5rem` | `1.3` | `600 (SemiBold)` | `-0.01em` |
| **Card Header (H3)** | `18px / 1.125rem`| `1.4` | `600 (SemiBold)` | `0.00em` |
| **Body Large** | `16px / 1.0rem` | `1.5` | `400 (Regular)` | `0.00em` |
| **Body Standard** | `14px / 0.875rem`| `1.5` | `400 (Regular)` | `0.00em` |
| **Label / Subtitle** | `12px / 0.75rem` | `1.4` | `500 (Medium)` | `0.01em` |
| **Micro / Tag** | `10px / 0.625rem`| `1.3` | `600 (SemiBold)` | `0.05em (Uppercase)` |

---

# 4. Spacing & Grid System

Layout alignment strictly adheres to a **4px base grid system**. Margins, paddings, gaps, and heights MUST use multiples of 4px.

### Spacing Tokens
- `space-3xs`: `2px`
- `space-2xs`: `4px`
- `space-xs`: `8px`
- `space-sm`: `12px`
- `space-md`: `16px`
- `space-lg`: `24px`
- `space-xl`: `32px`
- `space-2xl`: `48px`
- `space-3xl`: `64px`

### Container Padding Guidelines
- **App Workspace Outer Padding**: `24px` (`space-lg`)
- **Card Containers**: `20px` inner padding.
- **Modal Dialogs**: `24px` inner padding.
- **Table Cell Padding**: `12px 16px` (`space-sm space-md`).

---

# 5. Icons

The UI utilizes the **Lucide Icon** family (`lucide-react`) to maintain clean geometric visual consistency.

- **Stroke Width**: `2px` uniform stroke.
- **Icon Sizing Tokens**:
  - `Icon-Sm`: `16px x 16px` (Inline table buttons, badge icons).
  - `Icon-Md`: `20px x 20px` (Standard navigation, button icons).
  - `Icon-Lg`: `24px x 24px` (Header actions, section titles).
  - `Icon-Xl`: `48px x 48px` (Empty state hero graphics).
- **Alignment Rule**: Icons paired with text MUST align vertically centered with an explicit `8px` (`space-xs`) horizontal gap.

---

# 6. Buttons

Buttons communicate action hierarchy clearly through distinct visual variants and state feedback.

### Variant Hierarchy
1. **Primary Button**: Solid Electric Violet background (`#7C3AED`) or brand gradient fill, white bold text, subtle shadow. Used for single primary action per view (e.g. "+ New Content", "Run AI Prompt").
2. **Secondary Button**: Surface card fill (`#1F232B`), subtle border (`#262B35`), text primary (`#F8FAFC`). Used for supporting actions ("Save Draft", "Export").
3. **Ghost / Icon Button**: Transparent background, subtle text. Highlights on hover with soft background fill (`rgba(255,255,255,0.06)`). Used in toolbars and table rows.
4. **Destructive Button**: Solid or outlined Rose red (`#EF4444`). Used exclusively for irreversible deletion actions ("Delete Record", "Purge Trash").

### Button Interactive States
- **Default**: Base variant styling.
- **Hover**: Elevates background luminosity slightly; applies `transform: translateY(-1px)` transition.
- **Active / Pressed**: Scale down transition (`transform: scale(0.98)`).
- **Focused**: Displays high-contrast focus ring (`outline: 2px solid #7C3AED`, `outline-offset: 2px`).
- **Disabled**: Reduced opacity (`opacity: 0.4`), removes hover transforms, sets `cursor: not-allowed`.

### Standard Heights
- **Compact Button**: `32px` height, `12px` horizontal padding.
- **Standard Button**: `40px` height, `16px` horizontal padding.
- **Large Button**: `48px` height, `24px` horizontal padding.

---

# 7. Forms & Inputs

Form controls are engineered for high-speed keyboard input and clear validation states.

- **Input Container Styling**: Dark background (`#16191E`), border (`1px solid #262B35`), border-radius `6px`, text primary (`#F8FAFC`), padding `10px 14px`.
- **Focus State**: Border color transitions to Electric Violet (`#7C3AED`) with soft outer glow ring (`box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.2)`).
- **Error Validation State**: Border transitions to Rose red (`#EF4444`). Displays an inline validation message (`12px`, `#EF4444`) directly below the input container.
- **Select Dropdowns**: Styled popover menus matching card backgrounds, displaying hover highlights, search filtering input, and checkmarks on selected options.
- **Toggle Switches**: Pill-shaped toggle switches (`44px x 24px`) with smooth sliding thumb handle for boolean toggles.

---

# 8. Tables

Tables present structured data lists (Content records, Media items, Research clips) efficiently.

- **Sticky Header**: Headers remain fixed during scroll. Background `#16191E`, uppercase text typography (`11px`, weight `600`, tracking `0.05em`), muted text color (`#94A3B8`), bottom border `1px solid #262B35`.
- **Data Rows**: Height `48px`. Displays subtle hover row highlight (`rgba(255,255,255,0.02)`). Row borders use `1px solid #1F232B`.
- **Status Badges**: Rounded status pills (`border-radius: 9999px`, padding `4px 10px`, font-size `11px`):
  - `Draft`: Slate background (`rgba(100, 116, 139, 0.2)`), text `#94A3B8`.
  - `Scheduled`: Amber background (`rgba(245, 158, 11, 0.2)`), text `#F59E0B`.
  - `Published`: Emerald background (`rgba(16, 185, 129, 0.2)`), text `#10B981`.
- **Row Actions**: Action buttons (Edit, Delete, Export) remain right-aligned in the final column.

---

# 9. Cards

Cards organize contextual information into distinct visual containers.

- **Container Tokens**: Background `#16191E`, border `1px solid #262B35`, border-radius `12px`, inner padding `20px`.
- **Hover Elevation**: Interactive cards elevate with soft drop shadow (`box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4)`) and border glow (`border-color: #3B82F6`).

### Card Functional Variants
1. **KPI Metric Card**: Displays numeric statistic, percentage growth indicator, icon badge, and title label.
2. **Content Kanban Card**: Displays thumbnail preview, content title, status badge, word count, and updated date.
3. **AI Template Card**: Displays template title, target provider badge (OpenAI / Gemini / Ollama), prompt snippet, and action trigger.

---

# 10. Navigation Architecture

The application layout employs a two-tier navigation structure:

```
+-----------------------------------------------------------------------------------+
| APP TITLE BAR (Frameless Electron Header: Logo, Search Ctrl+K, Window Controls)   |
+-------------------+---------------------------------------------------------------+
| SIDEBAR NAV       | MAIN WORKSPACE CANVAS                                         |
| (Width: 240px)    |                                                               |
| - Dashboard       | +-----------------------------------------------------------+ |
| - Research        | | VIEW HEADER (Title, View Sub-Tabs, Action Buttons)       | |
| - Content         | +-----------------------------------------------------------+ |
| - AI Studio       | |                                                           | |
| - Analytics       | | PRIMARY MODULE VIEW BODY                                  | |
| - Calendar        | | (12-Column Responsive Grid Content Area)                   | |
| - Media           | |                                                           | |
| - Settings        | |                                                           | |
| - Plugins         | |                                                           | |
| - Exports         | |                                                           | |
| - Database        | |                                                           | |
| - Notifications   | |                                                           | |
| - Scheduler       | |                                                           | |
+-------------------+---------------------------------------------------------------+
```

- **Electron Title Bar**: Custom frameless window header featuring draggable drag region, app logo, quick global search shortcut trigger (`Ctrl+K` / `Cmd+K`), system health status indicator, and window controls (Minimize, Maximize, Close).
- **Primary Left Sidebar**: Vertical menu (`240px` width expanded, `64px` collapsed) listing all 13 core modules defined in [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md). Active menu items highlight with Electric Violet left accent border and elevated fill.
- **View Header Tabs**: Horizontal sub-navigation bar within module views with an animated sliding underline indicator.

---

# 11. Dashboard Layout

The main Dashboard view utilizes a 12-column responsive CSS grid with `24px` gutter gaps:

- **Top Welcome Bar (12 Cols)**: Displays creator greeting, date, quick status indicators, and primary action buttons ("+ New Content", "Run AI Prompt").
- **KPI Stat Strip (12 Cols)**: Four 3-column metric cards displaying:
  1. Active Drafts Count
  2. Scheduled Posts Count
  3. Monthly Output Velocity
  4. AI Token Utilization
- **Primary Kanban / Pipeline View (8 Cols)**: Displays active content records grouped by stage columns (`Idea`, `Research`, `Draft`, `Review`, `Scheduled`, `Published`).
- **Right Utility Panel (4 Cols)**: Displays mini publication calendar widget, local AI system status (FastAPI & Ollama status), and quick research notes.

---

# 12. Dark Mode Specification

Dark Mode is the default visual theme for VNEXIFY Creator OS:

- **Background Contrast**: Base canvas `#0D0F12`, Cards `#16191E`, Elevated Popovers `#1F232B`.
- **Border Definition**: Subdued slate borders (`#262B35`) prevent visual harshness while demarcating container bounds clearly.
- **Typography Contrast**: Primary text (`#F8FAFC`) achieves a high contrast ratio exceeding `14:1` against card backgrounds, eliminating eye strain during night writing sessions.

---

# 13. Light Mode Specification

Light Mode is fully supported for users preferring high-luminance workspace themes:

- **Background Palette**: Base canvas `#F8FAFC`, Cards `#FFFFFF`, Elevated Popovers `#F1F5F9`.
- **Border & Shadow Definition**: Soft gray borders (`#E2E8F0`) paired with subtle multi-layer drop shadows (`box-shadow: 0 1px 3px rgba(0,0,0,0.08)`).
- **Typography Contrast**: Primary text (`#0F172A`) achieves a contrast ratio exceeding `15:1` against white card containers.

---

# 14. Accessibility (a11y)

Accessibility standards ensure the desktop application is usable by everyone:

- **Color Contrast Standards**: All text elements MUST meet or exceed **WCAG 2.1 Level AA** standards (minimum `4.5:1` for normal text, `3.0:1` for large text/headings).
- **Keyboard Navigation**:
  - Full tab order navigation across all interactive inputs, buttons, and tables.
  - Visible focus ring (`2px solid #7C3AED`, `2px offset`) displayed on all focused elements.
  - Global keyboard shortcuts (`Cmd/Ctrl + 1` through `9` for main modules, `Escape` to close modals).
- **ARIA Attributes**: Interactive elements MUST supply explicit `aria-label`, `aria-expanded`, `role="button"`, `role="dialog"`, and `aria-live` attributes for screen reader compatibility.

---

# 15. Responsive Layout Rules

Designed to adapt seamlessly across desktop display sizes:

- **Compact Desktop (`<1280px` width)**: Left sidebar auto-collapses to icon-only mode (`64px`). Right utility panel stacks below the main content area or moves into a slide-over drawer.
- **Standard Desktop (`1280px - 1920px` width)**: Primary target viewport. Full 12-column grid rendering with expanded left sidebar (`240px`).
- **Ultra-Wide Desktop (`>1920px` width)**: Content canvas centers with a max-width container constraint (`1800px`), preventing extreme line-length stretching in markdown editors.

---

# 16. Animations & Motion

Motion design focuses on snappy, functional feedback rather than decorative distraction:

- **Duration Standard**: Fast micro-interactions MUST execute within `150ms` to `250ms`.
- **Easing Curve**: Standard easing curve `cubic-bezier(0.4, 0, 0.2, 1)`.
- **Animation Use Cases**:
  - **Modal / Popover Enter**: Fade and scale in (`opacity: 0 -> 1`, `transform: scale(0.96 -> 1.0)`).
  - **Sidebar Toggle**: Smooth width transition (`width: 64px <-> 240px`, `200ms`).
  - **Toast Entry**: Slide in from right margin (`transform: translateX(100% -> 0)`).

---

# 17. Loading States

To prevent jarring layout shifts during data fetching:

- **Skeleton Screen Placeholders**: Components loading data display pulsing skeleton placeholders (`@keyframes pulse`) matching the exact shape, height, and border-radius of the target element.
- **Inline Button Spinners**: Buttons executing async API operations display an embedded SVG spinner (`16px`), disabling duplicate clicks.
- **Global Linear Progress Bar**: Long-running file exports or database operations display a linear progress bar pinned to the top of the view header.

---

# 18. Empty States

Empty states guide users constructively when no records exist:

- **Container Layout**: Centered vertical flex container (`gap: 16px`) occupying the card or view body.
- **Elements Included**:
  1. Hero Icon (`48px x 48px`, color `#64748B`).
  2. Concise Header (e.g., "No Drafts Found").
  3. Supportive Description (e.g., "Get started by creating your first content draft or importing an outline.").
  4. Primary CTA Button (e.g., "+ Create New Draft").

---

# 19. Notifications & Toast System

System alerts and background job updates display via a non-intrusive toast system:

- **Toast Placement**: Stacked floating container at bottom-right viewport corner (`position: fixed`, `bottom: 24px`, `right: 24px`, `gap: 12px`, `z-index: 9999`).
- **Toast Styling**: Dark surface container (`#16191E`), border (`1px solid #262B35`), border-radius `8px`, shadow (`box-shadow: 0 10px 30px rgba(0,0,0,0.5)`).
- **Variant Indicators**:
  - `Success`: Left border accent `#10B981`, checkmark icon.
  - `Error`: Left border accent `#EF4444`, alert icon.
  - `Warning`: Left border accent `#F59E0B`, warning icon.
  - `Info`: Left border accent `#0EA5E9`, info icon.
- **Auto-Dismiss**: Toasts automatically dismiss after `4000ms`, with a manual close button (`X`) available.

---

# 20. Related Documentation Cross-References

This UI/UX Design Guideline document directly references and aligns with the following engineering documents:

- [PROJECT.md](PROJECT.md) - Project overview and baseline scope.
- [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) - Functional module definitions, MVP scope, and 13 core modules.
- [ARCHITECTURE.md](ARCHITECTURE.md) - Frontend React, Vite, and Electron container architecture.
- [TECH_STACK.md](TECH_STACK.md) - Frontend technology choices (React, TypeScript, Vite).
- [FILE_STRUCTURE.md](FILE_STRUCTURE.md) - Structure for frontend source code and design assets.
- [CODING_STANDARD.md](CODING_STANDARD.md) - Code style, typography scale rules, and component structure.
- [API_SPECIFICATION.md](API_SPECIFICATION.md) - Backend REST API request/response formats and error codes.
