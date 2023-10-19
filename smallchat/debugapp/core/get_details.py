from debugapp.models import FlockClient
import requests
import json
import time

def get_team_info(token):

    #sleep is used so that token is validated from their backend

    r = requests.get("https://api.flock.co/v1/users.getInfo", headers = {"Content-Type": "application/x-www-form-urlencoded"}, params={"token":token})

    print r.text

    if r.status_code == 200:

        if FlockClient.objects.filter(token=token).exists():
            user_info = FlockClient.objects.get(token=token)
            user_info.team_id = r.json()['teamId']
            user_info.save()

            return r.text
    else:
        return False


def get_channel_list(token):

    r = requests.get("https://api.flock.co/v1/channels.list", headers = {"Content-Type": "application/x-www-form-urlencoded"}, params={"token":token})

    if r.status_code == 200:

        return r.tex