# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 10:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170319_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 10, 19, 47, 103057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 10, 19, 47, 87430, tzinfo=utc)),
        ),
    ]
