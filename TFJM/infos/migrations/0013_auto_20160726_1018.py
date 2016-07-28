# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0012_auto_20160725_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='lien',
            name='isLienhttp',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lien',
            name='lienhttp',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lien',
            name='adresse',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
