from selenium.webdriver.common.by import By


class PasswordRecoverLocators:
    RECOVER_BTN = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить"
    SAVE_BTN = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить"
    SHOW_PASSWORD_ICON = By.XPATH, '//div[contains(@class,"icon-action")]'  # кнопка "Показать пароль"
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле ввода пароля
    INPUT_PASSWORD_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  # активное поле пароль
