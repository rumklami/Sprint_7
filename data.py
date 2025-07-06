class Url:
    BASE_PAGE = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    LIST_ORDERS = '/api/v1/orders'


class DataScooterRental:
    ONLY_LOGIN = {
        "login": "Vasiliy"
    }
    ONLY_PASS = {
        "password": "1a2b3c"
    }
