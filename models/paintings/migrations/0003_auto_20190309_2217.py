# Generated by Django 2.1 on 2019-03-09 22:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0002_auto_20190309_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 9, 22, 17, 21, 744544, tzinfo=utc)),
        ),
    ]