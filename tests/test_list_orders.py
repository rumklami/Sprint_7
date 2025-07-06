import allure

from api_methods import ApiMethods


class TestListOrders:
    @allure.title('Успешное получение списка заказов')
    def test_get_list_orders(self):
        with allure.step('Запускаем ручку GET /api/v1/orders'):
            list_orders = ApiMethods.get_list_orders()
        assert list_orders.status_code == 200
        assert list_orders.json().get("orders") != None

