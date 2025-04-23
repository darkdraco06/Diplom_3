import locators.main_page
from  pages.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Переход в "Личный кабинет"')
    def transition_personal_account_page(self):
        self.wait_for_load_element(locators.main_page.LINK_PERSONAL_ACCOUNT)
        self.wait_for_invisibility_element(locators.main_page.START_MODUL_WINDOWS)
        self.click_element(locators.main_page.LINK_PERSONAL_ACCOUNT)

    @allure.step('Переход в раздел "Конструктор"')
    def transition_construсtor_bar(self):
        self.wait_for_load_element(locators.main_page.BUTTON_CONSTRUCTOR)
        self.wait_for_invisibility_element(locators.main_page.START_MODUL_WINDOWS)
        self.click_element(locators.main_page.BUTTON_CONSTRUCTOR)

    @allure.step('Переход в раздел "Лента заказов"')
    def transition_feed_order(self):
        self.wait_for_load_element(locators.main_page.BUTTON_FEED_ORDER)
        self.wait_for_invisibility_element(locators.main_page.START_MODUL_WINDOWS)
        self.click_element(locators.main_page.BUTTON_FEED_ORDER)

    @allure.step('Перенос ингредиента "Булочка" в конструктор')
    def drag_and_drop_element_first_bun(self):
        self.wait_for_load_element(locators.main_page.INGREDIENT_FIRST_BUN)
        self.wait_for_invisibility_element(locators.main_page.START_MODUL_WINDOWS)
        self.drag_and_drop_element(locators.main_page.INGREDIENT_FIRST_BUN, locators.main_page.BURGER_CONSTRUCTOR)
        self.wait_for_load_element(locators.main_page.BUN_IN_ORDER)

    @allure.step('Получить значение каунтера первой булочки')
    def get_value_counter_first_bun(self):
        self.wait_for_load_element(locators.main_page.INGREDIENT_FIRST_BUN)
        self.wait_for_invisibility_element(locators.main_page.START_MODUL_WINDOWS)
        return int(self.get_text_element(locators.main_page.INGRIDIENT_COUNTER_FIRST_BUN))

    @allure.step('Проверям отображение модального окна с информацие о заказе')
    def check_visibility_modal_window_create_order_done(self):
        self.wait_for_load_element(locators.main_page.MODAL_WINDOW_CREATE_ORDER_DONE)
        data = self.get_find_element_on_page(locators.main_page.MODAL_WINDOW_CREATE_ORDER_DONE)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Проверяем отображение модального окна с деталями заказа')
    def check_visibility_modal_windows_ingridient_details(self):
        return self.get_find_element_on_page(locators.main_page.INGREDIENT_DETAILS_WINDOW).is_displayed()

    @allure.step('Кликам по кнопке "Оформить заказ')
    def click_button_place_order(self):
        self.click_element(locators.main_page.BUTTON_PLACE_ORDER)

    @allure.step('Ожидаем пропажи модального окна на главной странице')
    def wait_for_invisibility_start_modal_windows(self):
        self.wait_for_invisibility_element(locators.main_page.START_MODUL_WINDOWS)

    @allure.step('Кликаем по ингредиенту булочки')
    def click_ingridient_bun(self):
        self.click_element(locators.main_page.INGREDIENT_FIRST_BUN)

    @allure.step('Кликаем по по кнопке закрытия модального окна')
    def click_button_close_modal_window(self):
        self.click_element(locators.main_page.BUTTON_CLOSE_MODAL_WINDOWS_DETAILS)

    @allure.step('Проверяем что модальное ингридиента окно закрыто')
    def check_visibility_modal_windows_ingridient_details_close(self):
        self.wait_for_invisibility_element(locators.main_page.BUTTON_CLOSE_MODAL_WINDOWS_DETAILS)
        return self.get_find_element_on_page(locators.main_page.BUTTON_CLOSE_MODAL_WINDOWS_DETAILS).is_displayed()





