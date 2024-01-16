from pydantic import BaseModel, EmailStr
from datetime import datetime


class CustomerResponse(BaseModel):

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    username: str | None = None
    phone_number: str | None = None
    birth_date: str | None = None
    postcode: str
    country: str
    city: str
    address: str
    hashed_password: str
    cpf: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
