import allure
import locators.feed_page
import locators.main_page
import locators.history_order_page
import locators.profile_page
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from pages.history_order_page import HistoryOrderPage
import time
from utils import Utils

class TestFeedOrder:

    @allure.title('Проверка отображение окна подробной информации о заказе')
    @allure.description('Переходим на страницу Лента заказов. Кликаем на первый заказ и проверям видимость окна')
    def test_pen_popup_order_detail_click_order_popup_opened(self, browser, user_token):
        page_main = MainPage()
        feed_page = FeedPage()
        utils = Utils()

        page_main.transition_feed_order(browser)
        utils.create_order(user_token)
        time.sleep(3)
        feed_page.click_last_order(browser)
        time.sleep(3)
        windows = feed_page.check_visibility_modal_windows_order_details(browser, locators.feed_page.MODAL_WINDOW_ORDER)

        assert windows == "Element found"

    @allure.title('Проверка отображения заказов пользвоателя в Ленте Заказов')
    @allure.description('Создаем новый заказ под авторизованным пользователем. Сравниваем индентификато первого заказа в ленте заказов и последний в истории заказов пользователя')
    def test_user_order_displayed_feed_order_created_order_order_displayed(self, browser, user_token):
        page_main = MainPage()
        feed_page = FeedPage()
        profile_page = ProfilePage()
        history_page = HistoryOrderPage()
        utils = Utils()

        page_main.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.transition_feed_order(browser)
        time.sleep(2)
        page_main.add_token_in_local_storage(browser, user_token)
        utils.create_order(user_token)
        time.sleep(2)
        feed_last_order = feed_page.get_last_number_order_feed_order(browser)
        page_main.transition_personal_account_page(browser)
        time.sleep(2)
        profile_page.click_element(browser, locators.profile_page.LINK_HISTORY_ORDER)
        time.sleep(2)
        history_last_order = history_page.get_number_order_hystiri_order(browser)
        assert feed_last_order == history_last_order

    @allure.title('Проверка увеличения счетчка заказов за все время')
    @allure.description('Создаем новый заказ и сравнием новое значение заказов за все вермя увеличенное на один с новым значением')
    def test_count_all_time_order_up_create_order_count_order_up(self, browser, user_token):
        page_login = LoginPage()
        page_main = MainPage()
        feed_page = FeedPage()
        utils = Utils()

        page_login.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.transition_feed_order(browser)
        time.sleep(3)
        order_all_time = int(feed_page.get_number_order_all_time(browser)) + 1
        utils.create_order(user_token)
        time.sleep(2)
        new_order_all_time = int(feed_page.get_number_order_all_time(browser))

        assert order_all_time == new_order_all_time

    @allure.title('Проверка увеличения счетчка заказов за сегодня')
    @allure.description(        'Создаем новый заказ и сравнием новое значение заказов за сегодня увеличенное на один с новым значением')
    def test_count_today_order_up_create_order_count_order_today_up(self, browser, user_token):
        page_login = LoginPage()
        page_main = MainPage()
        feed_page = FeedPage()
        utils = Utils()

        page_login.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.transition_feed_order(browser)
        time.sleep(3)
        order_all_time = int(feed_page.get_number_order_today(browser)) + 1
        time.sleep(2)
        utils.create_order(user_token)
        time.sleep(2)
        new_order_all_time = int(feed_page.get_number_order_today(browser))

        assert order_all_time == new_order_all_time

    @allure.title('Проверяем что созданный заказ попадает в раздел "В работе"')
    @allure.description('Создаем новый заказ и проверяем его наличие в разделе "В работе"')
    def test_order_in_work_create_order_status_order_in_work(self, browser, user_token):
        page_main = MainPage()
        feed_page = FeedPage()
        utils = Utils()

        page_main.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.transition_feed_order(browser)
        time.sleep(2)
        order = "0" + str(utils.get_order_created_number(user_token))
        time.sleep(5)
        in_work = feed_page.get_number_order_in_work(browser)

        assert order == in_work
