# Generated by Django 5.1.2 on 2024-11-25 17:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0013_computer_added_by_printer_added_by"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="computer",
            name="computer_slug",
            field=models.SlugField(
                blank=True, max_length=9, unique=True, verbose_name="URL"
            ),
        ),
        migrations.AddField(
            model_name="printer",
            name="printer_slug",
            field=models.SlugField(
                blank=True, max_length=9, unique=True, verbose_name="URL"
            ),
        ),
        migrations.AlterField(
            model_name="computer",
            name="added_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="printer",
            name="added_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="printers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
