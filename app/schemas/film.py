from uuid import UUID
from pydantic import BaseModel, Field, validator

from .base import validate_string, validate_range, lowercases_digits_whitespace


class FilmSchema(BaseModel):
    film_name: str = Field(...)
    film_duration: int = Field(...)

    @validator('film_name')
    def validate_name(cls, v):
        validate_string(v, valid_chars=lowercases_digits_whitespace,
                        error_msg='Name must contain only letters, digits and whitespaces')
        return v

    @validator('film_duration')
    def validate_duration(cls, v):
        validate_range(v, left=1, right=500)
        return v

    class Config:
        orm_mode = True


class FilmOutputSchema(FilmSchema):
    id: UUID
