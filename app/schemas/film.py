from uuid import UUID
from pydantic import BaseModel, Field, validator

from .base import validate_name, validate_duration


class FilmSchema(BaseModel):
    film_name: str = Field(...)
    film_duration: int = Field(...)

    _validate_name = validator('film_name', allow_reuse=True)(validate_name)
    _validate_duration = validator('film_duration', allow_reuse=True)(validate_duration)

    class Config:
        orm_mode = True


class FilmOutputSchema(FilmSchema):
    id: UUID
