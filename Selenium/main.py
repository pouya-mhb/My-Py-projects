import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

definedBrowser = webdriver.Chrome('C:/Program Files/Python36/Lib/site-packages/selenium/webdriver/chrome')

definedBrowser.get("Google.com")
#assert 'google' in definedBrowser.title

element = definedBrowser.find_element_by_name('p')
element.send_keys('mhb'+ Keys.RETURN)

definedBrowser.quit()

