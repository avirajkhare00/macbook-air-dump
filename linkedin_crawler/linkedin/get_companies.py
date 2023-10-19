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

import csv

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

location = '["in:7127"]'
keywords = 'Product Manager'

BASE_URL = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'

url_params = {
    'facetGeoRegion' : location,
    'facetNetwork' : '["F"]',
    'keywords' : keywords,
    'origin' : 'FACETED_SEARCH'
}

#driver = webdriver.Firefox(executable_path='./geckodriver')
driver = Firefox(executable_path='./geckodriver')

#using tutorial - https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

driver.get("https://angel.co/login")

driver.find_element_by_id("user_email").send_keys(email)#your email or username here
driver.find_element_by_id("user_password").send_keys(password)# your password

driver.find_element_by_class_name("c-button--blue").click()

#above one is my connections recent only

driver.get("https://angel.co/jobs#find/f!%7B%22locations%22%3A%5B%221904-Bengaluru%2C%20Karnataka%22%5D%2C%22markets%22%3A%22E-Commerce%22%7D")

time.sleep(5)

retries = 0

SCROLL_PAUSE_TIME = 4

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        if retries >= 5:
            break
        else:
            retries = retries + 1
    last_height = new_height

all_elements = driver.find_elements_by_class_name('header-info')

all_startup_links = driver.find_elements_by_class_name('startup-link')

all_taglines = driver.find_elements_by_class_name('tagline')

print len(all_elements)

counter = 0

fields = ['name','description','url']

csv_data = []

for i in all_startup_links:

    print i.text
    print i.get_attribute('href')
    print all_taglines[counter].text

    csv_data.append({
        'name' : i.text.encode('utf-8'),
        'description' : all_taglines[counter].text.encode('utf-8'),
        'url' : i.get_attribute('href').encode('utf-8')
    })

    counter = counter + 1



with open('angelist_data_ecommerce.csv','w') as csvfile:

    # creating a csv writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields)
      
    # writing the header 
    writer.writeheader()

    writer.writerows(csv_data)

driver.close()

"""

#select page range blow
for i in range(1,100):

    counter = 0

    driver.get(BASE_URL)

    driver.implicitly_wait(2) # seconds

    #driver.execute_script("document.body.style.transform = 'scale(0.1)'")

    element = driver.find_element_by_class_name('mn-connection-card__name')
    #element.location_once_scrolled_into_view

    time.sleep(2)

    elements = driver.find_elements_by_class_name('search-result__info')

    print len(elements)

    for e in elements:

        link_href = e.find_element_by_css_selector('a').get_attribute('href')

        print link_href

        #open the page
        driver.get(link_href)

        time.sleep(2)

        driver.execute_script("document.body.style.transform = 'scale(0.4)'")

        driver.find_element_by_class_name('pv-top-card-v2-section__contact-info').click()

        time.sleep(2)

        contact_info = driver.find_elements_by_class_name('pv-contact-info__contact-link')

        for contact in contact_info:

            print contact.text

        #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')


driver.close()

"""