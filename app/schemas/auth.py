from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator

from .base import as_form, validate_name, validate_password


@as_form
class UserRegistrationSchema(BaseModel):
    email: EmailStr = Field(...)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    raw_password: str = Field(..., alias='password')

    _validate_name = validator('first_name', 'last_name', allow_reuse=True)(validate_name)
    _validate_password = validator('raw_password', allow_reuse=True)(validate_password)

    class Config:
        orm_mode = True


@as_form
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    raw_password: str = Field(..., alias='password')
