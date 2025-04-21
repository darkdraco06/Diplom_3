import time
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import locators.profile_page
import locators.login_page
import locators.main_page
import allure
import curl


class TestUserProfile:

    @allure.title('Проверка перехода на страницу "История заказов" из профиля пользователя')
    @allure.description('Выполняем переход в личный кабинет под авторизованным пользоватлем. Кликаем на ссылку История заказов и проверям переход на страницу Истори закзов')
    def test_link_history_orders_click_link_transition_orders_history_page(self, browser,  user):
        page_profile = ProfilePage()
        page_login = LoginPage()
        main_page = MainPage()

        main_page.transition_personal_account_page(browser)
        page_login.login_in_personal_account(browser, user)
        page_login.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        main_page.transition_personal_account_page(browser)
        page_profile.wait_load_button_exit(browser)
        page_profile.click_element(browser, locators.profile_page.LINK_HISTORY_ORDER)
        assert browser.current_url == curl.HISTORY_ORDER_PAGE

    @allure.title('Проверка выхода из профиля авторизованного пользвоателя')
    @allure.description('Выполняем переход в личный кабинет под авторизованным пользоватлем. Кликаем на ссылку "Выход" и проверям переход на страницу Входа в профиль')
    def test_link_exit_click_link_transition_login_page(self, browser, user):
        page_profile = ProfilePage()
        page_login = LoginPage()
        main_page = MainPage()

        main_page.transition_personal_account_page(browser)
        page_login.login_in_personal_account(browser, user)
        page_login.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        main_page.transition_personal_account_page(browser)
        page_profile.wait_load_button_exit(browser)
        page_profile.click_button_exit(browser)
        time.sleep(2)
        assert browser.current_url == curl.LOGIN_PAGE