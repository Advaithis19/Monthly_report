# Generated by Django 4.0.1 on 2022-02-12 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_alter_workshop_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 12, 10, 44, 28, 285595, tzinfo=utc), verbose_name='recorded date'),
        ),
    ]
