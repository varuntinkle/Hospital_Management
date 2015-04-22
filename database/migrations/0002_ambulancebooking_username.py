# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulancebooking',
            name='username',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]
