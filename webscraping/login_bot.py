#this code amulates a human accesing and filling forms and clicking the page
#for some reason for working with the below module we must import it like shown below
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
browser.get("https://login.five9.com/")
print(browser)
#the send_keys() module allows to fill the form with desired information
user = browser.find_element_by_id("username")
user.send_keys("esantana@thedealersupport.com")
password = browser.find_element_by_id('password')
password.send_keys("wAtEr6007-19E")
log_button = browser.find_element_by_id('loginBtn')
log_button.click()
reports = browser.find_element_by_id('app_reports_span')
reports.click()