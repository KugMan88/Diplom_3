import allure
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.password_recovery_page import PasswordRecoverPage
from pages.header_page import HeaderPage
from conftest import driver, create_and_delete_user


class TestPasswordRecover:
    @allure.title('Проверка перехода по клику на кнопку Восстановить пароль на странице логина')
    def test_click_password_recover_button(self, driver):
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        password_recover_page = PasswordRecoverPage(driver)
        header_page.click_user_account_btn()
        account_page.click_password_recover_btn()
        password_recover_page.click_recover_btn()
        assert password_recover_page.is_save_button_visible()

    @allure.title('Проверка перехода по кнопке Восстановить после ввода почты')
    def test_enter_email_and_click_recover(self, driver, create_and_delete_user):
        password_recover_page = PasswordRecoverPage(driver)
        password_recover_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        password_recover_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        password_recover_page.click_recover_btn()
        assert password_recover_page.is_save_button_visible()

    @allure.title('Проверка активности поля пароль после клика по иконке показать/скрыть')
    def test_active_password_field(self, driver, create_and_delete_user):
        PasswordRecoverPage(driver).open_page(Urls.FORGOT_PASSWORD_PAGE)
        PasswordRecoverPage(driver).set_email_for_recover_password(create_and_delete_user[0]['email'])
        PasswordRecoverPage(driver).click_recover_btn()
        PasswordRecoverPage(driver).is_save_button_visible()
        PasswordRecoverPage(driver).click_on_show_password_icon()
        assert PasswordRecoverPage(driver).is_password_field_active
