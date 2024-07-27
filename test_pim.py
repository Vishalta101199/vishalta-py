import json
import pytest
from selenium.webdriver.common.by import By

# Load test data
with open('data/pim_data.json') as f:
    pim_data = json.load(f)

@pytest.mark.parametrize("data", pim_data)
def test_pim(browser, data):
    browser.get('http://your-orangehrm-url.com')

    # Login to the system
    username_input = browser.find_element(By.ID, 'txtUsername')
    password_input = browser.find_element(By.ID, 'txtPassword')
    login_button = browser.find_element(By.ID, 'btnLogin')

    username_input.send_keys('Admin')
    password_input.send_keys('admin123')
    login_button.click()

    assert browser.current_url == 'http://your-orangehrm-url.com/dashboard', "Login failed"

    # Navigate to PIM module
    pim_module = browser.find_element(By.ID, 'menu_pim_viewPimModule')
    pim_module.click()

    if data['action'] == 'add':
        add_button = browser.find_element(By.ID, 'btnAdd')
        add_button.click()

        first_name_input = browser.find_element(By.ID, 'firstName')
        last_name_input = browser.find_element(By.ID, 'lastName')
        employee_id_input = browser.find_element(By.ID, 'employeeId')
        save_button = browser.find_element(By.ID, 'btnSave')

        first_name_input.send_keys(data['first_name'])
        last_name_input.send_keys(data['last_name'])
        employee_id_input.send_keys(data['employee_id'])
        save_button.click()

        success_message = browser.find_element(By.CLASS_NAME, 'message success fadable').text
        assert 'Successfully Saved' in success_message, "Employee addition failed"

    elif data['action'] == 'edit':
        search_input = browser.find_element(By.ID, 'empsearch_id')
        search_input.send_keys(data['employee_id'])
        search_button = browser.find_element(By.ID, 'searchBtn')
        search_button.click()

        employee_record = browser.find_element(By.LINK_TEXT, data['employee_id'])
        employee_record.click()

        edit_button = browser.find_element(By.ID, 'btnSave')
        edit_button.click()

        first_name_input = browser.find_element(By.ID, 'personal_txtEmpFirstName')
        last_name_input = browser.find_element(By.ID, 'personal_txtEmpLastName')

        first_name_input.clear()
        first_name_input.send_keys(data['new_first_name'])
        last_name_input.clear()
        last_name_input.send_keys(data['new_last_name'])

        save_button = browser.find_element(By.ID, 'btnSave')
        save_button.click()

        success_message = browser.find_element(By.CLASS_NAME, 'message success fadable').text
        assert 'Successfully Saved' in success_message, "Employee edit failed"

    elif data['action'] == 'delete':
        search_input = browser.find_element(By.ID, 'empsearch_id')
        search_input.send_keys(data['employee_id'])
        search_button = browser.find_element(By.ID, 'searchBtn')
        search_button.click()

        checkbox = browser.find_element(By.NAME, 'chkSelectRow[]')
        checkbox.click()

        delete_button = browser.find_element(By.ID, 'btnDelete')
        delete_button.click()

        confirm_button = browser.find_element(By.ID, 'dialogDeleteBtn')
        confirm_button.click()

        success_message = browser.find_element(By.CLASS_NAME, 'message success fadable').text
        assert 'Successfully Deleted' in success_message, "Employee deletion failed"
