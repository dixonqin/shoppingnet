# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 08:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0006_remove_shop_is_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=200)),
                ('sex', models.CharField(default='', max_length=10)),
                ('self_intro', models.CharField(default='', max_length=300)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderform',
            old_name='user',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='user',
            new_name='customer',
        ),
    ]
