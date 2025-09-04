from faker import Faker

fake = Faker()
from dotenv import load_dotenv
import allure
from selene import browser, have, be

load_dotenv()


class LoginPage:
    def __init__(self):
        self.login_nav_button = browser.element('a[href="/login"]')
        self.username = browser.element("#usernameInput")
        self.password = browser.element("#passwordInput")
        self.login_submit_button = browser.element('button[type=submit]')
        self.header = browser.element("#app-header")

    @allure.step("Open login page")
    def open(self):
        browser.open("/")
        self.login_nav_button.click()
        self.login_submit_button.should(be.visible)
        return self

    @allure.step("Fill in username")
    def fill_username(self, value):
        self.username.send_keys(value)
        return self

    @allure.step("Fill in email")
    def fill_email(self, value):
        self.username.send_keys(value)
        return self

    @allure.step("Enter password")
    def fill_password(self, value):
        self.password.send_keys(value)
        return self

    @allure.step("Click on the submit btn")
    def submit_form(self):
        self.login_submit_button.should(be.clickable).click()
        return self

    @allure.step("Login with credentials")
    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.submit_form()
        return self

    @allure.step("Check if login is successful")
    def should_be_logged_in(self, expected_username):
        self.header.with_(timeout=10).should(be.visible)
        self.header.should(have.text(expected_username))
        return self

    @allure.step("Check if validation on username/password works")
    def should_have_validation_error(self):
        browser.element('.notifications').should(be.visible)
