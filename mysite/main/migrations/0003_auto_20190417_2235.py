# Generated by Django 2.2 on 2019-04-17 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190417_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 22, 35, 52, 428610), verbose_name='date published'),
        ),
    ]
