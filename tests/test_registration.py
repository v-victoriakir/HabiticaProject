import re

from faker import Faker

from model.pages.main_page import MainPage

fake = Faker()


def generate_valid_username():
    pattern = re.compile(r'^[a-z0-9_-]+$')
    while True:
        username_part1 = fake.user_name()
        username_part2 = fake.user_name()
        return (username_part1 + username_part2)[0:20]  # ограничиваем длину username до 20 символов


def generate_invalid_long_username():
    pattern = re.compile(r'^[a-z0-9_-]+$')
    while True:
        username_part1 = fake.user_name()
        username_part2 = fake.user_name()
        combined_username = (username_part1 + username_part2)
        if len(combined_username) >= 21 and pattern.fullmatch(combined_username):
            return combined_username


# def test_form_submitted():
    # username = generate_valid_username()
    # email = fake.email()
    # password = fake.password(length=9)
    #
    # practice_form = MainPage()
    # practice_form.open()
    #
    # practice_form.fill_username(username)
    # practice_form.fill_email(email)
    # practice_form.fill_password(password)
    # practice_form.fill_password_again(password)
    # practice_form.submit_form()
    # practice_form.registered_welcome_modal()

#   тест рабочий, но временно отключила, чтобы не регистрировать кучу юзеров в сервисе

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


def test_validation_on_invalid_username():
    username = generate_invalid_long_username()
    email = fake.email()
    password = fake.password(length=9)

    practice_form = MainPage()
    practice_form.open()

    practice_form.fill_username(username)
    practice_form.fill_email(email)
    practice_form.fill_password(password)
    practice_form.fill_password_again(password)
    practice_form.submit_form()
    practice_form.check_if_username_is_long()


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
    practice_form.check_if_password_is_short()


def test_login_button_works():
    practice_form = MainPage()
    practice_form.open()

    practice_form.check_if_login_button_works()
