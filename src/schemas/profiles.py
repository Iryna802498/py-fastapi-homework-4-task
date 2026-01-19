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
    first_name: Annotated[Optional[str], AfterValidator(validate_name)] = None
    last_name: Annotated[Optional[str], AfterValidator(validate_name)] = None
    gender: Annotated[Optional[str], AfterValidator(validate_gender)] = None
    date_of_birth: Annotated[Optional[date], AfterValidator(validate_birth_date)] = None
    info: Annotated[Optional[str], AfterValidator(validate_info)] = None
    avatar: Annotated[Optional[UploadFile], AfterValidator(validate_image), File()] = None


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
