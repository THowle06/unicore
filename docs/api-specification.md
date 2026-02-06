# API Specification

This document defines the **backend API contract** for the academic study management application. It is intended to be implemented using **FastAPI** and backed by **Supabase (PostgreSQL + Auth)**.

The API follows RESTful principles and uses JSON for all request and response bodies.

## Table of Contents

- [API Specification](#api-specification)
  - [Table of Contents](#table-of-contents)
  - [1. General Conventions](#1-general-conventions)
    - [1.1 Base URL](#11-base-url)
    - [1.2 Authentication](#12-authentication)
    - [1.3 Common Response Codes](#13-common-response-codes)
  - [2. Authentication Endpoints (Wrapper)](#2-authentication-endpoints-wrapper)
    - [2.1 Get Current User](#21-get-current-user)
      - [2.1.1 Response](#211-response)
  - [3. Module Endpoints](#3-module-endpoints)
    - [3.1 Create Module](#31-create-module)
      - [3.1.1 Request Body](#311-request-body)
      - [3.1.2 Response (201 Created)](#312-response-201-created)
    - [3.2 Get All Modules](#32-get-all-modules)
      - [3.2.1 Query Parameters](#321-query-parameters)
      - [3.2.2 Response](#322-response)
    - [3.3 Get Module by ID](#33-get-module-by-id)
    - [3.4 Update Module](#34-update-module)
      - [3.4.1 Request Body](#341-request-body)
      - [3.4.2 Authorization Rule](#342-authorization-rule)
    - [3.5 Delete Module](#35-delete-module)
      - [3.5.1 Response](#351-response)
  - [4. Assignment Endpoints](#4-assignment-endpoints)
    - [4.1 Create Assignment](#41-create-assignment)
      - [4.1.1 Request Body](#411-request-body)
    - [4.2 Get Assignment by ID](#42-get-assignment-by-id)
    - [4.3 Update Assignment](#43-update-assignment)
    - [4.4 Delete Assignment](#44-delete-assignment)
  - [5. Grade Endpoints](#5-grade-endpoints)
    - [5.1 Create or Update Grade](#51-create-or-update-grade)
      - [5.1.1 Request Body](#511-request-body)
      - [5.1.2 Response](#512-response)
    - [5.2 Get Grade](#52-get-grade)
  - [6. File Endpoints](#6-file-endpoints)
    - [6.1 Upload File](#61-upload-file)
      - [6.1.1 Request](#611-request)
      - [6.1.2 Query Parameters](#612-query-parameters)
    - [6.2 Get File Metadata](#62-get-file-metadata)
  - [7. Study Group Endpoints](#7-study-group-endpoints)
    - [7.1 Create Study Group](#71-create-study-group)
      - [7.1.1 Request Body](#711-request-body)
    - [7.2 Join Study Group](#72-join-study-group)
    - [7.3 Get Study Group Members](#73-get-study-group-members)
  - [8. Versioning and Evolution](#8-versioning-and-evolution)
  - [9. Relationship to Implementation](#9-relationship-to-implementation)

---

## 1. General Conventions

### 1.1 Base URL

```text
/api/v1
```

---

### 1.2 Authentication

- Authentication is handled via **Supabase Auth**
- Clients must include a valid JWT access token in requests

```http
Authorization: Bearer <access_token>
```

Unless otherwise stated, **all endpoints require authentication**.

---

### 1.3 Common Response Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 422  | Validation Error      |
| 500  | Internal Server Error |

---

## 2. Authentication Endpoints (Wrapper)

> Note: Supabase handles authentication internally. These endpoints exist to provide a consistent API interface.

### 2.1 Get Current User

```http
GET /auth/me
```

#### 2.1.1 Response

```json
{
  "id": "uuid",
  "email": "user@example.com"
}
```

---

## 3. Module Endpoints

### 3.1 Create Module

```http
POST /modules
```

#### 3.1.1 Request Body

```json
{
  "code": "CS101",
  "name": "Programming Fundamentals",
  "credits": 20
}
```

#### 3.1.2 Response (201 Created)

```json
{
  "id": "uuid",
  "code": "CS101",
  "name": "Programming Fundamentals",
  "credits": 20,
  "created_at": "2026-02-06T12:00:00Z"
}
```

---

### 3.2 Get All Modules

```http
GET /modules
```

#### 3.2.1 Query Parameters

- `limit` (optional)
- `offset` (optional)

#### 3.2.2 Response

```json
[
  {
    "id": "uuid",
    "code": "CS101",
    "name": "Programming Fundamentals",
    "credits": 20
  }
]
```

---

### 3.3 Get Module by ID

```http
GET /modules/{module_id}
```

---

### 3.4 Update Module

```http
PUT /modules/{module_id}
```

#### 3.4.1 Request Body

```json
{
  "code": "CS101",
  "name": "Intro to Programming",
  "credits": 20
}
```

#### 3.4.2 Authorization Rule

- Only the module owner may update the module

---

### 3.5 Delete Module

```http
DELETE /modules/{module_id}
```

#### 3.5.1 Response

- `204 No Content`

---

## 4. Assignment Endpoints

### 4.1 Create Assignment

```http
POST /modules/{module_id}/assignments
```

#### 4.1.1 Request Body

```json
{
  "title": "Coursework 1",
  "description": "First assignment",
  "weight": 40,
  "due_date": "2026-03-15"
}
```

---

### 4.2 Get Assignment by ID

```http
GET /assignments/{assignment_id}
```

---

### 4.3 Update Assignment

```http
PUT /assignments/{assignment_id}
```

---

### 4.4 Delete Assignment

```http
DELETE /assignments/{assignment_id}
```

---

## 5. Grade Endpoints

### 5.1 Create or Update Grade

```http
POST /assignments/{assignment_id}/grade
```

#### 5.1.1 Request Body

```json
{
  "score": 72,
  "max_score": 100
}
```

#### 5.1.2 Response

```json
{
  "score": 72,
  "max_score": 100,
  "calculated_percentage": 72.0
}
```

---

### 5.2 Get Grade

```http
GET /assignments/{assignment_id}/grade
```

---

## 6. File Endpoints

### 6.1 Upload File

```http
POST /files/upload
```

#### 6.1.1 Request

- Multipart form data

#### 6.1.2 Query Parameters

- `module_id` (optional)
- `assignment_id` (optional)

---

### 6.2 Get File Metadata

```http
GET /files/{file_id}
```

---

## 7. Study Group Endpoints

### 7.1 Create Study Group

```http
POST /study-groups
```

#### 7.1.1 Request Body

```json
{
  "name": "Algorithms Study Group"
}
```

---

### 7.2 Join Study Group

```http
POST /study-groups/{group_id}/join
```

---

### 7.3 Get Study Group Members

```http
GET /study-groups/{group_id}/members
```

---

## 8. Versioning and Evolution

- The API is versioned via the URL path
- Backward-incompatible changes require a new version
- FastAPI automatically exposes the OpenAPI specification at `/docs`

---

## 9. Relationship to Implementation

- Each top-level resource maps to a FastAPI router
- Request and response bodies map to Pydantic schemas
- Authorization is enforced via dependency injection
- Database access is handled via Supabase client or repository layer

This document serves as the **authoritative API contract** for backend development.
