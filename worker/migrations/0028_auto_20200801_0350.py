# Generated by Django 2.1 on 2020-08-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0027_auto_20200801_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='purchased_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='claimed_date',
            field=models.DateTimeField(),
        ),
    ]
