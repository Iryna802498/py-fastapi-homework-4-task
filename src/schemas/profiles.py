from datetime import date
from typing import Annotated
from fastapi import UploadFile, File
from pydantic import BaseModel, field_validator, ConfigDict

from validation import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date
)


class ProfileRequestSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str
    avatar: Annotated[UploadFile, File()]

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
        if not value.strip():
            raise ValueError("Info field cannot be empty or contain only spaces.")
        return value

    @field_validator("avatar")
    @classmethod
    def valid_avatar(cls, value: UploadFile) -> UploadFile:
        result = validate_image(
            avatar=value
        )
        return result


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
