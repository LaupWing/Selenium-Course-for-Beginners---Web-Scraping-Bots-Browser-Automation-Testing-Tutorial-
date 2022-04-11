import os
from selenium import webdriver

# print(webdriver)
# os.environ['PATH'] += r"C:/Users/pin-d/Desktop/drivers/chromedriver"
driver = webdriver.Chrome(executable_path=r"C:/Users/pin-d/Desktop/drivers/chromedriver.exe")

# Getting element
driver.get("https://www.seleniumeasy.com/")
button = driver.find_element_by_css_selector('.btn.btn-success')
print(button)
button.click()

