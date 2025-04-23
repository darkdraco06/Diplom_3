import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestCreateOrder:

    @allure.title('Проверка оформления заказа под авторизованным пользователем')
    @allure.description('Авторизуемся под пользователем. Создаем бургер и оформляем заказ')
    def test_create_order_create_burger_click_buton_create_order_order_created(self, browser, user):
        page_login = LoginPage(browser)
        page_main = MainPage(browser)
        user_data, token = user
        page_main.transition_personal_account_page()
        page_login.login_in_personal_account(user_data)
        page_main.wait_for_invisibility_start_modal_windows()
        page_main.drag_and_drop_element_first_bun()
        page_main.click_button_place_order()

        assert page_main.check_visibility_modal_window_create_order_done() == "Element found"