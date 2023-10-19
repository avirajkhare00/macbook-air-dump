from debugapp.models import NewTicket, FlockClient

import uuid
import requests
import json


class NewTicketClass:

    def __init__(self, request):

        self.request = request


    def create_new_ticket(self):


        new_uuid = uuid.uuid4()

        NewTicket.objects.create(
            flock_team_id=self.request.POST['flock_team_id'],
            name=self.request.POST['name'],
            email=self.request.POST['email'],
            contact_number=self.request.POST['contact_number'],
            customer_query=self.request.POST['query'],
            group_id=new_uuid,
        )

        flock_client = FlockClient.objects.get(team_id=self.request.POST['flock_team_id'])

        # TODO inserting code here, will move while refactoring
        # will render unique id when rendering template...

        chat_window_url = "http://52.172.216.40/chat_window/?token=" + str(new_uuid)

        data = {
            "token": flock_client.token,
            "to": flock_client.default_channel,
            "text": "Hello, new support ticket is opened by " + self.request.POST['name'],
            "attachments": json.dumps([{"title": "Chat Window", "description": "Email address: " + self.request.POST[
                'email'] + "    " + "Contact Number: " + self.request.POST['contact_number'] + "\n" + "query: " +
                                                                               self.request.POST['query'], "views": {
                "widget": {"src": chat_window_url, "width": "600", "height": "500"}}}])

        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        r = requests.post("https://api.flock.co/v1/chat.sendMessage", data=data, headers=headers)

        print r.text

        customer_response_data = {
            "status": "success",
            "token": new_uuid
        }