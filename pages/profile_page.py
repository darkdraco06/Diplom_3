import locators.profile_page
from  pages.base_page import BasePage
import allure



class ProfilePage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Выход"')
    def wait_load_button_exit(self, browser):
        self.wait_for_load_element(browser, locators.profile_page.BUTTON_EXIT)

    @allure.step('Клик по кнопке "Выход"')
    def click_button_exit(self, browser):
        self.click_element(browser, locators.profile_page.BUTTON_EXIT)
