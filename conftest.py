import pytest
from selenium import webdriver
from helpers import *
from pages.main_page import MainPage
from pages.user_account_page import UserAccountPage
import requests
from data import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def create_and_delete_user():

    name = generate_random_string(10)
    email = generate_random_string(10)+'@yandex.ru'
    password = generate_random_string(10)

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(Urls.REGISTER_USER, data=payload)
    access_token = response.json()["accessToken"]
    yield login_data, access_token
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture
def login(driver, create_and_delete_user):
    main_page = MainPage(driver)
    user_account_page = UserAccountPage(driver)
    main_page.click_on_enter_btn()
    user_account_page.login(
        email=create_and_delete_user[0]['email'],
        password=create_and_delete_user[0]['password']
    )