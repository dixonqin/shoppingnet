# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0002_auto_20160725_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
