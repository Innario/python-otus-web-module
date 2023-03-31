import requests


class API:

    def __init__(self, url, api_token):
        self.url = url
        self.api_token = api_token
        self.session = requests.Session()

    def set_currency(self, currency):
        response = self.session.post(
            f'{self.url}/index.php?route=api/currency',
            params={'api_token': self.api_token},
            data={'currency': currency}
        )
        return response.status_code, response.json()

    def create_customer(self, firstname, lastname, email, phone):
        response = self.session.post(
            f'{self.url}/index.php?route=api/customer',
            params={'api_token': self.api_token},
            data={
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'telephone': phone
            }
        )
        return response.status_code, response.json()

    def add_to_cart(self, product_id, quantity):
        response = self.session.post(
            f'{self.url}/index.php?route=api/cart/add',
            params={'api_token': self.api_token},
            data={
                'product_id': product_id,
                'quantity': quantity
            }
        )
        return response.status_code, response.json()

    def get_cart_info(self):
        response = self.session.post(
            f'{self.url}/index.php?route=api/cart/products',
            params={'api_token': self.api_token},
            data={}
        )
        return response.status_code, response.json()

    def remove_from_cart(self, product_cart_id):
        response = self.session.post(
            f'{self.url}/index.php?route=api/cart/remove',
            params={'api_token': self.api_token},
            data={
                'key': product_cart_id
            }
        )
        return response.status_code, response.json()

    def edit_cart_product(self, product_cart_id, quantity):
        response = self.session.post(
            f'{self.url}/index.php?route=api/cart/edit',
            params={'api_token': self.api_token},
            data={
                'key': product_cart_id,
                'quantity': quantity
            }
        )
        return response.status_code, response.json()

    def get_shipping_methods(self):
        response = self.session.post(
            f'{self.url}/index.php?route=api/shipping/methods',
            params={'api_token': self.api_token},
            data={}
        )
        return response.status_code, response.json()

    def get_shipping_address(self, firstname, lastname, address, city, country_id, zone_id):
        response = self.session.post(
            f'{self.url}/index.php?route=api/shipping/address',
            params={'api_token': self.api_token},
            data={
                'firstname': firstname,
                'lastname': lastname,
                'address_1': address,
                'city': city,
                'country_id': country_id,
                'zone_id': zone_id
            }
        )
        return response.status_code, response.json()
