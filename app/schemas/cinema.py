from uuid import UUID
from pydantic import BaseModel, Field, validator

from .base import validate_name, validate_address


class CinemaSchema(BaseModel):
    cinema_name: str
    cinema_address: str
    city_name: str

    _validate_name = validator('cinema_name', allow_reuse=True)(validate_name)
    _validate_address = validator('cinema_address', allow_reuse=True)(validate_address)

    class Config:
        orm_mode = True


class CinemaOutputSchema(CinemaSchema):
    id: UUID
