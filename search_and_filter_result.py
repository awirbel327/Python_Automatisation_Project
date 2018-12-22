import time
import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://wiki.python.org/moin/')

elem = driver.find_element_by_id('searchinput')
elem.clear()
elem.send_keys("Beginner")
elem.send_keys(Keys.RETURN)
time.sleep(4)


select= Select(driver.find_element_by_xpath('//*/form/div/select'))
select.select_by_visible_text("Raw Text")
time.sleep(4)


driver.close()





