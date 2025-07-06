import allure
import pytest

from conftest import create_courier
from api_methods import ApiMethods


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    def test_success_authorization_courier(self, create_courier):
        login = create_courier[0]
        password = create_courier[1]
        with allure.step('Создаём курьера'):
            ApiMethods.register_courier(create_courier)
        with allure.step('Запускаем ручку регистрации курьера POST /api/v1/courier/login'):
            response = ApiMethods.login_courier(login, password)[1]
        assert response.status_code == 200 and response.json()['id'] != 0

    @allure.title('Проверка появления ошибки при авторизации с некорректным паролем')
    @pytest.mark.parametrize("password_change, expected_code", (['', 400], [None, 400], ['i-Z8MKUc29', 404]))
    def test_authorization_incorrect_password(self, create_courier, password_change, expected_code):
        login = create_courier[0]
        with allure.step('Создаём курьера'):
            ApiMethods.register_courier(create_courier)
        with allure.step('Запускаем ручку регистрации курьера POST /api/v1/courier/login'):
            response = ApiMethods.login_courier_with_1_parametr(login, password_change)
        assert response.status_code == expected_code

    @allure.title('Проверка появления ошибки при авторизации с некорректным логином')
    @pytest.mark.parametrize("login_change, expected_code", (['', 400], [None, 400], ['CantorGroaner', 404]))
    def test_authorization_incorrect_login(self, create_courier, login_change, expected_code):
        password = create_courier[1]
        with allure.step('Создаём курьера'):
            ApiMethods.register_courier(create_courier)
        with allure.step('Запускаем ручку регистрации курьера POST /api/v1/courier/login'):
            response = ApiMethods.login_courier_with_1_parametr(login_change, password)
        assert response.status_code == expected_code
