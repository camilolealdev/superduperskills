---
name: api-design
description: >
  Production REST API design patterns including resource naming, status codes, cursor pagination, filtering,
  standardized error envelopes, versioning, and rate-limiting headers. Use when creating or auditing API contracts,
  or when user mentions "api-design", "rest api patterns", "error envelope", or "cursor pagination".
argument-hint: "[resources|pagination|errors|versioning|status-codes]"
license: MIT
---

# API Design — Production REST API Standards

Based on [affaan-m/api-design](https://skillrepo.dev/skills/affaan-m/api-design) (v1.2A), this skill establishes standards for public and internal REST APIs.

## Key Standards

- **Resource Naming**: Plural nouns (`GET /v1/users`, `POST /v1/organizations/{id}/members`).
- **Cursor Pagination**: Opaque cursors (`GET /v1/posts?starting_after=obj_123&limit=25`).
- **Unified Error Envelope**:
  ```json
  {
    "error": {
      "code": "resource_not_found",
      "message": "User with ID 'usr_123' does not exist.",
      "param": "id",
      "doc_url": "https://api.docs.com/errors#resource_not_found"
    }
  }
  ```
