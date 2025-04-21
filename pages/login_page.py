import locators.login_page
from  pages.base_page import BasePage
import allure



class LoginPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def transition_forgot_password_page(self, browser):
        self.click_element(browser, locators.login_page.LINK_PASSWORD_RECOVERY)

    @allure.step('Вход в личный кабинет')
    def login_in_personal_account(self, browser, user):
        self.set_input_data(browser, locators.login_page.FIELD_EMAIL, user['email'])
        self.set_input_data(browser, locators.login_page.FIELD_PASSWORD, user['password'])
        self.click_element(browser, locators.login_page.BUTTON_LOGIN)




