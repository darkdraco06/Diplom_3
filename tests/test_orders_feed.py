import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from pages.history_order_page import HistoryOrderPage

from utils import Utils

class TestFeedOrder:

    @allure.title('Проверка отображение окна подробной информации о заказе')
    @allure.description('Переходим на страницу Лента заказов. Кликаем на первый заказ и проверям видимость окна')
    def test_pen_popup_order_detail_click_order_popup_opened(self, browser, user):
        page_main = MainPage(browser)
        feed_page = FeedPage(browser)
        utils = Utils()
        user_data, token = user

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.transition_feed_order()
        feed_page.wait_load_logo_feed_order()
        utils.create_order(token)
        feed_page.click_last_order()

        assert feed_page.check_visibility_modal_windows_order_details() == "Element found"

    @allure.title('Проверка отображения заказов пользвоателя в Ленте Заказов')
    @allure.description('Создаем новый заказ под авторизованным пользователем. Сравниваем индентификато первого заказа в ленте заказов и последний в истории заказов пользователя')
    def test_user_order_displayed_feed_order_created_order_order_displayed(self, browser, user):
        page_main = MainPage(browser)
        feed_page = FeedPage(browser)
        profile_page = ProfilePage(browser)
        history_page = HistoryOrderPage(browser)
        utils = Utils()
        user_data, token = user

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.transition_feed_order()
        page_main.add_token_in_local_storage(token)
        utils.create_order(token)
        feed_last_order = feed_page.get_last_number_order_feed_order()
        page_main.transition_personal_account_page()
        profile_page.wait_load_button_exit()
        profile_page.click_history_orders()
        history_page.wait_load_order_block_history()
        history_last_order = history_page.get_orders_user()
        assert feed_last_order in history_last_order

    @allure.title('Проверка увеличения счетчка заказов за все время')
    @allure.description('Создаем новый заказ и сравнием новое значение заказов за все вермя увеличенное на один с новым значением')
    def test_count_all_time_order_up_create_order_count_order_up(self, browser, user):
        page_main = MainPage(browser)
        feed_page = FeedPage(browser)
        utils = Utils()
        user_data, token = user

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.transition_feed_order()
        feed_page.wait_load_logo_feed_order()
        order_all_time = int(feed_page.get_number_order_all_time()) + 1
        utils.create_order(token)
        new_order_all_time = int(feed_page.get_number_order_all_time())

        assert order_all_time == new_order_all_time

    @allure.title('Проверка увеличения счетчка заказов за сегодня')
    @allure.description('Создаем новый заказ и сравнием новое значение заказов за сегодня увеличенное на один с новым значением')
    def test_count_today_order_up_create_order_count_order_today_up(self, browser, user):
        page_main = MainPage(browser)
        feed_page = FeedPage(browser)
        utils = Utils()
        user_data, token = user

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.transition_feed_order()
        feed_page.wait_load_logo_feed_order()
        order_all_time = int(feed_page.get_number_order_today()) + 1
        utils.create_order(token)
        new_order_all_time = int(feed_page.get_number_order_today())

        assert order_all_time == new_order_all_time

    @allure.title('Проверяем что созданный заказ попадает в раздел "В работе"')
    @allure.description('Создаем новый заказ и проверяем его наличие в разделе "В работе"')
    def test_order_in_work_create_order_status_order_in_work(self, browser, user):
        page_main = MainPage(browser)
        feed_page = FeedPage(browser)
        utils = Utils()
        user_data, token = user

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.transition_feed_order()
        feed_page.wait_load_logo_feed_order()
        order = "0" + str(utils.get_order_created_number(token))
        feed_page.wait_new_order_in_work(order)
        feed_page.get_orders_in_work()
        in_work = feed_page.get_number_order_in_work()

        assert order == in_work
