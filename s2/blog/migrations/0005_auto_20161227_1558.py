# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161227_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ManyToManyField(to='blog.Payment'),
        ),
        migrations.AddField(
            model_name='account',
            name='order',
            field=models.ForeignKey(default=datetime.datetime(2016, 12, 27, 7, 58, 44, 573000, tzinfo=utc), to='blog.Order'),
            preserve_default=False,
        ),
    ]
