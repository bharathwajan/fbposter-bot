from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import os
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

chromedriver="C:/Users/rbw19/Downloads/chromedriver_win32 (2)/chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications");
chrome_options.add_experimental_option("prefs", { \
	"profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
  })

driver = webdriver.Chrome(chromedriver,options=chrome_options)
driver.maximize_window()  
driver.get('https://facebook.com')

print('entering into facebook')

username=driver.find_element_by_id('email')
username.send_keys(os.environ["facebook_mail"])
print('username entered successfully')

password=driver.find_element_by_id('pass')
password.send_keys(os.environ["facebook_pass"])
print('password entered successfully')

loginbutton=driver.find_element_by_xpath('//button[@name="login"]')
loginbutton.click()
print('login button has been clicked')

# home=driver.find_element_by_xpath('//a[@class="_2s25"]').click()

time.sleep(5)

print('in homepage now')

time.sleep(5)


driver.find_element_by_xpath('//*[@class="oajrlxb2 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x i1ao9s8h esuyzwwr f1sip0of abiwlrkh p8dawk7l lzcic4wl bp9cbjyn b3i9ofy5 orhb3f3m czkt41v7 fmqxjp7s emzo65vh j83agx80 btwxx1t3 buofh1pr jifvfom9 l9j0dhe7 idiwt2bm kbf60n1y cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq"]').click()

print('text area is selected')

time.sleep(5)
driver.find_element_by_xpath('//*[@class="_1mf _1mj"]').send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")


print('phrase send successfully')

time.sleep(10)

print('sleep is complete ')

driver.find_element_by_xpath('//*[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5"]').click()

    
print('success')


