from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from core.database.database import SessionLocal
from core.utils import verify_token_valid

from typing import Generator

oauth = OAuth2PasswordBearer(tokenUrl='/auth')


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_token(token: str = Depends(oauth)):
    verify_token_valid(access_token=token)
