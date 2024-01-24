from pydantic import BaseModel


class ProductResponse(BaseModel):

    id: int
    ean: str
    name: str
    name_length: int
    description: str | None
    category_id: int

    weight: float | None
    length: float | None
    height: float | None
    width: float | None

    price: float
    seller_id: int
