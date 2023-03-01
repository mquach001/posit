from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class IdePage:

    URL = "https://posit.cloud/content/yours?sort=name_asc"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 25)
        # self.ide = (By.XPATH, "//div[@class='ideContainer']")

        # self.ide_loads = driver.page_source

    def ide_loads(self):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='RAM']")))
        if element.is_displayed():
            print("IDE loaded")
        else:
            print("IDE not loaded")



