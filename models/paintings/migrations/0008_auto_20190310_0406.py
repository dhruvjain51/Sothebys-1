# Generated by Django 2.1 on 2019-03-10 04:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0007_auto_20190310_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 10, 4, 6, 54, 68110, tzinfo=utc)),
        ),
    ]
