import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()

driver.get("https://app.createsmart.io/login")
driver.maximize_window()

#driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='mui-4']").send_keys("omar.moazzam@bssuniversal.com")

driver.find_element(By.XPATH, "//input[@id='mui-5']").send_keys("Omar@085")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
#
# '''-------View Icon-----'''
#
# driver.find_element(By.XPATH,"//*[@id='67a1e306d6d46c42d36c7cc5']/div[3]/div/button[1]").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='preview']/div/div/button[2]").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[1]/div[3]/div/button[2]").click()
# time.sleep(5)
#
# '''-------Edit Icon-----'''
#
# '''-------Edit Icon Text Component-----'''
#
# driver.find_element(By.XPATH,"//*[@id='67a1e306d6d46c42d36c7cc5']/div[3]/div/a[1]/button").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='simple-tabpanel-0']/div/div/div/div[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='confirmDeleteButton']").click()
# time.sleep(2)
#
# test= driver.find_element(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 text-right css-1s50f5r']/input[@name='left']")
# action = ActionChains(driver)
# action.double_click(on_element=test)
# action.perform()
# time.sleep(2)
# test.send_keys("a")
# test.clear()
# time.sleep(2)
# test.click()
# time.sleep(2)
# test.send_keys("100")
# time.sleep(2)
# #driver.find_element(By.XPATH,"//input[@type='number' and @name='left']").click()
# #time.sleep(3)
# #driver.find_element(By.XPATH,"//input[@type='number' and @name='left']").clear()
# #time.sleep(3)
# #driver.find_element(By.XPATH,"//input[@type='number' and @name='left']").send_keys("100")
#
# test1= driver.find_element(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 text-right css-1s50f5r']/input[@type='number' and @name='top']")
# action = ActionChains(driver)
# action.double_click(on_element=test1)
# action.perform()
# time.sleep(2)
# test1.send_keys("d")
# test1.clear()
# time.sleep(2)
# test1.click()
# time.sleep(2)
# test1.send_keys("200")
# time.sleep(2)
#
#
# #driver.find_element(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 text-right css-1s50f5r']/input[@type='number' and @name='top']").click()
# #driver.find_element(By.XPATH,"//input[@name='top']").clear()
# #time.sleep(3)
# #driver.find_element(By.XPATH,"//input[@name='top']").send_keys("100")
# #time.sleep(5)
#
# driver.find_element(By.XPATH,"//*[@id='propertise_container']/div[3]/div[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='outsetCheckbox' and @type='checkbox']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='insetCheckbox' and @type='checkbox']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='propertise_container']/div[4]/div[1]").click()
#
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='propertise_container']/div[4]/div[2]/div/div/div/div/div/div/div[3]/div/div[2]/span/input").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='propertise_container']/div[4]/div[2]/div/div/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/button").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='modal']/div/div[3]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='modal']/div/div[3]/div/div/div/div[2]/div[2]/div/div[2]/button[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='mui-component-select-backgroundSize']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/ul/li[3]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='propertise_container']/div[5]/div[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='borderShown']").click()
#
# border_width= driver.find_element(By.XPATH,"//input[@class='input' and @name='borderWidth']")
# action = ActionChains(driver)
# action.double_click(on_element=border_width)
# action.perform()
# time.sleep(2)
# border_width.send_keys("d")
# border_width.clear()
# time.sleep(2)
# border_width.click()
# time.sleep(2)
# border_width.send_keys("5")
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//*[@id='mui-component-select-borderStyle']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//li[normalize-space()='Dashed']").click()
# time.sleep(3)
# border_radius =  driver.find_element(By.XPATH,"//div[contains(@class,'unitBox row-property')]//div[1]//input[1]")
#
# #driver.find_element(By.XPATH,"//div[contains(@class,'unitBox row-property')]//div[1]//input[1]").send_keys("4")
# action = ActionChains(driver)
# action.double_click(on_element=border_radius)
# action.perform()
# time.sleep(2)
# border_radius.send_keys("d")
# border_radius.clear()
# time.sleep(2)
# border_radius.click()
# time.sleep(2)
# border_radius.send_keys("5")
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[contains(@class,'deactive')]").click()
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//*[@id='propertise_container']/div[6]/div[1]").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//div[@class='body animationControl MuiBox-root css-0']//input[@name='animationCheckbox']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@name='play']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//div[@id='mui-component-select-type']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//li[@role='option' and contains(@class, 'MuiMenuItem-root') and @aria-selected='true']").click()
# time.sleep(3)
# # driver.find_element(By.XPATH,"//button[normalize-space()='Save All Changes']").click()
# # time.sleep(15)


driver.close()
