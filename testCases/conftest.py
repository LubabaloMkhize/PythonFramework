import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture()
def setup(browser):

    browser = browser.lower()

    if browser == "chrome":
        options = Options()

        # Enable these only in GitHub Actions
        if os.getenv("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")


    yield driver

    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        help="Browser to run the tests"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'Sauce Demo'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'Lubabalo Mkhize'

