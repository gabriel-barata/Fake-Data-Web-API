from sqlalchemy.orm import Session
from sqlalchemy import func
from faker import Faker

from datetime import date
import json

from core.database.models import (
    Customers,
    Products,
    Categories,
    Sellers
)
from core.variables import PRODUCTS_FILE, MULTI_FACTOR


class DataGenerator():

    def __init__(self, faker: Faker, db: Session, max_rows: int):

        self.faker = faker
        self.db = db
        self.max_rows = max_rows

        self._generate_customers_data()
        self._generate_sellers_data(MULTI_FACTOR)
        self._generate_products_and_categories_data()

    @staticmethod
    def __generate_random_password():

        """
        This function genrates a random hashed passowrd
        """

        import hashlib
        import secrets

        random_string = secrets.token_hex(8)

        hashed_password = hashlib.sha256(random_string.encode()).hexdigest()

        return hashed_password

    @staticmethod
    def __generate_cpf():

        """
        This function generates a random fictional CPF
        """

        from random import randrange

        numeros = [randrange(10) for _ in range(9)]
        n1, n2, n3, n4, n5, n6, n7, n8, n9 = numeros

        a = [num * (i + 2) for i, num in enumerate(reversed(numeros))]
        d1 = (sum(a) % 11)
        d1 = d1 if d1 < 10 else 0

        a = [d1 * (i + 2) for i in range(9)] + a
        d2 = 11 - (sum(a) % 11)
        d2 = d2 if d2 < 10 else 0

        cpf = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(
            *numeros, d1, d2
        )

        return cpf

    @staticmethod
    def __nullable(func, true_prob: float = 0.7, **kwargs):

        """
        This function is a way I found to generate null data over the columns
        """

        import random

        result = random.random() < true_prob

        if result:
            return func(**kwargs)

        else:
            return None

    @staticmethod
    def __simple_return(string: str):
        return string

    def _generate_customers_data(self):

        for i in range(0, self.max_rows):

            created_at = self.faker.date_time_between(
                start_date=date(2020, 1, 1))

            customer_dict = {
                "first_name": self.faker.first_name(),
                "last_name": self.faker.last_name(),
                "email": self.faker.unique.free_email(),
                "username": self.__nullable(
                    self.faker.unique.user_name),
                "phone_number": self.__nullable(
                    self.faker.phone_number),
                "birth_date": self.__nullable(
                    self.faker.date_of_birth,
                    **dict(minimum_age=18, maximum_age=60)),
                "postcode": self.faker.postcode(),
                "country": self.faker.current_country(),
                "city": self.faker.city(),
                "address": self.faker.street_address(),
                "hashed_password": self.__generate_random_password(),
                "cpf": self.__generate_cpf(),
                "created_at": created_at,
                "updated_at": self.faker.date_time_between(
                    start_date=created_at
                ),
                "is_active": self.faker.pybool(truth_probability=70)
            }

            current_customer = Customers(**customer_dict)
            self.db.add(current_customer)
            self.db.commit()

    def _generate_sellers_data(self, MULTI_FACTOR: float):

        for i in range(round(self.max_rows * MULTI_FACTOR)):

            created_at = self.faker.date_time_between(
                start_date=date(2020, 1, 1))

            seller_dict = {
                "name": self.faker.unique.company(),
                "postcode": self.faker.postcode(),
                "country": self.faker.current_country(),
                "city": self.faker.city(),
                "created_at": created_at,
                "updated_at": self.faker.date_time_between(
                    start_date=created_at),
                "is_active": self.faker.pybool(truth_probability=90)
            }

            seller = Sellers(**seller_dict)
            self.db.add(seller)
            self.db.commit()

    def _generate_products_and_categories_data(self):

        with open(PRODUCTS_FILE, 'r') as file:

            json_file = json.load(file)

        for _category, data in json_file['categories'].items():

            category_dict = {
                "name": _category,
                "description": data["description"]
            }

            category = Categories(**category_dict)
            self.db.add(category)
            self.db.commit()

            for prod in data["items"]:

                category = self.db.query(Categories).filter(
                    Categories.name == _category).first()

                seller = self.db.query(Sellers.id).order_by(
                    func.random()).first()

                prod_dict = {
                    "ean": self.faker.unique.ean(),
                    "name": prod["name"],
                    "name_length": len(prod["name"]),
                    "description": self.__nullable(
                        self.__simple_return,
                        **dict(string=prod["description"])),
                    "category_id": category.id,
                    "weight": self.__nullable(
                        self.__simple_return,
                        **dict(string=prod["weight"])),
                    "length": self.__nullable(
                        self.__simple_return,
                        **dict(string=prod["length"])),
                    "height": self.__nullable(
                        self.__simple_return,
                        **dict(string=prod["height"])),
                    "width": self.__nullable(
                        self.__simple_return,
                        **dict(string=prod["width"])),
                    "price": prod["price"],
                    "seller_id": seller.id
                }

                product = Products(**prod_dict)
                self.db.add(product)
                self.db.commit()

    def _generate_orders_data():

        ...
