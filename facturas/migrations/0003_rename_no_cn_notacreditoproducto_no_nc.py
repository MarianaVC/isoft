# Generated by Django 5.1 on 2024-09-02 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facturas", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notacreditoproducto",
            old_name="no_cn",
            new_name="no_nc",
        ),
    ]
