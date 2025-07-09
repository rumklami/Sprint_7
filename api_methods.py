import requests
from data import Url


class CourierMethods:
    @staticmethod
    def register_courier(courier_body):
        login, password, firstname = courier_body
        payload = {"login": login, "password": password, "firstName": firstname}
        response = requests.post(f'{Url.BASE_PAGE}{Url.CREATE_COURIER}', json=payload)
        return response

    @staticmethod
    def register_courier_with_parametr(courier_body):
        response = requests.post(f'{Url.BASE_PAGE}{Url.CREATE_COURIER}', json=courier_body)
        return response

    @staticmethod
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        courier = requests.post(f'{Url.BASE_PAGE}{Url.LOGIN_COURIER}', json=payload)
        return courier.json()['id'], courier

    @staticmethod
    def login_courier_with_1_parametr(login, password):
        payload = {"login": login, "password": password}
        courier = requests.post(f'{Url.BASE_PAGE}{Url.LOGIN_COURIER}', json=payload)
        return courier

    @staticmethod
    def delete_courier(courier_id):
        requests.delete(f'{Url.BASE_PAGE}{Url.CREATE_COURIER}/{courier_id}')


class OrderMethods:

    @staticmethod
    def create_order(order_body):
        response = requests.post(f'{Url.BASE_PAGE}{Url.CREATE_ORDER}', json=order_body)
        return response

    @staticmethod
    def get_list_orders():
        response = requests.get(f'{Url.BASE_PAGE}{Url.LIST_ORDERS}')
        return response
