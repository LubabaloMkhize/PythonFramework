# Python Test Automation Framework

This project is a Python-based test automation framework designed for efficient and scalable web application testing. It leverages `pytest` for test execution, `Selenium` for browser automation, and `Allure Report` for comprehensive test reporting.

## Features

*   **Pytest Framework**: Robust and flexible test framework for writing clear and concise tests.
*   **Page Object Model (POM)**: Organized test code using the Page Object Model for maintainability and reusability.
*   **Cross-Browser Testing**: Configurable to run tests across different browsers (e.g., Firefox, Chrome).
*   **Allure Reporting**: Generates rich and interactive test reports with detailed information about test execution.
*   **Test Tagging/Marking**: Ability to categorize and run specific sets of tests using `pytest` markers (e.g., `sanity`, `regression`).

## Project Structure

*   `testCases/`: Contains all the test scripts.
*   `pageObjects/`: Stores Page Object classes, representing different pages of the application under test.
*   `utilities/`: Houses helper functions, common utilities, and reusable components.
*   `Configurations/`: Likely contains configuration files for test environments, browser settings, etc.
*   `allure-results/`: Directory where Allure test results are generated.
*   `runTests.bat`: A batch script to execute tests with predefined parameters.

## Setup

To get this framework up and running on your local machine, follow these steps:

### Prerequisites

*   **Python 3.x**: Ensure Python is installed and added to your system's PATH.
*   **Git**: For cloning the repository.
*   **Browser Driver**: Download the appropriate browser driver (e.g., `geckodriver` for Firefox, `chromedriver` for Chrome) and place it in your system's PATH or a designated `drivers` folder within the project.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd PythonFramework
    ```
    (Replace `<repository_url>` with the actual URL of your Git repository)

2.  **Install dependencies**:
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    .\venv\Scripts\activate   # On Windows
    source venv/bin/activate # On macOS/Linux
    ```
    Install the required Python packages. While a `requirements.txt` was not found, common dependencies for such a project include:
    ```bash
    pip install pytest selenium allure-pytest
    ```
    You might need to install other packages depending on your specific test implementation.

## How to Run Tests

Tests can be executed using `pytest` directly or by using the provided `runTests.bat` script.

### Using `runTests.bat`

The `runTests.bat` script is configured to run tests marked with "sanity" and generate Allure reports for Firefox:

```bash
runTests.bat
```

### Using `pytest` directly

You can customize test execution using `pytest` command-line options.

*   **Run all tests**:
    ```bash
    pytest
    ```

*   **Run tests with a specific marker (e.g., 'sanity')**:
    ```bash
    pytest -m "sanity"
    ```

*   **Generate Allure results**:
    ```bash
    pytest --alluredir=allure-results
    ```

*   **Run tests verbosely and capture stdout**:
    ```bash
    pytest -s -v
    ```

*   **Example: Run sanity tests on Chrome and generate Allure reports**:
    ```bash
    pytest -s -v -m "sanity" --alluredir="allure-results" --browser chrome
    ```
    (Note: The `--browser` argument might require custom `pytest` hooks or configuration in your project to be recognized.)

## Viewing Allure Reports

After running tests with `--alluredir=allure-results`, you can generate and view the Allure report:

1.  **Install Allure Commandline (if not already installed)**:
    Follow instructions on the [Allure GitHub page](https://github.com/allure-framework/allure-docs#quick-start) or use a package manager (e.g., `scoop install allure` on Windows, `brew install allure` on macOS).

2.  **Generate and open the report**:
    ```bash
    allure serve allure-results
    ```
    This will open the generated report in your default web browser.
