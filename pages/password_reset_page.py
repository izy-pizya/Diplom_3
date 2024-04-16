import allure
from locators.account_page_locators import PasswordResetPageLocators
from pages.base_page import BasePage


class PasswordResetPage(BasePage):

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def input_email_for_reset(self, email):
        self.send_keys(PasswordResetPageLocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        self.click_element(PasswordResetPageLocators.RESET_BUTTON)

    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_show_password_icon(self):
        self.click_element(PasswordResetPageLocators.SHOW_PASSWORD_BUTTON)
