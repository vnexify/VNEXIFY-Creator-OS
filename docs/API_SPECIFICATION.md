# VNEXIFY Creator OS API Specification

- Version: v0.1
- Creation Date: 2026-08-06
- Status: Draft / Architecture Specification
- Author: Product Manager / Lead Architect, VNEXIFY Creator OS

---

## Table of Contents

- [1. Overview \& System Architecture](#1-overview--system-architecture)
- [2. API Design Principles](#2-api-design-principles)
- [3. API Versioning Strategy](#3-api-versioning-strategy)
- [4. Request Format](#4-request-format)
- [5. Response Format](#5-response-format)
- [6. Error Response Format](#6-error-response-format)
- [7. Authentication Strategy (Future)](#7-authentication-strategy-future)
- [8. Status Codes](#8-status-codes)
- [9. Pagination Strategy](#9-pagination-strategy)
- [10. Validation Strategy](#10-validation-strategy)
- [11. File Upload Strategy](#11-file-upload-strategy)
- [12. Logging Strategy](#12-logging-strategy)
- [13. Rate Limiting Strategy](#13-rate-limiting-strategy)
- [14. Future API Endpoint Catalog](#14-future-api-endpoint-catalog)
  - [System \& Health Module](#system--health-module)
  - [Dashboard Module](#dashboard-module)
  - [Research Module](#research-module)
  - [Content Module](#content-module)
  - [AI Studio Module](#ai-studio-module)
  - [Analytics Module](#analytics-module)
  - [Calendar Module](#calendar-module)
  - [Media Module](#media-module)
  - [Settings Module](#settings-module)
  - [Plugins Module](#plugins-module)
  - [Exports Module](#exports-module)
  - [Database Module](#database-module)
  - [Notifications Module](#notifications-module)
  - [Scheduler Module](#scheduler-module)
- [15. Related Documentation Cross-References](#15-related-documentation-cross-references)

---

# 1. Overview & System Architecture

The VNEXIFY Creator OS backend service provides a RESTful HTTP API built using Python FastAPI. It exposes structured endpoints consumed primarily by the Electron desktop shell and React frontend application over a secure local loopback connection (`http://127.0.0.1:<port>`).

This API specification defines the complete data contracts, request/response models, error handling semantics, and endpoint structures across all core system modules, adhering strictly to the system boundary guidelines in [ARCHITECTURE.md](ARCHITECTURE.md) and module requirements detailed in [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md).

> [!NOTE]
> This document is a formal **API Design Specification**. It contains no executable code or server implementations. Full API code implementations will follow in subsequent development phases as defined in [roadmap.md](roadmap.md).

---

# 2. API Design Principles

The VNEXIFY Creator OS API is designed around five core software engineering principles:

1. **RESTful Architecture**: Endpoints are resource-oriented, utilizing standard HTTP verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) to execute CRUD operations predictably.
2. **Predictable JSON Schemas**: All data exchanges utilize standard JSON payloads. Field names strictly follow `camelCase` naming conventions to map cleanly to frontend TypeScript models (in accordance with [CODING_STANDARD.md](CODING_STANDARD.md)).
3. **Local-First Low Latency**: Designed for zero-network-overhead local loopback operations with minimal payload sizes, non-blocking async execution, and fast SQLite database indexing.
4. **Stateless Operations**: Each API request contains all necessary parameters to fulfill the operation, relying on the backend SQLite database (stored in `backend/db/`) for state persistence.
5. **Deterministic Error Handling**: Every error response returns a standardized JSON error envelope with machine-readable error codes and actionable error messages.

---

# 3. API Versioning Strategy

To guarantee stability as the application evolves across release cycles (referencing [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md)):

* **URI Path Versioning**: All production endpoints MUST include an explicit version prefix in the URL path:
  ```text
  http://127.0.0.1:<port>/api/v1/content
  ```
* **Major Version Progression**: The major version number (`v1`, `v2`) is incremented only when breaking changes are introduced (e.g., removing a field, changing field data types, or altering endpoint URLs).
* **Non-Breaking Updates**: Adding new optional fields to request/response models or introducing new endpoints does not bump the major version.
* **Deprecation Policy**: Obsolete endpoints will return HTTP header warnings prior to removal:
  ```http
  Deprecation: @1773000000
  Link: <http://127.0.0.1:<port>/api/v2/content>; rel="successor-version"
  ```

---

# 4. Request Format

All state-modifying requests (`POST`, `PUT`, `PATCH`) MUST supply data in JSON format unless uploading binary media assets.

### Required HTTP Headers
* `Content-Type`: `application/json` (or `multipart/form-data` for media file uploads)
* `Accept`: `application/json`
* `X-Client-Version`: Client desktop application version (e.g., `0.1.0`)
* `X-Request-ID`: Universally Unique Identifier (UUIDv4) generated per IPC request by Electron for distributed tracing in backend logs.

### Request Body Schema Convention
Request fields MUST use `camelCase`. Example conceptual structure:

```json
{
  "title": "Unlocking Local-First AI Workflows",
  "slug": "unlocking-local-first-ai-workflows",
  "contentType": "Article",
  "tags": ["AI", "LocalFirst", "Productivity"],
  "isArchived": false
}
```

---

# 5. Response Format

All API responses follow a consistent top-level JSON wrapper envelope.

### Standard Success Response (Single Item)
Used for `200 OK` and `201 Created` responses returning a single entity:

```json
{
  "success": true,
  "data": {
    "id": "cnt_9f8d7e6a",
    "title": "Unlocking Local-First AI Workflows",
    "slug": "unlocking-local-first-ai-workflows",
    "status": "Draft",
    "wordCount": 1250,
    "createdAt": "2026-08-06T14:05:00Z",
    "updatedAt": "2026-08-06T14:05:00Z"
  },
  "meta": {
    "requestId": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-08-06T14:05:00Z"
  }
}
```

### Standard Success Response (Collection / List)
Used for endpoints returning multiple records, incorporating standard pagination metadata:

```json
{
  "success": true,
  "data": [
    {
      "id": "cnt_9f8d7e6a",
      "title": "Unlocking Local-First AI Workflows",
      "status": "Draft"
    }
  ],
  "meta": {
    "requestId": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-08-06T14:05:00Z",
    "pagination": {
      "currentPage": 1,
      "pageSize": 20,
      "totalRecords": 142,
      "totalPages": 8,
      "hasNextPage": true,
      "hasPrevPage": false
    }
  }
}
```

---

# 6. Error Response Format

When a request fails, the API returns a standard error envelope paired with the corresponding HTTP status code (`4xx` or `5xx`).

### Error Envelope Schema

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested content item 'cnt_9f8d7e6a' was not found.",
    "details": [
      {
        "field": "contentId",
        "issue": "No matching record exists in SQLite database."
      }
    ]
  },
  "meta": {
    "requestId": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-08-06T14:05:00Z"
  }
}
```

### Standard Error Code Registry

| Error Code | HTTP Status | Description |
| :--- | :--- | :--- |
| `VALIDATION_ERROR` | `400 Bad Request` | Request parameters or body failed syntax checks. |
| `UNAUTHORIZED` | `401 Unauthorized` | Missing or invalid local IPC authentication token. |
| `FORBIDDEN` | `403 Forbidden` | Access to the requested resource is denied by policy. |
| `RESOURCE_NOT_FOUND` | `404 Not Found` | Target record ID does not exist in the database. |
| `RESOURCE_CONFLICT` | `409 Conflict` | Unique key violation (e.g. duplicate title/slug). |
| `UNPROCESSABLE_ENTITY`| `422 Unprocessable Entity` | Pydantic schema validation failure on request payload. |
| `RATE_LIMIT_EXCEEDED` | `429 Too Many Requests` | Request volume exceeded local loopback rate limits. |
| `INTERNAL_SERVER_ERROR`| `500 Internal Error` | Unhandled backend exception or database failure. |
| `AI_PROVIDER_ERROR` | `503 Service Unavailable` | Cloud AI API or local Ollama engine failed to respond. |

---

# 7. Authentication Strategy (Future)

### Current Architecture (v1.0 MVP)
Because VNEXIFY Creator OS operates as a local-first desktop application on a single user's machine (as detailed in [SECURITY.md](SECURITY.md)):
- The FastAPI backend binds exclusively to local loopback `127.0.0.1` on a dynamically selected port.
- Electron generates an ephemeral, high-entropy IPC authorization token upon startup and supplies it to the backend process via environment parameters.
- Frontend HTTP requests include this token in a custom header: `X-Local-IPC-Token: <token>`.

### Future Authentication Architecture (v2 / v3 & Enterprise)
For future multi-device synchronization and Enterprise team workspaces (referencing [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md)):
* **OAuth 2.0 & OpenID Connect (OIDC)**: Integration with enterprise identity providers (Okta, Auth0, Google Workspace).
* **JSON Web Tokens (JWT)**: Secure short-lived Access Tokens passed via standard HTTP header:
  ```http
  Authorization: Bearer <jwt_access_token>
  ```
* **Role-Based Access Control (RBAC)**: Fine-grained permission scopes defined per token (`content:read`, `content:write`, `settings:admin`, `ai:execute`).

---

# 8. Status Codes

The API utilizes standard HTTP status codes to communicate outcome states clearly:

| Status Code | Reason Phrase | Usage Scenario |
| :--- | :--- | :--- |
| `200 OK` | OK | Successful `GET`, `PUT`, or `PATCH` operation. |
| `201 Created` | Created | Successful `POST` resulting in a new database record. |
| `204 No Content` | No Content | Successful `DELETE` operation or background trigger. |
| `400 Bad Request` | Bad Request | Invalid query parameters or malformed JSON syntax. |
| `401 Unauthorized` | Unauthorized | Missing or invalid local IPC token. |
| `403 Forbidden` | Forbidden | Action disallowed by current application state. |
| `404 Not Found` | Not Found | Requested endpoint or database entity does not exist. |
| `409 Conflict` | Conflict | Attempted creation violates unique schema index. |
| `422 Unprocessable` | Unprocessable Entity | Payload validation failure (returned by Pydantic). |
| `429 Too Many Requests`| Too Many Requests | Endpoint rate limit threshold exceeded. |
| `500 Internal Error` | Internal Server Error | Unhandled server exception (logged to `logs/backend.log`). |
| `503 Unavailable` | Service Unavailable | External AI service or local Ollama daemon unreachable. |

---

# 9. Pagination Strategy

All collection list endpoints (e.g. fetching content lists, research notes, media assets) MUST implement standard query parameter pagination to ensure low memory consumption.

### Query Parameters
* `page`: Integer (1-indexed, default: `1`).
* `limit`: Integer (items per page, default: `20`, maximum: `100`).
* `sortBy`: String (attribute to sort by, e.g. `createdAt`, `title`, `updatedAt`).
* `sortOrder`: String (`asc` or `desc`, default: `desc`).

### Example Paginated Query
```text
GET /api/v1/content?page=2&limit=20&sortBy=createdAt&sortOrder=desc
```

### Alternative Cursor Pagination
For high-volume append-only streams (such as system logs or media asset indexing), endpoints MAY support cursor-based pagination using a `cursor` string parameter representing the opaque offset token.

---

# 10. Validation Strategy

Input validation is enforced strictly at the backend boundary prior to database interaction:

1. **Pydantic Schema Validation**: Every endpoint defines explicit Request and Response Pydantic models in `backend/app/api/`.
2. **Type Safety & Coercion**: Enforces strict primitive types (String, Integer, Float, Boolean, UUID, Datetime).
3. **Constraint Enforcement**:
   - String length limits (e.g., Title: 1 to 255 characters).
   - RegEx pattern matching for slugs (`^[a-z0-9]+(?:-[a-z0-9]+)*$`).
   - Enum validation for states (`Draft`, `Review`, `Scheduled`, `Published`).
4. **Validation Failure Handling**: Automatically generates a `422 Unprocessable Entity` response detailing specific field-level validation errors.

---

# 11. File Upload Strategy

Managing media assets (graphics, thumbnails, audio tracks) requires a dual-strategy approach optimized for local desktop performance:

### Strategy A: Direct Path Indexing (Recommended for Local Desktop)
Since Electron and FastAPI run on the same client machine:
- The React UI uses native OS file pickers to obtain absolute local file paths.
- The UI sends the file path to `POST /api/v1/media/index`.
- The backend verifies file existence, extracts metadata (dimensions, mime type, size), copies the file to the local `assets/` workspace directory, and stores the record in SQLite.

### Strategy B: Multipart Form Upload (Fallback / HTTP Upload)
For standard file streaming:
- Endpoint: `POST /api/v1/media/upload`
- Content Type: `multipart/form-data`
- Max File Payload Size: `50 MB` per file.
- Server Actions: Validates file extension against allowed MIME types, generates SHA-256 content hash to prevent duplicates, writes file to `assets/`, and returns media entity JSON.

---

# 12. Logging Strategy

All API request cycles log structured diagnostic data to ensure maintainability (referencing [FILE_STRUCTURE.md](FILE_STRUCTURE.md) and [SECURITY.md](SECURITY.md)):

* **Log Output Location**: `logs/backend.log`
* **Log Format**: JSON Lines (JSONL) format for automated parsing.
* **Fields Logged Per Request**:
  - `timestamp`: ISO 8601 UTC string.
  - `requestId`: UUID matching `X-Request-ID`.
  - `method`: HTTP method (`GET`, `POST`, etc.).
  - `path`: Request path.
  - `statusCode`: Returned HTTP code.
  - `durationMs`: Execution time in milliseconds.
  - `clientIp`: Loopback IP (`127.0.0.1`).
* **Sensitive Data Protection**: API keys (OpenAI, Gemini), authorization tokens, and personal draft text are **automatically masked** before writing logs.

---

# 13. Rate Limiting Strategy

To prevent accidental infinite UI loops, runaway plugin execution, or local memory exhaustion:

* **Local Loopback Limits**:
  - Standard CRUD endpoints: `100 requests / minute` per client process.
  - Heavy compute endpoints (AI generation, PDF compilation): `10 requests / minute`.
* **Rate Limit Response Headers**:
  ```http
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 98
  X-RateLimit-Reset: 1773000060
  ```
* **Exceeded Threshold Behavior**: Returns `429 Too Many Requests` with error code `RATE_LIMIT_EXCEEDED`.

---

# 14. Future API Endpoint Catalog

Below is the comprehensive list of planned REST API endpoints structured across the 13 Core Modules specified in [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md):

### System & Health Module
- `GET /api/v1/health` - Check backend system health and DB connectivity.
- `GET /api/v1/system/info` - Get system environment, OS platform, and Python runtime metrics.

### Dashboard Module
- `GET /api/v1/dashboard/stats` - Retrieve aggregated pipeline statistics and output counts.
- `GET /api/v1/dashboard/activity` - Fetch recent creator activity logs and draft updates.

### Research Module
- `GET /api/v1/research/notes` - List research notes and web clips (paginated).
- `POST /api/v1/research/notes` - Create a new research note or bookmark.
- `GET /api/v1/research/notes/{id}` - Fetch a specific research note by ID.
- `PUT /api/v1/research/notes/{id}` - Update a research note.
- `DELETE /api/v1/research/notes/{id}` - Delete a research note.

### Content Module
- `GET /api/v1/content` - List content records with filtering by status/tags.
- `POST /api/v1/content` - Create a new content draft.
- `GET /api/v1/content/{id}` - Fetch complete content record including markdown body.
- `PUT /api/v1/content/{id}` - Update content body, title, or metadata.
- `PATCH /api/v1/content/{id}/status` - Update content pipeline stage (`Draft` -> `Published`).
- `DELETE /api/v1/content/{id}` - Move content record to trash.

### AI Studio Module
- `GET /api/v1/ai/models` - List available AI models (OpenAI, Gemini, Ollama).
- `POST /api/v1/ai/generate` - Execute an AI prompt generation request.
- `GET /api/v1/ai/prompts` - List saved system prompts and templates.
- `POST /api/v1/ai/prompts` - Save a new custom prompt template.
- `GET /api/v1/ai/providers/status` - Check connection health of local Ollama and cloud APIs.

### Analytics Module
- `GET /api/v1/analytics/overview` - Fetch performance metrics overview.
- `GET /api/v1/analytics/growth` - Fetch content output velocity metrics over time.

### Calendar Module
- `GET /api/v1/calendar/events` - Fetch scheduled content events within date range.
- `POST /api/v1/calendar/schedule` - Schedule a content record for publishing.
- `DELETE /api/v1/calendar/schedule/{id}` - Cancel a scheduled publishing event.

### Media Module
- `GET /api/v1/media/assets` - List indexed media assets in `assets/`.
- `POST /api/v1/media/upload` - Upload a new media file (multipart/form-data).
- `POST /api/v1/media/index` - Index an existing local file by file path.
- `GET /api/v1/media/assets/{id}` - Fetch media metadata and local asset path.
- `DELETE /api/v1/media/assets/{id}` - Unlink or remove a media asset.

### Settings Module
- `GET /api/v1/settings` - Fetch application configuration settings.
- `PUT /api/v1/settings` - Update application preferences and UI themes.
- `POST /api/v1/settings/keys` - Store encrypted cloud AI API keys (OpenAI, Gemini).
- `POST /api/v1/settings/backup` - Trigger a local SQLite database backup.

### Plugins Module
- `GET /api/v1/plugins` - List installed plugins in `plugins/`.
- `POST /api/v1/plugins/{id}/enable` - Enable a specific plugin.
- `POST /api/v1/plugins/{id}/disable` - Disable a specific plugin.
- `POST /api/v1/plugins/{id}/execute` - Execute a plugin workflow hook.

### Exports Module
- `POST /api/v1/exports/compile` - Compile a content item to specified format (`md`, `html`, `pdf`).
- `GET /api/v1/exports/history` - List generated files residing in `exports/`.

### Database Module
- `GET /api/v1/database/status` - Inspect SQLite DB file size, table counts, and indexes.
- `POST /api/v1/database/migrate` - Execute pending database schema migrations.
- `POST /api/v1/database/optimize` - Run SQLite `VACUUM` and index optimization.

### Notifications Module
- `GET /api/v1/notifications` - List unread desktop notifications.
- `PATCH /api/v1/notifications/{id}/read` - Mark a notification as read.

### Scheduler Module
- `GET /api/v1/scheduler/tasks` - List active background scheduler tasks.
- `POST /api/v1/scheduler/tasks/{id}/trigger` - Manually trigger a background task execution.

---

# 15. Related Documentation Cross-References

This API specification aligns directly with the following architecture and design documents across the repository:

- [PROJECT.md](PROJECT.md) - Project context, goals, and stakeholder requirements.
- [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) - Core modules, functional requirements, and MVP scope.
- [ARCHITECTURE.md](ARCHITECTURE.md) - System component boundaries and IPC data flow models.
- [TECH_STACK.md](TECH_STACK.md) - Specifications for FastAPI, Pydantic, SQLAlchemy, and SQLite.
- [FILE_STRUCTURE.md](FILE_STRUCTURE.md) - Placement rules for `backend/app/api/`, `logs/`, `assets/`, and `exports/`.
- [CODING_STANDARD.md](CODING_STANDARD.md) - Code style, JSON `camelCase` rules, and Python typing standards.
- [SECURITY.md](SECURITY.md) - Local loopback IPC security, key storage, and logging privacy rules.
