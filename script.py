import time
from selenium import webdriver

# Create a list of dictionaries containing the account details
accounts = [
    {"username": "account1@gmail.com", "password": "current_password1"},
    {"username": "account2@gmail.com", "password": "current_password2"},
    {"username": "account3@gmail.com", "password": "current_password3"},
]

# Set the new password for all accounts
new_password = "new_password"

# Initialize the web driver
driver = webdriver.Chrome()

# Loop through the accounts and change their passwords
for account in accounts:
    # Open the Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the page to load
    time.sleep(2)

    # Enter the account details and log in
    driver.find_element_by_name("username").send_keys(account["username"])
    driver.find_element_by_name("password").send_keys(account["password"])
    driver.find_element_by_css_selector("button[type='submit']").click()

    # Wait for the page to load
    time.sleep(2)

    # Navigate to the change password page
    driver.get("https://www.instagram.com/accounts/password/change/")

    # Wait for the page to load
    time.sleep(2)

    # Enter the current and new passwords and submit the form
    driver.find_element_by_name("old_password").send_keys(account["password"])
    driver.find_element_by_name("new_password1").send_keys(new_password)
    driver.find_element_by_name("new_password2").send_keys(new_password)
    driver.find_element_by_css_selector("button[type='submit']").click()

    # Wait for the password to be changed
    time.sleep(2)

# Close the web driver
driver.quit()
