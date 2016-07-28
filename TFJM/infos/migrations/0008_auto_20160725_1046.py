# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0007_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='lien',
            name='sscat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='infos.Sscategorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lien',
            name='adresse',
            field=models.FileField(upload_to='files/'),
        ),
    ]
