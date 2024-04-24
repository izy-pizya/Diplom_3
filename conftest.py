import pytest
from selenium import webdriver
from locators.account_page_locators import *
from locators.main_page_locators import *
from pages.account_page import AccountPage
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
    requests.delete(Urls.auth_user, headers={'Authorization': f'{token}'})
