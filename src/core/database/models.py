from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Boolean,
    ForeignKey,
    BigInteger,
    Float
    )
from sqlalchemy.orm import declarative_base


Base = declarative_base()


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
    username = Column(String(30), nullable=True, unique=True)
    phone_number = Column(String(12), nullable=True)
    birth_date = Column(String(10), nullable=True)

    postcode = Column(String(9), nullable=False)
    country = Column(String(60), nullable=False)
    city = Column(String(85), nullable=False)
    address = Column(String(255), nullable=False)

    hashed_password = Column(String(255), nullable=False)
    cpf = Column(String(14), unique=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    is_active = Column(Boolean, nullable=False)


class Categories(Base):

    __tablename__ = 'categories'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(55), nullable=False)
    description = Column(String(255), nullable=True)


class Sellers(Base):

    __tablename__ = 'sellers'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(55), nullable=False)
    postcode = Column(String(9), nullable=False)
    country = Column(String(60), nullable=False)
    city = Column(String(85), nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    is_active = Column(Boolean, nullable=False)


class Products(Base):

    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ean = Column(BigInteger, unique=True)
    name = Column(String, nullable=False)
    name_length = Column(String(55), nullable=False)
    description = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    weight = Column(Float(2), nullable=True)
    length = Column(Float(2), nullable=True)
    height = Column(Float(2), nullable=True)
    width = Column(Float(2), nullable=True)

    price = Column(Float(2), nullable=False)
    seller_id = Column(Integer, ForeignKey('sellers.id'))
