# Generated by Django 4.2.8 on 2024-01-23 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_amounttransitionhistory_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 17, 45, 57, 512257)),
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 17, 45, 57, 512257)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 17, 45, 57, 512257)),
        ),
    ]
