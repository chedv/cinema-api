from uuid import UUID
from sqlalchemy.orm import Session

from .. import models
from ...schemas import UserRegistrationSchema
from ... import utils


def create_user(db_session: Session, user: UserRegistrationSchema, user_role: str) -> models.User:
    hashed_password = utils.PasswordContext.get_hashed_password(user.raw_password)
    user = models.User(**user.dict(exclude={'raw_password'}), hashed_password=hashed_password, role=user_role)
    db_session.add(user)
    db_session.commit()
    return user


def get_user_by_uuid(db_session: Session, uuid: UUID) -> models.User:
    return db_session.query(models.User).filter(models.User.id == uuid).first()


def get_user_by_email(db_session: Session, email: str) -> models.User:
    return db_session.query(models.User).filter(models.User.email == email).first()
