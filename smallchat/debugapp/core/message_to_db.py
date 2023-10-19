import requests
import json

def send_data_db(message):

    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post("http://127.0.0.1:8001/save_to_db/", data=json.dumps(message), headers=headers)

    print r.status_code
    print r.text

