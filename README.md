## Posit take home assesment

**Thie repo contain the automation script for Posit's Takehome Assessment**

The assessment includes the following, these can be found in the test folder
1. posit_test.py - consist of all the test for the following:
* Create a space
* Creating a Project within the Space
* Verifying that the RStudio IDE loads
2. smoke_test - constains all the manual smoke test
* Smoke Test for posit.cloud

To run this test you will need to install the following
* **Python**
* **Selenium**

Installing Python on Windows
-
* Download Python https://www.python.org/downloads/
* Run executable on your PC

Installing Selenium on Windows
-
* pip install -U selenium

Installing Python on Mac via homebrew
-
Install Homebrew
* /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Python
* brew install python

Install Selenium
* pip install selenium

Executing the test
-
Open up a terminal
Naviate to the test folder
run the following

* python posit_test.py




