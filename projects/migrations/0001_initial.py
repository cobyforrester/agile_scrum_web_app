# Generated by Django 2.2.13 on 2020-07-01 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='AddTitle')),
                ('begin_date', models.DateField(default=datetime.date.today)),
                ('description', models.TextField(default='AddGoal')),
            ],
        ),
    ]
