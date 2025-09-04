from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, username, password):
        """Perform login"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        """Check if login is successful by dashboard presence"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.dashboard_header)
            )
            return True
        except:
            return False
