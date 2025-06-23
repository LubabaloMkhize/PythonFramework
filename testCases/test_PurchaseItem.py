import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_PurchaseItem:
    baseURL = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_parchaseItems(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        homePageVerification = self.driver.find_element(By.XPATH, self.hp.label_products_xpath).text

        if homePageVerification=="Products":
            allure.attach(self.driver.get_screenshot_as_png(),name="Home Page",attachment_type=AttachmentType.PNG)
            assert True
        else:
            assert False

        self.driver.quit()
