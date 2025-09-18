import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()

driver.get("https://app.createsmart.io/login")
driver.maximize_window()

#driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='mui-4']").send_keys("omar.moazzam@bssuniversal.com")

driver.find_element(By.XPATH, "//input[@id='mui-5']").send_keys("Omar@085")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)


# Dummy pytest test case
def test_dummy():
    assert True
