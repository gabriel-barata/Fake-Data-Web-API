from datetime import datetime, timedelta
from core.utils import verify_token_valid
from fastapi import APIRouter, Depends, HTTPException, status, Header
from models.token import TokenResponse
from models.user import UserLogin
from core.dependencies import get_db
from sqlalchemy.orm import Session
from core.database.models import Users
from core.utils import check_hashed_password
from dotenv import load_dotenv
from typing import Annotated
from jose import jwt
import os


load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
TOKEN_EXP = int(os.environ.get("TOKEN_EXP"))

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("", status_code=status.HTTP_200_OK, response_model=TokenResponse)
async def authenticate(
        data: UserLogin,
        db: Session = Depends(get_db)):

    """
    This route is used to authenticate user's credentials on system.
    Returns an access token.
    """

    user = db.query(Users).filter(Users.email == data.email).first()
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


@router.get("/test")
async def teste(
    access_token: Annotated[
        str,
        Header(description="Generate this token on /auth")]):

    verify_token_valid(access_token)

    return "working"
