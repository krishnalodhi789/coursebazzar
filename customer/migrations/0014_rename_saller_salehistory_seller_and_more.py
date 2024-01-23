# Generated by Django 4.2.8 on 2024-01-23 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_alter_amounttransitionhistory_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salehistory',
            old_name='saller',
            new_name='seller',
        ),
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 18, 15, 35, 664383)),
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 18, 15, 35, 664383)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 18, 15, 35, 664383)),
        ),
        migrations.AlterField(
            model_name='salehistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 18, 15, 35, 664383)),
        ),
    ]