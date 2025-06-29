from model.data.users import user
from model.pages.login_page import LoginPage


def test_login_email_successful():
    practice_form = LoginPage()
    practice_form.login_page_open()
    practice_form.login_with_email(user)
    practice_form.login_checked(user)


def test_login_username_successful():
    practice_form = LoginPage()
    practice_form.login_page_open()
    practice_form.login_with_username(user)
    practice_form.login_checked(user)
