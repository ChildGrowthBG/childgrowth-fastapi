from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.child import Child
from app.repository.child_repository import (
    delete_child,
    insert_child,
    select_child_by_id_and_user_id,
    select_children_by_user_id,
    update_child,
)
from app.schemas.child_schemas import ChildFormData, ChildResp


def to_child_resp(child: Child) -> ChildResp:
    return ChildResp(
        id=str(child.id),
        user_id=str(child.user_id),
        nickname=child.nickname,
        birth_month=child.birth_month,
        birth_year=child.birth_year,
        created_at=child.created_at,
        updated_at=child.updated_at,
    )


async def create_child(
    session: AsyncSession,
    *,
    user_id: int,
    data: ChildFormData,
) -> ChildResp:
    child = await insert_child(
        session,
        user_id=user_id,
        nickname=data.nickname,
        birth_month=data.birth_month,
        birth_year=data.birth_year,
    )
    return to_child_resp(child)


async def list_user_children(session: AsyncSession, user_id: int) -> list[ChildResp]:
    children = await select_children_by_user_id(session, user_id)
    return [to_child_resp(child) for child in children]


async def edit_child(
    session: AsyncSession,
    *,
    user_id: int,
    child_id: int,
    data: ChildFormData,
) -> ChildResp:
    child = await select_child_by_id_and_user_id(
        session,
        child_id=child_id,
        user_id=user_id,
    )
    if child is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child not found",
        )

    updated_child = await update_child(
        session,
        child,
        nickname=data.nickname,
        birth_month=data.birth_month,
        birth_year=data.birth_year,
    )
    return to_child_resp(updated_child)


async def remove_child(
    session: AsyncSession,
    *,
    user_id: int,
    child_id: int,
) -> None:
    child = await select_child_by_id_and_user_id(
        session,
        child_id=child_id,
        user_id=user_id,
    )
    if child is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Child not found",
        )

    await delete_child(session, child)
