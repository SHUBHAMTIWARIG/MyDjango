# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaways', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveaways',
            name='github_link',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
