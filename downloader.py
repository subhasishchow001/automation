# import Module
from selenium import webdriver
import time


#opening file
with open("/home/associates/url.txt", "r") as file:
	for line in file:
      # Create Chrome Object
         def webline(user_name):
            driver = webdriver.Chrome('/home/associates/.wdm/drivers/chromedriver/linux64/109.0.5414.74/chromedriver')
            # Open the url
            driver.get('https://www.savethevideo.com/vimeo-downloader?url='+line)

            # for input area
            buttonforclick = driver.find_element_by_xpath('//*[@id="url"]')
            buttonforclick.send_keys(user_name)

            # Click on start button
            start = driver.find_element_by_class_name(
                '//button[@class="flex items-center justify-center rounded-md shadow-sm border focus:outline-none relative bg-gray-800 hover:bg-gray-900 border-transparent focus:ring-gray-500 focus:ring-2 focus:ring-offset-2 px-6 py-3 text-base text-white mt-3 sm:mt-0 w-full sm:w-auto sm:ml-3"]')
            start.click()

            #close the newly opened window
            #time delay
            time.sleep(3)
            
            driver.close()

            #pressing the download button
            download = driver.find_element_by_class_name(
                '//button[@class="flex items-center justify-center rounded-md shadow-sm border focus:outline-none relative bg-blue-500 hover:bg-blue-600 border-transparent focus:ring-blue-500 focus:ring-2 focus:ring-offset-2 px-4 py-2 text-sm text-white w-full mt-4"]')
            download.click()
            

         webline(line)
# time.sleep(600)