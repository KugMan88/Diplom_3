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
        self.wait_visibility_element(UserAccountLocators.PROFILE_BTN)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_btn(self):
        self.click_to_visible_element(UserAccountLocators.EXIT_BTN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_list(self):
        self.click_to_visible_element(UserAccountLocators.ORDERS_HISTORY_BTN)

    @allure.step('Получение номера заказа в "История заказов"')
    def get_order_number(self):
        return self.get_text_of_element(UserAccountLocators.ORDER_NUMBER)
