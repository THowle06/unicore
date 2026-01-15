# UniCore

UniCore is a modular, API-first productivity platform designed for university students. It centralises academic deadlines, timetables, and group work into a single system while following modern software engineering best practices.

## Overview

UniCore is build as a full-stack monorepo using:

- A FastAPI backend
- A React + TypeScript frontend
- PostgreSQL hosted on Supabase
- Docker for local development and deployment

## Planned Features

- User authentication and authorisation
- Deadline and coursework management
- Weekly timetable management
- Group workspaces with shared deadlines
- Modular and extensible backend design

## Architecture Summary

UniCore follows an API-first architecture. The frontend consumes a versioned REST API exposed by the backend. The backend is structured using a layered architecture separating API routing, business logic, and persistence.

## Tech Stack

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy (async)
- PostgreSQL (Supabase)
- Alembic

### Frontend

- React
- TypeScript
- Tailwind CSS
- shadcn/ui

### Infrastructure

- Docker
- Docker Compose
- GitHub Actions

## Local Development

Full local setup instructions are available in [`docs/development.md`](docs/development.md).

## Project Status

UniCore is currently under active development. The initial focus is on core authentication and deadline management functionality.

## License

This project is licensed under the MIT License.
