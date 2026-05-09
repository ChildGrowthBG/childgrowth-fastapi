from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.dependancies.token import get_current_user_id
from app.schemas.child_schemas import ChildFormData, ChildResp
from app.services.child_service import (
    create_child,
    edit_child,
    list_user_children,
    remove_child,
)


router = APIRouter(prefix="/children", tags=["children"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ChildResp)
async def create(
    data: ChildFormData,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_db),
) -> ChildResp:
    return await create_child(session, user_id=user_id, data=data)


@router.get("", response_model=list[ChildResp])
async def list_all(
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_db),
) -> list[ChildResp]:
    return await list_user_children(session, user_id)


@router.put("/{child_id}", response_model=ChildResp)
async def update(
    child_id: int,
    data: ChildFormData,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_db),
) -> ChildResp:
    return await edit_child(session, user_id=user_id, child_id=child_id, data=data)


@router.delete("/{child_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    child_id: int,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_db),
) -> Response:
    await remove_child(session, user_id=user_id, child_id=child_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
