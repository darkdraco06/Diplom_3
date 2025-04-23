from  pages.base_page import BasePage
import locators.history_order_page
import allure


class HistoryOrderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Получаем список заказов в работе')
    def get_orders_user(self):
        orders = self.get_find_element_on_page(locators.history_order_page.ORDER_BLOCK).text
        return orders

    @allure.step('Ожидание загрузки блока с заказами')
    def wait_load_order_block_history(self):
        self.wait_for_load_element(locators.history_order_page.ORDER_BLOCK)
