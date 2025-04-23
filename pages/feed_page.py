from  pages.base_page import BasePage
import allure
import locators.feed_page


class FeedPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Кликаем на последний заказ в ленте')
    def click_last_order(self,):
        self.click_element(locators.feed_page.ORDER_BLOCK)

    @allure.step('Проверяем отображение модального окна с деталями заказа')
    def check_visibility_modal_windows_order_details(self):
        self.wait_for_load_element(locators.feed_page.MODAL_WINDOW_ORDER)
        data = self.get_find_element_on_page(locators.feed_page.MODAL_WINDOW_ORDER)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Получаем послений номер заказа из ленты заказов')
    def get_last_number_order_feed_order(self):
        return self.get_find_element_on_page(locators.feed_page.LAST_ORDER_FEED_ORDER).text

    @allure.step('Получаем количество заказов за все вермя')
    def get_number_order_all_time(self,):
        return self.get_text_element(locators.feed_page.NUMBER_ORDER_ALL_TIME)


    @allure.step('Получаем количество заказов за день')
    def get_number_order_today(self):
        return self.get_text_element(locators.feed_page.NUMBER_ORDER_TODAY)


    @allure.step('Получаем список заказов в работе')
    def get_number_order_in_work(self):
        return self.get_text_element(locators.feed_page.ORDER_IN_WORK)

    @allure.step('Ожидаем загрузки логотипа "Лента заказов')
    def wait_load_logo_feed_order(self):
        self.wait_for_load_element(locators.feed_page.LOGO_FEED_ORDER)

    @allure.step('Получаем список заказов в работе')
    def get_orders_in_work(self):
        orders_in_work = self.get_find_element_on_page(locators.feed_page.ORDER_IN_WORK).text
        return orders_in_work

    @allure.step('Ждем появления нового в заказа в поле "В работе"')
    def wait_new_order_in_work(self, text):
        self.wait_for_text_in_element(locators.feed_page.ORDER_IN_WORK, text)





