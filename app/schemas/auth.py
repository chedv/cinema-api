from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator

from .base import as_form, validate_string, validate_password, lowercases


@as_form
class UserRegistrationSchema(BaseModel):
    email: EmailStr = Field(...)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    raw_password: str = Field(..., alias='password')

    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if v is not None:
            validate_string(v, valid_chars=lowercases, error_msg='Name must contain only letters')
        return v

    @validator('raw_password')
    def validate_raw_password(cls, v):
        validate_password(v, min_length=8, uppercase=True, digit=True, special=True)
        return v

    class Config:
        orm_mode = True


@as_form
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    raw_password: str = Field(..., alias='password')
