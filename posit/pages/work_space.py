import select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class WorkSpace:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.select_project_button = (By.XPATH, "//span[contains(.,\'New Project\')]")

    def enter_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.name_field)).send_keys(name)


    def select_new_project_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.select_project_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.select_rstudio)).click()

