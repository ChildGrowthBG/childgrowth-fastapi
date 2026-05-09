from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.child import Child


async def insert_child(
    session: AsyncSession,
    *,
    user_id: int,
    nickname: str,
    birth_month: int,
    birth_year: int,
) -> Child:
    child = Child(
        user_id=user_id,
        nickname=nickname,
        birth_month=birth_month,
        birth_year=birth_year,
    )
    session.add(child)
    await session.commit()
    await session.refresh(child)
    return child


async def select_children_by_user_id(session: AsyncSession, user_id: int) -> list[Child]:
    result = await session.execute(
        select(Child).where(Child.user_id == user_id).order_by(Child.created_at.desc())
    )
    return list(result.scalars().all())


async def select_child_by_id_and_user_id(
    session: AsyncSession,
    *,
    child_id: int,
    user_id: int,
) -> Child | None:
    result = await session.execute(
        select(Child).where(Child.id == child_id, Child.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def update_child(
    session: AsyncSession,
    child: Child,
    *,
    nickname: str,
    birth_month: int,
    birth_year: int,
) -> Child:
    child.nickname = nickname
    child.birth_month = birth_month
    child.birth_year = birth_year
    await session.commit()
    await session.refresh(child)
    return child


async def delete_child(session: AsyncSession, child: Child) -> None:
    await session.delete(child)
    await session.commit()
