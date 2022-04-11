import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# print(webdriver)
# os.environ['PATH'] += r"C:/Users/pin-d/Desktop/drivers/chromedriver"
driver = webdriver.Chrome(executable_path=r"C:/Users/pin-d/Desktop/drivers/chromedriver.exe")

driver.implicitly_wait(30) # Waits for 30 seconds but stops when it finds it
# Getting element
driver.get("https://jqueryui.com/progressbar/#download")
button = driver.find_element(By.CSS_SELECTOR,'#downloadButton')
print(button)
button.click()

