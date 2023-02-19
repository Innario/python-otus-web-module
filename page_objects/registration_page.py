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

    def fill_registration_form(self, f_name, l_name, email, phone, password):
        self.input(By.CSS_SELECTOR, "#input-firstname", f_name)
        self.input(By.CSS_SELECTOR, "#input-lastname", l_name)
        self.input(By.CSS_SELECTOR, "#input-email", email)
        self.input(By.CSS_SELECTOR, "#input-telephone", phone)
        self.input(By.CSS_SELECTOR, "#input-password", password)
        self.input(By.CSS_SELECTOR, "#input-confirm", password)
        self.click(By.CSS_SELECTOR, "input[type='checkbox']")
        self.click(By.CSS_SELECTOR, ".btn.btn-primary")
        self.click(By.CSS_SELECTOR, ".btn.btn-primary")

    def is_new_user_created(self):
        return self.is_element_visible(By.CSS_SELECTOR, "#content > h2")
