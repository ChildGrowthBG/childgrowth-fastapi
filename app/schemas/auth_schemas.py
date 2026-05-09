from pydantic import BaseModel, EmailStr


class RegisterReq(BaseModel):
    email: EmailStr
    password: str
    name: str


class TokenResp(BaseModel):
    access_token: str
    token_type: str
