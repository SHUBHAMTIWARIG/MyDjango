# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20170429_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 29, 12, 28, 55, 374121, tzinfo=utc)),
        ),
    ]
