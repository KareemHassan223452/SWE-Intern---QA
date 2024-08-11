from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.addingQuantity = (By.XPATH, '//button[@aria-label="increase cart quantity"]')
        self.removeItem2 = (By.CSS_SELECTOR, '.btn._prim._i.-fw.-fh')
        self.removeItem = (By.CSS_SELECTOR, '.btn._def._ti.-mra')
        self.checkoutButton = (By.CSS_SELECTOR, '.btn._prim._md.-fw')

    def adding_quantity(self):
        self.driver.find_element(*self.addingQuantity).click()

    def remove_item(self):
        self.driver.find_element(*self.removeItem).click()
        self.driver.find_element(*self.removeItem2).click()

    def checkout_button(self):
        self.driver.find_element(*self.checkoutButton).click()
