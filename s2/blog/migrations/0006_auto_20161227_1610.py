# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161227_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=b'', max_length=100, editable=False),
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(default=b'', max_length=100, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.CharField(default=b'', max_length=100, editable=False),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
