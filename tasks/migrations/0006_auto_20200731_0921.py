# Generated by Django 2.2.13 on 2020-07-31 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200731_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed', 'start_date', 'id']},
        ),
    ]