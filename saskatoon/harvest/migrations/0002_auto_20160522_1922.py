# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-22 23:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('harvest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Address', verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='property',
            name='equipment',
            field=models.ManyToManyField(through='harvest.EquipmentTypeAtProperty', to='harvest.EquipmentType', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Actor', verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='property',
            name='trees',
            field=models.ManyToManyField(to='harvest.TreeType', verbose_name='Fruit trees'),
        ),
        migrations.AddField(
            model_name='historicalharvest',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalharvest',
            name='pick_leader',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='member.Person'),
        ),
        migrations.AddField(
            model_name='historicalharvest',
            name='property',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='harvest.Property'),
        ),
        migrations.AddField(
            model_name='historicalharvest',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='harvest.HarvestStatus'),
        ),
        migrations.AddField(
            model_name='harvestyield',
            name='harvest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.Harvest', verbose_name='Harvest'),
        ),
        migrations.AddField(
            model_name='harvestyield',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Actor', verbose_name='Recipient'),
        ),
        migrations.AddField(
            model_name='harvestyield',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.TreeType', verbose_name='Tree'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='equipment_reserved',
            field=models.ManyToManyField(blank=True, to='harvest.Equipment', verbose_name='Reserve equipment'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='pick_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Person', verbose_name=b'Pick leader'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='pickers',
            field=models.ManyToManyField(blank=True, related_name='harvests', to='member.Person', verbose_name="Pickers' names"),
        ),
        migrations.AddField(
            model_name='harvest',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='harvest.Property', verbose_name='Property'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='harvest.HarvestStatus', verbose_name='Harvest status'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='trees',
            field=models.ManyToManyField(to='harvest.TreeType', verbose_name='Trees'),
        ),
        migrations.AddField(
            model_name='equipmenttypeatproperty',
            name='equipment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.EquipmentType', verbose_name='Equipment type'),
        ),
        migrations.AddField(
            model_name='equipmenttypeatproperty',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.Property', verbose_name='Property'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.EquipmentType', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='harvest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='harvest.Harvest', verbose_name='harvest'),
        ),
        migrations.AlterUniqueTogether(
            name='equipmenttypeatproperty',
            unique_together=set([('equipment_type', 'property')]),
        ),
    ]