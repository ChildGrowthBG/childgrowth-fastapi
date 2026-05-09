from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.dependancies.token import get_current_user_id
from app.repository.user_repository import select_user_by_id
from app.schemas.user_schemas import UserResp


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResp)
async def get_current_user(
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_db),
) -> UserResp:
    user = await select_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return UserResp(id=user.id, email=user.email, name=user.name)
