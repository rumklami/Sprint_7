import allure
import pytest

from api_methods import OrderMethods
from data import OrderResponseAnswer
from helper import generate_order


class TestCreateOrders:
    @allure.title('Успешное создание заказа с выбором цвета, обоих цветов и без цвета')
    @pytest.mark.parametrize('colour', ('BLACK', ('BLACK', 'GREY'), ''))
    def test_success_create_order(self, colour):
        with allure.step('Запускаем ручку POST /api/v1/orders'):
            order_json = generate_order()
            order_json['colour'] = colour
            order = OrderMethods.create_order(order_json)
        assert order.status_code == OrderResponseAnswer.CREATE_SUCCESS[0] and order.json()[
            OrderResponseAnswer.CREATE_SUCCESS[1]] != 0
