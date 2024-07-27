from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.username_input = (By.ID, 'txtUsername')
        self.password_input = (By.ID, 'txtPassword')
        self.login_button = (By.ID, 'btnLogin')
        self.error_message = (By.ID, 'spanMessage')

    def load(self):
        self.browser.get('http://your-orangehrm-url.com')

    def login(self, username, password):
        self.browser.find_element(*self.username_input).send_keys(username)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.browser.find_element(*self.error_message).text
