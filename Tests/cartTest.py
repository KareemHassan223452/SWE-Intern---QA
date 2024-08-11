import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.homePage import HomePage
from Pages.Cart import Cart
import time


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.jumia.com.eg/")
    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    request.cls.cart_page = Cart(driver)
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestCart:

    def test_add_to_cart(self):
        # Close the ad
        print("Running test: test_adding_item_successful")
        self.home_page.close_ad()
        time.sleep(3)
        self.home_page.add_item_to_cart("Laptop")
        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, '.add.btn._prim.-pea._md')
        assert element is not None, "Test case failed"

    def test_add_item_quantity(self):
        # Close the ad
        print("Running test: test_adding_qunatity_successful")
        self.home_page.close_ad()
        time.sleep(3)
        self.home_page.add_item_to_cart("T1000 ULTRA Smart Watch SERIES 9 - Black")
        time.sleep(5)
        self.home_page.open_cart()
        time.sleep(5)
        self.cart_page.adding_quantity()
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, '//button[@aria-label="increase cart quantity"]')
        assert element is not None, "Test case failed"

    def test_remove_item_from_cart(self):
        # Close the ad
        print("Running test: Test_remove_item_successful")
        self.home_page.close_ad()
        time.sleep(3)
        self.home_page.add_item_to_cart("T1000 ULTRA Smart Watch SERIES 9 - Black")
        time.sleep(5)
        self.home_page.open_cart()
        time.sleep(3)
        self.cart_page.remove_item()
        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR,'.btn._prim.-mtl')
        assert element is not None, "Test case failed "
