# Generated by Django 2.2 on 2019-04-17 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190417_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 23, 54, 28, 803996), verbose_name='date published'),
        ),
    ]
