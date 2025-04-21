from pages.main_page import MainPage
import locators.profile_page
import locators.login_page
import locators.main_page
import allure
import time


class TestConstructorBurger:

    @allure.title('Проверка появления модального окна об инфомации об ингредиенте')
    @allure.description('Кликаем на ингредиент. Проверям что окно с информацией об ингредиенте отображается')
    def test_popup_details_click_ingridient_popup_appearance(self, browser):
        page_main = MainPage()

        page_main.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.click_element(browser, locators.main_page.INGREDIENT_FIRST_BUN)

        assert page_main.check_visibility_modal_windows(browser, locators.main_page.INGRIDIENT_MODUL_WINDOWS) == "Element found"

    @allure.title('Проверка закрытия модального окна по кнопке крестик')
    @allure.description('Кликаем на ингредиент. Дожидаемся отображения модального окна. Закрываем модальное окно через крестик. Проверям что окно не отображается')
    def test_close_popup_details_click_ingridient_close_popup(self, browser):
        page_main = MainPage()

        page_main.wait_for_invisibility_element(browser, locators.main_page.START_MODUL_WINDOWS)
        page_main.click_element(browser, locators.main_page.INGREDIENT_FIRST_BUN)
        page_main.click_element(browser, locators.main_page.BUTTON_CLOSE_MODAL_WINDOWS_DETAILS)
        time.sleep(2)

        assert page_main.check_visibility_modal_windows(browser, locators.main_page.INGRIDIENT_MODUL_WINDOWS) == "Element not found"