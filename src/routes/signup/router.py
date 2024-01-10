from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.user import UserRequest
from sqlalchemy.orm import Session
from core.database.models import Users
from core.database.database import get_db
from core.utils import hash_password

router = APIRouter(prefix="/sign_up", tags=["Sign up"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def sign_up(data: UserRequest, db: Session = Depends(get_db)):

    """
    This route is used to create an user
    """

    user = db.query(Users).filter(Users.email == data.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="email already registered")

    new_user = Users(
        name=data.name,
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password1),
    )

    db.add(new_user)
    db.commit()

    payload = {"message": "User account succesfully created"}

    return JSONResponse(content=payload)
