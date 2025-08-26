import allure
from dotenv import load_dotenv

from faker import Faker

from jsonschema import validate
from model.api.schemas import schemas

load_dotenv()


class TasksAPI:
    def __init__(self, session, auth_headers, base_url):
        self.session = session
        self.auth_headers = auth_headers
        self.base_url = base_url
        self.session.headers.update(auth_headers)
        self.fake = Faker()
        self.created_tasks = []  # Для отслеживания созданных задач

    def generate_random_title(self):
        return self.fake.sentence(nb_words=3).rstrip('.')

    @allure.step("Create a task")
    def create_task(self, task_text=None, task_type="todo"):
        """
        task_text (str, optional): Текст задачи. Если None - генерируется случайный
        task_type (str): Тип задачи (по умолчанию to do)
        """
        if task_text is None:
            task_text = f"TestTask_{self.generate_random_title()}"

        response = self.session.post(
            url=f"{self.base_url}/tasks/user",
            json={
                "text": task_text,
                "type": task_type
            }
        )
        assert response.status_code == 201, (
            f"Failed to create the {task_text} task, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        # validate(response.json(),schema=schemas.post_create_task)
        task_data = response.json()['data']
        self.created_tasks.append(task_data['id'])  # Добавляем в список созданных
        return task_data

    @allure.step("Getting a list of all user's tasks")
    def get_all_tasks(self):
        response = self.session.get(
            url=f"{self.base_url}/tasks/user"
        )
        assert response.status_code == 200, (
            f"Failed to get all tasks, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        return response.json()['data']

    @allure.step("Delete a task by ID")
    def delete_task_by_id(self, task_id):
        response = self.session.delete(
            url=f"{self.base_url}/tasks/{task_id}"
        )
        assert response.status_code == 200, (
            f"Failed delete the task {task_id}, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        # validate(response.json(),schema=schemas.delete_task)
        if task_id in self.created_tasks:
            self.created_tasks.remove(task_id)
        return response

    @allure.step("Move task to new position")
    def move_task_to_position(self, task_id, new_position):
        response = self.session.post(
            url=f"{self.base_url}/tasks/{task_id}/move/to/{new_position}"
        )
        assert response.status_code == 200, (
            f"Failed move the task {task_id} to the position {new_position}, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        # validate(response.json(),schema=schemas.post_move_task)
        return response

    @allure.step("Verify task type")
    def verify_task_type(self, task_id, expected_type):
        all_tasks = self.get_all_tasks()
        task = next((t for t in all_tasks if t['id'] == task_id), None)
        assert task is not None, f"Task {task_id} not found"
        assert task['type'] == expected_type, f"Task type {task['type']} doesn't match expected {expected_type}"
        return task

    @allure.step("Verify task exists")
    def verify_task_exists(self, task_id, should_exist=True):
        all_tasks = self.get_all_tasks()
        task_exists = any(task['id'] == task_id for task in all_tasks)

        if should_exist:
            assert task_exists, f"Task {task_id} should exist but wasn't found"
        else:
            assert not task_exists, f"Task {task_id} should not exist but was found"
        return task_exists

    @allure.step("Cleanup all created tasks")
    def cleanup_created_tasks(self):
        for task_id in self.created_tasks[:]:  # Используем копию списка для безопасного удаления
            try:
                self.delete_task_by_id(task_id)
            except Exception as e:
                print(f"Failed to delete task {task_id}: {e}")
        self.created_tasks.clear()

    @allure.step("Get task by ID")
    def get_task_by_id(self, task_id):
        all_tasks = self.get_all_tasks()
        task = next((t for t in all_tasks if t['id'] == task_id), None)
        assert task is not None, f"Task {task_id} not found"
        return task

    @allure.step("Verify task text")
    def verify_task_text(self, task_id, expected_text):
        task = self.get_task_by_id(task_id)
        assert task['text'] == expected_text, (
            f"Task text '{task['text']}' doesn't match expected '{expected_text}'"
        )
        return task

    @allure.step("Update task")
    def update_task(self, task_id, **kwargs):
        response = self.session.put(
            url=f"{self.base_url}/tasks/{task_id}",
            json=kwargs
        )
        assert response.status_code == 200, f"Failed to update task {task_id}"
        return response.json()['data']
