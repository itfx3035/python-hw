# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-19 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20191019_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='murl',
            name='url_alive',
            field=models.BooleanField(default=False),
        ),
    ]
