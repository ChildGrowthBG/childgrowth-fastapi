from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.schemas.auth_schemas import RegisterReq, TokenResp
from app.services.auth_service import create_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=TokenResp)
async def register(data: RegisterReq, session: AsyncSession = Depends(get_db)):
    resp = await create_user(session, data)
    return resp
