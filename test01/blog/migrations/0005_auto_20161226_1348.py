# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161223_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='lesson_name',
            field=models.CharField(default=datetime.datetime(2016, 12, 26, 5, 48, 11, 584000, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scores',
            name='score',
            field=models.IntegerField(),
        ),
    ]
