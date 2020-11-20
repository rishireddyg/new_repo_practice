from selenium import webdriver
from getpass import getpass

usr=input('Enter your User Name or Email Id : ')
pwd= getpass('Enter your Password : ')

driver = webdriver.Chrome("https://sites.google.com/a/chromium.org/chromedriver/home")
driver.get('https://www.facebook.com/')

username_box= driver.find_element_by_id('email')
username_box.send_keys(usr)

username_box= driver.find_element_by_id('pass')
username_box.send_keys(pwd)

login_btn= driver.find_element_by_id(u_0_b)
login_btn.submit()
