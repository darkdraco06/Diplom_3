from  pages.base_page import BasePage
import locators.history_order_page
import allure


class HistoryOrderPage(BasePage):
    @allure.step('Получаем номер последнего заказа пользователя из истории заказов')
    def get_number_order_hystiri_order(self, browser):
        return self.get_text_element(browser, locators.history_order_page.ORDER_BLOCK)