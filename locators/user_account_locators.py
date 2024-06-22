from selenium.webdriver.common.by import By


class UserAccountLocators:
    ENTER_BTN = By.XPATH, '//button[text()="Войти"]'  # кнопка "Войти"
    RESET_PASSWORD_BTN = By.XPATH, '//*[@href="/forgot-password"]'  # кнопка "Восстановить пароль"
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле ввода пароля
    PROFILE_BTN = By.XPATH, '//*[@href="/account/profile"]'  # профиль пользователя
    ORDERS_HISTORY_BTN = By.XPATH, '//*[@href="/account/order-history"]'  # история заказов
    EXIT_BTN = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка Выход
    ORDER_STATUS = By.XPATH, '//p[text()="Выполнен"]'  # статус заказа в истории
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'  # номер заказа в истории
