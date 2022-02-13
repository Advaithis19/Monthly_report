# Generated by Django 3.2.8 on 2022-02-13 08:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0002_alter_patent_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 13, 8, 18, 47, 591557, tzinfo=utc), verbose_name='recorded date'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='title'),
        ),
    ]
