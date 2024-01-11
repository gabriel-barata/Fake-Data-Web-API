from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.user import UserRequest
from sqlalchemy.orm import Session
from core.database.models import Users
from core.dependencies import get_db
from core.utils import hash_password

router = APIRouter(prefix="/sign_up", tags=["Sign up"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=dict)
async def sign_up(data: UserRequest, db: Session = Depends(get_db)):

    """
    This route is used to create an user
    """

    email = db.query(Users).filter(Users.email == data.email).first()
    if email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="email already registered")

    username = db.query(Users).filter(Users.username == data.username).first()
    if username:
        raise HTTPException(detail="username already in use",
                            status_code=status.HTTP_409_CONFLICT)

    new_user = Users(
        name=data.name,
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password),
    )

    db.add(new_user)
    db.commit()

    payload = {
        "message": "User account succesfully created",
        "Account": {
            "email": data.email,
            "username": data.username
            }
        }

    return JSONResponse(content=payload, status_code=status.HTTP_201_CREATED)
