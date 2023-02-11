import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

with open("/home/associates/Uji.txt", "r") as file:
    for line in file:
        print(line)
        time.sleep(1)
    #     opts=Options()
    #     opts.set_headless()
    #     assert opts.headless
    #     browser = Chrome(options=opts)
    # browser.get('https://duckduckgo.com')
    # search_form = browser.find_element_by_id('search_form_input_homepage')
    # search_form.send_keys(line)
    # search_form.submit()
        
        ####change this#####   
    
