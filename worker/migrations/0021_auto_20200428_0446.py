# Generated by Django 2.1 on 2020-04-28 04:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0020_auto_20200424_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='claimed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 4, 46, 34, 723168)),
        ),
    ]
