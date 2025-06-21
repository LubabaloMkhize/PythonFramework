from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    textbox_username_xpath="//input[contains(@id,'user-name')]"
    textbox_password_xpath="//input[contains(@placeholder,'Password')]"
    button_login_xpath="//input[contains(@id,'login-button')]"

    def __(self,driver):
        self.driver=driver


    def enterUsername(self,username):
        wait=WebDriverWait(self.driver, 30)
        element=wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_username_xpath)))
        element.send_keys(username)

    def enterPassword(self,password):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_password_xpath)))
        element.send_keys(password)

    def clickLoginButton(self):
        wait=WebDriverWait(self.driver, 30)
        element=wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        element.click()



