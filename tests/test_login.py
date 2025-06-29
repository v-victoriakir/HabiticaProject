from model.data.users import user
from model.pages.login_page import LoginPage


def test_successful_login_using_email():
    practice_form = LoginPage()
    practice_form.login_page_open()
    practice_form.login_with_email(user)
    practice_form.login_checked(user)


def test_successful_login_using_username():
    practice_form = LoginPage()
    practice_form.login_page_open()
    practice_form.login_with_username(user)
    practice_form.login_checked(user)


def test_validation_on_wrong_credentials_using_email():
    practice_form = LoginPage()
    practice_form.login_page_open()
    practice_form.invalid_login_with_email(user)
    practice_form.validation_checked()


def test_validation_on_wrong_credentials_using_username():
    practice_form = LoginPage()
    practice_form.login_page_open()
    practice_form.invalid_login_with_username(user)
    practice_form.validation_checked()
