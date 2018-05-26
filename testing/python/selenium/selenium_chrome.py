import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get("http://www.google.com")
#print driver.page_source.encode('utf-8')
driver.quit()
display.stop()

