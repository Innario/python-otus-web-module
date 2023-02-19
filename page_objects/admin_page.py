from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, browser):
        super(AdminPage, self).__init__(browser)
        self.browser.get(f"{self.browser.url}/admin")

    def login(self, username, password):
        self.logger.debug("Login in Admin panel")
        self.input(By.ID, "input-username", username)
        self.input(By.ID, "input-password", password)
        self.click(By.CSS_SELECTOR, ".btn.btn-primary")

    def open_new_product_form(self):
        self.logger.debug("Opening a new product form")
        self.click(By.CSS_SELECTOR, "#menu-catalog > .parent.collapsed")
        self.click(By.LINK_TEXT, "Products")  # collapse1 > li.active > a
        self.click(By.CSS_SELECTOR, ".fa.fa-plus")

    def count_products(self, name, model):
        self.logger.debug("Product calculation")
        self.filter_products(name, model)
        element = self.get_element(By.CSS_SELECTOR, ".table.table-bordered.table-hover > tbody")
        if element.text == "No results!":
            return 0
        table_rows = element.text.split("\n")
        n_products = len(table_rows)
        return n_products

    def filter_products(self, name, model):
        self.logger.debug("Product filtering")
        self.input(By.CSS_SELECTOR, "#input-name", name)
        self.input(By.CSS_SELECTOR, "#input-model", model)
        self.click(By.CSS_SELECTOR, "#button-filter")

    def open_products_table(self):
        self.click(By.CSS_SELECTOR, "#menu-catalog > .parent.collapsed")
        self.click(By.LINK_TEXT, "Products")  # collapse1 > li.active > a

    def delete_product(self, name, model):
        self.logger.debug("Removing a product")
        self.filter_products(name, model)
        self.click(By.CSS_SELECTOR, "input[type='checkbox']")
        self.click(By.CSS_SELECTOR, ".fa.fa-trash-o")
        alert = WebDriverWait(self.browser, 1).until(expected_conditions.alert_is_present())
        alert.accept()

    def is_username_input_found(self):
        self.logger.info("Checking for the presence of an element 'input-username'")
        return self.is_element_found(By.ID, "input-username")

    def is_password_input_found(self):
        self.logger.info("Checking for the presence of an element 'input-password'")
        return self.is_element_found(By.ID, "input-password")

    def is_forgotten_link_found(self):
        self.logger.info("Checking for the presence of an element 'Forgotten Password'")
        return self.is_element_found(By.LINK_TEXT, "Forgotten Password")

    def is_login_button_found(self):
        self.logger.info("Checking for the presence of an element '.btn.btn-primary'")
        return self.is_element_found(By.CSS_SELECTOR, ".btn.btn-primary")

    def is_opencart_link_found(self):
        self.logger.info("Checking for the presence of an element 'OpenCart'")
        return self.is_element_found(By.LINK_TEXT, "OpenCart")
