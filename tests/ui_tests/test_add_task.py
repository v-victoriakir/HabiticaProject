import allure
import pytest
from allure_commons.types import Severity
from faker import Faker

from model.ui.web_pages.dashboard_page import AddTaskButton
from model.ui.steps.login_steps import LoginSteps

fake = Faker()


@allure.tag('Web')
@allure.feature("Add Task")
@allure.title('Create a task')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("task_index", [0, 1, 2, 3])
def test_add_task(task_index):
    random_title = fake.sentence(nb_words=3).rstrip('.')
    tasks = AddTaskButton()
    login_steps = LoginSteps()

    with allure.step("Open login page and authenticate"):
        login_steps.login_with_username()
        login_steps.verify_login_successful()

    with allure.step(f"Create task from position {task_index} with random title"):
        tasks.click_add_task_btn()
        tasks.pick_task_by_index(task_index)
        tasks.name_a_task(random_title)
        tasks.click_create_btn()

    with allure.step("Verify task was created successfully"):
        tasks.check_task_in_list(random_title)
