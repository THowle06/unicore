# Contributing to UniCore

First off, thank you for considering contributing to UniCore! It's people like you that make UniCore such a great tool for university students.

## Table of Contents

- [Contributing to UniCore](#contributing-to-unicore)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
    - [Our Standards](#our-standards)
  - [Getting Started](#getting-started)
    - [Issues](#issues)
      - [Creating an Issue](#creating-an-issue)
      - [Issue Labels](#issue-labels)
    - [Pull Requests](#pull-requests)
      - [Before Submitting a PR](#before-submitting-a-pr)
      - [PR Checklist](#pr-checklist)
  - [Development Setup](#development-setup)
  - [Development Workflow](#development-workflow)
  - [Coding Standards](#coding-standards)
    - [Python Style Guide](#python-style-guide)
      - [Code Formatting](#code-formatting)
      - [Naming Conventions](#naming-conventions)
      - [Type Hints](#type-hints)
      - [Docstrings](#docstrings)
      - [Error Handling](#error-handling)
    - [Commit Messages](#commit-messages)
      - [Types](#types)
      - [Examples](#examples)
    - [Branch Naming](#branch-naming)
  - [Testing](#testing)
    - [Writing Tests](#writing-tests)
    - [Running Tests](#running-tests)
  - [Documentation](#documentation)
    - [Code Documentation](#code-documentation)
    - [API Documentation](#api-documentation)
    - [README Updates](#readme-updates)
  - [Review Process](#review-process)
    - [For Contributors](#for-contributors)
    - [For Reviewers](#for-reviewers)
    - [Approval Process](#approval-process)
  - [Questions?](#questions)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members
- Accept constructive criticism gracefully

## Getting Started

### Issues

#### Creating an Issue

Before creating an issue, please:

1. **Search existing issues** to avoid duplicates
2. **Use the issue template** if one is provided
3. **Provide detailed information** including:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Screenshots or code samples if relevant

#### Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

### Pull Requests

#### Before Submitting a PR

1. **Create an issue first** to discuss major changes
2. **Fork the repository** and create your branch from `main`
3. **Follow the coding standards** outlined below
4. **Write or update tests** for your changes
5. **Update documentation** as needed
6. **Ensure all tests pass** locally

#### PR Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex code
- [ ] Documentation updated (if applicable)
- [ ] Tests added/updated and passing
- [ ] No new warnings generated
- [ ] PR title is clear and descriptive
- [ ] PR description explains the changes

## Development Setup

1. **Fork and clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/unicore.git
   cd unicore
   ```

2. **Add upstream remote**

   ```bash
   git remote add upstream https://github.com/THowle06/unicore.git
   ```

3. **Install dependencies**

   ```bash
   uv sync
   source .venv/bin/activate
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Install pre-commit hooks** (recommended)

   ```bash
   uv add --dev pre-commit
   uv run pre-commit install
   ```

## Development Workflow

1. **Sync your fork with upstream**

   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow the coding standards
   - Add tests for new functionality

4. **Test your changes**

   ```bash
   # Run tests
   uv run pytest
   
   # Run linting
   uv run ruff check .
   
   # Format code
   uv run ruff format .
   
   # Type checking
   uv run mypy app/
   ```

5. **Commit your changes**

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

6. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

## Coding Standards

### Python Style Guide

This project follows [PEP 8](https://pep8.org/) with some additional guidelines:

#### Code Formatting

- **Line length**: Maximum 88 characters (Black default)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Organized and sorted (use `ruff` for auto-sorting)
  
  ```python
  # Standard library imports
  import os
  from typing import Optional
  
  # Third-party imports
  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel
  
  # Local imports
  from app.core.config import settings
  from app.db.models import User
  ```

#### Naming Conventions

- **Functions and variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private methods/attributes**: `_leading_underscore`

  ```python
  # Good
  def get_user_modules(user_id: int) -> list[Module]:
      pass
  
  class ModuleService:
      MAX_MODULES_PER_USER = 10
      
      def _validate_module(self, module: Module) -> bool:
          pass
  ```

#### Type Hints

Always use type hints for function parameters and return values:

```python
from typing import Optional, List

def create_assignment(
    title: str,
    due_date: datetime,
    module_id: int,
    description: Optional[str] = None
) -> Assignment:
    """Create a new assignment."""
    pass
```

#### Docstrings

Use Google-style docstrings:

```python
def calculate_grade(assignments: list[Assignment]) -> float:
    """Calculate the overall grade from a list of assignments.
    
    Args:
        assignments: List of Assignment objects with grades.
        
    Returns:
        The calculated average grade as a float between 0 and 100.
        
    Raises:
        ValueError: If assignments list is empty.
        
    Example:
        >>> assignments = [Assignment(grade=85), Assignment(grade=90)]
        >>> calculate_grade(assignments)
        87.5
    """
    if not assignments:
        raise ValueError("Cannot calculate grade from empty list")
    return sum(a.grade for a in assignments) / len(assignments)
```

#### Error Handling

- Use specific exception types
- Provide meaningful error messages
- Log errors appropriately

```python
from fastapi import HTTPException, status

def get_module(module_id: int) -> Module:
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Module with id {module_id} not found"
        )
    return module
```

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```text
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

#### Examples

```bash
feat(auth): add password reset functionality

Implement password reset feature using Supabase Auth.
Users can now request a password reset email.

Closes #123

---

fix(assignments): correct due date calculation

Fixed timezone handling bug that caused incorrect due dates
to be displayed for users in different timezones.

---

docs(readme): update installation instructions

Added section about uv package manager installation
```

### Branch Naming

Use descriptive branch names with the following pattern:

```text
<type>/<description>
```

Examples:

- `feature/assignment-notifications`
- `fix/authentication-bug`
- `docs/api-documentation`
- `refactor/database-queries`

## Testing

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)

```python
def test_create_module_success():
    """Test successful module creation."""
    # Arrange
    user = create_test_user()
    module_data = {
        "name": "Computer Science 101",
        "code": "CS101",
        "credits": 3
    }
    
    # Act
    module = create_module(user.id, module_data)
    
    # Assert
    assert module.name == "Computer Science 101"
    assert module.code == "CS101"
    assert module.user_id == user.id
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_modules.py

# Run with coverage report
uv run pytest --cov=app --cov-report=html

# Run tests matching a pattern
uv run pytest -k "test_create"
```

## Documentation

### Code Documentation

- Add docstrings to all public functions, classes, and modules
- Keep comments concise and meaningful
- Update docstrings when changing function behavior

### API Documentation

- FastAPI automatically generates OpenAPI documentation
- Ensure all endpoints have proper descriptions
- Document request/response models with Pydantic

```python
from pydantic import BaseModel, Field

class ModuleCreate(BaseModel):
    """Schema for creating a new module."""
    
    name: str = Field(..., description="Module name", example="Computer Science 101")
    code: str = Field(..., description="Module code", example="CS101")
    credits: int = Field(..., ge=1, le=10, description="Number of credits")

@router.post("/modules", response_model=Module, status_code=status.HTTP_201_CREATED)
async def create_module(
    module: ModuleCreate,
    current_user: User = Depends(get_current_user)
) -> Module:
    """
    Create a new module for the current user.
    
    - **name**: Module name (required)
    - **code**: Module code (required)
    - **credits**: Number of credits (1-10)
    """
    return await module_service.create(module, current_user.id)
```

### README Updates

Update the README.md when:

- Adding new features
- Changing setup instructions
- Modifying project structure
- Adding new dependencies

## Review Process

### For Contributors

1. **Respond to feedback** promptly and professionally
2. **Make requested changes** in new commits
3. **Keep the PR focused** on a single feature/fix
4. **Rebase if needed** to keep history clean

### For Reviewers

Reviewers should check:

- [ ] Code quality and adherence to standards
- [ ] Test coverage and test quality
- [ ] Documentation updates
- [ ] No breaking changes (or properly documented)
- [ ] Security considerations
- [ ] Performance implications

### Approval Process

1. At least one maintainer approval required
2. All CI checks must pass
3. No unresolved conversations
4. Code conflicts resolved

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the `question` label
- Reach out to the maintainers
- Check existing issues and discussions

Thank you for contributing to UniCore! 🎓
