from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, browser):
        super(AdminPage, self).__init__(browser)
        self.browser.get(f"{self.browser.url}/admin")

    def login(self, username, password):
        self.input(By.ID, "input-username", username)
        self.input(By.ID, "input-password", password)
        self.click(By.CSS_SELECTOR, ".btn.btn-primary")

    def is_username_input_found(self):
        return self.is_element_found(By.ID, "input-username")

    def is_password_input_found(self):
        return self.is_element_found(By.ID, "input-password")

    def is_forgotten_link_found(self):
        return self.is_element_found(By.LINK_TEXT, "Forgotten Password")

    def is_login_button_found(self):
        return self.is_element_found(By.CSS_SELECTOR, ".btn.btn-primary")

    def is_opencart_link_found(self):
        return self.is_element_found(By.LINK_TEXT, "OpenCart")

    def add_new_product(self):
        pass

    def is_new_product_found(self):
        # return self.is_element_found(By.CSS_SELECTOR, "sdad")
        pass
