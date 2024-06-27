import allure
from pages.main_page import MainPage
from conftest import driver, login, create_and_delete_user





class TestMainPage:
    @allure.title('Проверка появления всплывающее окна после клика по ингредиенту')
    def test_open_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun()
        popup_text = main_page.get_ingredient_popup_title()
        assert popup_text == "Детали ингредиента"

    @allure.title('Проверка закрытия всплывающего окна ингредиента кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun()
        main_page.click_close_btn()
        assert not main_page.is_ingredient_popup_visible()

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        start_quantity = MainPage(driver).check_counter_of_ingredients()
        MainPage(driver).add_filling_to_order_basket()
        end_quantity = MainPage(driver).check_counter_of_ingredients()
        assert end_quantity > start_quantity

    @allure.title('Проверка создания заказа')
    def test_make_order(self, driver, login, create_and_delete_user):
        main_page = MainPage(driver)
        main_page.click_on_element()
        main_page.add_bun_to_order_basket()
        main_page.add_sauce_to_order_basket()
        main_page.click_order_btn()
        main_page.check_order_status_text()
        assert main_page.is_order_status_text_visible