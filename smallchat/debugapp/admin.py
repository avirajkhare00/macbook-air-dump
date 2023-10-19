# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import FlockClient, NewTicket, TextMessage

# Register your models here.

admin.site.register(FlockClient)
admin.site.register(NewTicket)
admin.site.register(TextMessage)