from datetime import date
from typing import Annotated, Optional
from fastapi import UploadFile, File
from pydantic import BaseModel, ConfigDict, AfterValidator

from validation.profile import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date,
    validate_info
)


class ProfileRequestSchema(BaseModel):
    first_name: Annotated[str, AfterValidator(validate_name)]
    last_name: Annotated[str, AfterValidator(validate_name)]
    gender: Annotated[str, AfterValidator(validate_gender)]
    date_of_birth: Annotated[date, AfterValidator(validate_birth_date)]
    info: Annotated[str, AfterValidator(validate_info)]
    avatar: Annotated[UploadFile, AfterValidator(validate_image)]


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
