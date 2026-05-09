from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ChildBase(BaseModel):
    nickname: str = Field(min_length=1, max_length=255)
    birth_month: int = Field(alias="birthMonth", ge=1, le=12)
    birth_year: int = Field(alias="birthYear", ge=1900)

    model_config = ConfigDict(populate_by_name=True)


class ChildFormData(ChildBase):
    pass


class ChildResp(ChildBase):
    id: str
    user_id: str = Field(alias="userId")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
