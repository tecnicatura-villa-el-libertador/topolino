# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-16 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_auto_20170707_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='manual',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('Invalido', 'Invalido'), ('En curso', 'En curso'), ('Pendiente', 'Pendiente'), ('Finalizado', 'Finalizado')], default='Pendiente', max_length=15),
        ),
    ]
