import locators.profile_page
import locators.login_page
import locators.main_page
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


class TestCreateOrder:

    @allure.title('Проверка оформления заказа под авторизованным пользователем')
    @allure.description('Авторизуемся под пользователем. Создаем бургер и оформляем заказ')
    def test_create_order_create_burger_click_buton_create_order_order_created(self, browser, user):
        page_login = LoginPage()
        page_main = MainPage()

        page_main.transition_personal_account_page(browser)
        page_login.login_in_personal_account(browser, user)
        page_login.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.drag_and_drop_element_first_bun(browser)
        time.sleep(2)
        page_main.click_element(browser, locators.main_page.BUTTON_PLACE_ORDER)

        assert page_main.check_visibility_modal_windows(browser, locators.main_page.MODAL_WINDOW_CREATE_ORDER_DONE) == "Element found"

