# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_bill_maid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='additional_info',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
