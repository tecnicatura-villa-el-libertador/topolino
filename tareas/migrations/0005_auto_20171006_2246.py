# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-06 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0004_tarea_asignado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='asignado',
            field=models.TextField(default='Sin Asignacion', max_length=20),
        ),
    ]
