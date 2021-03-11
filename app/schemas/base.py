import inspect
from typing import Type, Optional, Set
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from pydantic import BaseModel
from pydantic.fields import ModelField
from fastapi import Form


lowercases_whitespace = set(ascii_lowercase + ' ')
lowercases_digits_whitespace = set(ascii_lowercase + digits + ' ')
lowercases_digits_whitespace_comma = set(ascii_lowercase + digits + ' ,')

lowercases = set(ascii_lowercase)
uppercases = set(ascii_uppercase)
specials = set(punctuation)
digits = set(digits)


def validate_string(v: str, valid_chars: Set[str], error_msg: str):
    if any(char.lower() not in valid_chars for char in v):
        raise ValueError(error_msg)


def validate_range(v: int, left: Optional[int] = None, right: Optional[int] = None) -> None:
    if (left is not None and v < left) or (right is not None and v > right):
        raise ValueError('Value is out of range')


def validate_password(v: str, **kwargs) -> None:
    min_length = kwargs.get('min_length')

    if min_length and len(v) < min_length:
        raise ValueError('Password must contain at least eight characters')
    if kwargs.get('uppercase') and all(char not in uppercases for char in v):
        raise ValueError('Password must contain at least one uppercase letter')
    if kwargs.get('digit') and all(char not in digits for char in v):
        raise ValueError('Password must contain at least one digit')
    if kwargs.get('special') and all(char not in specials for char in v):
        raise ValueError('Password must contain at least one special character')


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
