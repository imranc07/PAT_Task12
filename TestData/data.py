"""
This Python class is used to store constant data values required for testing the OrangeHRM webpage.

The class `OrangeHRMData` acts as a central repository for storing:
- URLs used in the tests (e.g., login page, dashboard).
- File path of the Excel file that contains test data for data-driven testing.
- The sheet name or index of the Excel sheet containing the relevant test data.
"""

class OrangeHRMData:

    # URL for the OrangeHRM login page
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    # URL for the OrangeHRM dashboard, used to verify successful login
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    
    # Path to the Excel file containing the test data
    excel_file = "F:\\Python-Selenium\\VScode\\GUVI_&_Tasks\\Task_12\\TestData\\testdata.xlsx"
    
    # Name or index of the sheet within the Excel file containing test data
    sheet_number = "Sheet1"
