from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Ожидание загрузки выбранного элемента')
    def wait_for_load_element(self, element):
        WebDriverWait(self.browser, 3).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Клик по выбранному элементу')
    def click_element(self, find_element):
        self.browser.find_element(*find_element).click()

    @allure.step('Ожидание пропажи модульного окна"')
    def wait_for_invisibility_element(self, element):
        WebDriverWait(self.browser, 5).until(expected_conditions.invisibility_of_element_located(element))

    @allure.step('Ввод выбранных значений в поле')
    def set_input_data(self, find_element, data):
        self.browser.find_element(*find_element).send_keys(data)

    @allure.step('Получаем значение элемента')
    def get_find_element_on_page(self, find_element):
        return self.browser.find_element(*find_element)

    @allure.step('Получаем активный элемент')
    def active_element_on_page(self):
       return self.browser.switch_to.active_element

    @allure.step('Добавляем токен в LocalStorage для работы под авторизованным пользователем')
    def add_token_in_local_storage(self, token):
        script = f"localStorage.setItem('accessToken', '{token}');"
        self.browser.execute_script(script)

    @allure.step('Претаскивание элемента через drag and drop')
    def drag_and_drop_element(self, element_source, element_target):
        target = self.browser.find_element(*element_target)
        source = self.browser.find_element(*element_source)
        ActionChains(self.browser).drag_and_drop(source, target).pause(5).perform()

    @allure.step('Получаем текст выбранного элемента')
    def get_text_element(self, element):
        return self.browser.find_element(*element).text

    @allure.step('Получаем текущую страницу в браузере')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Дожидаемся появления элесента с текстом')
    def wait_for_text_in_element(self, element, text):
         WebDriverWait(self.browser, 15).until(expected_conditions.text_to_be_present_in_element(element, text))

