# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class FlockClient(models.Model):

    team_id = models.CharField(max_length=100, null=True)
    user_id = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    user_token = models.CharField(max_length=100)
    default_channel = models.CharField(max_length=100, null=True)

    def __unicode__(self):

        return self.user_id

class NewTicket(models.Model):

    flock_team_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    group_id = models.CharField(max_length=100, null=True)
    customer_query = models.CharField(max_length=500, null=True, blank=True)
    json_data = JSONField(null=True)

    def __unicode__(self):

        return self.email


class TextMessage(models.Model):

    token = models.CharField(max_length=100)
    message_text = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=50)

    def __unicode__(self):

        return self.token

