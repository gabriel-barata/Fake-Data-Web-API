from core.database.base import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=func.now())
