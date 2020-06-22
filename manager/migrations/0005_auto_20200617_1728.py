# Generated by Django 2.2.5 on 2020-06-17 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20200617_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeattendance',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 17, 11, 58, 1, 659334, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='takeattendance',
            name='date_time',
            field=models.DateField(verbose_name='Date(mm/dd/yyyy)'),
        ),
    ]
