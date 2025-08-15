import os
import allure

import requests
from dotenv import load_dotenv

load_dotenv()

class AuthAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = os.getenv('HABITICA_BASE_URL')
        self.username = os.getenv('HABITICA_USERNAME')
        self.password = os.getenv('HABITICA_PASSWORD')
        self.auth_headers = None

    @allure.step("Authorization via API")
    def authorize(self):
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
