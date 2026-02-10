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
