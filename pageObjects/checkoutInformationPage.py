from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutInformationPage:

    pageTitle_xpath = "//span[contains(.,'Checkout: Your Information')]"

    firstNameField_id = "first-name"

    lastNameField_id = "last-name"

    postalCode_id = "postal-code"

    btnContinue_id= "continue"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, firstname):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.firstNameField_id)))
        element.send_keys(firstname)

    def enterLastName(self, lastname):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.lastNameField_id)))
        element.send_keys(lastname)

    def enterPostalCode(self, postalcode):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.postalCode_id)))
        element.send_keys(postalcode)

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.btnContinue_id)))
        element.click()