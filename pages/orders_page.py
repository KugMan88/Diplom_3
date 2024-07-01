import allure
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage


class OrdersPage(BasePage):
    @allure.step('Клик по заказу в списке Лента заказов')
    def click_order(self):
        self.click_to_visible_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Получение заказа по номеру в Ленте заказов')
    def get_order_in_orderlist(self, order):
        method, locator = OrdersPageLocators.ORDER_NUMBER
        locator = locator.format(order)
        return self.find_element((method, locator))

    @allure.step('Получение количества заказов выполненных за все время')
    def get_total_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TOTAL)

    @allure.step('Получение количества заказов выполненных за сегодня')
    def get_today_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TODAY)

    @allure.step('Получение заказа по номеру в разделе "В работе"')
    def get_order_number_in_work(self):
        return self.get_text_of_element(OrdersPageLocators.ORDER_IN_WORK)

    @allure.step('Проверка открытия всплывающего окна с деталями заказа')
    def is_order_details_popup_opened(self):
        return self.check_element(OrdersPageLocators.ORDER_STRUCTURE_TITLE).is_displayed()

    @allure.step('Проверка видимости заголовка "Лента заказов"')
    def is_orders_list_title_visible(self):
        return self.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Проверка наличия элемента "Все заказы готовы"')
    def check_all_orders_ready(self):
        return self.find_element(OrdersPageLocators.ALL_ORDERS_READY)
    @allure.step('Проверка наличия элемента "Заказ в работе"')
    def check_order_in_work(self):
        return self.find_element(OrdersPageLocators.ORDER_IN_WORK)