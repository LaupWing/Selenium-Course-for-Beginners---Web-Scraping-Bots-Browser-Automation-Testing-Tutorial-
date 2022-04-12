from lib2to3.pgen2 import driver
from selenium import webdriver


class Booking(webdriver.Chrome):
   def __init__(self, driver_path=r"C:/Users/pin-d/Desktop/drivers/chromedriver.exe"):
      self.driver_path = driver_path
      super(Booking, self).__init__()