from fastapi import FastAPI

from .routers import auth_router
from .handlers import ValidationError, validation_exception_handler


app = FastAPI()
app.include_router(auth_router, prefix='/api/v1')
app.add_exception_handler(ValidationError, validation_exception_handler)
