from uuid import UUID
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, status, Depends, HTTPException

from ..schemas import FilmSchema, FilmOutputSchema
from ..database.access import films
from ..utils.dependencies import get_db_session
from ..utils.auth import oauth2_schema


film_router = APIRouter(tags=['film'])


@film_router.post('/films', status_code=status.HTTP_201_CREATED)
def create_film(film: FilmSchema,
                token: str = Depends(oauth2_schema),
                db_session: Session = Depends(get_db_session)):
    print(token)
    try:
        film_model = films.create_film(db_session, film)
    except IntegrityError:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail='Film with specified parameters already exists')
    return {'film_uuid': film_model.id}


@film_router.get('/films', response_model=List[FilmOutputSchema])
def get_films(film_name: Optional[str] = None, db_session: Session = Depends(get_db_session)):
    if film_name is None:
        return films.get_films(db_session)
    else:
        return films.get_film_by_name(db_session, film_name)


@film_router.get('/films/{film_id}', response_model=FilmOutputSchema)
def get_film(film_id: UUID, db_session: Session = Depends(get_db_session)):
    film_model = films.get_film_by_uuid(db_session, film_id)
    if film_model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return film_model
