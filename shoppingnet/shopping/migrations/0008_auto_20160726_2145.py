# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tele',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderform',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='orderform',
            name='message',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='orderform',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderform',
            name='tele',
            field=models.IntegerField(default=0),
        ),
    ]
