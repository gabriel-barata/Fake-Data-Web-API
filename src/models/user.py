from pydantic import BaseModel, EmailStr, model_validator
from core.variables import PASSWORD_LENGTH, SPECIAL_CHARACTERS


class UserRequest(BaseModel):

    name: str | None = None
    username: str
    email: EmailStr
    password1: str
    password2: str

    @model_validator(mode="after")
    def check_passwords_match(self):

        pw1 = self.password1
        pw2 = self.password2

        if pw1 != pw2:
            raise ValueError("passwords does not match")

        is_valid = (len(pw1) > PASSWORD_LENGTH
                    and any(c.isupper() for c in pw1)
                    and any(c.islower() for c in pw1)
                    and any(c in SPECIAL_CHARACTERS for c in pw1))

        if not is_valid:
            raise ValueError('password does not match the requirements')

        return self
