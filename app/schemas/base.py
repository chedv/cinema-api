import inspect
from typing import Type
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from pydantic import BaseModel
from pydantic.fields import ModelField
from fastapi import Form


lowercase_letters = set(ascii_lowercase)
uppercase_letters = set(ascii_uppercase)
special_chars = set(punctuation)
digit_chars = set(digits)

valid_name_chars = set(ascii_lowercase + ' ')
valid_address_chars = set(ascii_lowercase + digits + ' ,')


def validate_name(cls, v):
    if v is None:
        return v
    if any(char.lower() not in valid_name_chars for char in v):
        raise ValueError('Name must contain only letters and white spaces')
    return v


def validate_address(cls, v):
    if v is None:
        return v
    if any(char.lower() not in valid_address_chars for char in v):
        raise ValueError('Address must contain only letters, digits, commas and white spaces')
    return v


def validate_password(cls, v):
    min_len = 8
    if len(v) < min_len:
        raise ValueError('Password must contain at least eight characters')
    if all(char not in uppercase_letters for char in v):
        raise ValueError('Password must contain at least one uppercase letter')
    if all(char not in digit_chars for char in v):
        raise ValueError('Password must contain at least one digit')
    if all(char not in special_chars for char in v):
        raise ValueError('Password must contain at least one special character')
    return v


def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, field_model in cls.__fields__.items():
        new_parameters.append(
            inspect.Parameter(
                field_model.alias,
                inspect.Parameter.POSITIONAL_ONLY,
                default=Form(...) if field_model.required else Form(field_model.default),
                annotation=field_model.outer_type_,
            )
        )

    async def as_form_func(**data):
        return cls(**data)

    signature = inspect.signature(as_form_func)
    signature = signature.replace(parameters=new_parameters)
    as_form_func.__signature__ = signature

    setattr(cls, 'as_form', as_form_func)
    return cls
