# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='outsider',
        ),
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.CharField(default='doctor', max_length=30),
            preserve_default=False,
        ),
    ]
