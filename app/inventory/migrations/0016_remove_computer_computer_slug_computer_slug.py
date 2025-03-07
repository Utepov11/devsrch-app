# Generated by Django 5.1.2 on 2024-11-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0015_remove_printer_printer_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="computer",
            name="computer_slug",
        ),
        migrations.AddField(
            model_name="computer",
            name="slug",
            field=models.SlugField(blank=True, unique=True, verbose_name="URL"),
        ),
    ]
