import re
from datetime import date
from io import BytesIO

from PIL import Image
from fastapi import UploadFile

from database.models.accounts import GenderEnum


def validate_name(name: str) -> None:
    if re.fullmatch(r'[A-Za-z]+', name) is None:
        raise ValueError(f'{name} contains non-english letters')


def validate_image(avatar: UploadFile) -> None:
    supported_image_formats = ["JPG", "JPEG", "PNG"]
    max_file_size = 1 * 1024 * 1024

    contents = avatar.file.read()
    if len(contents) > max_file_size:
        raise ValueError("Image size exceeds 1 MB")

    try:
        image = Image.open(BytesIO(contents))
        image_format = image.format
        if image_format not in supported_image_formats:
            raise ValueError(f"Unsupported image format: {image_format}. Use one of next: {supported_image_formats}")
    except IOError:
        raise ValueError("Invalid image format")
    finally:
        avatar.file.seek(0)


def validate_gender(gender: str) -> None:
    if gender not in [g.value for g in GenderEnum]:
        raise ValueError(f"Gender must be one of: {', '.join(g.value for g in GenderEnum)}")


def calculate_years(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def validate_birth_date(birth_date: date) -> None:
    if birth_date.year < 1900:
        raise ValueError('Invalid birth date - year must be greater than 1900.')

    age = calculate_years(birth_date=birth_date)
    if age < 18:
        raise ValueError('You must be at least 18 years old to register.')


def validate_info(info: str) -> None:
    if not info or len(info.strip()) == 0:
        raise ValueError('Info field cannot be empty or contain only spaces.')
