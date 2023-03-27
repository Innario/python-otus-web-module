import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SearchResultPage(BasePage):

    @allure.step("Getting search result")
    def searching_result(self):
        list_products = self.get_elements(By.CSS_SELECTOR, ".product-layout.product-grid.col-lg-3.col-md-3.col-sm-6.col-xs-12")
        return list_products

    @allure.step("Check search stub if product not found")
    def search_stub_check(self):
        self.get_element(By.CSS_SELECTOR, "#content > p:nth-child(7)")
        list_products = self.get_elements(By.CSS_SELECTOR, ".product-layout.product-grid.col-lg-3.col-md-3.col-sm-6.col-xs-12")
        return list_products  # нужна ли проверка на пустой список найденного??
