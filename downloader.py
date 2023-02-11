# import Module
from selenium import webdriver
import time

# Create Chrome Object

# driver = webdriver.Chrome('/home/associates/.wdm/drivers/chromedriver/linux64/109.0.5414.74/chromedriver')
with open("/home/associates/url.txt", "r") as file:
    lines=file.readlines()
    count=0
    for line in lines:
        count +=1
        print (line)


#   for line in file:
#       print(line)
# time.sleep(1)

# def webline(user_name):
    
    # Open the url
    # driver.get('https://www.savethevideo.com/vimeo-downloader')

    # Username for
    # username = driver.find_element_by_xpath('//*[@id="url"]')
    # username.send_keys(user_name)

    # Password for login
    # password = driver.find_element_by_xpath('//*[@id="user_pass"]')
    # password.send_keys(pass_word)

    # Click on signin button
    # signin = driver.find_element_by_xpath(
    #     '//*[@id="wp-submit"]')
    # signin.click()


# webline(line)

    
