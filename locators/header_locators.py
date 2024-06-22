from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_BTN = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # кнопка "Конструктор"
    ORDERS_LIST_BTN = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'  # кнопка "Лента Заказов"
    ACCOUNT_BTN = By.XPATH, '//*[@href="/account"]'  # кнопка "Личный Кабинет"


