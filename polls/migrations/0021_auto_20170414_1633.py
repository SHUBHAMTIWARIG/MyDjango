# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20170408_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 14, 11, 3, 54, 729513, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
    ]
