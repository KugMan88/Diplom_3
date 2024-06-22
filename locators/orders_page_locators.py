from selenium.webdriver.common.by import By


class OrdersPageLocators:
    ORDERS_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  # заголовок "Лента заказов"
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в списке "Лента заказа"
    ORDER_STRUCTURE_TITLE = By.XPATH, '//p[text()="Cостав"]'  # заголовок "Состав" в окне с деталями заказа
    ORDER_NUMBER = By.XPATH, '//p[text()="{}"]'  # номер заказа из списка "Лента заказов"
    ALL_ORDERS_READY = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'  # текст "Все текущие заказы готовы!"
    ORDER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'  # номер заказа в работе
    COMPLETED_ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'  # количество заказов выполненных сегодня
    COMPLETED_ORDERS_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'  # количество заказов выполненных за всё время

