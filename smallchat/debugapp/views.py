# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from models import FlockClient, NewTicket, TextMessage
from django.core import serializers
from core.get_details import get_team_info, get_channel_list
from core.request_maker import request_maker
from core.token_decoder import TokenDecoder

from core.event_listener_class import FlockEventListener
from core.new_ticket import NewTicketClass

import requests
import json
import uuid

from rq import Queue
from worker import conn

# Create your views here.

q = Queue(connection=conn)

#TODO ChannelMember missing

# Create your views here.

class EventListenerClass(APIView):

    def get(self, request):

        return Response(status=status.HTTP_200_OK, template_name=None)

    def post(self, request):

        if request.data['name'] == "app.install":

            FlockEventListener(request).app_install()

            #scheduling job to get team id as of now, additional details later
            #q.enqueue(request_maker, "http://127.0.0.1:8001/get_team_details/", "GET", {"Content-Type": "application/x-www-form-urlencoded"}, {"token":request.data['token']})

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


class SaveToDb(APIView):

    def post(self, request):

        print request.data

        TextMessage.objects.create(
            token=request.data['token'],
            message_text=request.data['message'],
            user=request.data['user']
        )

        return Response(status=status.HTTP_200_OK)

class ReteriveMessage(APIView):

    def post(self, request):

        if TextMessage.objects.filter(token=request.data['token']).exists():

            messages = serializers.serialize("json", TextMessage.objects.filter(token=request.data['token']))

            return Response(status=status.HTTP_200_OK, data=messages)

        else:

            #this is fresh chat
            return Response(status=status.HTTP_200_OK, data=None)


class EventListenerPostback(APIView):

    def get(self, request):

        if 'flockEventToken' in request.query_params.keys():

            user_id = TokenDecoder(request.query_params['flockEventToken']).decode_token()

            user_token = FlockClient.objects.get(user_id=user_id['userId']).token

            team_info = json.loads(get_team_info(user_token))

            channel_list = json.loads(get_channel_list(user_token))

            return render(request, 'html/config.html', {
                'team_details' : team_info,
                'channels' : channel_list
            })

        if 'selectedPage' in request.query_params.keys():

            team_id = FlockClient.objects.get(team_id=request.query_params['teamId'])
            team_id.default_channel = request.query_params['selectedPage']
            team_id.save()

            return Response(status=status.HTTP_200_OK, data="Thank You")

        else:

            return Response(status=status.HTTP_200_OK)

class GetTeamDetails(APIView):

    def get(self, request):
        #will make more conditions and functions according to later needs
        get_team_info(request.query_params['token'])
        return Response(status=status.HTTP_200_OK)

class WidgetView(APIView):

    @xframe_options_exempt
    def get(self, request):

        return render(request, 'html/chat_window.html', {
            "token" : request.query_params['token']
        })


class NewTicketView(APIView):

    def post(self, request):

        NewTicketClass(request).create_new_ticket()

        return Response(status=status.HTTP_200_OK, template_name=None, data=customer_response_data)



#will remove this class later
class MessagePort(APIView):

    def post(self, request):

        return Response(status=status.HTTP_200_OK, data="No use")
