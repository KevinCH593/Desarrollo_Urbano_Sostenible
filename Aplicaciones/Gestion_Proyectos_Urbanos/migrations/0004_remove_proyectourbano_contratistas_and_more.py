# Generated by Django 5.1.3 on 2025-02-07 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Proyectos_Urbanos', '0003_zonaverde_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectourbano',
            name='contratistas',
        ),
        migrations.AddField(
            model_name='proyectourbano',
            name='contratista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Proyectos_Urbanos.contratista'),
        ),
    ]
