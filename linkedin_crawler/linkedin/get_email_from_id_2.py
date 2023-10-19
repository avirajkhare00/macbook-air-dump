from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json
import time

email = "sahiba@hellomeets.com"
password = "AYUSHI2018"

driver = webdriver.Firefox(executable_path='./geckodriver')

#using tutorial - https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2


#using tutorial - https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

driver.get("https://www.linkedin.com/")

driver.find_element_by_id("login-email").send_keys(email)#your email or username here
driver.find_element_by_id("login-password").send_keys(password)# your password

driver.find_element_by_id("login-submit").click()


f = open('founder_linkedin.txt','r')

for profile_href in f.readlines():

    print profile_href

    #open the page
    driver.get(profile_href)

    driver.execute_script("document.body.style.transformOrigin = 'top left'")
    driver.execute_script("document.body.style.transform = 'scale(0.4)'")

    driver.find_element_by_class_name('pv-top-card-v2-section__link--contact-info').click()

    time.sleep(2)
    
    try:
        contact_info = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pv-contact-info__contact-link"))
        )
        
        contact_info = driver.find_elements_by_class_name('pv-contact-info__contact-link')

        for contact in contact_info:

            print contact.text
        
    except:
        
        pass
    
driver.close()
