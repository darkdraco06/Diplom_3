import locators.login_page
from  pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Переход на страницу восстановления пароля')
    def transition_forgot_password_page(self):
        self.click_element(locators.login_page.LINK_PASSWORD_RECOVERY)

    @allure.step('Вход в личный кабинет')
    def login_in_personal_account(self, user):
        self.set_input_data(locators.login_page.FIELD_EMAIL, user['email'])
        self.set_input_data( locators.login_page.FIELD_PASSWORD, user['password'])
        self.wait_for_load_element(locators.login_page.BUTTON_LOGIN)
        self.click_element(locators.login_page.BUTTON_LOGIN)

    @allure.step('Ждем загрузки кнопки "Вход"')
    def wait_load_button_login(self):
        self.wait_for_load_element(locators.login_page.BUTTON_LOGIN)



