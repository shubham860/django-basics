# Generated by Django 2.2 on 2019-04-17 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190417_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 23, 52, 32, 665709), verbose_name='date published'),
        ),
    ]
