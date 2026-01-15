# UniCore – System Specification

## 1. Introduction

UniCore is a web-based productivity platform designed to support university students in managing academic responsibilities.

## 2. Scope

The system provides tools for managing deadlines, timetables, and group work. It is designed for individual students and small groups.

## 3. Functional Requirements

### 3.1 User Authentication

- Users must be able to register and log in
- Passwords must be securely hashed
- Authenticated users access protected resources

### 3.2 Deadline Management

- Users can create, update, and delete deadlines
- Deadlines have due dates, priorities, and statuses
- Deadlines may be personal or shared with groups

### 3.3 Timetable Management

- Users can manage weekly timetable entries
- Timetable entries can be recurring

### 3.4 Group Management

- Users can create groups
- Users can invite other users to groups
- Groups can share deadlines

## 4. Non-Functional Requirements

- The system must be secure by default
- The system must be responsive and performant
- The system must be maintainable and modular
- The system must be containerised for development

## 5. System Modules

- Authentication Module
- Deadline Module
- Timetable Module
- Group Module

## 6. Out of Scope

- Native mobile applications
- File storage and uploads
- Third-party LMS integrations

## 7. Future Enhancements

- Push notifications
- Calendar (ICS) integration
- Supabase Auth integration
