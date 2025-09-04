import os

import allure
from faker import Faker

from model.ui.web_pages.login_page import LoginPage

fake = Faker()


class LoginSteps:
    def __init__(self):
        self.login_page = LoginPage()

    @allure.step("Login with username")
    def login_with_username(self):
        habitica_username = os.getenv("HABITICA_USERNAME")
        habitica_password = os.getenv("HABITICA_PASSWORD")

        self.login_page.open()
        self.login_page.login(habitica_username, habitica_password)
        return self

    @allure.step("Login with email")
    def login_with_email(self):
        habitica_email = os.getenv("HABITICA_EMAIL")
        habitica_password = os.getenv("HABITICA_PASSWORD")

        self.login_page.open()
        self.login_page.login(habitica_email, habitica_password)
        return self

    @allure.step("Login with username and invalid password")
    def invalid_login_with_username(self):
        habitica_username = os.getenv("HABITICA_USERNAME")
        random_password = fake.password(length=9)

        self.login_page.open()
        self.login_page.login(habitica_username, random_password)
        return self

    @allure.step("Login with email and invalid password")
    def invalid_login_with_email(self):
        habitica_email = os.getenv("HABITICA_EMAIL")
        random_password = fake.password(length=9)

        self.login_page.open()
        self.login_page.login(habitica_email, random_password)
        return self

    @allure.step("Verify successful login")
    def verify_login_successful(self):
        habitica_username = os.getenv("HABITICA_USERNAME")
        self.login_page.should_be_logged_in(habitica_username)
        return self

    @allure.step("Verify validation error")
    def verify_validation_error(self):
        self.login_page.should_have_validation_error()
        return self
