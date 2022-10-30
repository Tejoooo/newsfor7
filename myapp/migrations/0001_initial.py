# Generated by Django 4.1 on 2022-10-29 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=30)),
            ],
        ),
    ]
