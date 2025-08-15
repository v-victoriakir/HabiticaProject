import re
import allure
from allure_commons.types import Severity

from faker import Faker

from model.ui.web_pages.main_page import MainPage

fake = Faker()

def generate_valid_username():
    pattern = re.compile(r'^[a-z0-9_-]+$')
    while True:
        username_part1 = fake.user_name()
        username_part2 = fake.user_name()
        combined_username = (username_part1 + username_part2)
        if len(combined_username) <= 20 and pattern.fullmatch(
                combined_username):
            return combined_username


def generate_invalid_long_username():
    pattern = re.compile(r'^[a-z0-9_-]+$')
    while True:
        username_part1 = fake.user_name()
        username_part2 = fake.user_name()
        combined_username = (username_part1 + username_part2)
        if len(combined_username) >= 21 and pattern.fullmatch(
                combined_username):  # ставим длину username >= 20 символов
            return combined_username

@allure.tag('web')
@allure.feature("Registration")
@allure.title('Successful sign up')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.BLOCKER)
def test_form_submitted():
    username = generate_valid_username()
    email = fake.email()
    password = fake.password(length=9)

    signup_form = MainPage()
    signup_form.open()

    signup_form.fill_username(username)
    signup_form.fill_email(email)
    signup_form.fill_password(password)
    signup_form.fill_password_again([password])
    signup_form.submit_form()
    signup_form.registered_welcome_modal()

@allure.tag('web')
@allure.feature("Registration")
@allure.title('Validation on required fields not filled')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_required_fields():
    username = generate_valid_username()
    email = fake.email()
    password = fake.password(length=9)

    signup_form = MainPage()
    signup_form.open()

    signup_form.fill_username(username)
    signup_form.fill_email(email)
    signup_form.fill_password(password)
    signup_form.submit_form()
    signup_form.check_if_required_fields_not_filled()

@allure.tag('web')
@allure.feature("Registration")
@allure.title('Validation on invalid username')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_invalid_long_username():
    username = generate_invalid_long_username()
    email = fake.email()
    password = fake.password(length=9)

    signup_form = MainPage()
    signup_form.open()

    signup_form.fill_username(username)
    signup_form.fill_email(email)
    signup_form.fill_password(password)
    signup_form.fill_password_again([password])
    signup_form.check_if_username_is_long()

@allure.tag('web')
@allure.feature("Registration")
@allure.title('Validation on invalid password')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_validation_on_invalid_short_password():
    username = generate_valid_username()
    email = fake.email()
    password = fake.password(length=7)

    signup_form = MainPage()
    signup_form.open()

    signup_form.fill_username(username)
    signup_form.fill_email(email)
    signup_form.fill_password(password)
    signup_form.fill_password_again([password])
    signup_form.check_if_password_is_short()

@allure.tag('web')
@allure.feature("Registration")
@allure.title('Availability of the Log In form')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_login_button_works():
    signup_form = MainPage()
    signup_form.open()

    signup_form.check_if_login_button_works()
