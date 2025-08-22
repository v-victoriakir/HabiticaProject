import os

import allure
import requests

from jsonschema import validate
from model.api.schemas import schemas

from dotenv import load_dotenv

load_dotenv()

from faker import Faker

fake = Faker()


class AuthAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = os.getenv('HABITICA_BASE_URL')
        self.username = os.getenv('HABITICA_USERNAME')
        self.password = os.getenv('HABITICA_PASSWORD')
        self.auth_headers = None

    @allure.step("Successful authorization via API ")
    def auth_successful(self):
        client_headers = {
            'x-client': os.getenv('HABITICA_X_CLIENT'),
            'x-api-user': os.getenv('HABITICA_X_API_USER')
        }
        self.session.headers.update(client_headers)

        response = self.session.post(
            url=f"{self.base_url}/user/auth/local/login",
            data={"username": self.username, "password": self.password}
        )
        assert response.status_code == 200, (
            f"Login failed: expected 200, got {response.status_code}\n"
            f"Response text: {response.text}"
        )
        # validate(response.json(),schema=schemas.post_auth_successful)

        self.auth_headers = {
            "x-api-user": response.json()['data']['id'],
            "x-api-key": response.json()['data']['apiToken']
        }
        return response

    @allure.step("Save authorized session via API")
    def get_session(self):
        """Returns the authenticated session with headers"""
        if not self.auth_headers:
            raise RuntimeError("You must call authorize() first")
        return self.session, self.auth_headers, self.base_url

    @allure.step("Unsuccessful authorization via API ")
    def auth_unsuccessful(self, test_username, test_password):
        response = self.session.post(
            url=f"{self.base_url}/user/auth/local/login",
            json={
                "username": test_username,
                "password": test_password
            },
            headers={
                'x-client': os.getenv('HABITICA_X_CLIENT'),
                'Content-Type': 'application/json'
            }
        )
        # validate(response.json(),schema=schemas.post_auth_unsuccessful)
        return response
