import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.homePage import HomePage
from Pages.Login import LoginPage
from Pages.Cart import Cart
import time


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.jumia.com.eg/")
    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.cart_page = Cart(driver)
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_login_success(self):
        # Close the ad
        print("Running test: test_login_success")
        self.home_page.close_ad()
        time.sleep(3)

        # Open account section
        self.home_page.open_account()
        time.sleep(3)

        # Sign in
        self.home_page.sign_in()
        time.sleep(3)

        # Enter username
        self.login_page.enter_username('Kareemhassan2003@gmail.com')
        time.sleep(3)

        # Click login button on the username page
        self.login_page.click_login()
        time.sleep(3)

        # Enter password
        self.login_page.enter_password('20x3sidney')
        time.sleep(3)

        # Click login button on the password page
        self.login_page.click_login2()
        time.sleep(5)

        # Verify dashboard title

        element = self.driver.find_element(By.ID, 'card_otp')
        assert element is not None, "Test case failed"

    def test_login_failed(self):
        # Close the ad
        print("Running test: test_login_failed")
        self.home_page.close_ad()
        time.sleep(3)

        # Open account section
        self.home_page.open_account()
        time.sleep(3)

        # Sign in
        self.home_page.sign_in()
        time.sleep(3)

        # Enter username
        self.login_page.enter_username('fakekareemhassan.com')
        time.sleep(3)

        # Click login button on the username page
        self.login_page.click_login()
        time.sleep(3)

        element = self.driver.find_element(By.ID, 'input_identifierValue')
        assert element is not None, "Test case failed"

    def test_login_noinput(self):
        # Close the ad
        print("Running test: test_login_failed")
        self.home_page.close_ad()
        time.sleep(3)

        # Open account section
        self.home_page.open_account()
        time.sleep(3)

        # Sign in
        self.home_page.sign_in()
        time.sleep(3)

        # Enter username
        self.login_page.enter_username('')
        time.sleep(3)

        # Click login button on the username page
        self.login_page.click_login()
        time.sleep(3)

        element = self.driver.find_element(By.ID, 'input_identifierValue')
        assert element is not None, "Test case failed"

    def test_login_nopass(self):
        # Close the ad
        print("Running test: test_login_failed")
        self.home_page.close_ad()
        time.sleep(3)

        # Open account section
        self.home_page.open_account()
        time.sleep(3)

        # Sign in
        self.home_page.sign_in()
        time.sleep(3)

        # Enter username
        self.login_page.enter_username('Kareemhassan2003@gmail.com')
        time.sleep(3)

        # Click login button on the username page
        self.login_page.click_login()
        time.sleep(3)

        # Enter password
        self.login_page.enter_password('')
        time.sleep(3)

        # Click login button on the password page
        self.login_page.click_login2()
        time.sleep(5)

        # Verify dashboard title

        element = self.driver.find_element(By.NAME, 'password')
        assert element is not None, "Test case failed"


    def test_search_item(self):
        # Close the ad
        print("Running test: test_searching_item_successful")
        self.home_page.close_ad()
        time.sleep(3)

        self.home_page.search_items("Laptop")
        time.sleep(3)
        element = self.driver.find_element(By.ID, 'fi-q')
        assert element is not None, "Test case failed"
