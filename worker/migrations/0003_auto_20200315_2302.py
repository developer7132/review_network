# Generated by Django 3.0.4 on 2020-03-15 23:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_auto_20200315_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='date_joined',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='worker',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='worker',
            name='status',
            field=models.CharField(default='deactive', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='bitcoin_address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
