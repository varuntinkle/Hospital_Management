# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20150404_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
