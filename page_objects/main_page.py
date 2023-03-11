import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class MainPage(BasePage):

    def is_logo_found(self):
        self.logger.info("Checking for the presence of an element 'img-responsive'")
        return self.is_element_found(By.CLASS_NAME, "img-responsive")

    def is_menu_found(self):
        self.logger.info("Checking for the presence of an element '#menu'")
        return self.is_element_found(By.CSS_SELECTOR, "#menu")

    def is_slideshow_found(self):
        self.logger.info("Checking for the presence of an element 'slideshow0'")
        return self.is_element_found(By.ID, "slideshow0")

    def is_pagination_found(self):
        self.logger.info("Checking for the presence of an element 'swiper-pagination-bullets'")
        return self.is_element_found(By.CSS_SELECTOR,
                                     ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets")

    def is_product_row_found(self):
        self.logger.info("Checking for the presence of an element '.row'")
        return self.is_element_found(By.CSS_SELECTOR, ".row")

    @allure.step("Click on an element 'Show All Desktops' from menu")
    def click_all_desktops_from_menu(self):
        self.logger.info("Click on an element 'Show All Desktops' from menu")
        menu_element_desktop = self.browser.find_element(By.LINK_TEXT, "Desktops")
        action = ActionChains(self.browser)
        hover = action.move_to_element(menu_element_desktop)
        hover.perform()
        WebDriverWait(self.browser, 2)
        self.browser.find_element(By.LINK_TEXT, "Show All Desktops").click()

    @allure.step("Click 'Apple Cinema 30'")
    def click_product(self):
        self.logger.info("Click 'Apple Cinema 30'")
        self.browser.find_element(By.LINK_TEXT, "Apple Cinema 30\"").click()

    def open_register_page(self):
        self.logger.info("Opening the registration page")
        self.browser.find_element(By.CSS_SELECTOR, ".fa.fa-user").click()
        self.browser.find_element(By.LINK_TEXT, "Register").click()

    @allure.step("Change currency")
    def change_currency(self, to):
        self.logger.info("Change currency")
        self.click(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle")
        self.click(By.CSS_SELECTOR, f"[name={to}]")

    @allure.step("Get product price")
    def get_product_prices(self):
        self.logger.info("Get product price")
        prices = []
        for element in self.get_elements(By.CSS_SELECTOR, ".price"):
            product_price = element.text.split("\n")
            prices.extend(product_price)
        return prices
