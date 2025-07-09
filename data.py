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


class CourierResponseAnswer:
    CREATE_SUCCESS = [201, '"ok":true']
    CREATE_FAILED_LOGIN = [409, 'Этот логин уже используется. Попробуйте другой.']
    CREATE_BAD_REQUEST = [400, 'Недостаточно данных для создания учетной записи']
    AUTHORIZATION_SUCCESS = [200, 'id']
    AUTHORIZATION_BAD_REQUEST = [400, '"message":  "Недостаточно данных для входа"']
    AUTHORIZATION_NOT_FOUND = [404, '"message": "Учетная запись не найдена"']

class OrderResponseAnswer:
    CREATE_SUCCESS = [201, 'track']
    GET_LIST_SUCCESS = [200, 'orders']
