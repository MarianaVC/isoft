# Generated by Django 5.1 on 2024-09-02 22:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("zonas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
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
                ("nombre", models.CharField(default="", max_length=400)),
                ("paterno", models.CharField(default="", max_length=400)),
                ("materno", models.CharField(default="", max_length=400)),
                ("razon_social", models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="TipoPersona",
            fields=[
                (
                    "cve_tipo_persona",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("descripcion", models.CharField(default="", max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="usuarios.persona",
                    ),
                ),
                (
                    "cve_cliente",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            bases=("usuarios.persona",),
        ),
        migrations.AddField(
            model_name="persona",
            name="cve_tipo_persona",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="usuarios.tipopersona",
            ),
        ),
        migrations.CreateModel(
            name="Vendedor",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="usuarios.persona",
                    ),
                ),
                (
                    "cve_vendedor",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "cve_zona",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zonas.zona"
                    ),
                ),
            ],
            bases=("usuarios.persona",),
        ),
    ]