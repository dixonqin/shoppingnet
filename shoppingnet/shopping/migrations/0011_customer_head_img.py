# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_remove_customer_head_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='head_img',
            field=models.ImageField(blank=True, default='img/no_img.jpg', null=True, upload_to='img'),
        ),
    ]
