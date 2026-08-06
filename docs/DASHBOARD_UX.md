# VNEXIFY Creator OS Dashboard UX Architecture

- Version: v0.1
- Creation Date: 2026-08-06
- Status: Draft / UX Architecture Specification
- Author: Lead Product Designer & UX Architect, VNEXIFY Creator OS

---

## Table of Contents

- [1. Executive Overview \& Design Philosophy](#1-executive-overview--design-philosophy)
- [2. Navigation Hierarchy](#2-navigation-hierarchy)
- [3. Spacing Rules \& Layout Grid](#3-spacing-rules--layout-grid)
- [4. Component Hierarchy](#4-component-hierarchy)
- [5. Master ASCII Wireframes](#5-master-ascii-wireframes)
  - [Overall Desktop App Window Layout](#overall-desktop-app-window-layout)
  - [Main Workspace Breakdown](#main-workspace-breakdown)
  - [Right Information Panel Breakdown](#right-information-panel-breakdown)
- [6. Primary Structural Regions](#6-primary-structural-regions)
  - [1. Window Layout Frame](#1-window-layout-frame)
  - [2. Header (App Window Bar)](#2-header-app-window-bar)
  - [3. Left Sidebar (Module Navigation)](#3-left-sidebar-module-navigation)
  - [4. Main Workspace (Primary Canvas)](#4-main-workspace-primary-canvas)
  - [5. Right Information Panel (Utility Drawer)](#5-right-information-panel-utility-drawer)
  - [6. Bottom Status Bar (System Footer)](#6-bottom-status-bar-system-footer)
- [7. Detailed Dashboard Sections Specification](#7-detailed-dashboard-sections-specification)
  - [Section 1: Today's Tasks](#section-1-todays-tasks)
  - [Section 2: AI Assistant Status](#section-2-ai-assistant-status)
  - [Section 3: Recent Projects](#section-3-recent-projects)
  - [Section 4: Research Queue](#section-4-research-queue)
  - [Section 5: Content Pipeline](#section-5-content-pipeline)
  - [Section 6: Publishing Queue](#section-6-publishing-queue)
  - [Section 7: Calendar Preview](#section-7-calendar-preview)
  - [Section 8: Quick Actions](#section-8-quick-actions)
  - [Section 9: System Health](#section-9-system-health)
  - [Section 10: Backend Status](#section-10-backend-status)
- [8. Related Documentation Cross-References](#8-related-documentation-cross-references)

---

# 1. Executive Overview & Design Philosophy

VNEXIFY Creator OS is an intelligent, local-first desktop operating workspace crafted specifically for digital content creators, solopreneurs, and independent media desks. The Dashboard serves as the central command bridge where creators start their workday, track creative velocity, inspect multi-model AI availability, and manage content lifecycles.

The UX design architecture enforces seven core design tenets (aligned with [UI_UX_GUIDELINES.md](UI_UX_GUIDELINES.md)):

1. **Clean**: Uncluttered visual interface with crisp container boundaries, high-contrast typography, and explicit visual separation between workspace regions.
2. **Minimal**: Zero unnecessary UI chrome. Tools, metadata, and controls emerge contextually without cluttering the primary creative canvas.
3. **Professional**: Engineering-grade desktop ergonomics with standardized 4px grid spacing, consistent status indicators, and keyboard-first navigation shortcuts.
4. **AI-First**: Dedicated real-time indicators for multi-model AI availability (ChatGPT, Gemini, Ollama) and prompt execution shortcuts embedded directly into the daily workflow.
5. **Productivity-Focused**: Immediate visibility into active content stages, editorial deadlines, quick capture notes, and automated background task results.
6. **Dark Theme First**: Deep slate canvas (`#0D0F12`), container cards (`#16191E`), and electric violet accents (`#7C3AED`) designed to reduce eye strain during extended creation sessions.
7. **Responsive Layout**: Fluid grid architecture that adapts seamlessly across compact desktop (`<1280px`), standard desktop (`1280px - 1920px`), and ultra-wide displays (`>1920px`).

> [!NOTE]
> This document is a formal **UX Architecture & Wireframe Specification**. It defines spatial layouts, navigation trees, wireframes, and component interaction behaviors. It contains NO React component code, HTML markup, CSS stylesheets, or Tailwind utility classes.

---

# 2. Navigation Hierarchy

The application employs a 4-level structural navigation hierarchy:

```
[LEVEL 0: APP WINDOW CONTAINER] (Frameless Electron Window, Window Controls, Drag Handle)
   │
   ├── [LEVEL 1: GLOBAL HEADER]
   │      ├── App Logo & Workspace Title
   │      ├── Global Quick Search Input (Cmd+K / Ctrl+K)
   │      ├── Quick Action Buttons (+ New Draft, Run AI Prompt)
   │      └── System Health Status Badge (FastAPI & Ollama Status)
   │
   ├── [LEVEL 2: PRIMARY LEFT SIDEBAR] (Module Navigation)
   │      ├── 01. Dashboard (Active View)
   │      ├── 02. Research
   │      ├── 03. Content
   │      ├── 04. AI Studio
   │      ├── 05. Analytics
   │      ├── 06. Calendar
   │      ├── 07. Media
   │      ├── 08. Settings
   │      ├── 09. Plugins
   │      ├── 10. Exports
   │      ├── 11. Database
   │      ├── 12. Notifications
   │      └── 13. Scheduler
   │
   ├── [LEVEL 3: MAIN WORKSPACE CANVAS] (12-Column Responsive Layout)
   │      ├── Header Welcome Banner & Quick Action Cards
   │      ├── Metric KPI Stat Cards Strip (4 Columns)
   │      ├── Primary Content Pipeline Board / Recent Projects (8 Columns)
   │      └── Task & Research Queue Canvas (4 Columns)
   │
   └── [LEVEL 4: UTILITY RIGHT PANEL & STATUS BAR]
          ├── Right Utility Panel (AI Status, Calendar Preview, Publishing Queue)
          └── Bottom Status Bar (Backend status, Ollama status, DB state, Memory)
```

---

# 3. Spacing Rules & Layout Grid

### Spacing Scale (4px Base Grid)
Layout dimensions, margins, paddings, and container gaps MUST adhere strictly to the 4px base spacing scale defined in [UI_UX_GUIDELINES.md](UI_UX_GUIDELINES.md):

- `space-3xs`: `2px` (Fine borders, micro badges)
- `space-2xs`: `4px` (Tight inline spacing)
- `space-xs` : `8px` (Icon-to-text gaps, small padding)
- `space-sm` : `12px` (Input padding, list item vertical gaps)
- `space-md` : `16px` (Standard card padding, component gaps)
- `space-lg` : `24px` (Main section gutters, container margins)
- `space-xl` : `32px` (Section dividers)
- `space-2xl`: `48px` (Major region spacing)

### Layout Grid Specifications
- **Grid Architecture**: 12-column responsive CSS grid container.
- **Gutter Width**: `24px` (`space-lg`) between major grid columns.
- **Row Gap**: `24px` (`space-lg`) between vertical section rows.
- **Sidebar Width**: `240px` expanded, `64px` collapsed.
- **Right Utility Panel Width**: `320px` expanded, auto-docked in compact view.
- **Header Height**: `48px` fixed.
- **Status Bar Height**: `28px` fixed.

---

# 4. Component Hierarchy

```
Dashboard View Component Tree
├── AppWindowFrame
│   ├── FramelessTitleBar
│   │   ├── AppLogo & TitleLabel
│   │   ├── GlobalSearchCommandBar (Ctrl+K)
│   │   ├── SystemHealthQuickBadge
│   │   └── WindowControlButtons (Min, Max, Close)
│   ├── MainLayoutContainer
│   │   ├── NavigationSidebar (Left, 240px)
│   │   │   ├── UserProfileWidget
│   │   │   ├── ModuleNavigationList (13 Core Modules)
│   │   │   └── SidebarCollapseToggle
│   │   ├── MainWorkspaceCanvas (Center, 8-12 Columns)
│   │   │   ├── WelcomeHeaderBanner
│   │   │   ├── QuickActionsBar
│   │   │   ├── MetricKpiStrip (4 Stat Cards)
   │   │   ├── ContentPipelineKanbanBoard
   │   │   ├── RecentProjectsList
   │   │   └── TodaysTasksWidget
   │   └── RightInformationPanel (Right, 320px)
   │       ├── AiAssistantStatusWidget
   │       ├── ResearchQueueWidget
   │       ├── PublishingQueueWidget
   │       └── CalendarPreviewWidget
   └── SystemStatusBar (Bottom, 28px)
       ├── BackendConnectionStatusIndicator
       ├── OllamaModelStatusIndicator
       ├── DatabaseStateIndicator
       ├── ActiveTaskSpinner
       └── SystemMemoryUtilizationMeter
```

---

# 5. Master ASCII Wireframes

### Overall Desktop App Window Layout

```text
+--------------------------------------------------------------------------------------------------------------------+
| [V] VNEXIFY Creator OS  |  [ Search Workspace (Ctrl+K) ]  |  [ 🟢 FastAPI OK ]  [ ⚡ Ollama Ready ]  | [_] [□] [X] |
+-------------------------+---------------------------------+------------------------------------------+-------------+
| SIDEBAR (240px) | MAIN WORKSPACE CANVAS (8 Cols)                    | RIGHT INFORMATION PANEL (320px)          |
|-----------------|---------------------------------------------------|------------------------------------------|
| [≡] Workspace   | WELCOME BANNER                                    | AI ASSISTANT STATUS                      |
|                 | Hello Creator! You have 3 posts due today.        | Provider: Ollama (Local)                 |
| [D] Dashboard * | [+ New Draft]  [🤖 Run AI Prompt]  [📤 Export]    | Active Model: llama3:8b (Ready)         |
| [R] Research    |---------------------------------------------------| Memory: 4.2 GB RAM                       |
| [C] Content     | METRIC KPI STRIP                                  | [ Switch Model ]  [ Test Connection ]    |
| [A] AI Studio   | +---------------+ +---------------+ +-----------+ |------------------------------------------|
| [M] Media       | | Active Drafts | | Scheduled     | | Monthly   | | TODAY'S TASKS                            |
| [Y] Analytics   | |     14        | |     4         | | Velocity  | | [x] Review newsletter outline             |
| [L] Calendar    | | +2 this week  | | Next: 4:00 PM | | 28 Posts  | | [ ] Draft YouTube video script           |
| [E] Exports     | +---------------+ +---------------+ +-----------+ | [ ] Approve podcast thumbnail graphics   |
| [P] Plugins     |---------------------------------------------------|------------------------------------------|
| [S] Settings    | CONTENT PIPELINE (Kanban Stage Board)             | RESEARCH QUEUE                           |
| [B] Database    | +----------+ +----------+ +----------+ +--------+ | * Local-First AI Architecture            |
| [N] Notifs      | | IDEA (3) | | DRAFT(4) | | REVIW(2) | | SCHED  | | * Video editing workflow trends          |
| [K] Scheduler   | |----------| |----------| |----------| |--------| | * SQLite WAL mode performance benchmarks |
|                 | | AI Tools | | Local OS | | Script A | | Post B | |------------------------------------------|
|                 | | Video X  | | Blog Z   | | Recap Y  | | News C | | CALENDAR PREVIEW (August 2026)          |
|                 | +----------+ +----------+ +----------+ +--------+ | S  M  T  W  T  F  S                      |
|                 |---------------------------------------------------| 2  3  4  5  6* 7  8                      |
|                 | RECENT PROJECTS                                   | Next: "AI Tools Overview" @ 4:00 PM      |
|                 | * Building Local-First Desktop Systems (Draft)    |------------------------------------------|
|                 | * Solopreneur Content Operations Guide (Review)   | PUBLISHING QUEUE                         |
|                 | * Weekly Creator Tech Wrap-Up #42 (Published)     | [Substack] Weekly Tech Recap (4:00 PM)   |
|                 |                                                   | [YouTube] Local AI Deep Dive (Tomorrow)  |
+-----------------+---------------------------------------------------+------------------------------------------+
| 🟢 Backend: 127.0.0.1:8000 (v0.1) | ⚡ Ollama: Active | 💾 DB: 4.2 MB | ⏱️ IPC: 2ms | 🧠 RAM: 184 MB | 🔔 0 Alerts |
+--------------------------------------------------------------------------------------------------------------------+
```

---

### Main Workspace Breakdown

```text
+--------------------------------------------------------------------------------------------------+
| WELCOME & QUICK ACTIONS BANNER                                                                   |
| Welcome back, Creator!  |  Current Workspace: Main Studio  |  Today: Thursday, Aug 6, 2026         |
| [+ Create New Content]   [🤖 Open AI Prompt Studio]   [📥 Import Research Clip]   [📊 Analytics] |
+--------------------------------------------------------------------------------------------------+
| METRIC KPI STAT CARDS                                                                            |
| +---------------------+ +---------------------+ +---------------------+ +--------------------+ |
| | ACTIVE DRAFT PIPELINE| | UPCOMING SCHEDULED | | MONTHLY VELOCITY   | | AI TOKEN USAGE     | |
| | 14 Items            | | 4 Posts Pending     | | 28 Published Posts| | 142.5k Tokens      | |
| | ^ 12% vs last week  | | Next: Today @ 4:00P | | ^ 18% vs target   | | 85% Local (Ollama) | |
| +---------------------+ +---------------------+ +---------------------+ +--------------------+ |
+--------------------------------------------------------------------------------------------------+
| CONTENT PIPELINE STAGE BOARD (Drag & Drop Kanban Columns)                                        |
| +-------------------+ +-------------------+ +-------------------+ +------------------------+ |
| | IDEA STAGE (3)    | | DRAFT STAGE (4)   | | REVIEW STAGE (2)  | | SCHEDULED STAGE (4)    | |
| |-------------------| |-------------------| |-------------------| |------------------------| |
| | [Card: AI Tools]  | | [Card: Local OS]  | | [Card: Script A]  | | [Card: Post B]         | |
| | Tag: Tech | 800w  | | Tag: Eng | 1,450w | | Tag: Video | 2,100w| | Tag: News | 650w      | |
| |-------------------| |-------------------| |-------------------| |------------------------| |
| | [Card: Video X]   | | [Card: Blog Z]    | | [Card: Recap Y]   | | [Card: Newsletter C]   | |
| +-------------------+ +-------------------+ +-------------------+ +------------------------+ |
+--------------------------------------------------------------------------------------------------+
| RECENT PROJECTS LIST                                                                             |
| Title                                 | Type        | Status     | Word Count | Last Updated     |
| -------------------------------------+-------------+------------+------------+----------------- |
| Building Local-First Desktop Systems  | Article     | Draft      | 1,450 w    | 12 mins ago      |
| Solopreneur Content Operations Guide  | Newsletter  | Review     | 2,100 w    | 2 hours ago      |
| Creator OS Architecture Overview      | Video Script| Scheduled  | 3,400 w    | Yesterday        |
+--------------------------------------------------------------------------------------------------+
```

---

### Right Information Panel Breakdown

```text
+----------------------------------------------------------+
| RIGHT INFORMATION PANEL (320px Fixed Utility Container)  |
+----------------------------------------------------------+
| AI ASSISTANT STATUS                                      |
| Status: 🟢 Connected & Ready                             |
| Default Provider: Ollama (Local Loopback)                |
| Primary Model: llama3:8b-instruct                        |
| Secondary Provider: OpenAI (ChatGPT-4o)                  |
| Active Context Window: 8,192 Tokens                      |
| [ ⚙️ Configure AI ]   [ 🔄 Refresh Models ]              |
+----------------------------------------------------------+
| TODAY'S TASKS (Interactive Checkbox List)                |
| [x] Finalize outline for Local-First AI article          |
| [ ] Draft script for YouTube Episode #14                 |
| [ ] Review thumbnail graphics in Media Library           |
| [ ] Schedule Substack newsletter broadcast               |
| [+ Add Quick Task... ]                                   |
+----------------------------------------------------------+
| RESEARCH QUEUE (Quick Reference Cards)                   |
| 📌 SQLite WAL Mode Performance Benchmarks                |
|    Saved from: github.com/sqlite/benchmarks              |
| 📌 Modern Desktop Window Management Design Patterns      |
|    Saved from: uxdesign.cc/desktop-patterns              |
| [+ Clip Web Reference ]                                  |
+----------------------------------------------------------+
| PUBLISHING QUEUE & CALENDAR PREVIEW                      |
| AUGUST 2026                                              |
| Su  Mo  Tu  We  Th  Fr  Sa                               |
|  2   3   4   5   6*  7   8                               |
|                                                          |
| Upcoming Broadcasts:                                     |
| * Today @ 4:00 PM  | Substack: Creator OS Deep Dive      |
| * Tomorrow @ 10:00A| YouTube: Local AI Setup Guide       |
+----------------------------------------------------------+
```

---

# 6. Primary Structural Regions

The dashboard layout is divided into 6 distinct structural regions:

### 1. Window Layout Frame
- **Purpose**: Provides the top-level structural grid and viewport boundary for the entire Electron desktop window.
- **User Interaction**: Resizing the window triggers responsive layout adaptation (collapsing sidebars or repositioning cards).
- **Future Features**: Multi-window tear-out support (detaching the editor or AI studio into separate native windows).

### 2. Header (App Window Bar)
- **Purpose**: Houses custom frameless window controls, application title, global search bar (`Ctrl+K`), and system status indicators.
- **User Interaction**: Clicking window control buttons (Minimize, Maximize, Close); clicking the global search input opens the command palette; dragging the header moves the desktop window.
- **Future Features**: Quick workspace switcher dropdown and active profile selector.

### 3. Left Sidebar (Module Navigation)
- **Purpose**: Displays primary vertical navigation links across all 13 core OS modules specified in [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md).
- **User Interaction**: Clicking a navigation item switches the active workspace view; clicking the bottom collapse button toggles sidebar width between `240px` and `64px`.
- **Future Features**: Drag-and-drop module reordering and customizable favorite shortcuts.

### 4. Main Workspace (Primary Canvas)
- **Purpose**: Serves as the primary operational canvas housing the welcome banner, metric cards, content pipeline kanban board, and recent projects list.
- **User Interaction**: Dragging cards across kanban columns transitions content lifecycle states (`Idea` -> `Draft` -> `Review` -> `Scheduled`); clicking project rows opens the editor.
- **Future Features**: Customizable widget grid with drag-and-drop layout rearrangement.

### 5. Right Information Panel (Utility Drawer)
- **Purpose**: Houses persistent utility modules for AI assistant status, daily task checklists, research queues, and calendar previews.
- **User Interaction**: Checking off tasks, clicking research clips to insert into active drafts, toggling AI provider models.
- **Future Features**: Collapsible slide-over drawer mode for compact screens.

### 6. Bottom Status Bar (System Footer)
- **Purpose**: Provides real-time diagnostic telemetry regarding backend process health, Ollama local model connectivity, database metrics, and memory consumption.
- **User Interaction**: Clicking status indicators opens detailed system diagnostic popovers (referencing [API_SPECIFICATION.md](API_SPECIFICATION.md)).
- **Future Features**: Live network traffic monitor and local disk space warnings.

---

# 7. Detailed Dashboard Sections Specification

For each of the 10 mandatory dashboard sections, the table below specifies Purpose, User Interaction, and Future Features:

### Section 1: Today's Tasks
* **Purpose**: Displays the creator's daily priority task checklist to keep production on schedule.
* **User Interaction**: Creators click checkboxes to mark tasks complete, click "+ Add Task" to insert a quick item, or drag items to re-prioritize.
* **Future Features**: Automatic task generation derived from scheduled publication deadlines and AI-driven task prioritization.

### Section 2: AI Assistant Status
* **Purpose**: Reports real-time status, active provider (Ollama, OpenAI, Gemini), model selection, and memory footprint of the AI engine.
* **User Interaction**: Creators click "Switch Model" to alternate between local Ollama and cloud LLMs; click "Test Connection" to run latency checks.
* **Future Features**: Real-time context window usage bar, estimated token cost calculation, and local GPU temperature monitoring.

### Section 3: Recent Projects
* **Purpose**: Lists recently modified content drafts, scripts, and articles for rapid context resumption.
* **User Interaction**: Clicking a project row immediately opens the record in the Content Editor workspace; hovering displays quick actions (Edit, Export, Trash).
* **Future Features**: Multi-file selection, batch tag assignment, and version history preview popovers.

### Section 4: Research Queue
* **Purpose**: Displays recent web clips, reference bookmarks, and topic notes saved in the Research module.
* **User Interaction**: Creators click a research clip to open details or click "Insert into Draft" to attach reference material directly to an active project.
* **Future Features**: Automatic background web page scraping, semantic clustering of related research notes, and AI auto-summarization.

### Section 5: Content Pipeline
* **Purpose**: Visualizes content distribution across production lifecycle stages (`Idea`, `Research`, `Draft`, `Review`, `Scheduled`, `Published`).
* **User Interaction**: Creators drag content cards between stage columns to trigger status transitions (`PATCH /api/v1/content/{id}/status`).
* **Future Features**: Custom stage creation, automated stage transition triggers, and bottleneck alerts.

### Section 6: Publishing Queue
* **Purpose**: Shows upcoming posts queued for release across target channels (Substack, YouTube, Medium, LinkedIn).
* **User Interaction**: Creators click queued items to preview exported bundles or adjust scheduled release timestamps.
* **Future Features**: One-click manual publishing triggers, platform-specific format validation checks, and distribution status webhooks.

### Section 7: Calendar Preview
* **Purpose**: Provides a compact monthly calendar view highlighting publication deadlines and content events.
* **User Interaction**: Clicking a calendar date filters the main workspace to display items scheduled for that day; clicking scheduled dots opens event details.
* **Future Features**: Drag-and-drop date rescheduling, multi-channel color coding, and holiday/trend event overlays.

### Section 8: Quick Actions
* **Purpose**: Prominently displays high-frequency operational triggers to minimize click depth.
* **User Interaction**: Single-click actions for "+ New Draft", "Run AI Prompt Studio", "Import Media", and "Compile Export".
* **Future Features**: User-configurable action buttons and custom macro script execution triggers.

### Section 9: System Health
* **Purpose**: Monitors local desktop application diagnostics, CPU/RAM utilization, and process stability.
* **User Interaction**: Clicking health badges opens detailed resource consumption graphs and diagnostic log viewers (`logs/backend.log`).
* **Future Features**: Automated memory leak alerts, background process auto-restart controls, and local storage threshold warnings.

### Section 10: Backend Status
* **Purpose**: Displays the live connection state, loopback IP port, API response latency, and version of the managed Python FastAPI backend service.
* **User Interaction**: Clicking status indicator triggers an immediate health check ping (`GET /health`) and displays IPC connection latency.
* **Future Features**: Backend process restart button, port configuration selector, and API request rate limit monitors.

---

# 8. Related Documentation Cross-References

This Dashboard UX Architecture document directly aligns with and references the following engineering documents:

- [PROJECT.md](PROJECT.md) - Project context, baseline scope, and stakeholder goals.
- [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) - Core modules, functional requirements, and MVP scope.
- [UI_UX_GUIDELINES.md](UI_UX_GUIDELINES.md) - Design system tokens, color palettes, typography scales, 4px grid spacing, and component states.
- [ARCHITECTURE.md](ARCHITECTURE.md) - System component boundaries, React frontend, Electron shell, and FastAPI backend relationship.
- [CODING_STANDARD.md](CODING_STANDARD.md) - Code style, TypeScript standards, and component structure guidelines.
- [API_SPECIFICATION.md](API_SPECIFICATION.md) - Backend REST API request/response formats and error codes.
- [DATABASE_DESIGN.md](DATABASE_DESIGN.md) - Database entity relationships and SQLite performance strategy.
