# Generated by Django 5.1.2 on 2024-11-24 13:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0011_device"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Device",
        ),
    ]
