import allure
from allure_commons.types import Severity

from model.ui.web_pages.login_page import LoginPage
from model.ui.web_pages.dashboard_page import ProfileMenu

@allure.tag('Web')
@allure.feature("Authorisation")
@allure.title('Successful authorisation with email')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.BLOCKER)
def test_successful_login_using_email():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.login_with_email()
    login_form.login_checked()

@allure.tag('Web')
@allure.feature("Authorisation")
@allure.title('Successful authorisation with username')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.BLOCKER)
def test_successful_login_using_username():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.login_with_username()
    login_form.login_checked()

@allure.tag('Web')
@allure.feature("Authorisation")
@allure.title('Validation on invalid password when authorising with email')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_wrong_credentials_using_email():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.invalid_login_with_email()
    login_form.validation_checked()

@allure.tag('Web')
@allure.feature("Authorisation")
@allure.title('Validation on invalid password when authorising with username')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_wrong_credentials_using_username():
    login_form = LoginPage()
    login_form.login_page_open()
    login_form.invalid_login_with_username()
    login_form.validation_checked()

@allure.tag('Web')
@allure.feature("Authorisation")
@allure.title('Successful log out')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_log_out():
    login_form = LoginPage()
    profile_menu = ProfileMenu()

    login_form.login_page_open()
    login_form.login_with_email()
    login_form.login_checked()
    profile_menu.open_profile_menu()
    profile_menu.click_menu_item('Log Out')
#     НЕ РАБОТАЕТ, НЕ МОГУ ВЫЗВАТЬ PROFILE MENU В DASHBOARD_PAGE.PY
