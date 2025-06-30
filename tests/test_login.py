from model.data.users import user
from model.pages.login_page import LoginPage


def test_successful_login_using_email():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.login_with_email(user)
    login_form.login_checked(user)


def test_successful_login_using_username():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.login_with_username(user)
    login_form.login_checked(user)


def test_validation_on_wrong_credentials_using_email():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.invalid_login_with_email(user)
    login_form.validation_checked()


def test_validation_on_wrong_credentials_using_username():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.invalid_login_with_username(user)
    login_form.validation_checked()
