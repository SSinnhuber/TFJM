# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0003_categorie_side_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='side_image',
        ),
        migrations.AddField(
            model_name='categorie',
            name='image',
            field=models.ImageField(default=1, upload_to='media/photos/'),
            preserve_default=False,
        ),
    ]