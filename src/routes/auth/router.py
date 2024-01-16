from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    )
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from jose import jwt

from datetime import datetime, timedelta
from typing import Annotated
import os

from core.dependencies import get_db
from core.utils import check_hashed_password
from core.database.models import Users
from models.token import TokenResponse
from models.user import UserLogin

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
TOKEN_EXP = int(os.environ.get("TOKEN_EXP"))

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def authenticate(
        request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)):

    """
    This route is used to authenticate user's credentials on system.
    Returns an access token.
    """

    data = UserLogin(
        username=request_form.username,
        password=request_form.password
        )

    user = db.query(Users).filter(Users.username == data.username).first()
    if not user:
        raise HTTPException(
            detail="this user does not exist",
            status_code=status.HTTP_400_BAD_REQUEST
            )

    if not check_hashed_password(data.password, user.hashed_password):
        raise HTTPException(
            detail="username or password incorrect",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    expiration = datetime.utcnow() + timedelta(minutes=TOKEN_EXP)
    payload = dict(
        sub=user.username,
        exp=expiration
    )
    access_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)

    return TokenResponse(
        access_token=access_token,
        expires_at=datetime.strftime(expiration, "%a, %d/%m/%y %H:%M:%S")
        )
