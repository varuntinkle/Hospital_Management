# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20150407_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulancebooking',
            name='Day',
            field=models.CharField(max_length=9),
        ),
    ]
