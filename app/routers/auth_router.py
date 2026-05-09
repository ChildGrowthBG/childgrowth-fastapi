from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.schemas.auth_schemas import LoginReq, RegisterReq, TokenResp
from app.services.auth_service import create_user, login_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=TokenResp)
async def register(data: RegisterReq, session: AsyncSession = Depends(get_db)):
    resp = await create_user(session, data)
    return resp


@router.post("/login", response_model=TokenResp)
async def login(data: LoginReq, session: AsyncSession = Depends(get_db)):
    resp = await login_user(session, data)
    return resp
