from  pages.base_page import BasePage

import allure
import locators.feed_page


class FeedPage(BasePage):

    @allure.step('Кликаем на последний заказ в ленте')
    def click_last_order(self, browser):
        self.click_element(browser, locators.feed_page.ORDER_BLOCK)

    @allure.step('Проверяем отображение модального окна с деталями заказа')
    def check_visibility_modal_windows_order_details(self, browser, element):
        data = self.get_find_element_on_page(browser, element)
        if data.is_displayed():
            return "Element found"
        else:
            return "Element not found"

    @allure.step('Получение номера заказа авторизованного пользователя')
    def get_number_order_user(self, browse):
        return self.get_text_element(browse, locators.feed_page.NUMBER_NEW_ORDER)

    @allure.step('Закрываем модальное окно после создания заказа')
    def close_popup_created_order(self, browser):
        self.click_element(browser, locators.feed_page.BUTTON_CLOSE_POPUP_ORDER)

    @allure.step('Получаем послений номер заказа из ленты заказов')
    def get_last_number_order_feed_order(self, browser):
        return self.get_text_element(browser, locators.feed_page.LAST_ORDER_FEED_ORDER)

    @allure.step('Получаем количество заказов за все вермя')
    def get_number_order_all_time(self, browser):
        return self.get_text_element(browser, locators.feed_page.NUMBER_ORDER_ALL_TIME)


    @allure.step('Получаем количество заказов за день')
    def get_number_order_today(self, browser):
        return self.get_text_element(browser, locators.feed_page.NUMBER_ORDER_TODAY)


    @allure.step('Получаем список заказов в работе')
    def get_number_order_in_work(self, browser):
        return self.get_text_element(browser, locators.feed_page.ORDER_IN_WORK)


