# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 10:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20170429_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 29, 10, 30, 54, 835733, tzinfo=utc)),
        ),
    ]