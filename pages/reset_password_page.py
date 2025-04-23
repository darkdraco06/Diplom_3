import locators.reset_password
from  pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Клик по кнопке "Отобразить пароль"')
    def click_button_show_password(self):
        self.wait_for_load_element(locators.reset_password.BUTTON_VIEWING_PASSWORD)
        self.click_element(locators.reset_password.BUTTON_VIEWING_PASSWORD)

    @allure.step('Получаем значение элемента поля "Пароль"')
    def get_element_field_password(self):
        return self.get_find_element_on_page(locators.reset_password.INPUT_PASSWORD)
