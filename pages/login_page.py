from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.email_field = (By.NAME, "email")
        self.password_field = (By.NAME, "password")
        self.continue_button = (By.XPATH, "//button[contains(.,'Continue')]")
        self.login_button = (By.XPATH, "//button[contains(.,'Log In')]")
        self.cloud_button = (By.XPATH, "/html/body/div/div/div[1]/div/div/div[1]/div/a[1]")



    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.email_field)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def click_cloud_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cloud_button)).click()