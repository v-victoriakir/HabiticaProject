import allure
from dotenv import load_dotenv

load_dotenv()

class TasksAPI:
    def __init__(self, session, auth_headers, base_url):
        self.session = session
        self.auth_headers = auth_headers
        self.base_url = base_url
        self.session.headers.update(auth_headers)

    @allure.step("Create a task of a specified by a test type")
    def create_task(self, task_text, task_type):
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
        return response.json()['data']

    @allure.step("Getting a list of all user's tasks")
    def get_all_tasks(self):
        response = self.session.get(
            url=f"{self.base_url}/tasks/user"
        )
        assert response.status_code == 200, (
            f"Failed to get all tasks, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        return response

    @allure.step("Delete a task by ID")
    def delete_task_by_id(self, task_id):
        response = self.session.delete(
            url=f"{self.base_url}/tasks/{task_id}"
        )
        assert response.status_code == 200, (
            f"Failed delete the task {task_id}, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        return response