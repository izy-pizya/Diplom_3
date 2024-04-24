import allure
from locators.orderlist_page_locators import OrderListPageLocators
from locators.account_page_locators import AccountPageLocators
from pages.orderlist_page import OrderListPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from conftest import *


class TestOrderListPage:
    @allure.title('Check opening the order details popup')
    def test_get_order_popup(self, driver):
        mainpage = MainPage(driver)
        mainpage.click_orderlist_button()
        page = OrderListPage(driver)
        page.click_order()

        assert page.find_element(OrderListPageLocators.ORDER_CONTENT).is_displayed() == True

    @allure.title('Check if the created order appears in the Order Feed')
    def test_find_order_in_list(self, driver, create_user):
        mainpage = MainPage(driver)
        accpage = AccountPage(driver)

        accpage.go_to_site(Urls.url_main)
        accpage.click_element(MainPageLocators.ENTER_BUTTON)
        accpage.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        accpage.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        accpage.click_element(AuthPageLocators.ENTER_BUTTON)
        accpage.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        mainpage.create_order()
        accpage.click_account_button()
        accpage.click_order_list_link()
        accpage.wait_until_element_visibility(10, AccountPageLocators.ORDER_STATUS)
        my_order = accpage.get_order_number()
        mainpage.click_orderlist_button()
        page = OrderListPage(driver)
        page.wait_until_element_visibility(15, OrderListPageLocators.ORDER_LIST_TITLE)
        order = page.get_order_in_orderlist(my_order)

        assert my_order in order

    @allure.title('Check if the total orders counter increases after creating an order')
    def test_total_orders_counter(self, driver, create_user):
        accpage = AccountPage(driver)
        accpage.go_to_site(Urls.url_main)
        accpage.click_element(MainPageLocators.ENTER_BUTTON)
        accpage.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        accpage.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        accpage.click_element(AuthPageLocators.ENTER_BUTTON)
        accpage.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        mainpage.click_orderlist_button()
        before_total = orderpage.get_alltime_orders_total()
        mainpage.create_order()
        mainpage.click_orderlist_button()
        after_total = orderpage.get_alltime_orders_total()

        assert before_total < after_total

    @allure.title('Check if the orders counter for today increases after creating an order')
    def test_today_orders_counter(self, driver, create_user):
        accpage = AccountPage(driver)
        accpage.go_to_site(Urls.url_main)
        accpage.click_element(MainPageLocators.ENTER_BUTTON)
        accpage.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        accpage.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        accpage.click_element(AuthPageLocators.ENTER_BUTTON)
        accpage.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        mainpage.click_orderlist_button()
        before_total = orderpage.get_today_orders_total()
        mainpage.create_order()
        mainpage.click_orderlist_button()
        after_total = orderpage.get_today_orders_total()

        assert before_total < after_total

    @allure.title('Check if the newly created order appears among the orders in progress')
    def test_new_order_appears_in_work_list(self, driver, create_user):
        accpage = AccountPage(driver)
        accpage.go_to_site(Urls.url_main)
        accpage.click_element(MainPageLocators.ENTER_BUTTON)
        accpage.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0][0])
        accpage.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[0][1])
        accpage.click_element(AuthPageLocators.ENTER_BUTTON)
        accpage.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)
        mainpage = MainPage(driver)
        new_order = mainpage.create_order()
        mainpage.click_orderlist_button()
        page = OrderListPage(driver)
        page.wait_until_element_invisibility(20, OrderListPageLocators.ALL_READY_TITLE)
        order_in_work = page.get_order_number_in_work()

        assert new_order in order_in_work
