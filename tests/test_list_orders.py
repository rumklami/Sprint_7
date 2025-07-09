import allure

from api_methods import OrderMethods
from data import OrderResponseAnswer


class TestListOrders:
    @allure.title('Успешное получение списка заказов')
    def test_get_list_orders(self):
        with allure.step('Запускаем ручку GET /api/v1/orders'):
            list_orders = OrderMethods.get_list_orders()
        assert list_orders.status_code == OrderResponseAnswer.GET_LIST_SUCCESS[0]
        assert list_orders.json().get(OrderResponseAnswer.GET_LIST_SUCCESS[1]) != None

