# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0008_auto_20160725_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
    ]
