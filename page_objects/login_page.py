import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Authorization")
    def fill_authorization_form(self, email, password):
        self.logger.info("Filling out the user authorization form")
        self.input(By.CSS_SELECTOR, "#input-email", email)
        self.input(By.CSS_SELECTOR, "#input-password", password)
        self.logger.info("Click on Login button")
        self.click(By.CSS_SELECTOR, ".btn.btn-primary[value='Login']")
