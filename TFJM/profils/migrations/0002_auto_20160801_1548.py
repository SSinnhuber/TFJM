# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='bio',
        ),
        migrations.AddField(
            model_name='profil',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='img',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
