from selenium.webdriver.common.by import By

ORDER_BLOCK = [By.XPATH, '//div[@class="OrderFeed_contentBox__3-tWb"]/ul/li[1]']
MODAL_WINDOW_ORDER = [By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]']
NUMBER_NEW_ORDER = [By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]']
BUTTON_CLOSE_POPUP_ORDER = [By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
LAST_ORDER_FEED_ORDER = [By.XPATH, '//div[@class="OrderFeed_contentBox__3-tWb"]/ul/li[1]/a/div/p[@class="text text_type_digits-default"]']
NUMBER_ORDER_ALL_TIME =[By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
NUMBER_ORDER_TODAY = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[last()]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
ORDER_IN_WORK = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[1]']
ORDER_IN_WORK_BAR = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]']
