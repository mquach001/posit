from selenium import webdriver
from pages.login_page import LoginPage
from pages.new_space_page import SpacePage
from pages.project_page import ProjectsPage
from pages.ide_validate import IdePage

import datetime

# Generate a timestamp string in the format of "New Space YYYY-MM-DD HH:MM:SS"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a new instance of the Firefox browser
driver = webdriver.Firefox()

# Navigate to https://posit.cloud login page
driver.get("https://login.posit.cloud/login")

#Login to posit.cloud
login_page = LoginPage(driver)
login_page.enter_email("email")
login_page.click_continue_button()
login_page.enter_password("password")
login_page.click_login_button()
login_page.click_cloud_button()

#Creates a space name called New Space including the timestamp
name = f" {timestamp}"

#Create a New Space
new_space_page = SpacePage(driver)
new_space_page.click_new_space_button()
new_space_page.enter_name('New Space' + name)
new_space_page.click_create_button()
new_space_page.select_new_workspace()

#Create a New Project wihin Space
project_page = ProjectsPage(driver)
project_page.select_new_project_menu()
project_page.select_rstudio()

#Verify IDE Loads
ide_page = IdePage(driver)
ide_page.ide_loads()

#Close the browser window
driver.quit()
