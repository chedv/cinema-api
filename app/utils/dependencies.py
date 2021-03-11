from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.database import DBSession
from ..database import models
from .auth import oauth2_schema, decode_access_token


def get_db_session():
    db_session = DBSession()
    try:
        yield db_session
    finally:
        db_session.close()


def get_current_user(token: str = Depends(oauth2_schema), 
                     db_session: Session = Depends(get_db_session)) -> models.User:
    user_model = decode_access_token(db_session, token)
    if user_model is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Authentication credentials were not provided')
    return user_model
