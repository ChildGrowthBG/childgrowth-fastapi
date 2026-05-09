from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


async def insert_user(
    session: AsyncSession,
    *,
    email: str,
    password: str,
    name: str,
) -> User:
    user = User(email=email, password=password, name=name)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def select_user_by_email(session: AsyncSession, email: str) -> User | None:
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def select_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    result = await session.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
