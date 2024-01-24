from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_pag
from fastapi_pagination import (
    Page,
    add_pagination,
    Params
)
from fastapi import (
    APIRouter,
    Depends,
    Query
     )
from sqlalchemy.orm import Session

from typing import Annotated

from models.categories import CategoryResponse
from core.dependencies import get_db, validate_token
from core.database.models import Categories


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    dependencies=[Depends(validate_token)]
)


@router.get("", response_model=Page[CategoryResponse])
async def get_categories(
    db: Session = Depends(get_db),
    page: Annotated[int, Query(
        ge=1,
        description="The page returned"
    )] = 1,
    size: Annotated[int, Query(
        ge=1, le=50,
        description="The number of results per page"
    )] = 20
):

    categories = db.query(Categories)

    params = Params(page=page, size=size)

    return sqlalchemy_pag(categories, params=params)


add_pagination(router)
