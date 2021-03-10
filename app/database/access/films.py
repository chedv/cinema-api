from uuid import UUID
from typing import Optional, List
from sqlalchemy.orm import Session

from .. import models
from ...schemas import FilmSchema


def create_film(db_session: Session, film: FilmSchema) -> models.Film:
    film_model = models.Film(**film.dict())
    db_session.add(film_model)
    db_session.commit()
    return film_model


def get_film_by_uuid(db_session: Session, uuid: UUID) -> Optional[models.Film]:
    return db_session.query(models.Film).filter(models.Film.id == uuid).first()


def get_film_by_name(db_session: Session, name: str) -> Optional[models.Film]:
    return db_session.query(models.Film).filter(models.Film.film_name == name).first()


def get_films(db_session: Session) -> List[models.Film]:
    return db_session.query(models.Film).all()
