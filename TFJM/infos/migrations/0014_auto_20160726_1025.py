# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0013_auto_20160726_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]