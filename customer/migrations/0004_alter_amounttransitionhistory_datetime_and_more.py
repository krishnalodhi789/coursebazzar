# Generated by Django 4.2.8 on 2024-01-23 06:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_amounttransitionhistory_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 11, 34, 46, 645227)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 11, 34, 46, 645227)),
        ),
        migrations.AlterField(
            model_name='datahistory',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 11, 34, 46, 645227)),
        ),
        migrations.CreateModel(
            name='CourseOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.course')),
                ('saller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseoffer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]