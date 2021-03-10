import functools
from typing import Type
from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError


def validation_exception_handler(request: Request, exception: ValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={'detail': exception.errors()})
