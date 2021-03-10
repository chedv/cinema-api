from uuid import UUID
from typing import Optional, List
from sqlalchemy.orm import Session

from .. import models
from ...schemas import CinemaSchema


def create_cinema(db_session: Session, cinema: CinemaSchema) -> models.Cinema:
    cinema_model = models.Cinema(**cinema.dict())
    db_session.add(cinema_model)
    db_session.commit()
    return cinema_model


def get_cinema_by_uuid(db_session: Session, uuid: UUID) -> Optional[models.Cinema]:
    return db_session.query(models.Cinema).filter(models.Cinema.id == uuid).first()


def get_cinema_by_name(db_session: Session, name: str) -> Optional[models.Cinema]:
    return db_session.query(models.Cinema).filter(models.Cinema.cinema_name == name).first()


def get_cinemas(db_session: Session) -> List[models.Cinema]:
    return db_session.query(models.Cinema).all()


def get_cinemas_by_city(db_session: Session, city: str) -> List[models.Cinema]:
    return db_session.query(models.Cinema).filter(models.Cinema.city_name == city).all()
