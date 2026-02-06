# Backend Domain & Data Model Specification

## Table of Contents

- [Backend Domain \& Data Model Specification](#backend-domain--data-model-specification)
  - [Table of Contents](#table-of-contents)
  - [1. Purpose of This Document](#1-purpose-of-this-document)
  - [2. System Domain Overview](#2-system-domain-overview)
    - [2.1 Key Assumptions](#21-key-assumptions)
  - [3. Core Entities](#3-core-entities)
    - [3.1 User (Supabase Auth)](#31-user-supabase-auth)
      - [3.1.1 Usage](#311-usage)
    - [3.2 Module](#32-module)
      - [3.2.1 Business Rules](#321-business-rules)
    - [3.3 Assignment](#33-assignment)
      - [3.3.1 Business Rules](#331-business-rules)
    - [3.4 Grade](#34-grade)
      - [3.4.1 Business Rules](#341-business-rules)
    - [3.5 File](#35-file)
      - [3.5.1 Business Rules](#351-business-rules)
    - [3.6 Study Group](#36-study-group)
      - [3.6.1 Business Rules](#361-business-rules)
    - [3.7 Study Group Membership](#37-study-group-membership)
      - [3.7.1 Business Rules](#371-business-rules)
  - [4. Entity Relationship Summary](#4-entity-relationship-summary)
  - [5. Ownership \& Access Control Model](#5-ownership--access-control-model)
    - [5.1 Ownership Rules](#51-ownership-rules)
    - [5.2 Access Rules](#52-access-rules)
  - [6. Implementation Notes](#6-implementation-notes)

## 1. Purpose of This Document

This document defines the **core domain model** for the backend of the academic study management application. It specifies:

- Core entities and their responsibilities
- Entity attributes and relationships
- Ownership and access assumptions
- Constraints relevant to backend implementation

This specification is backend-first and is designed to map directly to:

- PostgreSQL tables (Supabase)
- FastAPI Pydantic models
- Row Level Security (RLS) policies

---

## 2. System Domain Overview

The system is an academic study management platform that allows authenticated users to manage:

- Academic modules
- Assignments within modules
- Grades and calculated results
- Uploaded study files
- Collaborative study groups

### 2.1 Key Assumptions

- Authentication is handled by **Supabase Auth**
- Users are uniquely identified by `auth.users.id`
- All business logic and validation occurs in the backend
- Users own their data by default unless explicitly shared

---

## 3. Core Entities

### 3.1 User (Supabase Auth)

Users are managed entirely by Supabase Auth and are **not duplicated** in the application schema.

**Source Table**: `auth.users`

| Field      | Type      | Description                |
| ---------- | --------- | -------------------------- |
| id         | UUID (PK) | Unique user identifier     |
| email      | VARCHAR   | User email address         |
| created_at | TIMESTAMP | Account creation timestamp |

#### 3.1.1 Usage

- Referenced via foreign keys only
- Used for ownership and access control

---

### 3.2 Module

Represents an academic module or course unit.

**Table**: `modules`

| Field      | Type      | Constraints        |
| ---------- | --------- | ------------------ |
| id         | UUID      | Primary key        |
| code       | VARCHAR   | NOT NULL           |
| name       | VARCHAR   | NOT NULL           |
| credits    | INTEGER   | NOT NULL           |
| owner_id   | UUID      | FK → auth.users.id |
| created_at | TIMESTAMP | Default: now()     |
| updated_at | TIMESTAMP | Auto-updated       |

#### 3.2.1 Business Rules

- A module belongs to exactly one user
- Only the owner may update or delete the module
- A module may contain multiple assignments

---

### 3.3 Assignment

Represents coursework or assessments within a module.

**Table**: `assignments`

| Field       | Type      | Constraints     |
| ----------- | --------- | --------------- |
| id          | UUID      | Primary key     |
| module_id   | UUID      | FK → modules.id |
| title       | VARCHAR   | NOT NULL        |
| description | TEXT      | Optional        |
| weight      | DECIMAL   | NOT NULL        |
| due_date    | DATE      | Optional        |
| created_at  | TIMESTAMP | Default: now()  |
| updated_at  | TIMESTAMP | Auto-updated    |

#### 3.3.1 Business Rules

- Each assignment must belong to a module
- Assignment weights are used in grade calculations
- Validation may ensure total weights per module ≤ 100%

---

### 3.4 Grade

Represents a grade awarded for an assignment.

**Table**: `grades`

| Field                 | Type      | Constraints         |
| --------------------- | --------- | ------------------- |
| id                    | UUID      | Primary key         |
| assignment_id         | UUID      | FK → assignments.id |
| score                 | DECIMAL   | NOT NULL            |
| max_score             | DECIMAL   | NOT NULL            |
| calculated_percentage | DECIMAL   | Derived             |
| created_at            | TIMESTAMP | Default: now()      |

#### 3.4.1 Business Rules

- One grade per assignment (1:1 relationship)
- Calculated fields are generated server-side
- Grades inherit access permissions from assignments

---

### 3.5 File

Stores metadata for files uploaded to Supabase Storage.

**Table**: `files`

| Field         | Type      | Constraints                    |
| ------------- | --------- | ------------------------------ |
| id            | UUID      | Primary key                    |
| owner_id      | UUID      | FK → auth.users.id             |
| assignment_id | UUID      | FK → assignments.id (nullable) |
| module_id     | UUID      | FK → modules.id (nullable)     |
| storage_path  | VARCHAR   | NOT NULL                       |
| file_name     | VARCHAR   | Optional                       |
| file_type     | VARCHAR   | Optional                       |
| created_at    | TIMESTAMP | Default: now()                 |

#### 3.5.1 Business Rules

- Actual file content lives in Supabase Storage
- Database stores metadata only
- File must be linked to either a module or assignment

---

### 3.6 Study Group

Represents a collaborative study group.

**Table**: `study_groups`

| Field      | Type      | Constraints        |
| ---------- | --------- | ------------------ |
| id         | UUID      | Primary key        |
| name       | VARCHAR   | NOT NULL           |
| owner_id   | UUID      | FK → auth.users.id |
| created_at | TIMESTAMP | Default: now()     |

#### 3.6.1 Business Rules

- Study groups are owned by a user
- Owners manage membership and permissions

---

### 3.7 Study Group Membership

Join table representing group membership.

**Table**: `study_group_members`

| Field     | Type      | Constraints          |
| --------- | --------- | -------------------- |
| id        | UUID      | Primary key          |
| group_id  | UUID      | FK → study_groups.id |
| user_id   | UUID      | FK → auth.users.id   |
| role      | VARCHAR   | e.g. admin, member   |
| joined_at | TIMESTAMP | Default: now()       |

#### 3.7.1 Business Rules

- A user may belong to multiple groups
- Role defines permissions within the group

---

## 4. Entity Relationship Summary

```text
User
 ├── Modules (1:N)
 │    └── Assignments (1:N)
 │         └── Grade (1:1)
 │
 ├── Files (1:N)
 │
 └── Study Groups (N:M via study_group_members)
```

---

## 5. Ownership & Access Control Model

This section informs **Row Level Security (RLS)** configuration in Supabase.

### 5.1 Ownership Rules

- `modules.owner_id = auth.uid()`
- `files.owner_id = auth.uid()`
- `study_groups.owner_id = auth.uid()`

### 5.2 Access Rules

- Users may only access modules they own
- Assignments are accessible through owned modules
- Grades inherit access from assignments
- Study group members may access shared resources (future extension)

---

## 6. Implementation Notes

- UUIDs should be generated server-side
- All timestamps should be stored in UTC
- Business logic validation occurs in FastAPI
- Database constraints enforce referential integrity

---

This document serves as the authoritative source for backend domain design.
