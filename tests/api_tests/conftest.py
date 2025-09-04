import pytest

from model.api.auth import AuthAPI
from model.api.tasks import TasksAPI


@pytest.fixture
def tasks_api():
    auth = AuthAPI()
    auth.auth_successful()
    session, headers, base_url = auth.get_session()
    api = TasksAPI(session, headers, base_url)
    yield api
    api.cleanup_created_tasks()
