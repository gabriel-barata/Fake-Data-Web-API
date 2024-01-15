from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Boolean,
    )
from core.database.base import Base


class Users(Base):

    """
    This table keeps API users data.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=True, server_default=func.now())


class Customers(Base):

    __tablename__ = "customers"

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    phone_number = Column(String(12), nullable=True)
    birth_date = Column(String(10), nullable=True)

    postcode = Column(String(9), nullable=False)
    country = Column(String(60), nullable=False)
    city = Column(String(85), nullable=False)
    address = Column(String(255), nullable=True)

    hashed_password = Column(String(255), nullable=False)
    cpf = Column(String(14), unique=True)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    is_active = Column(Boolean)
