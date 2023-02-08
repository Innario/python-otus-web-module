from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class MainPage(BasePage):

    def is_logo_found(self):
        return self.is_element_found(By.CLASS_NAME, "img-responsive")

    def is_menu_found(self):
        return self.is_element_found(By.CSS_SELECTOR, "#menu")

    def is_slideshow_found(self):
        return self.is_element_found(By.ID, "slideshow0")

    def is_pagination_found(self):
        return self.is_element_found(By.CSS_SELECTOR,
                                     ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets")

    def is_product_row_found(self):
        return self.is_element_found(By.CSS_SELECTOR, ".row")

    def click_all_desktops_from_menu(self):
        menu_element_desktop = self.browser.find_element(By.LINK_TEXT, "Desktops")
        action = ActionChains(self.browser)
        hover = action.move_to_element(menu_element_desktop)
        hover.perform()
        wait = WebDriverWait(self.browser, 2)
        self.browser.find_element(By.LINK_TEXT, "Show All Desktops").click()

    def click_product(self):
        self.browser.find_element(By.LINK_TEXT, "Apple Cinema 30\"").click()

    def open_register_page(self):
        self.browser.find_element(By.CSS_SELECTOR, ".fa.fa-user").click()
        self.browser.find_element(By.LINK_TEXT, "Register").click()

    def change_currency(self, to):
        self.click(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle")
        self.click(By.CSS_SELECTOR, f"[name={to}]")

    def get_product_prices(self):
        prices = []
        for element in self.get_elements(By.CSS_SELECTOR, ".price"):
            product_price = element.text.split("\n")
            prices.extend(product_price)
        return prices
