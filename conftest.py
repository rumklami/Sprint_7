import pytest

from api_methods import CourierMethods
from helper import generate_courier


@pytest.fixture
def create_courier():
    courier_body = generate_courier()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    yield [login, password, firstname]
    courier_id = CourierMethods.login_courier(login, password)[0]
    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def create_courier_without_delete():
    courier_body = generate_courier()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    return [login, password, firstname]
