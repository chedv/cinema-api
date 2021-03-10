import uuid
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import BaseModel


user_cinema_session = Table(
    'user_cinema_session',
    BaseModel.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id')),
    Column('cinema_session_id', UUID(as_uuid=True), ForeignKey('cinema_session.id'))
)


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    cinema_sessions = relationship('CinemaSession', secondary=user_cinema_session, back_populates='users')


class Cinema(BaseModel):
    __tablename__ = 'cinema'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    cinema_name = Column(String, unique=True, nullable=False, index=True)
    cinema_address = Column(String, unique=True, nullable=False)
    city_name = Column(String, nullable=False)

    cinema_sessions = relationship('CinemaSession', back_populates='cinema')


class Film(BaseModel):
    __tablename__ = 'film'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    film_name = Column(String, unique=True, nullable=False, index=True)
    film_duration = Column(Integer, nullable=False)

    cinema_sessions = relationship('CinemaSession', back_populates='film')


class CinemaSession(BaseModel):
    __tablename__ = 'cinema_session'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    session_place = Column(String, unique=True, nullable=False)
    session_start = Column(DateTime, nullable=False)
    session_price = Column(Numeric(precision=5, scale=2), nullable=False)
    cinema_id = Column(UUID(as_uuid=True), ForeignKey('cinema.id'), nullable=False)
    film_id = Column(UUID(as_uuid=True), ForeignKey('film.id'), nullable=False)

    cinema = relationship('Cinema', back_populates='cinema_sessions')
    film = relationship('Film', back_populates='cinema_sessions')
    users = relationship('User', secondary=user_cinema_session, back_populates='cinema_sessions')
