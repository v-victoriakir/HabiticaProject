import os
from model.api.auth import AuthAPI

import allure
from allure_commons.types import Severity

from dotenv import load_dotenv
load_dotenv()

@allure.tag('API')
@allure.feature("Auth")
@allure.title('Test login works with correct username and password')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.BLOCKER)
def test_successful_login():
    auth = AuthAPI()
    response = auth.auth_successful()
    assert response.status_code == 200, (
        f"Login failed: expected 200, got {response.status_code}\n"
        f"Response text: {response.text}"
    )
    response_data = response.json()
    auth_data = response_data['data']
    assert 'id' in auth_data, "Response data should contain user ID"
    assert 'apiToken' in auth_data, "Response data should contain API token"

    assert auth.auth_headers is not None, "Auth headers should be set after successful login"
    assert auth.auth_headers['x-api-user'] == auth_data['id'], \
        "Auth header user ID should match response user ID"
    assert auth.auth_headers['x-api-key'] == auth_data['apiToken'], \
        "Auth header API token should match response API token"
    print("Successful login test passed")

@allure.tag('API')
@allure.feature("Auth")
@allure.title('Test login with completely invalid credentials')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_unsuccessful_login_with_nonexistent_user():
    auth = AuthAPI()
    response = auth.auth_unsuccessful(
        test_username="nonexistent_user_123",
        test_password="any_password"
    )
    assert response.status_code == 401, \
        f"Expected 401 for invalid credentials, got {response.status_code}"
    print("Invalid credentials test passed - correctly rejected with 401")

@allure.tag('API')
@allure.feature("Auth")
@allure.title('Test login with invalid password')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_unsuccessful_login_with_wrong_password():
    auth = AuthAPI()
    response = auth.auth_unsuccessful(
        test_username=os.getenv('HABITICA_USERNAME'),
        test_password="any_password"
    )
    assert response.status_code == 401, \
        f"Expected 401 for wrong password, got {response.status_code}"
    print("Wrong password test passed - correctly rejected with 401")

@allure.tag('API')
@allure.feature("Auth")
@allure.title('Test login with empty credentials')
@allure.label('owner', 'Victoria K')
@allure.severity(Severity.CRITICAL)
def test_unsuccessful_login_empty_credentials():
    auth = AuthAPI()
    response = auth.auth_unsuccessful(
        test_username="",
        test_password=""
    )
    assert response.status_code in [400, 401], \
        f"Expected 400/401 for empty credentials, got {response.status_code}"
    print("Empty credentials test passed - correctly rejected")