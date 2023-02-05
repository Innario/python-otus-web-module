import time

from page_objects.admin_page import AdminPage


def test_add_new_product_in_admin(browser):
    admin_page = AdminPage(browser)
    admin_page.login("user", "bitnami")
    time.sleep(2)
    # admin_page.add_new_product()
    # assert admin_page.is_new_product_found()
