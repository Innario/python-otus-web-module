from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_main_page(browser):
    browser.find_element(By.CLASS_NAME, "img-responsive")
    browser.find_element(By.CSS_SELECTOR, "#menu")
    browser.find_element(By.ID, "slideshow0")
    browser.find_element(By.CSS_SELECTOR,
                         ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets")
    browser.find_element(By.CLASS_NAME, "row")


def test_catalog_elements(browser):
    menu_element_desktop = browser.find_element(By.LINK_TEXT, "Desktops")
    action = ActionChains(browser)
    hover = action.move_to_element(menu_element_desktop)
    hover.perform()
    wait = WebDriverWait(browser, 5)
    browser.find_element(By.LINK_TEXT, "Show All Desktops").click()
    browser.find_element(By.CSS_SELECTOR, "#list-view")
    wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".product-layout.product-grid.col-lg-4.col-md-4.col-sm-6.col-xs-12")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#banner0")))


def test_product_page(browser):
    browser.get(browser.url + "/test")
    browser.find_elements(By.CSS_SELECTOR, ".fa.fa-heart")
    browser.find_elements(By.CSS_SELECTOR, ".fa.fa-exchange")
    browser.find_element(By.CSS_SELECTOR, "#button-cart")
    browser.find_element(By.CSS_SELECTOR, ".thumbnails > li > .thumbnail")
    assert len(browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-3"))


def test_admin_login_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.ID, "input-password")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.find_element(By.LINK_TEXT, "OpenCart")


def test_registration_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    browser.find_element(By.CSS_SELECTOR, "#input-lastname")
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "#input-confirm")
    browser.find_element(By.CSS_SELECTOR, "[name=agree]")
    browser.find_element(By.CSS_SELECTOR, "[value=Continue]")
