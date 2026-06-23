from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login():
    #Initializing the WebDriver (Chrome)
    print("Opening Browser...")
    driver = webdriver.Chrome()

    try:
        #Opening the demo site specifically made for practice automation
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # locating the form elements using their IDs
        print("Locating elements...")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        #Fill the form with required demo credentials
        print("Entering Credentials")
        username_field.send_keys("student")
        password_field.send_keys("Password123")

        #Submit the form
        submit_button.click()
        
        print("Waiting for the next page to load")
        success_message_locator = (By.CLASS_NAME, "post-title")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(success_message_locator))

        #Extract the text from success_message
        success_message = driver.find_element(*success_message_locator).text

        #Assert the success message
        assert "Logged In Successfully" in success_message
        print("QA Test Passed: Form filled and success message verified")

    finally:
        #close the browser completely
        driver.quit()

if __name__ == "__main__":
    test_successful_login()
