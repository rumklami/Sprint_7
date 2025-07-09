import allure
import pytest

from api_methods import CourierMethods
from data import DataScooterRental, CourierResponseAnswer


class TestCreateCourier:
    @allure.title('Успешная регистрация курьера')
    def test_success_courier_registration1(self, create_courier):
        with allure.step('Запускаем ручку POST /api/v1/courier'):
            courier = CourierMethods.register_courier(create_courier)
        assert courier.status_code == CourierResponseAnswer.CREATE_SUCCESS[0] and CourierResponseAnswer.CREATE_SUCCESS[1] in courier.text

    @allure.title('Регистрация 2 одинаковых курьеров')
    def test_courier_registation_409(self, create_courier):
        with allure.step('Запускаем ручку POST /api/v1/courier'):
            CourierMethods.register_courier(create_courier)
            courier = CourierMethods.register_courier(create_courier)
        assert courier.status_code == CourierResponseAnswer.CREATE_FAILED_LOGIN[0] and CourierResponseAnswer.CREATE_FAILED_LOGIN[1] in courier.text

    @allure.title('Регистрация курьера с одним обязятельным полем')
    @pytest.mark.parametrize('courier_json', (DataScooterRental.ONLY_LOGIN, DataScooterRental.ONLY_PASS))
    def test_courier_registration_400(self, courier_json):
        with allure.step('Запускаем ручку POST /api/v1/courier'):
            courier = CourierMethods.register_courier_with_parametr(courier_json)
        assert courier.status_code == CourierResponseAnswer.CREATE_BAD_REQUEST[0] and CourierResponseAnswer.CREATE_BAD_REQUEST[1] in courier.text
