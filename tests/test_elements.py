import time

from page_objects.admin_page import AdminPage
from page_objects.desktops_catalog import DesktopsCatalog
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.registration_page import RegistrationPage


def test_main_page(browser):
    main_page = MainPage(browser)
    assert main_page.is_logo_found()
    assert main_page.is_menu_found()
    assert main_page.is_slideshow_found()
    assert main_page.is_pagination_found()
    assert main_page.is_pagination_found()


def test_catalog_elements(browser):
    main_page = MainPage(browser)
    main_page.click_all_desktops_from_menu()
    desktops_catalog = DesktopsCatalog(browser)
    assert desktops_catalog.is_list_view_icon_found()
    assert desktops_catalog.is_product_visible()
    assert desktops_catalog.is_banner_visible()


def test_product_page(browser):
    main_page = MainPage(browser)
    main_page.click_product()
    product_page = ProductPage(browser)

    assert product_page.is_fa_hearts_found()
    assert product_page.is_fa_exchanges_found()
    assert product_page.is_button_cart_found()
    assert product_page.is_thumbnails_found()
    assert len(product_page.get_related_products())


def test_admin_login_page(browser):
    admin_page = AdminPage(browser)
    time.sleep(2)
    assert admin_page.is_username_input_found()
    assert admin_page.is_password_input_found()
    assert admin_page.is_forgotten_link_found()
    assert admin_page.is_login_button_found()
    assert admin_page.is_opencart_link_found()


def test_registration_page(browser):
    main_page = MainPage(browser)
    main_page.open_register_page()
    registration_page = RegistrationPage(browser)
    assert registration_page.is_input_firstname_found()
    assert registration_page.is_input_lastname_found()
    assert registration_page.is_input_password_found()
    assert registration_page.is_input_password_confirm_found()
    assert registration_page.is_agree_checkbox_found()
    assert registration_page.is_continue_button_found()
