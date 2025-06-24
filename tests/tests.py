import re

from faker import Faker
from model.habitica import MainPage

fake = Faker()

def generate_valid_username():
    pattern = re.compile(r'^[a-z0-9_-]+$')
    while True:
        username = fake.user_name()
        if pattern.match(username):
            return username
# здесь возник вопрос - возможно ли исключать генерацию username, которые уже заняты в системе?

def test_form_submitted():
    username = generate_valid_username()
    email = fake.email()
    password = fake.password(length=9)

    practice_form = MainPage()
    practice_form.open()

    practice_form.fill_username(username)
    practice_form.fill_email(email)
    practice_form.fill_password(password)
    practice_form.fill_password_again(password)
    practice_form.submit_form()
    practice_form.registered_welcome_modal()

def test_validation_on_required_fields():
    username = generate_valid_username()
    email = fake.email()
    password = fake.password(length=9)

    practice_form = MainPage()
    practice_form.open()

    practice_form.fill_username(username)
    practice_form.fill_email(email)
    practice_form.fill_password(password)
    practice_form.submit_form()
    practice_form.check_if_required_fields_not_filled()

def test_validation_on_password_length():
    username = generate_valid_username()
    email = fake.email()
    password = fake.password(length=7)

    practice_form = MainPage()
    practice_form.open()

    practice_form.fill_username(username)
    practice_form.fill_email(email)
    practice_form.fill_password(password)
    practice_form.fill_password_again(password)
    practice_form.submit_form()
    practice_form.check_if_required_fields_not_filled()