"""
This file contains all the locators used for interacting with elements on the OrangeHRM webpage.

The class `OrangeHRMLocators` serves as a central repository for storing:
- Locators for input fields, buttons, and other elements required in the test scripts.
- These locators are used by Selenium to locate and interact with the corresponding web elements on the UI.
"""

class OrangeHRMLocators:

    # Locator for the username input field
    username_locator = 'username'
    
    # Locator for the password input field
    password_locator = 'password'
    
    # XPath locator for the login button
    login_button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    
    # XPath locator for the logout dropdown 
    logout_dropdown_locator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span'
    
    # XPath locator for the logout button within the dropdown
    logout_button_locator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'
