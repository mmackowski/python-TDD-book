from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(capabilities=cap, executable_path="geckodriver.exe")
# browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title