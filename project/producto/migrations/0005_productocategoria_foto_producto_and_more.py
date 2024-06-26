# Generated by Django 5.0.4 on 2024-05-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_productocategoria_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='productocategoria',
            name='foto_producto',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='productocategoria',
            name='fecha',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Última actualización'),
        ),
    ]
