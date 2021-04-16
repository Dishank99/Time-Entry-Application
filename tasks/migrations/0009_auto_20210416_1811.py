# Generated by Django 3.1.2 on 2021-04-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20210416_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_time_of_task_starting',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='is_task_started',
            field=models.BooleanField(default=False),
        ),
    ]