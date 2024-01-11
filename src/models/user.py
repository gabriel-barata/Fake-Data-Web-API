from pydantic import BaseModel, EmailStr, field_validator
from core.variables import PASSWORD_LENGTH, SPECIAL_CHARACTERS
import re


class UserRequest(BaseModel):

    name: str | None = None
    username: str
    email: EmailStr
    password: str

    @field_validator('password')
    def check_password_match_requirements(cls, value: str):

        pwd = value

        is_valid = (len(pwd) > PASSWORD_LENGTH
                    and any(c.isupper() for c in pwd)
                    and any(c.islower() for c in pwd)
                    and any(c in SPECIAL_CHARACTERS for c in pwd)
                    and any(c.isdigit() for c in pwd))

        if not is_valid:
            raise ValueError('password does not match the requirements')

        return pwd

    @field_validator('username')
    def check_username_match_requiremnets(cls, value: str):

        username = value

        if not re.match('^[a-zA-Z0-9_]+$', value):
            raise ValueError('username does not match the requirements')

        return username
