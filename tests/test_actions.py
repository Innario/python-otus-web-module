import allure
import pytest

from page_objects.account_page import AccountPage
from page_objects.admin_page import AdminPage
from page_objects.cart_page import CartPage
from page_objects.catalog_page import CatalogPage
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.new_product_form import NewProductForm
from page_objects.product_page import ProductPage
from page_objects.registration_page import RegistrationPage
from page_objects.search_result_page import SearchResultPage


@allure.tag("SMOKE")
@allure.feature("Actions with products")
@allure.story("Add new product")
@allure.title("Adding a new product in the admin panel")
@pytest.mark.parametrize("name,tag,model", [("Test New Product", "Test meta tag", "TEST6")])
def test_add_new_product_in_admin(browser, name, tag, model):
    admin_page = AdminPage(browser)
    admin_page.login("user", "bitnami")
    new_product_form = NewProductForm(browser)
    admin_page.open_new_product_form()
    new_product_form.add_product(name, tag, model)
    n_products = admin_page.count_products(name, model)
    assert n_products > 0, "No such product found!"


@allure.tag("SMOKE")
@allure.feature("Actions with products")
@allure.story("Delete new product")
@allure.title("Deleting a new product in the admin panel")
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


@allure.tag("SMOKE")
@allure.feature("Registration")
@allure.story("Registration in OpenCart")
@allure.title("New user registration")
def test_registration_user_in_opencart(browser, random_user):
    main_page = MainPage(browser)
    main_page.open_register_page()
    registration_page = RegistrationPage(browser)
    print(f"Creating user {random_user.f_name} {random_user.l_name}")
    registration_page.fill_registration_form(random_user.f_name, random_user.l_name, random_user.email,
                                             random_user.phone, random_user.password)
    assert registration_page.is_new_user_created()


@allure.tag("SMOKE")
@allure.feature("Main page features")
@allure.story("Currency change")
@allure.title("Currency change")
@pytest.mark.parametrize("currency,symbol", [("EUR", "€"), ("USD", "$"), ("GBP", "£")])
def test_currency_change(browser, currency, symbol):
    main_page = MainPage(browser)
    main_page.change_currency(currency)
    prices = main_page.get_product_prices()
    print(f"Checking prices for {currency}({symbol}), got:\n{'|'.join(prices)}")
    assert all(symbol in price for price in prices), f"Symbol {symbol} does not found in prices {prices}"


@allure.tag("SMOKE")
@allure.feature("Searching products")
@allure.story("")
@allure.title("")
@pytest.mark.parametrize("product_name", ["macbook", "canon"])
def test_search_existing_product(browser, product_name):
    main_page = MainPage(browser)
    main_page.input_product_name(product_name)

    search_result = SearchResultPage(browser)
    result_list = search_result.searching_result()
    assert len(result_list) > 0
    for element in result_list:
        print(element.text)
        assert product_name in element.text.lower()


@allure.tag("SMOKE")
@allure.feature("Searching products")
@allure.story("")
@allure.title("")
def test_search_non_existing_product(browser):
    main_page = MainPage(browser)
    main_page.input_product_name("nokia")

    search_result = SearchResultPage(browser)
    result_list = search_result.search_stub_check()
    assert len(result_list) == 0


@allure.tag("SMOKE")
@allure.feature("Searching products")
@allure.story("")
@allure.title("")
def test_add_product_to_cart_without_authorisation(browser):
    """
    1 - клик на название продукта на главной
    2 - на экране продукта выбрать опции покупки
    3 - тап "добавить в корзину"
    4 - проверка появления алерта успеха добавления
    5 - переходим с алерта в корзину и проверяем наличие продукта в ней
    """
    main_page = MainPage(browser)
    main_page.click_product("Canon EOS 5D")
    product_page = ProductPage(browser)
    cart_page = CartPage(browser)
    cart_page.add_to_cart_with_product_options()
    cart_page.cart_checkout("Canon EOS 5D")


@allure.tag("SMOKE")
@allure.feature("Searching products")
@allure.story("")
@allure.title("")
def test_removing_product_from_cart(browser):
    """
    1 - без авторизации перейти в раздел меню Tablets
    2 - перейти на деталь продукта
    3 - добавить в корзину
    4 - проверить аллерт
    5 - перейти в корзину по иконке хедера
    6 - проверить наличие продукта в списке корзины
    7 - удалить продукт по кнопке Х
    8 - проверить отсутствие элемента продукта
    9 - проверить видимость заглушки пустой корзины
    """
    main_page = MainPage(browser)
    cart_page = CartPage(browser)

    main_page.click_menu_tab("Tablets")
    cart_page.add_to_cart("Samsung Galaxy Tab 10.1")
    cart_page.cart_checkout("Samsung Galaxy Tab 10.1")
    cart_page.remove_product_from_cart()
    assert cart_page.cart_is_empty()


@allure.tag("SMOKE")
@allure.feature("Searching products")
@allure.story("")
@allure.title("")
def test_opencart_login_and_logout(browser):
    """
    1 - клик на иконку логина
    2 - ввод учетки нажатие на логин иконку
    3 - проверка что отобразился заголовок Мой аккаунт, Мои заказы, My Affiliate Account, Newsletter
    4 - клик на иконку логина
    5 - тап logout
    6 - проверка отображения заголовка Account Logout
    7 - тап Continue
    8 - проверка на видимость слайдера #slideshow0
    """
    main_page = MainPage(browser)
    main_page.open_login_page()

    login_page = LoginPage(browser)
    login_page.fill_authorization_form("qwerty@qwer.ty", "qwerty")

    account_page = AccountPage(browser)
    account_page.is_user_logged_in()
    account_page.logout()
    account_page.is_user_logged_out()


@allure.tag("SMOKE")
@allure.feature("Searching products")
@allure.story("")
@allure.title("")
def test_adding_product_to_wishlist(browser):
    """
    1 - открыть страницу Phones & PDAs
    2 - тап сердце на превью товара
    3 - проверка что отобразился алерт из которого можно перейти в вишлист
    4 - открыть страницу MP3 Players
    5 - перейти на деталку продукта и тапнуть сердце
    6 - проверка что отобразился алерт из которого можно перейти в вишлист
    7 - проверка что в вишлисте 2 добавленных товара
    """
    main_page = MainPage(browser)
    catalog_page = CatalogPage(browser)
    product_page = ProductPage(browser)
    login_page = LoginPage(browser)

    main_page.click_menu_tab("Phones & PDAs")
    catalog_page.adding_product_to_wishlist_from_preview()
    login_page.fill_authorization_form("qwerty@qwer.ty", "qwerty")
    product_page.product_check_in_the_wishlist("HTC Touch HD")
    main_page.click_show_all_from_menu("MP3 Players", "Show All MP3 Players")
    catalog_page.adding_product_to_wishlist_from_detailview("iPod Classic")
    product_page.product_check_in_the_wishlist("iPod Classic")
