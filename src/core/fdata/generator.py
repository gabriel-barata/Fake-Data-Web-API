from sqlalchemy.orm import Session
from faker import Faker

from datetime import date

from core.database.models import Customers


class DataGenerator():

    def __init__(self, faker: Faker, db: Session, max_rows: int):

        self.faker = faker
        self.db = db
        self.max_rows = max_rows

        self._generate_customers_data()

    @staticmethod
    def __generate_random_password():

        import hashlib
        import secrets

        random_string = secrets.token_hex(8)

        hashed_password = hashlib.sha256(random_string.encode()).hexdigest()

        return hashed_password

    @staticmethod
    def __generate_cpf():

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

    def _generate_customers_data(self):

        for i in range(0, self.max_rows):

            created_at = self.faker.date_time_between(
                start_date=date(2020, 1, 1))

            customer_dict = {
                "first_name": self.faker.first_name(),
                "last_name": self.faker.last_name(),
                "email": self.faker.unique.free_email(),
                "username": self.faker.unique.user_name(),
                "phone_number": self.faker.phone_number(),
                "birth_date": self.faker.date_of_birth(
                    minimum_age=18,
                    maximum_age=60),
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
