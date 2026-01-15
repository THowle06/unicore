# UniCore – Architecture

## High-Level Architecture

UniCore follows a client-server architecture. The frontend communicates with the backend via a RESTful API.

## Backend Architecture

The backend uses a layered architecture:

- API layer (FastAPI routers)
- Service layer (business logic)
- Repository layer (database access)

## Frontend Architecture

The frontend is built using React and TypeScript. It consumes the backend API and manages UI state independently.

## Authentication Strategy

Authentication is handled by the backend using JWT-based access tokens. Passwords are hashed using a secure hashing algorithm.

Supabase Auth is considered as a future enhancement.

## Database Design

The system uses PostgreSQL hosted on Supabase. SQLAlchemy is used as the ORM with asynchronous database access.

## Deployment Model

The application is containerised using Docker. In development, services are orchestrated using Docker Compose.
