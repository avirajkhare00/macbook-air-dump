import requests
import json

def request_maker(url, request_type, headers, params):

    if request_type == 'GET':

        r = requests.get(url, headers=headers, params=params)

        if r.status_code == 200:

            print "Success: " + r.text

        else:

            print "Check " + r.text

    if request_type == 'POST':

        r = requests.get(url, headers=headers, data=params)

        if r.status_code == 200:

            print "Success: " + r.text

        else:

            print "Check " + r.text
