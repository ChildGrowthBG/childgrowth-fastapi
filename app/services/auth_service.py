from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.password import hash_password
from app.dependancies.token import create_access_token
from app.repository.user_repository import insert_user, select_user_by_email
from app.schemas.auth_schemas import RegisterReq, TokenResp


async def create_user(session: AsyncSession, data: RegisterReq) -> TokenResp:
    existing_user = await select_user_by_email(session, data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )

    user = await insert_user(
        session,
        email=data.email,
        password=hash_password(data.password),
        name=data.name,
    )
    token = create_access_token(user.id)

    return TokenResp(access_token=token, token_type="bearer")
