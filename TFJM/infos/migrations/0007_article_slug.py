# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0006_sscategorie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
