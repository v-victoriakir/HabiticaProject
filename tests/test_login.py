from model.pages.login_page import LoginPage
from model.pages.dashboard_page import ProfileMenu


def test_successful_login_using_email():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.login_with_email()
    login_form.login_checked()


def test_successful_login_using_username():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.login_with_username()
    login_form.login_checked()


def test_validation_on_wrong_credentials_using_email():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.invalid_login_with_email()
    login_form.validation_checked()


def test_validation_on_wrong_credentials_using_username():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.invalid_login_with_username()
    login_form.validation_checked()

def test_log_out():
    login_form = LoginPage()
    profile_menu = ProfileMenu()

    login_form.login_page_open()
    login_form.login_with_email()
    login_form.login_checked()
    profile_menu.open_profile_menu()
    profile_menu.click_menu_item('Log Out')
#     НЕ РАБОТАЕТ, НЕ МОГУ ВЫЗВАТЬ PROFILE MENU В DASHBOARD_PAGE.PY
