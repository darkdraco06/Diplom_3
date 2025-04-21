import requests
import curl
import allure


class ApiMethod:

    @staticmethod
    @allure.step('Выполняем запрос на создание пользователя')
    def api_method_create_user(payload):
        return requests.post(f'{curl.CREATE_USER}', data=payload)

    @staticmethod
    @allure.step('Выполняем запрос на удаление пользователя')
    def api_method_delete_user(token):
        return requests.delete(f'{curl.DELETE_USER}', headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Выполняем авторизацию пользователя')
    def api_method_login_user(email, password):
        return requests.post(f'{curl.LOGIN_USER}', json={'email': email, 'password': password})

    @staticmethod
    @allure.step('Создаем новый заказ через api и получаем его номер')
    def api_create_order(token):
        return requests.post(f'{curl.CREATE_ORDER}', json={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]}, headers={'Authorization': f'{token}'})

