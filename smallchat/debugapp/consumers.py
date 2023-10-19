from channels import Group
from channels.sessions import channel_session
from debugapp.core.message_to_db import send_data_db
import json
from rq import Queue
from worker import conn

# Create your views here.

q = Queue(connection=conn)

from models import NewTicket

@channel_session
def ws_connect(message):

    #below we will make a get request at same place to get same channel id and will open it :)

    token = message['query_string'].split('=')[1]

    if NewTicket.objects.filter(group_id=token).exists():

        label = token
        message.reply_channel.send({"accept": True})
        Group(label).add(message.reply_channel)
        message.channel_session['label'] = label


@channel_session
def ws_receive(message):

    label = message.channel_session['label']
    data = json.loads(message['text'])

    #queuing job here to reduce time delay to save in db
    q.enqueue(send_data_db, {'message':data['message'], 'user': data['user'], 'token':data['token']})

    Group(label).send({'text' : json.dumps({'message':data['message'], 'user': data['user']})})


@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group(label).discard(message.reply_channel)