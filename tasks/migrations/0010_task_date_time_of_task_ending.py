# Generated by Django 3.1.2 on 2021-04-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20210416_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_time_of_task_ending',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
