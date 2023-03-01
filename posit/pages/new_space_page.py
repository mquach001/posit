from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SpacePage:
    URL = "https://posit.cloud/content/yours?sort=name_asc"


    def get_current_url(self):
        return self.driver.current_url

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.name_field = (By.XPATH, "//*[@id='name']")
        self.new_space_button = (By.XPATH, "//button[contains(.,'New Space')]")
        self.create_button = (By.XPATH, "//button[@type='submit']/span[text()='Create']")
        self.new_workspace = (By.XPATH, "//div[@class='spaceNameWithOwner']")

    def enter_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.name_field)).send_keys(name)

    def click_new_space_button(self):
        self.wait.until(EC.element_to_be_clickable(self.new_space_button)).click()

    def select_new_workspace(self):
        self.wait.until(EC.visibility_of_element_located(self.new_workspace)).click()

    def select_space(self):
        self.wait.until(EC.visibility_of_element_located(self.select_create_space)).click()

    def click_create_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()

