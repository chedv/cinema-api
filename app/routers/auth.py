from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..schemas import UserRegistrationSchema, UserLoginSchema
from ..database.access.users import create_user
from ..utils.dependencies import get_db_session
from ..utils.auth import authenticate, create_access_token


auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegistrationSchema = Depends(UserRegistrationSchema.as_form),
                  db_session: Session = Depends(get_db_session)):
    try:
        user_model = create_user(db_session, user, user_role='client')
    except IntegrityError:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='User with specified parameters already exists')
    return {'user_uuid': user_model.id}


@auth_router.post('/login')
def login_user(user: UserLoginSchema = Depends(UserLoginSchema.as_form),
               db_session: Session = Depends(get_db_session)):
    user_model = authenticate(db_session, user.email, user.raw_password)
    if not user_model:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid email or password')

    acces_token = create_access_token(user_model)
    return {'access_token': acces_token, 'token_type': 'bearer'}
