import os

import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options

from utils import web_attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_config(request):
    browser.config.base_url = "https://habitica.com"
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.type_by_js = True

    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "128.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    #
    # selenoid_login = os.getenv("SELENOID_LOGIN")
    # selenoid_pass = os.getenv("SELENOID_PASS")
    # selenoid_url = os.getenv("SELENOID_URL")
    #
    # options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(
    #     command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
    #     options=options)
    #
    # browser.config.driver = driver

    yield

    web_attach.add_html(browser)
    web_attach.add_screenshot(browser)
    web_attach.add_logs(browser)
    web_attach.add_video(browser)

    browser.quit()
