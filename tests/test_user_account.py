import allure
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.header_page import HeaderPage
from conftest import driver, login, create_and_delete_user


class TestUserAccount:
    @allure.title('Проверка перехода в личный кабинет через кнопку "Личный кабинет" в шапке')
    def test_redirect_to_account_from_header(self, driver, login):
        UserAccountPage(driver).click_account_btn()
        assert UserAccountPage(driver).get_current_url() == Urls.PROFILE_PAGE

    @allure.title('Проверка перехода в раздел История заказов')
    def test_redirect_to_order_history(self, driver, login):
        UserAccountPage(driver).click_account_btn()
        UserAccountPage(driver).click_on_order_list()
        assert UserAccountPage(driver).get_current_url() == Urls.ORDERS_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        header_page.click_user_account_btn()
        account_page.is_profile_button_visible()
        account_page.click_logout_btn()
        account_page.is_enter_button_visible()
        assert account_page.get_enter_button_text() == 'Войти'
