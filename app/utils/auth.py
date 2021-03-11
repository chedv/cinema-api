import jwt
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..database import models
from ..database.access import users
from settings import settings


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


class PasswordContext:
    context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def verify(cls, raw_password: str, hashed_password: str) -> bool:
        return cls.context.verify(raw_password, hashed_password)

    @classmethod
    def get_hashed_password(cls, raw_password: str) -> str:
        return cls.context.hash(raw_password)


def authenticate(db_session: Session, email: str, raw_password: str) -> Optional[models.User]:
    user = users.get_user_by_email(db_session, email)
    if user and PasswordContext.verify(raw_password, user.hashed_password):
        return user
    return None


def create_access_token(user: models.User, expire_minutes: int = 30) -> str:
    encode_data = {'sub': user.email, 'exp': datetime.utcnow() + timedelta(minutes=expire_minutes)}
    return jwt.encode(encode_data, settings.jwt_secret, algorithm='HS256')


def decode_access_token(db_session: Session, token: str) -> Optional[models.User]:
    try:
        decoded_data = jwt.decode(token, settings.jwt_secret, algorithms=['HS256'])
    except jwt.PyJWTError as exc:
        return
    return users.get_user_by_email(db_session, decoded_data['sub'])
