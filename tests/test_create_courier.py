import allure
import pytest

from api_methods import ApiMethods
from conftest import create_courier
from data import DataScooterRental


class TestCreateCourier:
    @allure.title('Успешная регистрация курьера')
    def test_success_courier_registration1(self, create_courier):
        with allure.step('Запускаем ручку POST /api/v1/courier'):
            courier = ApiMethods.register_courier(create_courier)
        assert courier.status_code == 201 and '"ok":true' in courier.text

    @allure.title('Регистрация 2 одинаковых курьеров')
    def test_courier_registation_409(self, create_courier):
        with allure.step('Запускаем ручку POST /api/v1/courier'):
            ApiMethods.register_courier(create_courier)
            courier = ApiMethods.register_courier(create_courier)
        assert courier.status_code == 409 and 'Этот логин уже используется. Попробуйте другой.' in courier.text


    @allure.title('Регистрация курьера с одним обязятельным полем')
    @pytest.mark.parametrize('courier_json', (DataScooterRental.ONLY_LOGIN, DataScooterRental.ONLY_PASS))
    def test_courier_registration_400(self, courier_json):
        with allure.step('Запускаем ручку POST /api/v1/courier'):
            courier = ApiMethods.register_courier_with_parametr(courier_json)
        assert courier.status_code == 400 and 'Недостаточно данных для создания учетной записи' in courier.text
