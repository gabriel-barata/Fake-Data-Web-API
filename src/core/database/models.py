from core.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    username = Column(String(100))
    email = Column(String(100), nullable=True)
    hashed_password = Column(String(100))
    created_at = Column(DateTime, nullable=True, server_default=func.now())
