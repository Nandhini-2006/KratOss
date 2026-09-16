from pydantic import BaseModel, EmailStr


class ProfileUpdate(BaseModel):
    name: str
    email: EmailStr


class ProfileResponse(BaseModel):
    id: int
    name: str
    email: str