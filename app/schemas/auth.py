from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    """Schema for user registration request."""

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Schema for authentication response containing tokens and user info."""

    access_token: str
    refresh_token: str
    user: dict
