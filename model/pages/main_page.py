import allure
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.username = browser.element("#usernameInput")
        self.email = browser.element('input[placeholder="Email"]')
        self.password = browser.element('input[placeholder="Password"]')
        self.repeat_password = browser.element('input[placeholder="Confirm Password"]')
        self.signup_button = browser.element('//button[contains(text(), "Sign Up")]')
        self.welcome_modal = browser.element("#avatar-modal___BV_modal_body_")
        self.login_nav_button = browser.element('a[href="/login"]')
        # self.display_name = browser.element('input[placeholder="Новое отображаемое имя"]')

    @allure.step("Open main page")
    def open(self):
        browser.open("/")
        return self

    @allure.step("Fill in username")
    def fill_username(self, username):
        self.username.send_keys(username)
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

    @allure.step("Click on the submit btn")
    def submit_form(self):
        self.signup_button.click()
        return self

    @allure.step("Check that sign up is successful")
    def registered_welcome_modal(self):
        browser.with_(timeout=15).element("#avatar-modal___BV_modal_body_").should(be.visible)
        self.welcome_modal.should(have.text("Welcome to"))
        # self.display_name.should(have.exact_text(username))  ---> не пойму как сделать проверку на то, чтобы после
        # регистрации в welcome окне отображаемое username соответствовало тому, которое было введено на этапе
        # регистрации
        return self

    @allure.step("Check if validation on required fields works")
    def check_if_required_fields_not_filled(self):
        browser.element('.notifications').should(be.visible)
        browser.element('.notifications').should(have.text("Password confirmation doesn't match password."))
        return self

    @allure.step("Check if validation on username length works")
    def check_if_username_is_long(self):
        browser.element('.input-error').should(be.visible)
        browser.element('.input-error').should(have.text("Usernames must be between 1 and 20 characters."))
        return self

    @allure.step("Check if validation on password length works")
    def check_if_password_is_short(self):
        browser.element('.input-error').should(be.visible)
        browser.element('.input-error').should(have.text("Password must be 8 characters or more."))
        return self

    @allure.step("Check if the Login bnt opens the sign in form")
    def check_if_login_button_works(self):
        self.login_nav_button.click()
        browser.element('//button[contains(text(), "Login")]').should(be.visible)
        return self
