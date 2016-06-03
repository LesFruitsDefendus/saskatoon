# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_fr',
            field=models.CharField(max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='name_fr',
            field=models.CharField(max_length=150, null=True, verbose_name='Name'),
        ),
    ]
