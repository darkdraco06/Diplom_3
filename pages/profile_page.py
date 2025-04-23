import locators.profile_page
from  pages.base_page import BasePage
import allure



class ProfilePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Ожидание загрузки кнопки "Выход"')
    def wait_load_button_exit(self):
        self.wait_for_load_element(locators.profile_page.BUTTON_EXIT)

    @allure.step('Клик по кнопке "Выход"')
    def click_button_exit(self):
        self.click_element(locators.profile_page.BUTTON_EXIT)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders(self):
        self.click_element(locators.profile_page.LINK_HISTORY_ORDER)
