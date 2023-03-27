import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CatalogPage(BasePage):

    @allure.step("Checking the visibility of the banner on the main page.")
    def is_banner_visible(self):
        return self.is_element_visible(By.CSS_SELECTOR, "#banner0")

    @allure.step("")
    def is_list_view_icon_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#list-view")

    @allure.step("")
    def is_product_visible(self):
        return self.is_element_visible(By.CSS_SELECTOR,
                                       ".product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12")

    @allure.step("Adding a product to the wishlist from the product preview.")
    def adding_product_to_wishlist_from_preview(self):
        # heart_list = self.get_elements(By.CSS_SELECTOR, ".product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12 .fa.fa-heart")
        # self.click(By.CSS_SELECTOR, random.choice(heart_list))
        self.click(By.CSS_SELECTOR,
                   ".product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12 .fa.fa-heart")  # TODO клик на сердце продукта в превью, а лучше на рандомный продукт из имеющихся
        self.is_element_visible(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        self.click(By.LINK_TEXT, "wish list")

    @allure.step("Adding a product to the wishlist from the detail page.")
    def adding_product_to_wishlist_from_detailview(self, product_name):
        self.click(By.LINK_TEXT, product_name)  # TODO клик на продукт, а лучше на рандомный продукт из имеющихся
        # heart_list = self.get_elements(By.CSS_SELECTOR, ")
        # self.click(By.CSS_SELECTOR, random.choice(heart_list))
        self.click(By.CSS_SELECTOR, ".btn.btn-default .fa.fa-heart")
        self.is_element_visible(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        self.click(By.LINK_TEXT, "wish list")
