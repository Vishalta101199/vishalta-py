import json
import pytest
from pages.login_page import LoginPage

# Load test data
with open('data/login_data.json') as f:
    login_data = json.load(f)

@pytest.mark.parametrize("data", login_data)
def test_login(browser, data):
    login_page = LoginPage(browser)
    login_page.load()

    login_page.login(data['username'], data['password'])

    if data['expected_result'] == 'success':
        assert browser.current_url == 'http://your-orangehrm-url.com/dashboard', "Login failed"
    else:
        error_message = login_page.get_error_message()
        assert error_message == 'Invalid credentials', "Error message not displayed correctly"
