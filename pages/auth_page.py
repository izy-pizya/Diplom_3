import allure
from locators.account_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step('Нажимаем на Восстановить пароль')
    def click_password_reset_link(self):
        self.click_element(AuthPageLocators.RESET_PASSWORD_LINK)
