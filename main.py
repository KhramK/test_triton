
from selenium import webdriver

import Basket
import Registration

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

Registration.run_all_test(driver)
Basket.run_all_test(driver)
