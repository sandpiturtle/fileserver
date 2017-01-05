# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 21:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import file_engine.validators


class Migration(migrations.Migration):

    dependencies = [
        ('file_engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content_type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='destruction_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 5, 22, 52, 1, 758359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/', validators=[file_engine.validators.validate_type]),
        ),
    ]
