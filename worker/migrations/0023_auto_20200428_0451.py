# Generated by Django 2.1 on 2020-04-28 04:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0022_auto_20200428_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='claimed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 4, 51, 18, 546674, tzinfo=utc)),
        ),
    ]
