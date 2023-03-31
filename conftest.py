import json
import os
import random

import allure
import pytest
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.31.50")
    parser.addoption("--driver_path", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.31.50:8081", action="store", help="This is opencart App")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bv")
    executor = request.config.getoption("--executor")
    driver_path = request.config.getoption("--driver_path")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    vnc = request.config.getoption("--vnc")
    # driver = None

    if executor == "local":
        if browser == "firefox" or browser == "ff":
            options = FirefoxOptions()
            options.headless = headless
            driver = webdriver.Firefox(executable_path=f"{driver_path}{os.sep}/geckodriver", options=options)
        elif browser == "chrome":
            options = ChromeOptions()
            options.headless = headless
            driver = webdriver.Chrome(executable_path=f"{driver_path}{os.sep}/chromedriver", options=options)
        elif browser == "yandex":
            options = ChromeOptions()
            options.headless = headless
            driver = webdriver.Chrome(executable_path=f"{driver_path}{os.sep}/yandexdriver", options=options)
        elif browser == "safari":
            options = SafariOptions()
            options.headless = headless
            driver = webdriver.Safari(options=options)
        else:
            raise Exception("Driver not supported")
    else:
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "name": "Inna",
                "enableVNC": vnc,
                # "enableVideo": video,
                # "enableLog": logs
            },
        }

        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities=capabilities
        )

        allure.attach(
            name=driver.session_id,
            body=json.dumps(driver.capabilities),
            attachment_type=allure.attachment_type.JSON)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def api_token(request):
    assert load_dotenv()
    response = requests.Session().post(
        f'{request.config.getoption("--url")}/index.php?route=api/login',
        data={
            'username': os.environ.get("api_user"),
            'key': os.environ.get("api_key"),
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data
    return response.json()['api_token']


@pytest.fixture
def random_user():
    class UserData:
        f_name = f"testName{random.randint(0, 9999)}"
        l_name = "testlastName"
        email = f"test_{random.randint(0, 9999)}@mail.com"
        phone = "78090389499"
        password = "pass1"

    return UserData()
