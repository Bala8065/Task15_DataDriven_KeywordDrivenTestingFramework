import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Setup and teardown of WebDriver"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()
