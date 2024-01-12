# Generated by Django 4.2.8 on 2024-01-12 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0008_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountTransitionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transitionhistory', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
