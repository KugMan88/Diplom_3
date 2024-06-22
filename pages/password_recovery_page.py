import allure
from locators.password_recovery_locators import PasswordRecoverLocators
from pages.base_page import BasePage


class PasswordRecoverPage(BasePage):
    @allure.step('Ввод email в поле для восстановления пароля')
    def set_email_for_recover_password(self, email):
        self.set_text_to_element(PasswordRecoverLocators.INPUT_EMAIL, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recover_btn(self):
        self.move_to_element_and_click(PasswordRecoverLocators.RECOVER_BTN)

    @allure.step('Клик по иконке Показать/скрыть пароль')
    def click_on_show_password_icon(self):
        self.click_to_visible_element(PasswordRecoverLocators.SHOW_PASSWORD_ICON)
