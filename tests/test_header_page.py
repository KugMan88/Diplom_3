import allure
from locators.orders_page_locators import OrdersPageLocators
from pages.header_page import HeaderPage
from data import Urls
from conftest import driver


class TestHeaderPage:
    @allure.title('Проверка перехода в "Конструктор"')
    def test_redirect_to_constructor(self, driver):
        HeaderPage(driver).click_orders_list_btn()
        HeaderPage(driver).wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        HeaderPage(driver).click_constructor_btn()
        current_url = HeaderPage(driver).get_current_url()
        assert current_url == Urls.MAIN_PAGE

    @allure.title('Проверка перехода в Ленту заказов')
    def test_redirect_to_order_list(self, driver):
        HeaderPage(driver).click_orders_list_btn()
        current_url = HeaderPage(driver).get_current_url()
        assert current_url == Urls.FEED
