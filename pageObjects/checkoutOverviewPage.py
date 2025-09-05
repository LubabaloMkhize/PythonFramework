from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutOverviewPage:
    pageTitle_xpath = "//span[contains(.,'Checkout: Overview')]"
    buttonfinish_id ="finish"

    def __init__(self, driver):
        self.driver = driver

    def clickFinishButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.buttonfinish_id)))
        element.click()