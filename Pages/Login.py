# pages/login_page.py
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'input_identifierValue')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.CSS_SELECTOR, '.mdc-button.mdc-button--touch.mdc-button--raised.access-btn')
        self.loginButton2 = (By.ID, 'loginButton')

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def click_login2(self):
        self.driver.find_element(*self.loginButton2).click()



