import time
import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("file:///Users/alexeidudarev/Documents/Exercise%20Files%20Phyton/CH03/03_02/html_code_03_02.html")

select= Select(driver.find_element_by_name('numReturnSelect'))
select.select_by_index(4)
time.sleep(2)
select.select_by_visible_text("200")
time.sleep(2)
select.select_by_value("250")
time.sleep(2)

options = select.options
print(options)

submit_button = driver.find_element_by_name('continue')
submit_button.submit();
time.sleep(2)

driver.close()
