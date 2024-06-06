from pydantic import BaseModel, Field, EmailStr

from app.schemas.model import GeneralResponse


class UserBase(BaseModel):
    uid: str
    email: EmailStr
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None


class UserCreate(UserBase):
    ...


class UserUpdate(BaseModel):
    email: str | None
    names: str | None
    last_names: str | None
    address: str | None
    age: int | None


class UserInDB(GeneralResponse, UserBase):
    ...


class UserSearch(BaseModel):
    names__icontains: str | None = Field(None, alias="names")
    email__icontains: str | None = Field(None, alias="email")

    class Config:
        allow_population_by_field_name = True