# Generated by Django 2.2.13 on 2020-07-10 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_userproject_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
    ]
