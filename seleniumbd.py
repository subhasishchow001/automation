import os
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

username="admin"
password="admin123@#$"
time.sleep(3)
opts = webdriver.ChromeOptions()
opts.headless =True
# chromedriver="/usr/lib/chromium-browser/chromedriver.exe"
# driver = webdriver.Chrome(chromedriver)
# print(driver)
# os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

search_url="https://junior.wordpress.demo.rnjcs.in/advert-media/wp-login.php?redirect_to=https%3A%2F%2Fjunior.wordpress.demo.rnjcs.in%2Fadvert-media%2Fwp-admin%2F%3Flanguage%3Den%26c%3Dwp-admin&reauth=1" 
# print(search_url)
# print(username,password)
# exit()
driver.navigate().to(search_url)
driver.find_element_by_id('user_login').send_keys(username)
driver.find_element_by_id('user_pass').send_keys(password)
driver.find_element_by_id("wp-submit").submit()
driver.forward()
print(driver.requests())
