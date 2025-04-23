import pytest
from selenium import webdriver
import curl
from api_methods import ApiMethod
from utils import Utils


@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    browser = None

    if request.param == "firefox":
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(curl.MAIN_SITE)

    yield browser

    browser.quit()

@pytest.fixture
def user():
    user = Utils()
    user_data = user.create_user()
    response = user.auth_user(user_data["email"], user_data["password"])
    token = response.json()['accessToken']
    yield user_data, token

    if "email" in user_data and "password" in user_data:
        ApiMethod.api_method_delete_user(token)

@pytest.fixture
def random_user_data():
    user = Utils()
    user_data = user.generate_random_data_user_json()
    return user_data

