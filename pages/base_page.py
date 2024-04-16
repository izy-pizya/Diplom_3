from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url='https://stellarburgers.nomoreparties.site/'):
        return self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_until_element_visibility(self, time, locator):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_until_element_invisibility(self, time, locator):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def drag_and_drop_element(self, locator_from, locator_to):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()
