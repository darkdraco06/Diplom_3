from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import locators.profile_page
import locators.login_page
import locators.main_page
import allure
import curl


class TestGoingToSitePage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Выполняем переход на страницу восстаноления пароля, через ссылку "Восстаноление пароля" на странице личнного аккаунта')
    def test_transition_forgot_page_positive_result(self, browser):
        page_main = MainPage()
        page_login = LoginPage()

        page_main.transition_personal_account_page(browser)
        page_login.transition_forgot_password_page(browser)

        assert browser.current_url == curl.FORGOT_PASSWORD


    @allure.title('Проверка перехода на страницу личного кабинета под авторизованным пользоватлем')
    @allure.description('Проверяем переход в личный кабинет, через ссылку "Личный кабиент" под авторизованным пользоватлем. После перехода открывается страница профиля пользователя')
    def test_link_personal_account_click_link_transition_open_page_profile(self, browser, user):
        page_profile = ProfilePage()
        page_login = LoginPage()
        main_page = MainPage()

        main_page.transition_personal_account_page(browser)
        page_login.login_in_personal_account(browser, user)
        page_login.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        main_page.transition_personal_account_page(browser)
        page_profile.wait_load_button_exit(browser)

        assert browser.current_url == curl.PROFILE_PAGE

    @allure.title('Проверка перехода в раздел "Лента заказов')
    @allure.description('Загурзака сайта начинается с загрузки раздела Конструктор. Проверяем переход в раздел Лента заказов, кликая на кнопку Лента заказов. Открывается раздел Лента заказов ')
    def test_transition_feed_order_click_button_feed_order_open_page_feed(self, browser):
        page_main = MainPage()

        page_main.transition_feed_order(browser)

        assert browser.current_url == curl.FEED_ORDER

    @allure.title('Проверка перехода в раздел "Конструктор')
    @allure.description('Проверяем переход в раздел Конструктор, кликая на кнопку Лента заказов, потом на кнопку Конструтор. Открывается раздел Главная страница с разеделом конструктор ')
    def test_transition_constructor_click_button_constructor_open_main_page(self, browser):
        page_main = MainPage()

        page_main.transition_feed_order(browser)
        page_main.transition_construсtor_bar(browser)

        assert browser.current_url == curl.MAIN_SITE