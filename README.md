# UI Test Automation Project

Automation framework built with Python, Selenium and Pytest using the Page Object Model (POM) design pattern.

## Features
- Login tests
- Parametrized login scenarios
- Logout test
- Add/remove products from cart
- Cart validation
- Complete checkout flow
- Negative checkout scenarios
- Product sorting validation
- Screenshots on test failure
- HTML test reports

## Tech Stack
- Python
- Selenium WebDriver
- Pytest

## Run Tests

```bash
pip install -r requirements.txt
pytest
```

Generate HTML report:

```bash
pytest --html=report.html
```

## Project Structure

pages/ - page objects and page methods  
tests/ - test cases  
utils/ - reusable waits/helpers  
conftest.py - fixtures and WebDriver setup  
screenshots/ - failed test screenshots