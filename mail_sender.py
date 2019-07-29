from selenium import webdriver
import time
# if chromedriver is not in your path, you’ll need to add it here
 
browser  = webdriver.Chrome()

browser.get('http://gmail.com')
browser.implicitly_wait(10)
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('login_id')
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(2)
passwordElem = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

passwordElem.send_keys('password')
signinButton = browser.find_element_by_id('passwordNext')
signinButton.click()
browser.implicitly_wait(25)
taskElem = browser.find_element_by_xpath('//*[@id=":aw"]/div/div')
taskElem.click()
time.sleep(4)
taskElem = browser.find_element_by_xpath('//*[@id=":gb"]')
taskElem.send_keys('whom_to_send.com')
taskElem = browser.find_element_by_xpath('//*[@id=":ft"]')
taskElem.send_keys('This is Subject')

taskElem = browser.find_element_by_xpath('//*[@id=":gy"]')
taskElem.send_keys('Hi, How are you?')

taskElem = browser.find_element_by_xpath('//*[@id=":fj"]')
taskElem.click()









                   

