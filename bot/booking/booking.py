from selenium import webdriver
import booking.constants as const

class Booking(webdriver.Chrome):
   def __init__(self, driver_path=const.DRIVER_PATH):
      self.driver_path = driver_path
      super(Booking, self).__init__()

   def land_first_page(self):
      self.get(const.BASE_URL)