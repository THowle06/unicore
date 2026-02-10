from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.api.deps import get_supabase_client
from app.main import app


@pytest.fixture
def mock_supabase():
    """Create a mock Supabase client."""
    return MagicMock()


@pytest.fixture
def client_with_mock(mock_supabase):
    """TestClient with mocked Supabase dependency."""
    app.dependency_overrides[get_supabase_client] = lambda: mock_supabase
    client = TestClient(app)
    yield client, mock_supabase
    app.dependency_overrides.clear()


def test_register_user_success(client_with_mock) -> None:
    """Test successful user registration."""
    client, mock_supabase = client_with_mock

    # Setup mock response
    mock_user = MagicMock()
    mock_user.id = "test-user-id"
    mock_user.email = "test@example.com"

    mock_session = MagicMock()
    mock_session.access_token = "test-access-token"
    mock_session.refresh_token = "test-refresh-token"

    mock_response = MagicMock()
    mock_response.user = mock_user
    mock_response.session = mock_session

    mock_supabase.auth.sign_up.return_value = mock_response

    # Make request
    response = client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "securepassword123"},
    )

    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["access_token"] == "test-access-token"
    assert data["refresh_token"] == "test-refresh-token"
    assert data["user"]["id"] == "test-user-id"
    assert data["user"]["email"] == "test@example.com"


def test_register_user_invalid_email(client_with_mock) -> None:
    """Test registration with invalid email format."""
    client, _ = client_with_mock

    response = client.post(
        "/api/auth/register",
        json={"email": "not-an-email", "password": "securepassword123"},
    )

    # Pydantic validation should fail
    assert response.status_code == 422


def test_register_user_missing_password(client_with_mock) -> None:
    """Test registration without password."""
    client, _ = client_with_mock

    response = client.post("/api/auth/register", json={"email": "test@example.com"})

    # Pydantic validation should fail
    assert response.status_code == 422


def test_register_user_supabase_failure(client_with_mock) -> None:
    """Test registration when Supabase returns no user."""
    client, mock_supabase = client_with_mock

    mock_response = MagicMock()
    mock_response.user = None  # Simulate failure
    mock_response.session = None

    mock_supabase.auth.sign_up.return_value = mock_response

    response = client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "securepassword123"},
    )

    assert response.status_code == 400
    assert "Registration failed" in response.json()["detail"]


def test_register_user_exception_handling(client_with_mock) -> None:
    """Test registration when Supabase raises an exception."""
    client, mock_supabase = client_with_mock

    mock_supabase.auth.sign_up.side_effect = Exception("Supabase connection error")

    response = client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "securepassword123"},
    )

    assert response.status_code == 400
    assert "Supabase connection error" in response.json()["detail"]
