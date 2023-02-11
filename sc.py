# import Module
from selenium import webdriver

# Create Chrome Object
driver = webdriver.Chrome('/home/associates/.wdm/drivers/chromedriver/linux64/109.0.5414.74/chromedriver')
# with open("/home/associates/Uji.txt", "r") as file:
# 	for line in file:
# 		print(line)
# 		time.sleep(1)

def webline(user_name, pass_word):
	
	# Open the url
	driver.get('https://junior.wordpress.demo.rnjcs.in/advert-media/wp-admin')

	# Username for
	username = driver.find_element_by_xpath('//*[@id="user_login"]')
	username.send_keys(user_name)

	# Password for login
	password = driver.find_element_by_xpath('//*[@id="user_pass"]')
	password.send_keys(pass_word)

	# Click on signin button
	signin = driver.find_element_by_xpath(
		'//*[@id="wp-submit"]')
	signin.click()


webline("admin", "admin123@#$")
