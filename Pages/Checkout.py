from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.enterAddress = (By.ID, 'fi-address1')
        self.selectCity = (By.ID, 'fi-cityId')
        self.selectCity2 = (By.XPATH, '//option[value()="566"]')
        self.saveButton = (By.CSS_SELECTOR, 'btn _prim')
        self.confirmDeliveryDetails = (By.XPATH, '//button[text()= "Confirm delivery details"]')
        self.confirmPaymentMethod = (By.XPATH, '//button[text()= "Confirm payment method"]')
        self.confirmOrder = (By.XPATH, '//button[text()= "Confirm order"]')

    def enter_address(self, address):
        self.driver.find_element(*self.enterAddress).send_keys(address)

    def select_city(self):
        self.driver.find_element(*self.selectCity).click()
        self.driver.find_element(*self.selectCity2).click()

    def save_button(self):
        self.driver.find_element(*self.saveButton).click()

    def confirm_delivery_details(self):
        self.driver.find_element(*self.confirmDeliveryDetails).click()

    def confirm_payment_method(self):
        self.driver.find_element(*self.confirmPaymentMethod).click()

    def confirm_order(self):
        self.driver.find_element(*self.confirmOrder).click()
