# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_ambulancebooking_ambulanceschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulanceschedule',
            name='Day',
            field=models.CharField(max_length=9),
        ),
    ]
