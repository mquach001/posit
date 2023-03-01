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
Download Pycharm IDE
https://www.jetbrains.com/pycharm/download/#section=windows
* Run and install
* Open up Pycharm
* File -> Open directory of project
* Configure Python interpreter
* File -> Setting -> Build, Execution, Deployment -> Console -> Python Console 
![python_interpreter](https://user-images.githubusercontent.com/8264480/222023473-913801f3-5d03-42e7-86c3-a4d601a725a3.JPG)
* Right click posit_test.py and select Run posit_test.py 
![running_test](https://user-images.githubusercontent.com/8264480/222024113-043f9c7f-1be5-4ffd-9310-e67e5626c6ad.JPG)





