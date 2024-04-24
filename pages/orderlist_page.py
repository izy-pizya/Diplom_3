import allure
from locators.orderlist_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.click_element(OrderListPageLocators.ORDER_LINK)

    @allure.step('Ищем заказ по номеру в Ленте заказов')
    def get_order_in_orderlist(self, order):
        path = OrderListPageLocators.ORDER_NUMBER_IN_LIST[0]
        locator = OrderListPageLocators.ORDER_NUMBER_IN_LIST[1]
        locator = locator.format(order)
        return self.get_element_text((path, locator))

    @allure.step('Получаем общее количество заказов, выполненных за все время')
    def get_alltime_orders_total(self):
        return self.get_element_text(OrderListPageLocators.ORDERS_TOTAL)

    @allure.step('Получаем общее количество заказов, выполненных за сегодня')
    def get_today_orders_total(self):
        return self.get_element_text(OrderListPageLocators.ORDERS_TODAY)

    @allure.step('Ищем заказ по номеру среди заказов в работе')
    def get_order_number_in_work(self):
        return self.get_element_text(OrderListPageLocators.ORDER_IN_WORK)
