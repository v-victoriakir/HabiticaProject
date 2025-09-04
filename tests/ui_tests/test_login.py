import allure
from allure_commons.types import Severity

from model.ui.steps.login_steps import LoginSteps


@allure.tag('Web')
@allure.feature("WEB_auth")
@allure.title('Successful authorisation with username')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.BLOCKER)
def test_successful_login_with_email():
    login_steps = LoginSteps()

    with allure.step("Login with valid username and password"):
        login_steps.login_with_username()

    with allure.step("Verify login is successful"):
        login_steps.verify_login_successful()


@allure.tag('Web')
@allure.feature("WEB_auth")
@allure.title('Successful authorisation with email')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.BLOCKER)
def test_successful_login_using_username():
    login_steps = LoginSteps()

    with allure.step("Login with valid email and password"):
        login_steps.login_with_email()

    with allure.step("Verify login is successful"):
        login_steps.verify_login_successful()


@allure.tag('Web')
@allure.feature("WEB_auth")
@allure.title('Validation on invalid password when authorising with email')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_wrong_credentials_using_email():
    login_steps = LoginSteps()

    with allure.step("Open login page and attempt login with invalid password using email"):
        login_steps.invalid_login_with_email()

    with allure.step("Verify validation error appears"):
        login_steps.verify_validation_error()


@allure.tag('Web')
@allure.feature("WEB_auth")
@allure.title('Validation on invalid password when authorising with username')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_wrong_credentials_using_username():
    login_steps = LoginSteps()

    with allure.step("Open login page and attempt login with invalid password using username"):
        login_steps.invalid_login_with_username()

    with allure.step("Verify validation error appears"):
        login_steps.verify_validation_error()
