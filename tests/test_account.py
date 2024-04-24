import allure
from locators.account_page_locators import AuthPageLocators
from pages.account_page import AccountPage
from static_data import Urls
from conftest import *


class TestAccountPage:
    @allure.title('Check navigation via the Personal Account button')
    def test_go_to_account_from_header(self, driver, create_user):
        page = AccountPage(driver)
        page.go_to_site(Urls.url_main)
        page.click_element(MainPageLocators.ENTER_BUTTON)
        page.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        page.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        page.click_element(AuthPageLocators.ENTER_BUTTON)
        page.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        page.click_account_button()
        current_url = page.get_current_url()

        assert current_url == Urls.url_account

    @allure.title('Check navigation to the Order History section')
    def test_go_to_order_history(self, driver, create_user):
        page = AccountPage(driver)
        page.go_to_site(Urls.url_main)
        page.click_element(MainPageLocators.ENTER_BUTTON)
        page.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        page.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        page.click_element(AuthPageLocators.ENTER_BUTTON)
        page.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        page.click_account_button()
        page.click_order_list_link()
        current_url = page.get_current_url()

        assert current_url == Urls.url_history

    @allure.title('Check user logout functionality')
    def test_user_logout(self, driver, create_user):
        page = AccountPage(driver)
        page.go_to_site(Urls.url_main)
        page.click_element(MainPageLocators.ENTER_BUTTON)
        page.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        page.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        page.click_element(AuthPageLocators.ENTER_BUTTON)
        page.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        page.click_account_button()
        page.click_logout_button()
        page.wait_until_element_visibility(10, AuthPageLocators.ENTER_BUTTON)
        button_text = page.get_element_text(AuthPageLocators.ENTER_BUTTON)

        assert button_text == 'Войти'
