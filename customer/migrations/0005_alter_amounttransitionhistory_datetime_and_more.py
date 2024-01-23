# Generated by Django 4.2.8 on 2024-01-23 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_amounttransitionhistory_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 12, 0, 21, 430506)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 12, 0, 21, 430506)),
        ),
        migrations.AlterField(
            model_name='courseoffer',
            name='offer',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='datahistory',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 12, 0, 21, 430506)),
        ),
    ]