import os
from selenium import webdriver

# print(webdriver)
os.environ['PATH'] += r"C:/Users/pin-d/Desktop/drivers"
driver = webdriver.Chrome()