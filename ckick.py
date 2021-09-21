from selenium import webdriver
import time
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument('--headless') 
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-data-dir=chrome-data")
options.add_argument("--incognito")




#options.binary_location = "/usr/bin/chromium"
#options.binary_location = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(chrome_options=options)
# clear all cookies in scope of session
driver.delete_all_cookies()
#time.sleep(1)
driver.get('https://www.pequediamantes.com/post/la-supergaviota')
#time.sleep(10)
all_cookies = driver.get_cookies()
print ('muestro Cookies ::')
print (all_cookies)
print ('---------------------------------')

# click submit button
submit_button = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[2]/div/div[2]/div/div[1]/article/div/div[3]/div/div[4]/button/span[2]/div')
submit_button.click()
driver.close
driver.quit()

#button = driver.find_element_by_class_name("like-button _1GlVp")
#button.click()

