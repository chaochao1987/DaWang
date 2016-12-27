# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='order_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
