# Generated by Django 4.0.1 on 2022-02-11 13:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultancies', '0002_alter_consultancy_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultancy',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 2, 11, 13, 44, 19, 196178, tzinfo=utc), verbose_name='recorded date'),
        ),
        migrations.AlterField(
            model_name='consultancy',
            name='f_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='faculty involved'),
        ),
    ]
