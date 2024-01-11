from core.database.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Generator
from sqlalchemy.orm import Session
from core.utils import verify_token_valid

oauth = OAuth2PasswordBearer(tokenUrl='/auth')


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_token(db: Session = Depends(get_db), token: str = Depends(oauth)):
    verify_token_valid(access_token=token)
