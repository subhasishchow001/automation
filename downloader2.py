import time
with open("/home/associates/Uji.txt", "r") as file:
	for line in file:
		print(line)
		time.sleep(1)