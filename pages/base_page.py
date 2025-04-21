import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import allure
import  time


class BasePage:
    @allure.step('Ожидание загрузки выбранного элемента')
    def wait_for_load_element(self, browser, element):
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Клик по выбранному элементу')
    def click_element(self, browser, find_element):
        browser.find_element(*find_element).click()

    @allure.step('Ожидание пропажи модульного окна"')
    def wait_for_invisibility_element(self, browser, element):
        WebDriverWait(browser, 3).until(expected_conditions.invisibility_of_element(element))

    @allure.step('Ввод выбранных значений в поле')
    def set_input_data(self, browser, find_element, data):
        browser.find_element(*find_element).send_keys(data)

    @allure.step('Поиск выбранного элемента')
    def find_element_on_page(self, browser, find_element):
        browser.find_element(*find_element)

    @allure.step('Получаем значение элемента')
    def get_find_element_on_page(self, browser, find_element):
        return browser.find_element(*find_element)

    @allure.step('Получаем активный элемент')
    def active_element_on_page(self, browser):
       return browser.switch_to.active_element

    @allure.step('Добавляем токен в LocalStorage для работы под авторизованным пользователем')
    def add_token_in_local_storage(self, browser, token):
        script = f"localStorage.setItem('accessToken', '{token}');"
        browser.execute_script(script)

    @allure.step('Претаскивание элемента через drag and drop')
    def drag_and_drop_element(self, browser, element_source, element_target):
        target = browser.find_element(*element_target)
        source = browser.find_element(*element_source)
        ActionChains(browser).drag_and_drop(source, target).pause(5).perform()


    @allure.step('Получаем текст выбранного элемента')
    def get_text_element(self, browser, element):
        return browser.find_element(*element).text

