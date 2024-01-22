from pydantic import BaseModel
from datetime import datetime


class SellerResponse(BaseModel):

    id: int
    name: str
    postcode: str
    country: str
    city: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
