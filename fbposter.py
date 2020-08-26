from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import os
from selenium.common.exceptions import *

chromedriver="G:\chromedriver"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", { \
	"profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
  })

driver = webdriver.Chrome(chromedriver,options=chrome_options)
driver.get('https://facebook.com')
print('entering into facebook')

username=driver.find_element_by_id('email')
username.send_keys('enter your mail address here')
print('username entered successfully')

password=driver.find_element_by_id('pass')
password.send_keys('enter your password here')
print('password entered successfully')

loginbutton=driver.find_element_by_xpath('//button[@name="login"]')
loginbutton.click()
print('login button has been clicked')

home=driver.find_element_by_xpath('//a[@class="_2s25"]').click()

time.sleep(5)

print('in homepage now')

post_box=driver.find_element_by_xpath('//textarea[@class="_3en1 _480e navigationFocus _23pl"]')
post_box.click()
print('text area is selected')

time.sleep(5)

print('sleep is complete ')

driver.switch_to_active_element().send_keys('Test sucessfull')
print('phrase send successfully')

time.sleep(10)

print('sleep is complete ')

try:
    print('inside try block')
    post_button=driver.find_element_by_xpath('//button[@class="_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]')
    post_button.click()
    
except NoSuchElementException:
    print('inside except')
    time.sleep(10)
    post_button.click()
    
print('success')


