from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    label_products_xpath = "//span[@class='title'][contains(.,'Products')]"
    button_addToCart_xpath = "//button[contains(@data-test,'add-to-cart-sauce-labs-backpack')]"
    button_removeItem_xpath = "//button[contains(@id,'remove-sauce-labs-backpack')]"
    link_shoppingCart_xpath = "//a[@class='shopping_cart_link'][contains(.,'1')]"

    def __init__(self, driver):
        self.driver = driver

    def clickAddToCartButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_addToCart_xpath)))
        element.click()

    def clickShoppingCart(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_shoppingCart_xpath)))
        element.click()