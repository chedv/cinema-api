from fastapi import Depends

from app.database.database import DBSession
from .auth import oauth2_schema


def get_db_session():
    db_session = DBSession()
    try:
        yield db_session
    finally:
        db_session.close()


def get_current_user(token: str = Depends(oauth2_schema)):
    return token
