# Generated by Django 3.1.2 on 2021-04-16 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=500),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('dateOfCreation', models.DateField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]