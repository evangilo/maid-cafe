# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_auto_20170320_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='end_bill',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
