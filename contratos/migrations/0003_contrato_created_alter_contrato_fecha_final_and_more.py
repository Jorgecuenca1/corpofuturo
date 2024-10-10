# Generated by Django 5.0.6 on 2024-06-01 03:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contratos", "0002_alter_contrato_fecha_final_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contrato",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contrato",
            name="fecha_final",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="contrato",
            name="fecha_inicio",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
