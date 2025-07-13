import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.cartPage import CartPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_PurchaseItem:
    baseURL = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.MINOR)
    def test_print(self):
        print("Success")

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_parchaseItems(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cp = CartPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        homePageVerification = self.driver.find_element(By.XPATH, self.hp.label_products_xpath).text

        if homePageVerification=="Products":
            allure.attach(self.driver.get_screenshot_as_png(),name="Home Page",attachment_type=AttachmentType.PNG)
            assert True
        else:
            assert False

        self.hp.clickAddToCartButton()

        self.driver.find_element(By.XPATH, self.hp.button_removeItem_xpath).is_displayed()

        allure.attach(self.driver.get_screenshot_as_png(), name="Item Selected", attachment_type=AttachmentType.PNG)

        self.hp.clickShoppingCart()

        allure.attach(self.driver.get_screenshot_as_png(), name="Shopping Cart", attachment_type=AttachmentType.PNG)

        cartPageVerification = self.driver.find_element(By.XPATH, self.cp.label_cartPage_xpath).text

        if cartPageVerification == "Your Cart":
            allure.attach(self.driver.get_screenshot_as_png(), name="Cart Page", attachment_type=AttachmentType.PNG)
            assert True
        else:
            assert False

        self.cp.clickCheckoutButton()

        self.driver.quit()
