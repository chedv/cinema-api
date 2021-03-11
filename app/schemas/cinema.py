from uuid import UUID
from pydantic import BaseModel, Field, validator

from .base import (
    validate_string, 
    lowercases_whitespace, 
    lowercases_digits_whitespace, 
    lowercases_digits_whitespace_comma
)


class CinemaSchema(BaseModel):
    cinema_name: str
    cinema_address: str
    city_name: str

    @validator('cinema_name')
    def validate_name(cls, v):
        validate_string(v, valid_chars=lowercases_digits_whitespace, 
                        error_msg='Name must contain only letters, digits and whitespaces')
        return v

    @validator('cinema_address')
    def validate_address(cls, v):
        validate_string(v, valid_chars=lowercases_digits_whitespace_comma,
                        error_msg='Name must contain only letters, digits, whitespaces and commas')
        return v

    @validator('city_name')
    def validate_city_name(cls, v):
        validate_string(v, valid_chars=lowercases_whitespace,
                        error_msg='Name must contain only letters and whitespaces')
        return v

    class Config:
        orm_mode = True


class CinemaOutputSchema(CinemaSchema):
    id: UUID
