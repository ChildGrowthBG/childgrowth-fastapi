from fastapi import APIRouter, status

from app.schemas.auth_schemas import RegisterReq


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: RegisterReq):
    # TODO implement
    return {"message": "User registered successfully"}
