# UniCore

> A comprehensive productivity application for university students to manage modules, assignments, and deadlines in one unified system.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)

## 📋 Table of Contents

- [UniCore](#unicore)
  - [📋 Table of Contents](#-table-of-contents)
  - [Overview](#overview)
  - [✨ Features](#-features)
    - [Planned Features](#planned-features)
    - [Completed Features](#completed-features)
  - [🛠 Tech Stack](#-tech-stack)
    - [Backend](#backend)
    - [DevOps](#devops)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Configuration](#configuration)
    - [Running the Application](#running-the-application)
      - [Local Development (without Docker)](#local-development-without-docker)
      - [With Docker Compose](#with-docker-compose)
  - [📁 Project Structure](#-project-structure)
  - [🔧 Development](#-development)
    - [Running Tests](#running-tests)
    - [Code Style](#code-style)
    - [Adding Dependencies](#adding-dependencies)
  - [🐳 Docker](#-docker)
    - [Building the Image](#building-the-image)
    - [Docker Compose Services](#docker-compose-services)
  - [📚 API Documentation](#-api-documentation)
  - [🗺 Roadmap](#-roadmap)
    - [Phase 1 (Current)](#phase-1-current)
    - [Phase 2](#phase-2)
    - [Phase 3](#phase-3)
    - [Phase 4 (Future Enhancements)](#phase-4-future-enhancements)
  - [🤝 Contributing](#-contributing)
    - [Development Workflow](#development-workflow)
  - [📄 License](#-license)
  - [📧 Contact](#-contact)

## Overview

UniCore is designed to help university students stay organised by providing a centralised platform for:

- Managing course modules and schedules
- Tracking assignments and deadlines
- Monitoring academic progress
- Organising study materials

**Current Status** - Early development - core backend services are being implemented.

## ✨ Features

### Planned Features

- [ ] Module management (add, edit, delete courses)
- [ ] Assignment tracking with deadline notifications
- [ ] Calendar integration
- [ ] Grade tracking with overall module calculation
- [ ] File upload and organisation
- [ ] Collaborative study groups

### Completed Features

- Currently in initial development phase

## 🛠 Tech Stack

### Backend

- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Package Manager:** uv
- **Database:** PostgreSQL (Supabase)
- **Authentication:** Supabase Auth
- **ORM:** SQLAlchemy

### DevOps

- **Containerisation:** Docker
- **CI/CD:** GitHub Actions
- **Hosting:** TBD (planned FastAPI Cloud)

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- Docker and Docker Compose
- Git
- [Supabase CLI](https://supabase.com/docs/guides/cli) (optional, for local development)

### Installation

1. Clone the repository

    ```bash
    git clone https://github.com/THowle06/unicore.git
    cd unicore
    ```

2. Install dependencies with uv

    ```bash
    uv sync
    ```

3. Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```

### Configuration

1. Copy the example environment file

    ```bash
    cp .env.example .env
    ```

2. Configure your `.env` file with the following variables:

    ```env
    # FastAPI
    DEBUG=True
    SECRET_KEY=your-secret-key-here
    API_V1_PREFIX=/api/v1
    
    # Supabase
    SUPABASE_URL=https://your-project.supabase.co
    SUPABASE_SECRET_KEY=your-secret-key
    SUPABASE_PUBLISHABLE_KEY=your-publishable-key
    
    # CORS
    ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
    ```

3. Set up Supabase project

    - Create a new project at [supabase.com](https://supabase.com)
    - Copy your project URL and anon key to `.env`
    - Configure authentication providers in Supabase dashboard

### Running the Application

#### Local Development (without Docker)

```bash
# Start the FastAPI server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at [http://localhost:8000](http://localhost:8000)

#### With Docker Compose

```bash
# Build and start all services
docker compose up --build

# Run in detached mode
docker compose up -d

# Stop services
docker compose down
```

The API will be available at [http://localhost:8000](http://localhost:8000)

## 📁 Project Structure

```text
unicore/
```

## 🔧 Development

### Running Tests

```bash
# Run all tests with pytest
uv run pytest

# Run with coverage
uv run pytest --cov=app --cov-report=html

# Run specific test file
uv run pytest app/tests/test_auth.py

# Run with verbose output
uv run pytest -v
```

### Code Style

This project uses Ruff for linting and formatting.

```bash
# Run linter
uv run ruff check .

# Fix auto-fixable issues
uv run ruff check --fix .

# Format code
uv run ruff format .

# Type checking with mypy
uv run mypy app/
```

### Adding Dependencies

```bash
# Add a new package
uv add package-name

# Add a development dependency
uv add --dev package-name

# Update all dependencies
uv sync --upgrade
```

## 🐳 Docker

### Building the Image

```bash
docker build -t unicore:latest .
```

### Docker Compose Services

The `docker-compose.yml` includes:

- **api**: FastAPI application
- **postgres**: PostgreSQL database (if not using Supabase)
- **redis**: Cache layer (optional)

```bash
# View logs
docker compose logs -f api

# Execute commands in container
docker compose exec api bash

# Rebuild specific service
docker compose up --build api
```

## 📚 API Documentation

When the server is running, interactive API documentation is available at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/docs)

## 🗺 Roadmap

### Phase 1 (Current)

- [x] Set up project infrastructure
- [ ] Design database schema
- [ ] Implement Supabase authentication
- [ ] Create basic CRUD operations for modules
- [ ] Set up Docker containerisation

### Phase 2

- [ ] Assignment management system
- [ ] Notification service
- [ ] Grade calculation engine

### Phase 3

- [ ] File management with Supabase Storage
- [ ] Study groups feature

### Phase 4 (Future Enhancements)

- [ ] Frontend UI implementation
- [ ] Calendar integration
- [ ] Mobile-responsive design

See the [open issues](https://github.com/THowle06/unicore/issues) for a full list of proposed features and known issues.

## 🤝 Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) first.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Workflow

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Project Link: [https://github.com/THowle06/unicore](https://github.com/THowle06/unicore)

---

**Note**: This project is under active development. Features and documentation are subject to change.
