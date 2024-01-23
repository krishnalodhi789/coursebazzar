# Generated by Django 4.2.8 on 2024-01-23 12:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_datahistory_datatime_datahistory_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2024, 1, 23, 17, 45, 35, 501012))),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyhistories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 17, 45, 35, 501012)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 17, 45, 35, 501012)),
        ),
        migrations.DeleteModel(
            name='DataHistory',
        ),
        migrations.AddField(
            model_name='buyhistory',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datahistories', to='customer.course'),
        ),
    ]