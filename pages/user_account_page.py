import allure
from locators.user_account_locators import UserAccountLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class UserAccountPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_password_recover_btn(self):
        self.click_to_visible_element(UserAccountLocators.RESET_PASSWORD_BTN)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_account_btn(self):
        self.move_to_element_and_click(HeaderLocators.ACCOUNT_BTN)
        self.find_element(UserAccountLocators.PROFILE_BTN)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_btn(self):
        self.click_to_visible_element(UserAccountLocators.EXIT_BTN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_list(self):
        self.click_to_visible_element(UserAccountLocators.ORDERS_HISTORY_BTN)

    @allure.step('Получение номера заказа в "История заказов"')
    def get_order_number(self):
        return self.get_text_of_element(UserAccountLocators.ORDER_NUMBER)

    @allure.step('Вход в систему с email: {email}')
    def login(self, email, password):
        self.set_text_to_element(UserAccountLocators.INPUT_EMAIL, email)
        self.set_text_to_element(UserAccountLocators.INPUT_PASSWORD, password)
        self.click_to_visible_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Проверка видимости статуса заказа')
    def is_order_status_visible(self):
        return self.find_element(UserAccountLocators.ORDER_STATUS)

    @allure.step('Проверка видимости кнопки "Профиль"')
    def is_profile_button_visible(self):
        return self.find_element(UserAccountLocators.PROFILE_BTN)

    @allure.step('Проверка видимости кнопки "Войти"')
    def is_enter_button_visible(self):
        return self.find_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Получение текста кнопки "Войти"')
    def get_enter_button_text(self):
        return self.get_text_of_element(UserAccountLocators.ENTER_BTN)