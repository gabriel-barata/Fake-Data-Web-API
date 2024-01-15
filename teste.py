from faker import Faker
from datetime import date

faker = Faker("pt_BR")


def __generate_random_password():

    import hashlib
    import secrets

    random_string = secrets.token_hex(8)

    hashed_password = hashlib.sha256(random_string.encode()).hexdigest()

    return hashed_password


def __gera_cpf():

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


print("PERSONAL INFO\n")
print(faker.first_name())
print(faker.last_name())
print(faker.unique.free_email())
print(faker.unique.user_name())
print(faker.phone_number())
print(faker.date_of_birth(minimum_age=18, maximum_age=60))

print("\nADDRESS\n")
print(faker.postcode())
print(faker.current_country())
print(faker.city())
print(faker.street_address())

print("\nSENSITIVE INFO\n")
print(__generate_random_password())
print(__gera_cpf())

print("APP RELATED DATA")
created_at = faker.date_time_between(
    start_date=date(2020, 1, 1))
print(created_at)
print(faker.date_time_between(start_date=created_at))
print(faker.pybool(truth_probability=70))
