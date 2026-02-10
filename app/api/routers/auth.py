from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from supabase import Client

from app.api.deps import get_supabase_client
from app.schemas.auth import TokenResponse, UserRegister

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post(
    "/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED
)
async def register_user(
    user_data: UserRegister, supabase: Annotated[Client, Depends(get_supabase_client)]
):
    """Register a new user with email and password.

    Args:
        user_data: User registration details containing email and password.
        supabase: Supabase client instance for authentication operations.

    Raises:
        HTTPException: 400 Bad Request if:
            - Registration fails (user or session is None)
            - Email is already registered
            - Password doesn't meet security requirements
            - Supabase service is unavailable 

    Returns:
        TokenResponse: Contains access token, refresh token, and user information.
            - access_token: JWT token for authenting API requests
            - refresh_token: Token used to obtain a new access token when expired
            - user: User object with id and email
    """
    try:
        response = supabase.auth.sign_up(
            {"email": user_data.email, "password": user_data.password}
        )

        if not response.user or not response.session:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Registration failed"
            )

        return TokenResponse(
            access_token=response.session.access_token,
            refresh_token=response.session.refresh_token,
            user={"id": response.user.id, "email": response.user.email},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
