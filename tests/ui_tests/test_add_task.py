import allure
from allure_commons.types import Severity

from faker import Faker

from model.ui.web_pages.dashboard_page import AddTaskButton
from model.ui.web_pages.login_page import LoginPage

fake = Faker()

@allure.tag('web')
@allure.feature("Add Task")
@allure.title('Create a task of Habit type')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_add_habit():
    random_title = fake.sentence(nb_words=3).rstrip('.')

    tasks = AddTaskButton()
    login = LoginPage()

    login.login_page_open()
    login.login_with_email()
    login.login_checked()
    tasks.click_add_task_btn()
    tasks.pick_task('Habit')
    tasks.name_a_task(random_title)
    tasks.click_create_btn()
    tasks.check_task_in_list(random_title)

@allure.tag('web')
@allure.feature("Add Task")
@allure.title('Create a task of Daily type')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_add_daily():
    random_title = fake.sentence(nb_words=3).rstrip('.')

    tasks = AddTaskButton()
    login = LoginPage()

    login.login_page_open()
    login.login_with_email()
    login.login_checked()
    tasks.click_add_task_btn()
    tasks.pick_task('Daily')
    tasks.name_a_task(random_title)
    tasks.click_create_btn()
    tasks.check_task_in_list(random_title)

@allure.tag('web')
@allure.feature("Add Task")
@allure.title('Create a task of To Do type')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_add_to_do():
    random_title = fake.sentence(nb_words=3).rstrip('.')

    tasks = AddTaskButton()
    login = LoginPage()

    login.login_page_open()
    login.login_with_email()
    login.login_checked()
    tasks.click_add_task_btn()
    tasks.pick_task('To Do')
    tasks.name_a_task(random_title)
    tasks.click_create_btn()
    tasks.check_task_in_list(random_title)

@allure.tag('web')
@allure.feature("Add Task")
@allure.title('Create a task of Reward type')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_add_reward():
    random_title = fake.sentence(nb_words=3).rstrip('.')

    tasks = AddTaskButton()
    login = LoginPage()

    login.login_page_open()
    login.login_with_email()
    login.login_checked()
    tasks.click_add_task_btn()
    tasks.pick_task('Reward')
    tasks.name_a_task(random_title)
    tasks.click_create_btn()
    tasks.check_task_in_list(random_title)
