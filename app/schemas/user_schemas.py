from pydantic import BaseModel, EmailStr


class UserResp(BaseModel):
    id: int
    email: EmailStr
    name: str
