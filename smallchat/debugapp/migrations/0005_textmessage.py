# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debugapp', '0004_newticket_customer_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('message_text', models.TextField(blank=True, null=True)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
    ]
