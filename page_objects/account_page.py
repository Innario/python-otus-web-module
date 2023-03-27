from selenium.webdriver.common.by import By

from .base_page import BasePage


class AccountPage(BasePage):

    def is_user_logged_in(self):
        self.logger.info("Checking the display of elements on the account page")
        self.is_element_visible(By.CSS_SELECTOR, "#content > h2:nth-child(1)")
        self.is_element_visible(By.CSS_SELECTOR, "#content > h2:nth-child(3)")
        self.is_element_visible(By.CSS_SELECTOR, "#content > h2:nth-child(5)")
        self.is_element_visible(By.CSS_SELECTOR, "#content > h2:nth-child(7)")

    def logout(self):
        self.logger.info("logout")
        self.click(By.CSS_SELECTOR, "a[title='My Account']")
        self.click(By.LINK_TEXT, "Logout")

    def is_user_logged_out(self):
        self.logger.info("Сhecking items after logging out of the account on the account page")
        self.is_element_visible(By.CSS_SELECTOR, "#content > h1")
        self.click(By.LINK_TEXT, "Continue")
        self.is_element_visible(By.CSS_SELECTOR, "slideshow0")
