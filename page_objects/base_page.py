from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def click(self, locator, selector):
        element = self.get_element(locator, selector)
        ActionChains(self.browser).move_to_element(element).pause(0.5).click().perform()
        return element

    def is_element_found(self, locator, selector):
        try:
            # WAITER
            self.browser.find_element(locator, selector)
            return True
        except Exception as ex:
            print(f"Element {selector} by {locator} not found: {ex}")
            return False

    def get_elements(self, locator, selector):
        try:
            # WAITER
            return self.browser.find_elements(locator, selector)

        except Exception as ex:
            print(f"Elements {selector} by {locator} not found: {ex}")
            return []

    def get_element(self, locator, selector):
        try:
            wait = WebDriverWait(self.browser, 1)
            return wait.until(expected_conditions.visibility_of_element_located((locator, selector)))
        except Exception as ex:
            print(f"Element by {locator} not found: {ex}")
            return

    def is_element_visible(self, locator, selector):
        try:
            wait = WebDriverWait(self.browser, 1)
            wait.until(expected_conditions.visibility_of_element_located((locator, selector)))
            return True
        except Exception as ex:
            print(f"Element {selector} by {locator} not visible: {ex}")
            return False

    def input(self, locator, selector, value):
        element = self.click(locator, selector)
        element.clear()
        element.send_keys(value)
