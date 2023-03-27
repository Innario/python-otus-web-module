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

    @allure.step("Click Show All element from menu")
    def click_show_all_from_menu(self, tab_name, all_section_link):
        self.logger.info(f"Click on an element '{tab_name}' from menu")
        menu_element_desktop = self.browser.find_element(By.LINK_TEXT, tab_name)
        action = ActionChains(self.browser)
        hover = action.move_to_element(menu_element_desktop)
        hover.perform()
        WebDriverWait(self.browser, 2)
        self.browser.find_element(By.LINK_TEXT, all_section_link).click()

    def click_menu_tab(self, tab_name):
        self.click(By.LINK_TEXT, tab_name)

    @allure.step("Click {product_name}")
    def click_product(self, product_name):
        self.logger.info(f"Click {product_name}")
        self.browser.find_element(By.LINK_TEXT, product_name).click()

    @allure.step("Opening register page")
    def open_register_page(self):
        self.logger.info("Opening the registration page")
        self.browser.find_element(By.CSS_SELECTOR, ".fa.fa-user").click()
        self.browser.find_element(By.LINK_TEXT, "Register").click()

    @allure.step("")
    def open_login_page(self):
        self.logger.info("Opening the login page")
        self.browser.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
        self.browser.find_element(By.LINK_TEXT, "Login").click()

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

    @allure.step("Get product price")
    def input_product_name(self, searching_product_name):
        # может перенести серчинг в отдельный класс HeaderPage?
        self.click(By.CSS_SELECTOR, "#search")
        self.input(By.CSS_SELECTOR, ".form-control.input-lg", f"{searching_product_name}")
        self.click(By.CSS_SELECTOR, ".fa.fa-search")
