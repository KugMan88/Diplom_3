import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Клик по видимому элементу')
    def click_to_visible_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).click()

    @allure.step('Проверка отображения элемента на странице')
    def check_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверка невидимости элемента на странице')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(locator))

    @allure.step('Ожидание невидимости элемента на странице')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Открыть страницу')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Ожидание открытия новой вкладки')
    def wait_open_new_tab(self, index):
        WebDriverWait(self.driver, 15).until(EC.number_of_windows_to_be(index))

    @allure.step('Ожидание открытия страницы {url}')
    def wait_open_page(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = self.find_element(locator_from)
        element_to = self.find_element(locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step('Перемещение до элемента и клик по нему')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
