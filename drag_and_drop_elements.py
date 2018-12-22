import time
import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('http://jqueryui.com/droppable')
driver.switch_to.frame(0)

action_chains= ActionChains(driver)

source= driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')
action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)

action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()
