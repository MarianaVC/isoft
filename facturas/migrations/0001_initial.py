# Generated by Django 5.1 on 2024-09-02 22:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Factura",
            fields=[
                (
                    "no_factura",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("fecha_factura", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="FacturaNotaCredito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty_dev", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="FacturaProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.IntegerField(default=1)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=6)),
                ("iva", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name="NotaCredito",
            fields=[
                (
                    "no_nc",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("fecha_nc", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="NotaCreditoProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.IntegerField(default=1)),
            ],
        ),
    ]
