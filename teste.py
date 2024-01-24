import json
from faker import Faker

faker = Faker("pt_BR")

for i in range(10):

    print(faker.unique.localized_ean())
