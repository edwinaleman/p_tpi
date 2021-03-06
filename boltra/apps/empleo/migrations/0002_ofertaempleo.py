# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('empleo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfertaEmpleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numPuestos', models.IntegerField()),
                ('tipoContrato', models.CharField(max_length=50)),
                ('nivelExperiencia', models.CharField(max_length=25)),
                ('genero', models.CharField(max_length=15)),
                ('edadMin', models.IntegerField()),
                ('edadMax', models.IntegerField()),
                ('salarioMax', models.IntegerField()),
                ('salarioMim', models.IntegerField()),
                ('depResidencia', models.CharField(max_length=50)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleo.Carrera')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Empresa')),
            ],
        ),
    ]
