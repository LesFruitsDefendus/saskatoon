# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-02 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[(b'RequestForParticipation', 'Request for participation'), (b'Harvest', 'Harvest')], default='Harvest', max_length=100),
            preserve_default=False,
        ),
    ]
