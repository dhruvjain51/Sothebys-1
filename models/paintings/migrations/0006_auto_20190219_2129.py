# Generated by Django 2.1 on 2019-02-19 21:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0005_auto_20190219_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
