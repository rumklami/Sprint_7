import allure
import pytest

from api_methods import CourierMethods
from data import CourierResponseAnswer


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    def test_success_authorization_courier(self, create_courier):
        login = create_courier[0]
        password = create_courier[1]
        with allure.step('Создаём курьера'):
            CourierMethods.register_courier(create_courier)
        with allure.step('Запускаем ручку регистрации курьера POST /api/v1/courier/login'):
            response = CourierMethods.login_courier(login, password)[1]
        assert response.status_code == CourierResponseAnswer.AUTHORIZATION_SUCCESS[0] and response.json()[
            CourierResponseAnswer.AUTHORIZATION_SUCCESS[1]] != 0

    @allure.title('Проверка появления ошибки при авторизации с некорректным паролем')
    @pytest.mark.parametrize("password_change, expected_code", (
    ['', CourierResponseAnswer.AUTHORIZATION_BAD_REQUEST[0]],
    [None, CourierResponseAnswer.AUTHORIZATION_BAD_REQUEST[0]],
    ['i-Z8MKUc29', CourierResponseAnswer.AUTHORIZATION_NOT_FOUND[0]]))
    def test_authorization_incorrect_password(self, create_courier_without_delete, password_change, expected_code):
        login = create_courier_without_delete[0]
        with allure.step('Создаём курьера'):
            CourierMethods.register_courier(create_courier_without_delete)
        with allure.step('Запускаем ручку регистрации курьера POST /api/v1/courier/login'):
            response = CourierMethods.login_courier_with_1_parametr(login, password_change)
        assert response.status_code == expected_code

    @allure.title('Проверка появления ошибки при авторизации с некорректным логином')
    @pytest.mark.parametrize("login_change, expected_code", (['', CourierResponseAnswer.AUTHORIZATION_BAD_REQUEST[0]],
                                                             [None, CourierResponseAnswer.AUTHORIZATION_BAD_REQUEST[0]],
                                                             ['CantorGroaner',
                                                              CourierResponseAnswer.AUTHORIZATION_NOT_FOUND[0]]))
    def test_authorization_incorrect_login(self, create_courier_without_delete, login_change, expected_code):
        password = create_courier_without_delete[1]
        with allure.step('Создаём курьера'):
            CourierMethods.register_courier(create_courier_without_delete)
        with allure.step('Запускаем ручку регистрации курьера POST /api/v1/courier/login'):
            response = CourierMethods.login_courier_with_1_parametr(login_change, password)
        assert response.status_code == expected_code
