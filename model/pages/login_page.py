import allure
from selene import browser, have, be

from model.data.users import User


class LoginPage:
    def __init__(self):
        self.login_button = browser.element('a[href="/login"]')
        self.username = browser.element("#usernameInput")
        self.password = browser.element("#passwordInput")
        self.login_button_to_submit = browser.element('//button[contains(text(), "Login")]')
        self.header = browser.element("#app-header")

    @allure.step("Открыть страницу логина")
    def login_page_open(self):
        browser.open("/")
        self.login_button.click()
        browser.element('//button[contains(text(), "Login")]').should(be.visible)
        return self

    @allure.step("Ввод username")
    def fill_username(self, value):
        self.username.send_keys(value)
        return self

    @allure.step("Ввод email")
    def fill_email(self, value):
        self.username.send_keys(value)
        return self

    @allure.step("Ввод пароля")
    def fill_password(self, value):
        self.password.send_keys(value)
        return self

    @allure.step("Отправка формы по кнопке")
    def submit_form(self):
        self.login_button_to_submit.click()
        return self

    @allure.step("Отправка формы через username")
    def login_with_username(self, user: User):
        self.fill_username(user.username)
        self.fill_password(user.password)
        self.submit_form()
        return self

    @allure.step("Отправка формы через email")
    def login_with_email(self, user: User):
        self.fill_username(user.email)
        self.fill_password(user.password)
        self.submit_form()
        return self

    @allure.step("Проверка успешного логина")
    def login_checked(self, user: User):
        self.header.should(be.visible)
        self.header.should(have.value(user.username))
