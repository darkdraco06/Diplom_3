from pages.main_page import MainPage
import allure


class TestConstructorBurger:

    @allure.title('Проверка появления модального окна об инфомации об ингредиенте')
    @allure.description('Кликаем на ингредиент. Проверям что окно с информацией об ингредиенте отображается')
    def test_popup_details_click_ingridient_popup_appearance(self, browser):
        page_main = MainPage(browser)

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.click_ingridient_bun()

        assert page_main.check_visibility_modal_windows_ingridient_details()

    @allure.title('Проверка закрытия модального окна по кнопке крестик')
    @allure.description('Кликаем на ингредиент. Дожидаемся отображения модального окна. Закрываем модальное окно через крестик. Проверям что окно не отображается')
    def test_close_popup_details_click_ingridient_close_popup(self, browser):
        page_main = MainPage(browser)

        page_main.wait_for_invisibility_start_modal_windows()
        page_main.click_ingridient_bun()
        page_main.click_button_close_modal_window()

        assert page_main.check_visibility_modal_windows_ingridient_details_close() == False