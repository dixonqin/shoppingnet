# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_auto_20160727_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=20)),
                ('object_name', models.CharField(choices=[('商店', '商店'), ('商品', '商品')], default='商品', max_length=4)),
                ('field_name', models.CharField(choices=[('名称', '名称'), ('类别', '类别')], default='名称', max_length=4)),
            ],
        ),
    ]
