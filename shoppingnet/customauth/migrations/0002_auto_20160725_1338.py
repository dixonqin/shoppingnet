# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_shop',
            field=models.BooleanField(default=False),
        ),
    ]
