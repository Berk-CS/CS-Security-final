from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# URL and login credentials
url = "http://localhost:7000/home"
username = "your_username"
password = "your_password"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome('C:/Users/henez/Downloads/chromedriver_win32/chromedriver.exe')  # Update with your chromedriver path

try:
    # Open the login page
    driver.get(url)

    # Wait for username and password fields to be clickable
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    # Fill in the username and password fields
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the result (you can adjust this)
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

    # Print the current URL after login (you can add more actions here as needed)
    print("Current URL:", driver.current_url)

finally:
    # Close the browser window
    driver.quit()
