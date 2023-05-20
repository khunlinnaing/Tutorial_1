# Generated by Django 4.2.1 on 2023-05-18 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('joined_date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 18, 4, 11, 57, 91487))),
            ],
        ),
    ]
