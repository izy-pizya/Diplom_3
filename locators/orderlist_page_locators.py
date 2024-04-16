from selenium.webdriver.common.by import By


class OrderListPageLocators:
    ORDER_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  #Заголовок Лента заказов
    ORDER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]' #номер заказа в работе
    ORDERS_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'
    #количество выполненных заказов (за все время)
    ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'
    #количество выполненных заказов (за сегодня)
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ORDER_NUMBER_IN_LIST = By.XPATH, '//p[text()="{}"]'  # номер заказа из Ленты заказов
    ORDER_CONTENT = By.XPATH, '//p[text()="Cостав"]'  # заголовок Состав в окне с деталями заказа
    ALL_READY_TITLE = By.XPATH, '//li[text()="Все текущие заказы готовы!"]' # текст Все текущие заказы готовы!
