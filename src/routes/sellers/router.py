from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_pag
from fastapi_pagination import (
    Page,
    add_pagination,
    Params
)
from fastapi import (
    APIRouter,
    Depends,
    Path,
    Query
    )
from sqlalchemy.orm import Session

from typing import Annotated
from datetime import datetime

from core.dependencies import get_db, validate_token
from models.sellers import SellerResponse
from core.database.models import Sellers

router = APIRouter(
    prefix="/sellers",
    tags=["Sellers"],
    dependencies=[Depends(validate_token)])


@router.get("", response_model=Page[SellerResponse])
async def get_sellers(
    db: Session = Depends(get_db),
    page: Annotated[int, Query(
        ge=1,
        description="The page returned"
    )] = 1,
    size: Annotated[int, Query(
        ge=1,
        le=50,
        description="The number of results per page"
    )] = 20,
    min_creation_date: Annotated[str | None, Query(
        description="Customers created after | format => DD-MM-YYYY"
    )] = None,
    max_creation_date: Annotated[str | None, Query(
        description="Customers created after | format => DD-MM-YYYY"
    )] = None
):

    """
    This route brings all sellers given the provided query values
    """

    params = Params(page=page, size=size)

    sellers = db.query(Sellers)

    if min_creation_date:

        sellers = sellers.filter(Sellers.created_at >= datetime.strptime(
            min_creation_date, "%d-%m-%Y"
        ))

    if max_creation_date:

        sellers = sellers.filter(Sellers.created_at <= datetime.strptime(
            max_creation_date, "%d-%m-%Y"
        ))

    return sqlalchemy_pag(sellers, params=params)


@router.get("/{identifier}", response_model=SellerResponse)
async def get_seller(
    identifier: Annotated[str, Path(
        title="id or name",
        description="The id or name of the requested seller"
    )],
    db: Session = Depends(get_db)
):

    """
    This route brings a specific seller by id or name
    """

    seller = db.query(Sellers)

    if identifier.isdigit():
        identifier = int(identifier)
        seller = seller.filter(Sellers.id == identifier).first()

    else:
        seller = seller.filter(Sellers.name == identifier).first()

    return seller


add_pagination(router)
