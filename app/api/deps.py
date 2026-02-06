from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import Client, create_client
from supabase_auth.types import User

from app.core.config import settings

security = HTTPBearer()


def get_supabase_client() -> Client:
    """Create and return a Supabase client instance.

    Returns:
        Client: A configured Supabase client for interacting with the database and auth services.
    """
    if not settings.SUPABASE_URL or not settings.SUPABASE_SECRET_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_SECRET_KEY must be configured")
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_SECRET_KEY)


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    supabase: Annotated[Client, Depends(get_supabase_client)],
) -> User:
    try:
        token = credentials.credentials
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )
        return user.user
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        ) from Exception
