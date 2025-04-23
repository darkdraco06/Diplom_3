from selenium.webdriver.common.by import By


LINK_PERSONAL_ACCOUNT = [By.XPATH, '//p[text()="Личный Кабинет"]']
START_MODUL_WINDOWS = [By.XPATH, '//div[@class="Modal_modal__P3_V5"]']
BUTTON_LOGIN_ACCOUNT = [By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]']
BUTTON_PLACE_ORDER = [By.XPATH, '//button[text()="Оформить заказ"]']
BUTTON_CONSTRUCTOR = [By.XPATH, '//p[text()="Конструктор"]']
BUTTON_FEED_ORDER = [By.XPATH, '//p[text()="Лента Заказов"]']
INGREDIENT_DETAILS_WINDOW = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"]
BUTTON_CLOSE_MODAL_WINDOWS_DETAILS = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]
BURGER_CONSTRUCTOR = [By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]']
MODAL_WINDOW_CREATE_ORDER_DONE = [By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]']
BUN_IN_ORDER = [By.XPATH, '//span[text()="Флюоресцентная булка R2-D3 (верх)"]']
INGRIDIENT_COUNTER_FIRST_BUN = [By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]"]
INGREDIENT_FIRST_BUN = [By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/parent::*']
