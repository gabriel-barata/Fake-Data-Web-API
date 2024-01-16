from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_pag
from fastapi_pagination import Page, add_pagination, Params
from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from typing import Annotated
from datetime import datetime

from core.dependencies import get_db, validate_token
from core.database.models import Customers
from models.customers import CustomerResponse

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
    dependencies=[Depends(validate_token)])


@router.get("", response_model=Page[CustomerResponse])
async def get_customers(
    db: Session = Depends(get_db),
    page: Annotated[int, Query(
        ge=1,
        description="The return page")] = 1,
    size: Annotated[int, Query(
        ge=1,
        le=50,
        description="The number of results per page")] = 20,
    min_creation_date: Annotated[str | None, Query(
        description="Customers created after | format => DD-MM-YYYY"
    )] = None,
    max_creation_date: Annotated[str | None, Query(
        description="Customers created after | format => DD-MM-YYYY"
    )] = None
):

    """
    This route brings all customers given the provided query values
    """

    customers = db.query(Customers)

    if min_creation_date:

        customers = customers.filter(Customers.created_at >= datetime.strptime(
            min_creation_date, "%d-%m-%Y"
        ))

    if max_creation_date:

        customers = customers.filter(Customers.created_at <= datetime.strptime(
            max_creation_date, "%d-%m-%Y"
        ))

    params = Params(page=page, size=size)

    return sqlalchemy_pag(customers, params=params)


@router.get("/{identifier}", response_model=CustomerResponse)
async def get_customer(
    identifier: Annotated[str, Path(
        description="id or username of the requested customer",
        title="id or username")],
    db: Session = Depends(get_db)
):

    """
    This route brings a specific customer by id or username
    """

    customer = db.query(Customers)

    if identifier.isdigit():
        identifier = int(identifier)
        customer = customer.filter(Customers.id == identifier).first()

    else:
        customer = customer.filter(Customers.username == identifier).first()

    return customer

add_pagination(router)
