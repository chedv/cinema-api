from app.database.database import DBSession


def get_db_session():
    db_session = DBSession()
    try:
        yield db_session
    finally:
        db_session.close()
