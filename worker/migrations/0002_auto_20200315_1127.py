# Generated by Django 3.0.4 on 2020-03-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='first_name',
            field=models.CharField(default='first_name', max_length=30),
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name',
            field=models.CharField(default='last_name', max_length=30),
        ),
        migrations.AddField(
            model_name='worker',
            name='username',
            field=models.CharField(default='username', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_email',
            field=models.EmailField(max_length=254),
        ),
    ]