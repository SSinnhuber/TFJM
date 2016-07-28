# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sscategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infos.Categorie')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='sscat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infos.Sscategorie'),
        ),
    ]
