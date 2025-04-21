import locators.reset_password
from  pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):
    @allure.step('Клик по кнопке "Отобразить пароль"')
    def click_button_show_password(self, browser):
        self.wait_for_load_element(browser, locators.reset_password.BUTTON_VIEWING_PASSWORD)
        self.click_element(browser, locators.reset_password.BUTTON_VIEWING_PASSWORD)

    @allure.step('Получаем значение элемента поля "Пароль"')
    def get_element_field_password(self, browser):
        return self.get_find_element_on_page(browser, locators.reset_password.INPUT_PASSWORD)

