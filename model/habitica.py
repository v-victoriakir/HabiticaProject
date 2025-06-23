import allure
from selene import browser, have, be


class MainPage:
    def __init__(self):
        self.username = browser.element("#usernameInput")
        self.email = browser.element('input[placeholder="Электронная почта"]')
        self.password = browser.element('input[placeholder="Пароль"]')
        self.repeat_password = browser.element('input[placeholder="Подтвердите пароль"]')
        self.welcome_modal = browser.element("#avatar-modal___BV_modal_body_")
        # self.display_name = browser.element('input[placeholder="Новое отображаемое имя"]')


    @allure.step("Открыть главную страницу")
    def open(self):
        browser.open("/")
        return self

    @allure.step("Ввод логина")
    def fill_username(self, value):
        self.username.send_keys(value)
        return self

    @allure.step("Ввод эл. почты")
    def fill_email(self, value):
        self.email.send_keys(value)
        return self

    @allure.step("Ввод пароля")
    def fill_password(self, value):
        self.password.send_keys(value)
        return self

    @allure.step("Повторный ввод пароля")
    def fill_password_again(self, value):
        self.repeat_password.send_keys(value)
        return self

    @allure.step("Отправка формы")
    def submit_form(self):
        browser.element('//button[contains(text(), "Регистрация")]').click()
        return self

    @allure.step("Проверка регистрации")
    def registered_welcome_modal(self):
        browser.with_(timeout=15).element("#avatar-modal___BV_modal_body_").should(be.visible)
        self.welcome_modal.should(have.text("Добро пожаловать в"))
        # self.display_name.should(have.exact_text(username))
        return self

    @allure.step("Проверка наличия валидации на незаполненных обязательных полях")
    def check_if_required_fields_not_filled(self):
        browser.element("#userForm").should(have.attribute("class").value("was-validated"))
        return self