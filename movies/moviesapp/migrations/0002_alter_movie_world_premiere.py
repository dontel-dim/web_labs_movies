# Generated by Django 5.1.7 on 2025-03-24 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date.today, verbose_name='Премьера в мире'),
        ),
    ]
