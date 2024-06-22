import allure
from locators.orders_page_locators import OrdersPageLocators
from locators.user_account_locators import UserAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.user_account_page import UserAccountPage
from conftest import driver, login, create_and_delete_user


class TestOrderListPage:
    @allure.title('Проверка всплывающего окна с деталями заказа')
    def test_open_order_details_popup(self, driver):
        HeaderPage(driver).click_orders_list_btn()
        OrdersPage(driver).click_order()
        assert OrdersPage(driver).check_element(OrdersPageLocators.ORDER_STRUCTURE_TITLE).is_displayed()

    @allure.title('Проверка отображения созданного заказа в Ленте заказов')
    def test_new_order_in_orderlist(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        order_page = OrdersPage(driver)
        main_page.make_order_and_get_order_number()
        account_page.click_account_btn()
        account_page.click_on_order_list()
        account_page.find_element(UserAccountLocators.ORDER_STATUS)
        order_number = account_page.get_order_number()
        header_page.click_orders_list_btn()
        order_page.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        wanted_order = order_page.get_order_in_orderlist(order_number)
        assert wanted_order.is_displayed()

    @allure.title('Проверка изменения счетчика "Выполнено за все время" после создания заказа')
    def test_change_counter_total_orders(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        main_page.find_element(MainPageLocators.INGREDIENT_BUN)
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        total_number = orders_page.get_total_orders_number()
        header_page.click_constructor_btn()
        main_page.wait_visibility_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        new_total_number = orders_page.get_total_orders_number()
        assert int(new_total_number) == int(total_number) + 1

    @allure.title('Проверка изменения счетчика "Выполнено за сегодня" после создания заказа')
    def test_change_counter_today_orders(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        order_page = OrdersPage(driver)
        main_page.find_element(MainPageLocators.INGREDIENT_BUN)
        header_page.click_orders_list_btn()
        order_page.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        today_number = order_page.get_today_orders_number()
        header_page.click_constructor_btn()
        main_page.wait_visibility_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        order_page.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        new_number = order_page.get_today_orders_number()
        assert int(new_number) == int(today_number) + 1

    @allure.title('Проверка отображения нового заказа в списке "В работе"')
    def test_new_order_appears_in_work_list(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        new_order = main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_element(OrdersPageLocators.ALL_ORDERS_READY)
        orders_page.wait_visibility_element(OrdersPageLocators.ORDER_IN_WORK)
        order_in_work = orders_page.get_order_number_in_work()
        assert new_order in order_in_work
