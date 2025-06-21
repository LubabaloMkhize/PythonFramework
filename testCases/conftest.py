import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("Chrome Browser Launched")
    elif browser == 'firefox':
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Firefox Browser Launched")
    else:
        driver=webdriver.edge(EdgeChromiumDriverManager.install())
        print("Edge Browser Launched")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] ='Sauce Demo'
    config._metadata['Module Name'] ='Login to sauce Demo'
    config._metadata['Tester Name'] ='Lubabalo Mkhize'

