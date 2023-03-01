from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.popup_menu = (By.XPATH, "//div[@class='popupButtonAndMenuContainer']")
        self.select_project_button = (By.XPATH, "//span[contains(.,\'New Project\')]")
        # self.select_rstudio = (By.XPATH, "//button[@class='action newRStudioProject']")


    def select_new_project_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.select_project_button)).click()

    def select_rstudio(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='action newRStudioProject']"))).click()

    def getURL(self):
        return self.driver.current_url

