import os

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
        self.login_submit_button = browser.element('//button[contains(text(), "Login")]')
        self.header = browser.element("#app-header")

    @allure.step("Open login page")
    def login_page_open(self):
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
        self.login_submit_button.click()
        return self

    @allure.step("Submit form using username")
    def login_with_username(self):
        habitica_username = os.getenv("HABITICA_USERNAME")
        habitica_password = os.getenv("HABITICA_PASSWORD")

        self.fill_username(habitica_username)
        self.fill_password(habitica_password)
        self.submit_form()
        return self

    @allure.step("Submit form using email")
    def login_with_email(self):
        habitica_email = os.getenv("HABITICA_EMAIL")
        habitica_password = os.getenv("HABITICA_PASSWORD")

        self.fill_username(habitica_email)
        self.fill_password(habitica_password)
        self.submit_form()
        return self

    @allure.step("Submit form using username with invalid password")
    def invalid_login_with_username(self):
        habitica_username = os.getenv("HABITICA_USERNAME")
        random_password = fake.password(length=9)

        self.fill_username(habitica_username)
        self.fill_password(random_password)
        self.submit_form()
        return self

    @allure.step("Submit form using email with invalid password")
    def invalid_login_with_email(self):
        habitica_email = os.getenv("HABITICA_EMAIL")
        random_password = fake.password(length=9)

        self.fill_username(habitica_email)
        self.fill_password(random_password)
        self.submit_form()
        return self

    @allure.step("Check if login is successful")
    def login_checked(self):
        habitica_username = os.getenv("HABITICA_USERNAME")

        self.header.should(be.visible)
        self.header.should(have.text(habitica_username))

    @allure.step("Check if validation on username/password works")
    def validation_checked(self):
        browser.element('.notifications').should(be.visible)
        browser.element('.notifications').should(have.text("your email address / username or password is incorrect."))
