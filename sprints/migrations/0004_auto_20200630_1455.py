# Generated by Django 2.2.13 on 2020-06-30 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0003_auto_20200630_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]