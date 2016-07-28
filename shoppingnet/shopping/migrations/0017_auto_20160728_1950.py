# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 11:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0016_auto_20160728_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='Rcontent',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='comment',
            name='Rrating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='date2',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
