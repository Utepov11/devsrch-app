# Generated by Django 5.1.2 on 2024-12-17 09:57

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0046_alter_computer_computer_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('accessory_id', models.AutoField(primary_key=True, serialize=False)),
                ('accessory_type', models.CharField(max_length=100, verbose_name='Наименование устройства')),
                ('accessory_inventory', models.CharField(max_length=9, verbose_name='Инвентарный номер')),
                ('accessory_snumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='Серийный номер')),
                ('accessory_location', models.CharField(max_length=50, verbose_name='Расположение')),
                ('accessory_date', models.DateField(default=datetime.date.today, verbose_name='Дата добавления')),
                ('slug', models.SlugField(blank=True, max_length=9, unique=True, verbose_name='URL')),
                ('accessory_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessory', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Периферия',
                'verbose_name_plural': 'Периферия',
            },
        ),
        migrations.DeleteModel(
            name='OtherDevice',
        ),
    ]
