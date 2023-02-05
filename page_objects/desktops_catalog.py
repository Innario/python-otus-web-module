from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class DesktopsCatalog(BasePage):

    def is_banner_visible(self):
        return self.is_element_visible(By.CSS_SELECTOR, "#banner0")

    def is_list_view_icon_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#list-view")

    def is_product_visible(self):
        return self.is_element_visible(By.CSS_SELECTOR,
                                       ".product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12")
