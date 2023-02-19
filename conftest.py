import os
import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome"
    )
    parser.addoption(
        "--driver_path", default=os.path.expanduser("~/Downloads/drivers")
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--url",
        default="http://192.168.31.50:8081",
        action="store",
        help="This is opencart App"
    )


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_path = request.config.getoption("--driver_path")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    # driver = None

    if _browser == "firefox" or _browser == "ff":
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(executable_path=f"{driver_path}{os.sep}/geckodriver", options=options)
    elif _browser == "chrome":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(executable_path=f"{driver_path}{os.sep}/chromedriver", options=options)
    elif _browser == "yandex":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(executable_path=f"{driver_path}{os.sep}/yandexdriver", options=options)
    elif _browser == "safari":
        options = SafariOptions()
        options.headless = headless
        driver = webdriver.Safari(options=options)
    else:
        raise Exception("Driver not supported")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture
def random_user():
    class UserData:
        f_name = f"testName{random.randint(0, 9999)}"
        l_name = "testlastName"
        email = f"test_{random.randint(0, 9999)}@mail.com"
        phone = "78090389499"
        password = "pass1"

    return UserData()
