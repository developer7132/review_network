# Generated by Django 3.0.4 on 2020-03-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='earning',
            field=models.FloatField(default=10),
        ),
    ]