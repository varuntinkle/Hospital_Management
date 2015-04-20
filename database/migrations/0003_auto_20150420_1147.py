# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150419_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crequest',
            name='appoint_no',
            field=models.IntegerField(),
        ),
    ]
