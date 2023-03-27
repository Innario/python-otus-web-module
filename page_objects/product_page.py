import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):

    def is_fa_hearts_found(self):
        return self.is_element_found(By.CSS_SELECTOR, ".fa.fa-heart")

    def is_fa_exchanges_found(self):
        return self.is_element_found(By.CSS_SELECTOR, ".fa.fa-exchange")

    def is_button_cart_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#button-cart")

    def is_thumbnails_found(self):
        return self.is_element_found(By.CSS_SELECTOR, ".thumbnail")

    @allure.step("")
    def get_related_products(self):
        return self.get_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-3")

    @allure.step("")
    def product_check_in_the_wishlist(self, product_name):
        self.is_element_visible(By.LINK_TEXT, product_name)
