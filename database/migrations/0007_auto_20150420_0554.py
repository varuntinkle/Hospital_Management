# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.FileField(upload_to=b'./', blank=True),
        ),
        migrations.AddField(
            model_name='reception',
            name='image',
            field=models.FileField(upload_to=b'./', blank=True),
        ),
        migrations.AddField(
            model_name='reception',
            name='name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
