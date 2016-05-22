# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-22 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='Content')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'equipment',
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'equipment type',
                'verbose_name_plural': 'equipment types',
            },
        ),
        migrations.CreateModel(
            name='EquipmentTypeAtProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('shared', models.BooleanField(default=b'False', verbose_name='Can be used outside of property')),
            ],
            options={
                'verbose_name': 'equipment type at property',
                'verbose_name_plural': 'equipment types at property',
            },
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('nb_required_pickers', models.IntegerField(default=3, verbose_name='Number of required pickers')),
                ('owner_present', models.BooleanField(default=b'True', verbose_name='Owner wants to be present')),
                ('owner_help', models.BooleanField(default=b'False', verbose_name='Owner wants to participate')),
                ('owner_fruit', models.BooleanField(default=b'True', verbose_name='Owner wants his share of fruits')),
                ('about', models.TextField(blank=True, max_length=1000, null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'harvest',
                'verbose_name_plural': 'harvests',
            },
        ),
        migrations.CreateModel(
            name='HarvestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=30, verbose_name='Short name')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'harvest status',
                'verbose_name_plural': 'harvest statuses',
            },
        ),
        migrations.CreateModel(
            name='HarvestYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_in_lb', models.FloatField(verbose_name='Total yield (lb)')),
            ],
            options={
                'verbose_name': 'harvest yield',
                'verbose_name_plural': 'harvest yields',
            },
        ),
        migrations.CreateModel(
            name='HistoricalHarvest',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('nb_required_pickers', models.IntegerField(default=3, verbose_name='Number of required pickers')),
                ('owner_present', models.BooleanField(default=b'True', verbose_name='Owner wants to be present')),
                ('owner_help', models.BooleanField(default=b'False', verbose_name='Owner wants to participate')),
                ('owner_fruit', models.BooleanField(default=b'True', verbose_name='Owner wants his share of fruits')),
                ('about', models.TextField(blank=True, max_length=1000, null=True, verbose_name='About')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical harvest',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=b'True', verbose_name='Is active')),
                ('trees_location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Trees location')),
                ('avg_nb_required_pickers', models.IntegerField(default=1, verbose_name='Required pickers on average')),
                ('public_access', models.BooleanField(default=b'False', verbose_name='Publicly accessible')),
                ('neighbor_access', models.BooleanField(default=b'False', verbose_name='Access to neighboring terrain if needed')),
                ('compost_bin', models.BooleanField(default=b'False', verbose_name='Compost bin closeby')),
                ('about', models.CharField(blank=True, max_length=1000, null=True, verbose_name='About')),
            ],
            options={
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='RequestForParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picker', models.EmailField(max_length=254, verbose_name='Email of contact')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone of contact')),
                ('number_of_people', models.IntegerField(default=0, verbose_name='How many people are you?')),
                ('first_time_picker', models.BooleanField(default=False, verbose_name='Is this your first pick with us?')),
                ('helper_picker', models.BooleanField(default=False, verbose_name='Can you help with equipment transportation?')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('confirmation_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Confirmed on')),
                ('showed_up', models.BooleanField(default=True, verbose_name='Showed up')),
                ('is_cancelled', models.BooleanField(default=False, verbose_name='Canceled')),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.Harvest', verbose_name='Harvest')),
            ],
            options={
                'verbose_name': 'request for participation',
                'verbose_name_plural': 'requests for participation',
            },
        ),
        migrations.CreateModel(
            name='TreeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=20, verbose_name='Name')),
                ('fruit_name', models.CharField(max_length=20, verbose_name='Fruit name')),
                ('season_start', models.DateField(blank=True, null=True, verbose_name='Season start date')),
            ],
            options={
                'verbose_name': 'tree type',
                'verbose_name_plural': 'tree types',
            },
        ),
    ]