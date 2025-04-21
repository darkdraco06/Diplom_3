import time

from pages.main_page import MainPage
import allure


class TestCreateBurger:

    @allure.title('Проверка увелечения каунтера ингредитента булочки')
    @allure.description('Проверям что при переносе выбранной булочки, через drag and drop в конструктор бургера увеличивает каунтер выбранной булочки на 2')
    def test_counter_ingredient_drag_and_drop_ingredient_counter_up(self, browser):
        page_main = MainPage()

        page_main.drag_and_drop_element_first_bun(browser)
        time.sleep(3)
        counter = page_main.get_value_counter_first_bun(browser)
        assert counter == 2