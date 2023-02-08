import pytest

from page_objects.admin_page import AdminPage
from page_objects.main_page import MainPage
from page_objects.new_product_form import NewProductForm
from page_objects.registration_page import RegistrationPage


@pytest.mark.parametrize("name,tag,model", [("Test New Product", "Test meta tag", "TEST6")])
def test_add_new_product_in_admin(browser, name, tag, model):
    admin_page = AdminPage(browser)
    admin_page.login("user", "bitnami")
    new_product_form = NewProductForm(browser)
    admin_page.open_new_product_form()
    new_product_form.add_product(name, tag, model)
    n_products = admin_page.count_products(name, model)
    assert n_products > 0, "No such product found!"


def test_delete_new_product_in_admin(browser):
    name = "TEST1"
    tag = "TESTTAG"
    model = "TESTMODEL"

    admin_page = AdminPage(browser)
    admin_page.login("user", "bitnami")
    new_product_form = NewProductForm(browser)
    admin_page.open_new_product_form()
    new_product_form.add_product(name, tag, model)
    admin_page.delete_product(name, model)


def test_registration_user_in_opencart(browser, random_user):
    main_page = MainPage(browser)
    main_page.open_register_page()
    registration_page = RegistrationPage(browser)
    print(f"Creating user {random_user.f_name} {random_user.l_name}")
    registration_page.fill_registration_form(random_user.f_name, random_user.l_name, random_user.email,
                                             random_user.phone, random_user.password)
    assert registration_page.is_new_user_created()


@pytest.mark.parametrize("currency,symbol", [("EUR", "€"), ("USD", "$"), ("GBP", "£")])
def test_currency_change(browser, currency, symbol):
    main_page = MainPage(browser)
    main_page.change_currency(currency)
    prices = main_page.get_product_prices()
    print(f"Checking prices for {currency}({symbol}), got:\n{'|'.join(prices)}")
    assert all(symbol in price for price in prices), f"Symbol {symbol} does not found in prices {prices}"
