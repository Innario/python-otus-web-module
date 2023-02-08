from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class NewProductForm(BasePage):

    def add_product(self, name, meta_tag, model):
        self.input(By.CSS_SELECTOR, "#input-name1", name)
        self.input(By.CSS_SELECTOR, "#input-meta-title1", meta_tag)
        self.click(By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
        self.input(By.CSS_SELECTOR, "#input-model", model)
        self.click(By.CSS_SELECTOR, ".fa.fa-save")
