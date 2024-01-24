from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_pag
from fastapi_pagination import (
    Page,
    add_pagination,
    Params
    )
from fastapi import (
    APIRouter,
    Depends,
    Query,
    Path
    )
from sqlalchemy.orm import Session

from typing import Annotated

from core.dependencies import get_db, validate_token
from models.products import ProductResponse
from core.database.models import Products


router = APIRouter(
            prefix="/products",
            tags=["Products"],
            dependencies=[Depends(validate_token)])


@router.get("", response_model=Page[ProductResponse])
async def get_products(
    db: Session = Depends(get_db),
    page: Annotated[int, Query(
        ge=1,
        description="the page returned"
    )] = 1,
    size: Annotated[int, Query(
        ge=1, le=50,
        description="the number of products returned per page"
    )] = 20,
    category_id: Annotated[int, Query(
        ge=0, description="the id of the category for the returned items"
    )] = None,
    min_price: Annotated[float, Query(
        description="minimal price for items"
    )] = None,
    max_price: Annotated[float, Query(
        ge=0,
        description="maximum price for items"
    )] = None,

):

    """
    This function returns all the products given the query parameters
    """

    products = db.query(Products)

    if category_id:

        products = products.filter(Products.category_id == category_id)

    if min_price:

        products = products.filter(Products.price >= min_price)

    if max_price:

        products = products.filter(Products.price <= max_price)

    params = Params(page=page, size=size)

    return sqlalchemy_pag(products, params=params)


@router.get("/{id}", response_model=ProductResponse)
async def get_product(
    id: Annotated[int, Path(
        ge=1,
        title="Product Id",
        description="The id of the requested product"
    )],
    db: Session = Depends(get_db)
):

    """
    This function returns a specific product given an id
    """

    product = db.query(Products).filter(Products.id == id).first()

    return product

add_pagination(router)
