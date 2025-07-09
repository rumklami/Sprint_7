import random

from faker import Faker

faker = Faker()

def generate_order():
    return {
    "firstName": faker.first_name(),
    "lastName": faker.last_name(),
    "address": (faker.address().replace('\n', ' ').replace(',', '').replace('.', '')
               .replace(')', '').replace('(', '').replace('!', '').replace('/', '')
               .strip())[:49],
    "metroStation": random.randint(0, 224),
    "phone": f"+7{random.randint(9000000000, 9999999999)}",
    "rentTime": random.randint(0,6),
    "deliveryDate": faker.date_between(start_date='+1d', end_date='+14d').isoformat(),
    "comment": faker.text(),
    "color": [
        random.choice(["BLACK", "GREY"])
    ]
}

def generate_courier():
    return {
    "login": faker.name(),
    "password": faker.password(),
    "firstName": faker.first_name()
}
