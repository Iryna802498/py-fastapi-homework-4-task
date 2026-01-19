from datetime import date
from fastapi import Form
from pydantic import BaseModel, field_validator, ConfigDict

from validation import (
    validate_name,
    validate_gender,
    validate_birth_date
)


class ProfileRequestSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str

    @field_validator("first_name")
    @classmethod
    def valid_first_name(cls, value: str) -> str:
        result = validate_name(
            name=value
        )
        return result

    @field_validator("last_name")
    @classmethod
    def valid_last_name(cls, value: str) -> str:
        result = validate_name(
            name=value
        )
        return result

    @field_validator("gender")
    @classmethod
    def valid_gender(cls, value: str) -> str:
        result = validate_gender(gender=value)
        return result

    @field_validator("date_of_birth")
    @classmethod
    def valid_date(cls, value: date) -> date:
        result = validate_birth_date(
            birth_date=value
        )
        return result

    @field_validator("info")
    @classmethod
    def valid_info(cls, value: str) -> str:
        if not value or value == "   ":
            raise ValueError("Info field cannot be empty or contain only spaces.")
        return value

    @classmethod
    def as_form(
        cls,
        first_name: str = Form(...),
        last_name: str = Form(...),
        gender: str = Form(...),
        date_of_birth: date = Form(...),
        info: str = Form(...)
    ):
        return cls(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            info=info
        )


class ProfileResponseSchema(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str
    avatar: str

    model_config = ConfigDict(from_attributes=True)
