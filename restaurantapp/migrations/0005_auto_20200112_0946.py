# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-12 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0004_auto_20200111_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='category',
            new_name='cuisines',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='details',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='currency',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tablebooking',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
