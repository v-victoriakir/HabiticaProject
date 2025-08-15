from model.api.auth import AuthAPI
from model.api.tasks import TasksAPI

import pytest
import allure
from allure_commons.types import Severity

from faker import Faker
fake = Faker()

def generate_random_title():
    random_title = fake.sentence(nb_words=3).rstrip('.')
    return random_title

@allure.tag('API')
@allure.feature("Task Operations")
@allure.title('Verify Type of a created task')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.NORMAL)
def test_task_creation_with_type_verification():
    auth = AuthAPI()
    auth.authorize()
    session, headers, base_url = auth.get_session()
    tasks_api = TasksAPI(session, headers, base_url)

    task_type = "habit"  # Can be parameterized
    task_text = f"TestTask_{generate_random_title()}"

    # 1. Create a new task with specified parameters - POST
    try:
        new_task = tasks_api.create_task(task_text=task_text, task_type=task_type)
        task_id = new_task['id']
        print(f"Created task - ID: {task_id}, Text: {task_text}, Expected Type: {task_type}")

        # Verify the returned task has correct type
        assert new_task['type'] == task_type, \
            f"Created task type {new_task['type']} doesn't match requested type {task_type}"
    except Exception as e:
        pytest.fail(f"Task creation failed: {str(e)}")

        # 2. Verify in task list - GET
    try:
        response = tasks_api.get_all_tasks()
        all_tasks = response.json()['data']

        # Find our specific task
        created_task = next((task for task in all_tasks if task['id'] == task_id), None)
        assert created_task is not None, f"Task {task_id} not found in task list"

        # Verify type matches
        assert created_task['type'] == task_type, \
            f"Task type in list {created_task['type']} doesn't match expected {task_type}"

        print(f"Verified task exists with correct type: {created_task['type']}")
    except Exception as e:
        pytest.fail(f"Task verification failed: {str(e)}")

@allure.tag('API')
@allure.feature("Task Operations")
@allure.title('Delete a task')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_task_create_delete():
    auth = AuthAPI()
    auth.authorize()
    session, headers, base_url = auth.get_session()
    tasks_api = TasksAPI(session, headers, base_url)

    task_type = "todo"  # Can be parameterized
    task_text = f"TestTask_{generate_random_title()}"

    # 1. Create a new task with specified parameters - POST
    try:
        new_task = tasks_api.create_task(task_text=task_text, task_type=task_type)
        task_id = new_task['id']
        print(f"Created new task - ID: {task_id}, Name: {task_text}, Type: {task_type}")
    except Exception as e:
        pytest.fail(f"Failed to create task: {str(e)}")

    # 2. Verify task exists in the list - GET
    try:
        response = tasks_api.get_all_tasks()
        all_tasks = response.json()['data']
        task_exists = any(task['id'] == task_id for task in all_tasks)
        assert task_exists, f"Created task {task_id} not found in task list"
        print(f"Verified task {task_id} exists")
    except Exception as e:
        pytest.fail(f"Task verification failed: {str(e)}")

    # 3. Delete the task - DELETE
    try:
        delete_response = tasks_api.delete_task_by_id(task_id)
        assert delete_response.status_code == 200, \
            f"Delete failed with status {delete_response.status_code}"
        print(f"Successfully deleted task {task_id}")
    except Exception as e:
        pytest.fail(f"Task deletion failed: {str(e)}")

    # 4. Verify task is deleted - GET
    try:
        updated_response = tasks_api.get_all_tasks()
        updated_tasks = updated_response.json()['data']
        still_exists = any(task['id'] == task_id for task in updated_tasks)
        assert not still_exists, f"Task {task_id} still exists after deletion"
        print(f"Verified task {task_id} is deleted")
    except Exception as e:
        pytest.fail(f"Deletion verification failed: {str(e)}")