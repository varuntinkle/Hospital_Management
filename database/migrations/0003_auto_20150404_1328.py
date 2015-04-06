# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150404_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='id',
        ),
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
