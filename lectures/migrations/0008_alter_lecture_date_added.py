# Generated by Django 3.2.8 on 2022-02-13 14:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0007_alter_lecture_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 13, 14, 31, 56, 825208, tzinfo=utc), verbose_name='recorded date'),
        ),
    ]
