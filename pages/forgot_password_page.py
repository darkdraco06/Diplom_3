from  pages.base_page import BasePage
import locators.forgot_password
import allure


class ForgotPasswordPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Вводим email в поле email"')
    def input_email_in_field_email(self, email):
        self.wait_for_load_element(locators.forgot_password.INPUT_EMAIL_PASSWORD_RECOVERY)
        self.set_input_data(locators.forgot_password.INPUT_EMAIL_PASSWORD_RECOVERY, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_reset(self):
        self.click_element(locators.forgot_password.BUTTON_PASSWORD_RECOVER)
