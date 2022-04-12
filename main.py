import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# print(webdriver)
# os.environ['PATH'] += r"C:/Users/pin-d/Desktop/drivers/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(30) # Waits for 30 seconds but stops when it finds it
# Getting element
driver.get("https://jqueryui.com/progressbar/#download")

try:
   no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
   no_button.click()
except:
   print('No element found')
button = driver.find_element(By.CSS_SELECTOR,'#downloadButton')
print(button)
button.click()

