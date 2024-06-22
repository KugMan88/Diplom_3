import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver, login, create_and_delete_user
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:
    @allure.title('Проверка появления всплывающее окна после клика по ингредиенту')
    def test_open_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        bun_element = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_BUN))
        bun_element.click()
        popup_text = main_page.get_text_of_element(MainPageLocators.INGREDIENT_POPUP_TITLE)
        assert popup_text == "Детали ингредиента"

    @allure.title('Проверка закрытия всплывающего окна ингредиента кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        bun_element = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_BUN))
        bun_element.click()
        main_page.click_close_btn()
        WebDriverWait(driver, 100).until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_POPUP))
        assert main_page.check_element(MainPageLocators.INGREDIENT_POPUP).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        ingredient_counter = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER))
        start_quantity = int(ingredient_counter.text)
        main_page.add_filling_to_order_basket()
        ingredient_counter = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_COUNTER))
        end_quantity = int(ingredient_counter.text)
        assert end_quantity > start_quantity

    @allure.title('Проверка создания заказа')
    def test_make_order(self, driver, login):
        MainPage(driver).find_element(MainPageLocators.INGREDIENT_BUN)
        MainPage(driver).add_bun_to_order_basket()
        MainPage(driver).add_sauce_to_order_basket()
        MainPage(driver).click_order_btn()
        MainPage(driver).find_element(MainPageLocators.ORDER_NUMBER)
        assert MainPage(driver).check_element(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True
