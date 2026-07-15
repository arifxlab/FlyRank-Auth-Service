from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.auth import UserResponse

router = APIRouter(
    tags=["Protected"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user

from fastapi import HTTPException, status


@router.get("/admin")
def admin_only(
    current_user: User = Depends(get_current_user),
):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access forbidden. Admin role required.",
    )