import allure
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.email = browser.element('input[type="email"]')
        self.password = browser.element('(//input[@type="password"])[1]')
        self.repeat_password = browser.element('(//input[@type="password"])[2]')
        self.signup_button = browser.element('button[type=submit]')
        self.welcome_modal = browser.element("#avatar-modal___BV_modal_body_")
        self.login_nav_button = browser.element('a[href="/login"]')

    @allure.step("Open main page")
    def open(self):
        browser.open("/")
        return self

    @allure.step("Fill in email")
    def fill_email(self, email):
        self.email.send_keys(email)
        return self

    @allure.step("Enter password")
    def fill_password(self, password):
        self.password.send_keys(password)
        return self

    @allure.step("Repeat password")
    def fill_password_again(self, password):
        self.repeat_password.send_keys(password)
        return self

    @allure.step("Check that submit button is disabled")
    def check_submit_button_disabled(self):
        self.signup_button.should(have.attribute('disabled'))
        return self

    @allure.step("Click on the submit btn")
    def submit_form(self):
        self.signup_button.should(have.no.attribute('disabled')).should(be.clickable).click()
        return self

    @allure.step("Click on Private Policy checkbox")
    def policy_checkbox_click(self):
        browser.element('label[for="privacyTOS"]').click()

    @allure.step("Click on Get Started")
    def get_started(self):
        self.signup_button.with_(timeout=10).should(be.clickable).click()
        return self

    @allure.step("Check that sign up is successful")
    def registered_welcome_modal(self):
        browser.with_(timeout=10).element("#avatar-modal___BV_modal_body_").should(be.visible)
        return self

    @allure.step("Check validation on email/password input")
    def check_validation(self):
        browser.element('.input-error').should(be.visible)
        return self

    @allure.step("Check if the Login bnt opens the sign in form")
    def check_if_login_button_works(self):
        self.login_nav_button.click()
        browser.element('button[type=submit]').should(be.visible)
        return self
