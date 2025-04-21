import time

import locators.main_page
from  pages.base_page import BasePage
import allure



class MainPage(BasePage):

    @allure.step('Переход в "Личный кабинет"')
    def transition_personal_account_page(self, browser):
        self.wait_for_load_element(browser, locators.main_page.LINK_PERSONAL_ACCOUNT)
        self.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        self.click_element(browser, locators.main_page.LINK_PERSONAL_ACCOUNT)

    @allure.step('Переход в раздел "Конструктор"')
    def transition_construсtor_bar(self, browser):
        self.wait_for_load_element(browser, locators.main_page.BUTTON_CONSTRUCTOR)
        self.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        self.click_element(browser, locators.main_page.BUTTON_CONSTRUCTOR)

    @allure.step('Переход в раздел "Лента заказов"')
    def transition_feed_order(self, browser):
        self.wait_for_load_element(browser, locators.main_page.BUTTON_FEED_ORDER)
        self.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        self.click_element(browser, locators.main_page.BUTTON_FEED_ORDER)

    @allure.step('Перенос ингредиента "Булочка" в конструктор')
    def drag_and_drop_element_first_bun(self, browser):
        self.wait_for_load_element(browser, locators.main_page.INGREDIENT_FIRST_BUN)
        self.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        self.drag_and_drop_element(browser, locators.main_page.INGREDIENT_FIRST_BUN, locators.main_page.BURGER_CONSTRUCTOR)

    @allure.step('Получить значение каунтера первой булочки')
    def get_value_counter_first_bun(self, browser):
        self.wait_for_load_element(browser, locators.main_page.INGREDIENT_FIRST_BUN)
        self.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        return int(self.get_text_element(browser, locators.main_page.INGRIDIENT_COUNTER_FIRST_BUN))

    @allure.step('Проверям отображение элемента на дисплее')
    def check_visibility_modal_windows(self, browser, element):
        data = self.get_find_element_on_page(browser, element)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"


