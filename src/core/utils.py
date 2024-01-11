from passlib.context import CryptContext
from dotenv import load_dotenv
from jose import jwt, JWTError
from fastapi import HTTPException, status
import os

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):

    return pwd_context.hash(password)


def check_hashed_password(username, password):

    return pwd_context.verify(username, password)


def verify_token_valid(access_token):

    try:
        jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid Token")

    return True
