# Generated by Django 4.2.8 on 2024-01-24 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_alter_amounttransitionhistory_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('key_points', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 36, 25, 197477)),
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 36, 25, 197477)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 36, 25, 197477)),
        ),
        migrations.AlterField(
            model_name='salehistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 36, 25, 197477)),
        ),
    ]