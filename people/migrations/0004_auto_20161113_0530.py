# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20161113_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]