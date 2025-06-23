from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    label_products_xpath = "//span[@class='title'][contains(.,'Products')]"

    def __init__(self, driver):
        self.driver = driver
