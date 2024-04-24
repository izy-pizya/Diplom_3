import allure
from locators.main_page_locators import MainPageLocators, HeadersLocators
from locators.orderlist_page_locators import OrderListPageLocators
from pages.base_page import BasePage
from static_data import Urls


class MainPage(BasePage):
    @allure.step('Переходим на страницу ЛК')
    def click_account_button(self):
        self.click_element(HeadersLocators.ACCOUNT_LINK)

    @allure.step('Переходим на страницу Лента заказов')
    def click_orderlist_button(self):
        self.click_element(HeadersLocators.ORDER_LIST_LINK)
        self.wait_until_element_visibility(10, OrderListPageLocators.ORDER_LIST_TITLE)

    @allure.step('Переходим в Конструктор')
    def click_construction_button(self):
        self.click_element(HeadersLocators.CONSTRUCTOR_LINK)
        self.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем на ингредиент')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_BUN)
        self.wait_until_element_visibility(10, MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Закрываем попап крестиком')
    def click_close_button(self):
        self.click_element(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Добавляем ингредиент "Флюоресцентная булка" в корзину заказа')
    def add_bun_to_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавляем ингредиент "Говяжий метеорит (отбивная)" в корзину заказа')
    def add_filling_to_basket(self):
        self.click_element(MainPageLocators.FILLING)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавляем ингредиент "Соус Spicy-X" в корзину заказа')
    def add_sauce_to_basket(self):
        self.click_element(MainPageLocators.SAUCES)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Получаем количество добавленного в корзину ингредиента')
    def check_counter_of_ingredients(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создаем заказ и получаем его номер')
    def create_order(self):
        self.go_to_site(Urls.url_main)
        self.wait_until_element_visibility(20, MainPageLocators.CONSTRUCTOR_TITLE)

        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.click_element(MainPageLocators.FILLING)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.click_element(MainPageLocators.SAUCES)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)
        self.click_element(MainPageLocators.ORDER_BUTTON)
        self.wait_until_element_visibility(10, MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_until_element_invisibility(20, MainPageLocators.DEFAULT_ORDER)

        order_number = self.get_element_text(MainPageLocators.ORDER_NUMBER)

        self.click_element(MainPageLocators.CLOSE_BUTTON)

        return order_number
