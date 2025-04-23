from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import allure
import curl


class TestUserProfile:

    @allure.title('Проверка перехода на страницу "История заказов" из профиля пользователя')
    @allure.description('Выполняем переход в личный кабинет под авторизованным пользоватлем. Кликаем на ссылку История заказов и проверям переход на страницу Истори закзов')
    def test_link_history_orders_click_link_transition_orders_history_page(self, browser, user):
        page_profile = ProfilePage(browser)
        page_login = LoginPage(browser)
        main_page = MainPage(browser)
        user_data, token = user

        main_page.transition_personal_account_page()
        page_login.login_in_personal_account(user_data)
        main_page.wait_for_invisibility_start_modal_windows()
        main_page.transition_personal_account_page()
        page_profile.wait_load_button_exit()
        page_profile.click_history_orders()
        assert page_profile.get_current_url() == curl.HISTORY_ORDER_PAGE

    @allure.title('Проверка выхода из профиля авторизованного пользвоателя')
    @allure.description('Выполняем переход в личный кабинет под авторизованным пользоватлем. Кликаем на ссылку "Выход" и проверям переход на страницу Входа в профиль')
    def test_link_exit_click_link_transition_login_page(self, browser, user):
        page_profile = ProfilePage(browser)
        page_login = LoginPage(browser)
        main_page = MainPage(browser)
        user_data, token = user

        main_page.transition_personal_account_page()
        page_login.login_in_personal_account(user_data)
        main_page.wait_for_invisibility_start_modal_windows()
        main_page.transition_personal_account_page()
        page_profile.wait_load_button_exit()
        page_profile.click_button_exit()
        page_login.wait_load_button_login()

        assert page_login.get_current_url() == curl.LOGIN_PAGE