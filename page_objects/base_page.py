import logging

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler("logs/tests_logs.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)

    @allure.step("Clicking element {locator}")
    def click(self, locator, selector):
        element = self.get_element(locator, selector)
        ActionChains(self.browser).move_to_element(element).pause(0.5).click().perform()
        return element

    @allure.step("Element is found")
    def is_element_found(self, locator, selector):
        try:
            # WAITER
            self.browser.find_element(locator, selector)
            return True
        except Exception as ex:
            self.logger.error(f"Element {selector} by {locator} not found: {ex}")
            allure.attach(f"Element {selector} by {locator} not found: {ex}")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            return False

    @allure.step("Getting elements")
    def get_elements(self, locator, selector):
        try:
            # WAITER
            return self.browser.find_elements(locator, selector)

        except Exception as ex:
            self.logger.error(f"Elements {selector} by {locator} not found: {ex}")
            allure.attach(f"Elements {selector} by {locator} not found: {ex}")

            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            return []

    @allure.step("Getting an element")
    def get_element(self, locator, selector):
        try:
            wait = WebDriverWait(self.browser, 1)
            return wait.until(expected_conditions.visibility_of_element_located((locator, selector)))
        except Exception as ex:
            self.logger.error(f"Element by {locator} not found: {ex}")
            allure.attach(f"Element by {locator} not found: {ex}")

            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            return

    @allure.step("Checking the visibility of an element")
    def is_element_visible(self, locator, selector):
        try:
            wait = WebDriverWait(self.browser, 1)
            wait.until(expected_conditions.visibility_of_element_located((locator, selector)))
            return True
        except Exception as ex:
            self.logger.error(f"Element {selector} by {locator} not visible: {ex}")
            allure.attach(f"Element {selector} by {locator} not visible: {ex}")

            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            return False

    @allure.step("Input {value} in input {locator}")
    def input(self, locator, selector, value):
        element = self.click(locator, selector)
        element.clear()
        element.send_keys(value)
        allure.attach(f"Clicked element {selector}")
