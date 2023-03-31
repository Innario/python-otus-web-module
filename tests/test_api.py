import allure
import pytest

from api_objects import API


@allure.tag("SMOKE")
@allure.feature("Currency")
@allure.story("Valid data")
@allure.title("Currency change")
@pytest.mark.parametrize("currency", ["EUR", "USD", "GBP"])
def test_change_currency(url, api_token, currency):
    api = API(url=url, api_token=api_token)
    code, data = api.set_currency(currency=currency)
    assert code == 200
    assert data['success'] == 'Success: Your currency has been changed!'


@allure.tag("SMOKE")
@allure.feature("Set customer")
@allure.story("Valid data")
@allure.title("Registering a user for the current session")
def test_set_customer_for_current_session(url, api_token):
    api = API(url=url, api_token=api_token)
    code, data = api.create_customer(firstname="Dear",
                                     lastname="Customer",
                                     email="customer@example.com",
                                     phone="+1 879 2548022")

    assert code == 200
    assert data['success'] == 'You have successfully modified customers'


@allure.tag("SMOKE")
@allure.feature("Cart")
@allure.story("Valid data")
@allure.title("Adding a Product to the Cart")
@pytest.mark.parametrize("product_id,quantity", [(43, 2), (34, 100)])
def test_adding_product_to_cart(url, api_token, product_id, quantity):
    api = API(url=url, api_token=api_token)

    # adding product to cart
    code, data = api.add_to_cart(product_id=product_id, quantity=quantity)
    assert code == 200
    assert data['success'] == 'Success: You have modified your shopping cart!'

    # checking the products in the shopping cart
    code, data = api.get_cart_info()
    assert code == 200
    assert int(data["products"][0]["product_id"]) == product_id
    assert int(data["products"][0]["quantity"]) == quantity


@allure.tag("SMOKE")
@allure.feature("Cart")
@allure.story("Valid data")
@allure.title("Changing the quantity of a product in the cart")
@pytest.mark.parametrize("product_id", [31, 28])
def test_edit_product_quantity_in_cart(url, api_token, product_id):
    api = API(url=url, api_token=api_token)

    # checking the products in the shopping cart
    code, data = api.add_to_cart(product_id=product_id, quantity=2)
    assert code == 200
    assert data['success'] == 'Success: You have modified your shopping cart!'

    # checking the products in the shopping cart
    code, data = api.get_cart_info()
    assert code == 200
    assert int(data['products'][0]['product_id']) == product_id
    assert int(data['products'][0]['quantity']) == 2
    product_cart_id = data['products'][0]['cart_id']

    # change the quantity of goods in the cart
    code, data = api.edit_cart_product(product_cart_id=product_cart_id, quantity=5)
    assert code == 200
    assert data['success'] == 'Success: You have modified your shopping cart!'

    code, data = api.get_cart_info()
    assert code == 200
    assert int(data['products'][0]['product_id']) == product_id
    assert int(data['products'][0]['quantity']) == 5


@allure.tag("SMOKE")
@allure.feature("Cart")
@allure.story("Valid data")
@allure.title("Removing a product from the cart")
@pytest.mark.parametrize("product_id,quantity", [(43, 2), (34, 100)])
def test_remove_from_cart(url, api_token, product_id, quantity):
    api = API(url=url, api_token=api_token)

    # adding product to cart
    code, data = api.add_to_cart(product_id=product_id, quantity=quantity)
    assert code == 200
    assert data['success'] == 'Success: You have modified your shopping cart!'

    # get cart_id
    code, data = api.get_cart_info()
    assert code == 200
    assert int(data["products"][0]["product_id"]) == product_id
    assert int(data["products"][0]["quantity"]) == quantity
    product_cart_id = data['products'][0]['cart_id']

    # removing a product from the cart
    code, data = api.remove_from_cart(product_cart_id=product_cart_id)
    assert code == 200
    assert data['success'] == 'Success: You have modified your shopping cart!'

    # checking the products in the shopping cart
    code, data = api.get_cart_info()
    assert code == 200
    assert data['products'] == []


@allure.tag("SMOKE")
@allure.feature("Shipping")
@allure.story("Valid data")
@allure.title("Getting all shipping methods")
def test_returning_available_shipping_methods(url, api_token):
    api = API(url=url, api_token=api_token)
    code, data = api.get_shipping_methods()
    assert code == 200
    assert "shipping_methods" in data


@allure.tag("SMOKE")
@allure.feature("Shipping")
@allure.story("Valid data")
@allure.title("Setting a shipping address")
def test_set_shipping_address(url, api_token):
    api = API(url=url, api_token=api_token)

    code, data = api.get_shipping_address(
        firstname='Customer',
        lastname='Dear',
        address='Somewhere',
        city='KLD',
        country_id='RUS',
        zone_id='KGD'
    )
    assert code == 200
    assert not data
