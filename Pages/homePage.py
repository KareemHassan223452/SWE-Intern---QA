from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.account_button = (By.CSS_SELECTOR, '.trig.-df.-i-ctr.-fs16')
        self.sign_in_button = (By.CSS_SELECTOR, '.btn._prim.-fw._md')
        self.cart_button = (By.CSS_SELECTOR, '.-df.-i-ctr.-gy9.-hov-or5.-phs.-fs16')
        self.search_input = (By.ID, 'fi-q')
        self.search_button = (By.CSS_SELECTOR, '.btn._prim._md.-mls.-fsh0')
        self.product_card = (By.CSS_SELECTOR, '.prd._fb.col.c-prd')
        self.add_to_cart_button = (By.CSS_SELECTOR, '.add.btn._prim.-pea._md')
        self.close_ad_button = (By.CLASS_NAME, 'cls')
        self.actions = ActionChains(driver)

    def close_ad(self):
        print("Attempting to close ad")
        try:
            close_ad_element = self.driver.find_element(*self.close_ad_button)
            print(f"Found element to close ad: {close_ad_element}")
            close_ad_element.click()
        except Exception as e:
            print(f"Failed to close ad: {e}")

    def open_account(self):
        print("Attempting to open account")
        self.driver.find_element(*self.account_button).click()

    def sign_in(self):
        print("Attempting to sign in")
        self.driver.find_element(*self.sign_in_button).click()

    def open_cart(self):
        print("Attempting to open cart")
        self.driver.find_element(*self.cart_button).click()

    def search_items(self, product_name):
        self.driver.find_element(*self.search_input).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    def add_item_to_cart(self, product_name):
        print(f"Adding item to cart: {product_name}")
        self.search_items(product_name)
        time.sleep(3)
        product = self.driver.find_element(*self.product_card)
        self.actions.move_to_element(product).perform()
        time.sleep(3)
        self.driver.find_element(*self.add_to_cart_button).click()
