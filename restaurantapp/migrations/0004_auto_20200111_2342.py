# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0003_resto_info_resto_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resto_info',
            name='location',
        ),
        migrations.RemoveField(
            model_name='resto_info',
            name='resto_name',
        ),
        migrations.DeleteModel(
            name='Resto_info',
        ),
    ]