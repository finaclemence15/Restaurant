# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_resto_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='resto_info',
            name='resto_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.Restaurant'),
            preserve_default=False,
        ),
    ]
