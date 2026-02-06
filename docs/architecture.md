# Backend Architecture

This document describes the **high-level architecture** of the backend system, including its internal structure, component responsibilities, and integration with external services. The goal is to provide clarity on *how* the backend is organised and *why* certain design decisions were made.

The architecture is intentionally kept **simple and modular**, suitable for a personal project while remaining scalable and maintainable.

## Table of Contents

- [Backend Architecture](#backend-architecture)
  - [Table of Contents](#table-of-contents)
  - [1. Architectural Overview](#1-architectural-overview)
  - [2. Core Design Principles](#2-core-design-principles)
  - [3. Application Structure](#3-application-structure)
  - [4. Layer Responsibilities](#4-layer-responsibilities)
    - [4.1 Router Layer (`api/routers`)](#41-router-layer-apirouters)
      - [4.1.1 Responsibilities](#411-responsibilities)
      - [4.1.2 Non-responsibilities](#412-non-responsibilities)
    - [4.2 Service Layer (`services/`)](#42-service-layer-services)
      - [4.2.1 Responsibilities](#421-responsibilities)
      - [4.2.2 Example](#422-example)
    - [4.3 Repository Layer (`repositories/`)](#43-repository-layer-repositories)
      - [4.3.1 Responsibilities](#431-responsibilities)
  - [5. Authentication and Authorization Flow](#5-authentication-and-authorization-flow)
  - [6. Supabase Integration](#6-supabase-integration)
    - [6.1 PostgreSQL](#61-postgresql)
    - [6.2 Authentication](#62-authentication)
    - [6.3 Storage](#63-storage)
  - [7. Error Handling Strategy](#7-error-handling-strategy)
    - [7.1 Examples](#71-examples)
  - [8. Configuration and Environment Management](#8-configuration-and-environment-management)
  - [9. Evolution and Scalability](#9-evolution-and-scalability)
  - [10. Summary](#10-summary)

---

## 1. Architectural Overview

The backend follows a **layered architecture** built around FastAPI, with clear separation of concerns between:

- API routing
- Business logic
- Data access
- External services (Supabase)

At a high level:

```text
Client
  ↓
FastAPI Router Layer
  ↓
Service Layer
  ↓
Data Access Layer
  ↓
Supabase (PostgreSQL, Auth, Storage)
```

---

## 2. Core Design Principles

The architecture is guided by the following principles:

- **Separation of concerns**: Each layer has a single responsibility
- **Backend-enforced logic**: All validation and business rules live server-side
- **Stateless API**: Authentication is token-based (JWT)
- **Incremental scalability**: New features can be added without restructuring
- **Framework alignment**: Design aligns naturally with FastAPI conventions

---

## 3. Application Structure

```text
app/
├── main.py              # FastAPI application entry point
│
├── api/
│   ├── deps.py          # Shared dependencies (auth, DB client)
│   └── routers/
│       ├── auth.py
│       ├── modules.py
│       ├── assignments.py
│       ├── grades.py
│       ├── files.py
│       └── study_groups.py
│
├── schemas/             # Pydantic request/response models
│   ├── module.py
│   ├── assignment.py
│   ├── grade.py
│   └── file.py
│
├── services/            # Business logic layer
│   ├── module_service.py
│   ├── assignment_service.py
│   ├── grade_service.py
│   └── file_service.py
│
├── repositories/        # Data access abstraction
│   ├── module_repository.py
│   ├── assignment_repository.py
│   └── grade_repository.py
│
├── core/
│   ├── config.py        # Environment and settings
│   └── security.py      # JWT handling and auth utilities
│
└── utils/               # Shared helper functions
```

---

## 4. Layer Responsibilities

### 4.1 Router Layer (`api/routers`)

#### 4.1.1 Responsibilities

- Define HTTP endpoints
- Validate request payloads (via Pydantic)
- Declare authentication and authorization dependencies
- Delegate work to services

#### 4.1.2 Non-responsibilities

- Business logic
- Database queries

---

### 4.2 Service Layer (`services/`)

#### 4.2.1 Responsibilities

- Implement business rules
- Perform validation across entities
- Coordinate multiple repositories
- Calculate derived values (e.g. grades)

#### 4.2.2 Example

- Ensuring assignment weights do not exceed 100%
- Computing grade percentages

---

### 4.3 Repository Layer (`repositories/`)

#### 4.3.1 Responsibilities

- Encapsulate all database access
- Execute queries against Supabase/PostgreSQL
- Return domain-level data structures

This layer prevents database logic from leaking into services or routers.

---

## 5. Authentication and Authorization Flow

1. User authenticates via Supabase Auth
2. Client receives a JWT access token
3. Token is sent in the `Authorization` header
4. FastAPI dependency validates the token
5. User ID (`auth.uid()`) is extracted and passed downstream
6. Supabase Row Level Security enforces data access rules

The backend trusts Supabase for identity verification and focuses on enforcing business-level permissions.

---

## 6. Supabase Integration

### 6.1 PostgreSQL

- Primary data store
- Enforces referential integrity
- Uses Row Level Security (RLS) for access control

### 6.2 Authentication

- Managed externally by Supabase Auth
- No user table duplication
- JWT-based stateless authentication

### 6.3 Storage

- Used for file uploads
- Database stores metadata only
- Access controlled via ownership rules

---

## 7. Error Handling Strategy

- Validation errors handled by FastAPI/Pydantic
- Business logic errors raised explicitly in services
- HTTP status codes map to error type

### 7.1 Examples

- `403 Forbidden` for unauthorized access
- `404 Not Found` for missing resources
- `422 Unprocessable Entity` for invalid input

---

## 8. Configuration and Environment Management

- Environment variables stored in `.env`
- Loaded via `core/config.py`
- Separate configuration for local and production environments

Sensitive values (e.g. Supabase keys) are never committed to version control.

---

## 9. Evolution and Scalability

This architecture supports future enhancements such as:

- Role-based permissions
- Shared modules and assignments
- Background tasks (notifications)
- Frontend integration (web or mobile)

The layered approach allows these features to be added with minimal disruption.

---

## 10. Summary

The backend architecture prioritises clarity, maintainability, and alignment with FastAPI and Supabase best practices. It is intentionally lightweight, making it well-suited for a personal project while remaining robust enough to support future growth.

This document complements the domain model and API specification and serves as a reference for implementation decisions.
