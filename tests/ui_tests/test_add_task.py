import allure
import pytest
from allure_commons.types import Severity

from faker import Faker

from model.ui.web_pages.dashboard_page import AddTaskButton
from model.ui.web_pages.login_page import LoginPage

fake = Faker()

@allure.tag('Web')
@allure.feature("Add Task")
@allure.title('Create a task')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("task_type", [
    ('Habit'),
    ('Daily'),
    ('To Do'),
    ('Reward')
])
def test_add_task(task_type):
    random_title = fake.sentence(nb_words=3).rstrip('.')
    tasks = AddTaskButton()
    login = LoginPage()

    with allure.step("Open login page and authenticate"):
        login.login_page_open()
        login.login_with_email()
        login.login_checked()

    with allure.step(f"Create {task_type} task with random title"):
        tasks.click_add_task_btn()
        tasks.pick_task(task_type)
        tasks.name_a_task(random_title)
        tasks.click_create_btn()

    with allure.step("Verify task was created successfully"):
        tasks.check_task_in_list(task_type)