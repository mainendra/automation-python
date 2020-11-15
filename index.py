from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = 'https://m-loginpage.surge.sh/'

def successLoginEntry():
    driver.get(url)
    username = driver.find_element_by_id('inputUsername')
    password = driver.find_element_by_id('inputPassword')
    username.send_keys('hello')
    password.send_keys('hello')

def errorLoginEntry():
    driver.get(url)
    username = driver.find_element_by_id('inputUsername')
    password = driver.find_element_by_id('inputPassword')
    username.send_keys('hello')
    password.send_keys('world')

def printMessage():
    print(driver.find_element_by_id('message').text)

successLoginEntry()
submitBtn = driver.find_element_by_tag_name('button')
time.sleep(1)
submitBtn.click()

time.sleep(1)
printMessage();

successLoginEntry()
password = driver.find_element_by_id('inputPassword')
time.sleep(1)
password.send_keys(Keys.RETURN)

time.sleep(1)
printMessage();

errorLoginEntry()
submitBtn = driver.find_element_by_tag_name('button')
time.sleep(1)
submitBtn.click()

time.sleep(1)
printMessage();

errorLoginEntry()
password = driver.find_element_by_id('inputPassword')
time.sleep(1)
password.send_keys(Keys.RETURN)

time.sleep(1)
printMessage();

# Exit browser after 1 sec
time.sleep(1)
driver.quit()
