from model.habitica import MainPage


def test_form_submitted():
    practice_form = MainPage()
    practice_form.open()

    practice_form.fill_username("MariaLopez1234567")
    practice_form.fill_email("MLopez7@gmail.com")
    practice_form.fill_password("123456789")
    practice_form.fill_password_again("123456789")
    practice_form.submit_form()
    practice_form.registered_welcome_modal()
