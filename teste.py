import json
from faker import Faker

faker = Faker("pt_BR")

with open('src/core/fdata/products.json', 'r') as file:
    json_file = json.load(file)

counter = 1


for category, data in json_file['categories'].items():

    print(category)
    print(data["description"])

    break
