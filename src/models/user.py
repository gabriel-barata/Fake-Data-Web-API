from pydantic import BaseModel, EmailStr, model_validator
from core.variables import PASSWORD_LENGTH, SPECIAL_CHARACTERS


class UserRequest(BaseModel):

    name: str | None = None
    username: str
    email: EmailStr
    password: str

    @model_validator(mode="after")
    def check_password_match_requirements(self):

        pwd = self.password

        is_valid = (len(pwd) > PASSWORD_LENGTH
                    and any(c.isupper() for c in pwd)
                    and any(c.islower() for c in pwd)
                    and any(c in SPECIAL_CHARACTERS for c in pwd))

        if not is_valid:
            raise ValueError('password does not match the requirements')

        return self
