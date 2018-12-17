import time
import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.python.org')

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()





