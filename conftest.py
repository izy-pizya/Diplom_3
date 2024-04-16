import pytest
from selenium import webdriver
from locators.account_page_locators import *
from locators.main_page_locators import *
from pages.base_page import BasePage
from static_data import Urls
from generator import *


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.url_main)
    yield driver
    driver.quit()

@pytest.fixture
def create_user():
    login_pass, token = create_new_user()
    yield login_pass, token
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers={'Authorization': f'{token}'})


@pytest.fixture
def signin(driver, create_user):
    page = BasePage(driver)
    page.go_to_site(Urls.url_main)
    page.click_element(MainPageLocators.ENTER_BUTTON)
    page.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
    page.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
    page.click_element(AuthPageLocators.ENTER_BUTTON)
    page.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
