from selenium.webdriver.common.by import By


ORDER_BLOCK = [By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r:nth-of-type(1)"]
MODAL_WINDOW_ORDER = [By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]']
LAST_ORDER_FEED_ORDER = (By.XPATH, ".//h2[contains(@class, 'text_type_digits-large')]")
NUMBER_ORDER_ALL_TIME =[By.XPATH, "(.//p[@class= 'OrderFeed_number__2MbrQ text text_type_digits-large'])[1]"]
NUMBER_ORDER_TODAY = [By.XPATH, "(.//p[@class= 'OrderFeed_number__2MbrQ text text_type_digits-large'])[2]"]
ORDER_IN_WORK = [By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]"]
LOGO_FEED_ORDER = [By.XPATH, '//h1[text()="Лента заказов"]']
