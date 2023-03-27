import time

import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CartPage(BasePage):

    @allure.step("Checking product in cart")
    def cart_checkout(self, product_name):
        self.click(By.CSS_SELECTOR, "#top-links a[href$='/cart']")  # ".alert.alert-success.alert-dismissible > a[href*='checkout/cart']"
        self.is_element_visible(By.LINK_TEXT, product_name)

    @allure.step("Adding a product with additional options to cart")
    def add_to_cart_with_product_options(self):
        self.select_by_text(By.CSS_SELECTOR, "#input-option226", "Red")
        self.input(By.CSS_SELECTOR, "#input-quantity", "2")
        self.click(By.CSS_SELECTOR, "#button-cart")

        self.is_element_visible(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        self.is_element_visible(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible > a[href*='canon-eos-5d']")

    @allure.step("Adding a product to the cart from the product detail page.")
    def add_to_cart(self, product_name):
        self.click(By.LINK_TEXT, product_name)
        self.click(By.CSS_SELECTOR, "#button-cart")
        self.is_element_visible(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    @allure.step("Removing product from cart")
    def remove_product_from_cart(self):
        self.click(By.CSS_SELECTOR, ".btn.btn-danger .fa.fa-times-circle")

    @allure.step("Checking for empty cart")
    def cart_is_empty(self):
        time.sleep(2)
        elements = self.get_elements(By.CSS_SELECTOR, "#content p")
        sources = [element.get_attribute("innerHTML") for element in elements]
        return "Your shopping cart is empty!" in sources
