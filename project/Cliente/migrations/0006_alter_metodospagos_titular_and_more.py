# Generated by Django 5.0.4 on 2024-05-01 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_metodospagos_options_alter_pais_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodospagos',
            name='titular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.usuarios'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='pais_origen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.pais'),
        ),
    ]
