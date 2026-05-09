from pydantic import BaseModel, EmailStr


class RegisterReq(BaseModel):
    email: EmailStr
    password: str
    name: str
