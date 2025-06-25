from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CartPage:
    label_cartPage_xpath = "//span[contains(.,'Your Cart')]"
    button_checkout_xpath = "//div[@id='cart_contents_container']/div/div[2]/button[2]"


    def __init__(self, driver):
        self.driver = driver

    def clickCheckoutButton(self):
        wait = WebDriverWait(self.driver,30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_checkout_xpath)))
        element.click()
