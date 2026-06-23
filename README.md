# qa-intern-task
Automated E2E login test using python and selenium for QA Intern application.

This repository contains my submission for the QA Test Intern position. The script automates a simple end to end (E2E) login test using Python and Selenium WebDriver

##Task Overview
The script performs the following actions:
1. Opens the browser and navigates to the Practice Test Automation demo site.
2. Locates the username, password and submit button elements using their `ID` tags.
3. Inputs the demo credentials and clicks submit.
4. Utilizes an Explicit Wait (`WebDriverWait`) to ensure the next page loads fully.
5. Asserts that the "Logged In Successfully" message is displayed on the screen.
6. Closes the browser automatically.

## Prerequisites
To run this script on your local machine, you will need:
* Python 3.x installed
* Selenium package installed

## How to Run
1. Clone or download this repository.
2. Open your terminal and install Selenium if you haven't already :
   `pip install selenium`
3. Run the script:
   `python test_login.py`

If successful the terminal will output : `QA Test Passed: Form filled and success message verified`


   
