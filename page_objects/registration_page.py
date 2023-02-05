from selenium.webdriver.common.by import By

from .base_page import BasePage


class RegistrationPage(BasePage):
    def is_input_firstname_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#input-firstname")

    def is_input_lastname_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#input-lastname")

    def is_input_password_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#input-password")

    def is_input_password_confirm_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#input-confirm")

    def is_agree_checkbox_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "[name=agree]")

    def is_continue_button_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "[value=Continue]")
