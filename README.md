# Data Driven Test Framework (DDF) using Page Object Model (POM)

Website Link: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

## Test Objective
The objective is to automate testing of the login functionality for the OrangeHRM demo website by using test data from an Excel file. The test will be executed using the Pytest framework and a Data Driven Test Framework (DDF) with the Page Object Model (POM) design pattern. The process includes adding test data to the Excel file, performing login tests based on that data, and shutting down the browser after the test execution

## Table of Contents
+ [Features]()
+ [Tech Stack]()
+ [Running Tests]()
+ [Project Structure]()

 
## Features
+ <ins>**Data-Driven Testing Framework (DDF):**</ins> Test data is fetched from an external Excel file, enabling the execution of tests with multiple data sets without modifying the test scripts.
+ <ins>**Page Object Model (POM):**</ins> Separation of test logic and UI interactions. Each web page has its own corresponding class that defines methods for interacting with the elements on that page.
+ <ins>**Pytest Framework:**</ins> Used to manage test cases, execute tests, and generate detailed reports.
+ <ins>**Excel Integration:**</ins> Test data for login credentials is stored and retrieved from an Excel file, making it easy to add, modify, or scale test data without changing code.
+ <ins>**Reusable Components:**</ins> Common actions like login, navigating to sections, and performing shutdown operations are encapsulated in reusable methods, improving maintainability.
+ <ins>**Cross-Platform Compatibility:**</ins> The framework can be run across different environments, supporting different operating systems and web browsers.
+ <ins>**Automation and Reporting:**</ins> Automation of repetitive tests with detailed reports on test results, making it easier to monitor and debug test executions.

## Tech Stack
* <ins>**Programming Language:**</ins> Python
* <ins>**Test Framework:**</ins> pytest and DDF
* <ins>**Automation Tool:**</ins> Selenium WebDriver
* <ins>**Reporting:**</ins> pytest-html
* <ins>**Browser Compatibility:**</ins> Chrome, Firefox, and optionally, Edge

## Running Tests
To execute tests, use the following commands:

1. Run All Tests:
```
pytest
```
2. Generate HTML Report:
```
pytest --html=Reports/test_report.html
```
3. Headless Browser Execution:
```
You can set up tests to run in headless mode directly in your test script.
```
4. Incognito Mode Execution:
```
You can set up tests to run in Incognito mode directly in your test script.
```

## Project Structure
```
Task_12/
│
├── TestScript/
│   └── test_login.py          # Main test script for data-driven login functionality
│
├── TestLocators/
│   └── locators.py            # Contains locators for various elements on the OrangeHRM page
│
├── TestData/
│   └── data.py                # Contains test data such as URL, Excel file details, and dashboard URL
│
├── Utilities/
│   └── excel_functions.py     # Utility functions to interact with the Excel file (read/write data)
│
├── Reports/
│   └── test_report.html       # HTML test report generated by pytest-html
│
└── README.md                  # Project documentation
```
