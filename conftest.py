import pytest

from api_methods import ApiMethods
from helper import generate_courier


@pytest.fixture
def create_courier():
    courier_body = generate_courier()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    yield [login, password, firstname]
    courier_id = ApiMethods.login_courier(login, password)[0]
    ApiMethods.delete_courier(courier_id)
