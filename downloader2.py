from selenium import webdriver
import time

class Printer:
	def fileopen(self):
		with open("/home/associates/url.txt", "r") as file:
			lines= file.readlines()
			for line in lines:
				print(line)


class Download(Printer):
	def downloader(user_name):
		driver = webdriver.Chrome('/home/associates/.wdm/drivers/chromedriver/linux64/109.0.5414.74/chromedriver')
		driver.get('https://www.savethevideo.com/vimeo-downloader')
		username = driver.find_element_by_xpath('//*[@id="url"]')
		user_name=line
		username.send_keys(user_name)


s=Download()
s.fileopen()
s.downloader()
		
		