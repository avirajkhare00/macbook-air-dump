from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import urllib
import time
import json

import os

email = "avirajkhare00@gmail.com"
password = "panzer000"

"""
New Delhi - '["in:7151"]'
Bengaluru - '["in:7127"]'
Chennai - '["in:6891"]'
Pune - '["in:7350"]'
Singapore - '["sg:0"]'
North West, Singapore - '["sg:10137"]'
North East, Singapore - '["sg:10136"]'
South East, Singapore - '["sg:10138"]'
South West, Singapore - '["sg:10139"]'
Central Singapore - '["sg:10135"]'
Hyderabad - '["in:6508"]'
Mumbai - '["in:7150"]'
Gurgaon - '["in:7391"]'
Noida - '["in:7392"]'
"""

location = '["in:6891"]'
keywords = 'React Developer'

BASE_URL = 'https://www.linkedin.com/search/results/people/?'

url_params = {
    'facetGeoRegion' : location,
    'facetNetwork' : '["S","O"]',
    'keywords' : keywords,
    'origin' : 'FACETED_SEARCH'
}

driver = webdriver.Firefox(executable_path='./geckodriver')

#using tutorial - https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

driver.get("https://www.linkedin.com/")

driver.find_element_by_id("login-email").send_keys(email)#your email or username here
driver.find_element_by_id("login-password").send_keys(password)# your password

driver.find_element_by_id("login-submit").click()

#https://www.linkedin.com/mynetwork/invite-connect/connections/
#above one is my connections recent only

i = 0
connect_request = 0

#select page range blow
while connect_request < 200:

    driver.get(BASE_URL + urllib.urlencode(url_params) + '&page=' + str(i))

    driver.implicitly_wait(4) # seconds

    driver.execute_script("document.body.style.transformOrigin = 'top left'")
    driver.execute_script("document.body.style.transform = 'scale(0.4)'")
    
    time.sleep(5)

    element = driver.find_element_by_class_name('nav-item__icon')
    element.location_once_scrolled_into_view

    time.sleep(2)

    elements = driver.find_elements_by_class_name('search-result__actions--primary')

    print len(elements)

    for j in range(len(elements)):

        if elements[j].text == 'Connect':

            time.sleep(1)
        
            elements[j].click()

            time.sleep(1)

            driver.find_element_by_class_name('button-secondary-large').click()

            time.sleep(1)

            driver.find_element_by_id('custom-message').send_keys('It would be pleasure to connect on Linkedin. Thank You!')

            driver.find_element_by_class_name('button-primary-large').click()

            connect_request = connect_request + 1

    i = i + 1

driver.close()

