import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(autouse=True)
def driver():
  driver=WebDriver()
  driver.maximize_window()
  driver.get("https://letcode.in/test")
  yield driver
  driver.quit()

