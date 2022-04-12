from selenium import webdriver
import booking.constants as const
import os

class Booking(webdriver.Chrome):
   def __init__(self, executable_path=const.DRIVER_PATH):
      self.executable_path = executable_path
      os.environ['PATH'] += self.executable_path
      super(Booking, self).__init__()

   def land_first_page(self):
      self.get(const.BASE_URL)