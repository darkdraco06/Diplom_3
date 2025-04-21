from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
import allure
import curl
import time


class TestPasswordRecovery:

    @allure.title('Проверка кнопки Восстановить с указанием email')
    @allure.description('Выполняем переход на страницу восстановления пароля, вводим email и на жимаем кнопку "Восстановить"')
    def test_button_recover_user_email_positive_result(self, browser, random_user_data):
        page_main = MainPage()
        page_login = LoginPage()
        page_forgot_password = ForgotPasswordPage()

        page_main.transition_personal_account_page(browser)
        page_login.transition_forgot_password_page(browser)
        page_forgot_password.input_email_in_field_email(browser, random_user_data["email"])
        page_forgot_password.click_button_reset(browser)
        time.sleep(2)

        assert browser.current_url == curl.RESET_PASSWORD

    @allure.title('Проверяем активацию поля "Пароль" при нажатии кнопки "Показать пароль"')
    @allure.description('Выполняем переход на страницу восстановления пароля, вводим email и на жимаем кнопку "Восстановить"')
    def test_button_active_user_email_positive_result(self, browser, random_user_data):
        page_main = MainPage()
        page_login = LoginPage()
        page_forgot_password = ForgotPasswordPage()
        page_reset_password = ResetPasswordPage()

        page_main.transition_personal_account_page(browser)
        page_login.transition_forgot_password_page(browser)
        page_forgot_password.input_email_in_field_email(browser, random_user_data["email"])
        page_forgot_password.click_button_reset(browser)
        page_reset_password.click_button_show_password(browser)

        assert page_reset_password.active_element_on_page(browser) == page_reset_password.get_element_field_password(browser)

