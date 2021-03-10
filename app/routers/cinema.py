from uuid import UUID
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, status, Depends, HTTPException

from ..schemas import CinemaSchema
from ..database.access import cinemas
from ..utils.dependencies import get_db_session
from ..utils.auth import authenticate, create_access_token


cinema_router = APIRouter(tags=['cinema'])


@cinema_router.post('/cinemas', status_code=status.HTTP_201_CREATED)
def create_cinema(cinema: CinemaSchema, db_session: Session = Depends(get_db_session)):
    try:
        cinema_model = cinemas.create_cinema(db_session, cinema)
    except IntegrityError:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail='Cinema with specified parameters already exists')
    return {'cinema_uuid': cinema_model.id}


@cinema_router.get('/cinemas', response_model=List[CinemaSchema])
def get_cinemas(city_name: Optional[str] = None, db_session: Session = Depends(get_db_session)):
    if city_name is None:
        return cinemas.get_cinemas(db_session)
    else:
        return cinemas.get_cinemas_by_city(db_session, city_name)


@cinema_router.get('/cinemas/{cinema_id}', response_model=CinemaSchema)
def get_cinema(cinema_id: UUID, db_session: Session = Depends(get_db_session)):
    cinema_model = cinemas.get_cinema_by_uuid(db_session, cinema_id)
    if cinema_model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return cinema_model
