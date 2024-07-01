from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTER_ACCOUNT_BTN = By.XPATH, '//button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт"
    BURGER_CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'  # заголовок "Соберите бургер"
    CREATE_ORDER_BTN = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    INGREDIENT_BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'  # ингридиент "Флюоресцентная булка R2-D3"
    INGREDIENT_SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]'  # ингредиент "Соус Spicy-X"
    INGREDIENT_FILLING = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]'  # ингридиент "Мясо бессмертных моллюсков Protostomia"
    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]//p[contains(@class, "counter__num")]'  # счетчик ингредиента "Краторная булка N-200i"
    INGREDIENT_POPUP_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]'  # заголовок всплывающего окна "Детали ингредиента"
    INGREDIENT_POPUP = By.XPATH, '//*[contains(@class, "contentBox")]'  # всплывающее окно "Детали ингредиента"
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]'  # корзина заказа
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'  # номер заказа в всплывающем окне
    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[text()="9999"]'  # номер заказа по умолчанию в всплывающем окне
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'  # "Ваш заказ начали готовить" в всплывающем окне
    CLOSE_BTN = By.XPATH, '//button[contains(@class,"close")]'  # кнопка закрытия всплывающего окна
