import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_config(request):
    options = Options()
    # форсим chrome на открытие в ENG локали
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': 'en,en_US'}
    )
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    browser.config.base_url = "https://habitica.com"
    browser.config.window_height = 2500
    browser.config.window_width = 1400
    browser.config.type_by_js = True

    # Подключаем менеджер драйвера Хрома
    # Здесь менеджер драйвера Хрома проверит версии и установит нужную.

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
