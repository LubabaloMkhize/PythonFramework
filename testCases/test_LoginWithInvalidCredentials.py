import allure
import pytest

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_LoginWithInvalidCredentials:
    baseURL = ReadConfig.getBaseURL()
    username = ReadConfig.getInvalidUsername()
    password = ReadConfig.getInvalidPassword()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page With Invalid Credentials", attachment_type=AttachmentType.PNG)

        self.driver.quit()