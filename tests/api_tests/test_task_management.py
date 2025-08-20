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
    auth.auth_successful()
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
        all_tasks = tasks_api.get_all_tasks()

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
    auth.auth_successful()
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
        all_tasks = tasks_api.get_all_tasks()
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
        updated_tasks = tasks_api.get_all_tasks()
        still_exists = any(task['id'] == task_id for task in updated_tasks)
        assert not still_exists, f"Task {task_id} still exists after deletion"
        print(f"Verified task {task_id} is deleted")
    except Exception as e:
        pytest.fail(f"Deletion verification failed: {str(e)}")

@allure.tag('API')
@allure.feature("Task Operations")
@allure.title('Move task to new position')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.NORMAL)
def test_move_task_to_top():
    auth = AuthAPI()
    auth.auth_successful()
    session, headers, base_url = auth.get_session()
    tasks_api = TasksAPI(session, headers, base_url)

    task_type = "habit"  # Can be parameterized
    task1 = tasks_api.create_task(task_text=f"Task1_{generate_random_title()}", task_type=task_type)
    task2 = tasks_api.create_task(task_text=f"Task2_{generate_random_title()}", task_type=task_type)
    task3 = tasks_api.create_task(task_text=f"Task3_{generate_random_title()}", task_type=task_type)

    initial_tasks = tasks_api.get_all_tasks()
    initial_order = [task['id'] for task in initial_tasks if task['id'] in [task1['id'], task2['id'], task3['id']]]

    print(f"Initial order: {initial_order}")

    with allure.step(f"Move task {task3['id']} to position 0"):
        move_response = tasks_api.move_task_to_position(task3['id'], 0)
        assert move_response.status_code == 200

    updated_tasks = tasks_api.get_all_tasks()
    updated_order = [task['id'] for task in updated_tasks if task['id'] in [task1['id'], task2['id'], task3['id']]]

    print(f"Updated order: {updated_order}")

    assert updated_order[0] == task3['id'], f"Task3 should be first, but got: {updated_order}"
    print(f"Task moved to beginning successfully.")

    tasks_api.delete_task_by_id(task1['id'])
    tasks_api.delete_task_by_id(task2['id'])
    tasks_api.delete_task_by_id(task3['id'])

# добавить проверку на удаление задач

# ПОЧЕМУ ПОРЯДОК НЕ ПОМЕНЯЛСЯ?
# PASSED [100%]
# Initial order: ['c599f0fe-4e21-4982-81fd-ea22476d4a5f', '8942c471-605d-4589-9e51-caf8d8b86b49', 'c8f8bb52-3523-4f82-8255-f262f005491e']
# Updated order: ['c599f0fe-4e21-4982-81fd-ea22476d4a5f', '8942c471-605d-4589-9e51-caf8d8b86b49', 'c8f8bb52-3523-4f82-8255-f262f005491e']
# Task moved to beginning successfully.


@allure.tag('API')
@allure.feature("Task Operations")
@allure.title('Move task to new position')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.NORMAL)
def test_move_task_to_bottom():
    auth = AuthAPI()
    auth.auth_successful()
    session, headers, base_url = auth.get_session()
    tasks_api = TasksAPI(session, headers, base_url)

    task_type = "todo"  # Can be parameterized
    task1 = tasks_api.create_task(task_text=f"Task1_{generate_random_title()}", task_type=task_type)
    task2 = tasks_api.create_task(task_text=f"Task2_{generate_random_title()}", task_type=task_type)
    task3 = tasks_api.create_task(task_text=f"Task3_{generate_random_title()}", task_type=task_type)

    initial_tasks = tasks_api.get_all_tasks()
    initial_order = [task['id'] for task in initial_tasks if task['id'] in [task1['id'], task2['id'], task3['id']]]

    print(f"Initial order: {initial_order}")

    with allure.step(f"Move task {task3['id']} to position 0"):
        move_response = tasks_api.move_task_to_position(task1['id'], -1)
        assert move_response.status_code == 200

    updated_tasks = tasks_api.get_all_tasks()
    updated_order = [task['id'] for task in updated_tasks if task['id'] in [task1['id'], task2['id'], task3['id']]]

    print(f"Updated order: {updated_order}")

    assert updated_order[-1] == task1['id'], f"Task1 should be at the bottom, but got: {updated_order}"
    print(f"Task moved to the bottom successfully.")

    tasks_api.delete_task_by_id(task1['id'])
    tasks_api.delete_task_by_id(task2['id'])
    tasks_api.delete_task_by_id(task3['id'])

# ПОЧЕМУ ПОРЯДОК НЕ ПОМЕНЯЛСЯ?
# PASSED [100%]
# Initial order: ['d5fce4a2-4d14-41a7-9bea-5cc40f3b7443', '685325c7-d340-4efa-b37e-166f8a09b8e0', '2a178289-3fc8-4c8f-99cf-d0cf8e50a4b8']
# Updated order: ['d5fce4a2-4d14-41a7-9bea-5cc40f3b7443', '685325c7-d340-4efa-b37e-166f8a09b8e0', '2a178289-3fc8-4c8f-99cf-d0cf8e50a4b8']
# Task moved to the bottom successfully.