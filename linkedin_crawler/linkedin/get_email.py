#here we will have email, current profession and linkedin id
#we will use linkedin id to do following tasks
#if linkedin id is already present in server's db then do not crawl it
#if linkedin id is already present in server's db then no need to send that person a connection request.

#from selenium import webdriver
from seleniumrequests import Firefox
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

location = '["in:7151","in:7392","in:7391"]'
keywords = 'blockchain'

BASE_URL = 'https://www.linkedin.com/search/results/people/'

url_params = {
    'facetGeoRegion' : location,
    'facetNetwork' : '["F"]',
    'keywords' : keywords,
    'origin' : 'FACETED_SEARCH'
}

#driver = webdriver.Firefox(executable_path='./geckodriver')
driver = Firefox(executable_path='/Users/avirajkhare00/hellomeets/linkedin_crawler/linkedin/geckodriver')

#using tutorial - https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

driver.get("https://www.linkedin.com/")

driver.find_element_by_id("login-email").send_keys(email)#your email or username here
driver.find_element_by_id("login-password").send_keys(password)# your password

driver.find_element_by_id("login-submit").click()

#above one is my connections recent only

#select page range blow
for i in range(1,600):

    counter = 0

    driver.get(BASE_URL + '?' + urllib.urlencode(url_params)+'&page=' + str(i))

    driver.implicitly_wait(2) # seconds

    driver.execute_script("document.body.style.transformOrigin = 'top left'")
    driver.execute_script("document.body.style.transform = 'scale(0.1)'")

    #element = driver.find_element_by_class_name('mn-connection-card__name')
    #element.location_once_scrolled_into_view

    time.sleep(2)

    elements = driver.find_elements_by_class_name('search-result__info')

    print len(elements)

    for e in elements:

        link_href = e.find_element_by_css_selector('a').get_attribute('href')

        print link_href

        #open the page
        #driver.get(link_href)

        #time.sleep(2)

        #driver.execute_script("document.body.style.transform = 'scale(0.4)'")

        #driver.find_element_by_class_name('pv-top-card-v2-section__contact-info').click()

        #time.sleep(2)

        #contact_info = driver.find_elements_by_class_name('pv-contact-info__contact-link')

        #for contact in contact_info:

            #print contact.text

        #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')


driver.close()