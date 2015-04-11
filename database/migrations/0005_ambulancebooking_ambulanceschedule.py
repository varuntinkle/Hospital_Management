# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20150406_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbulanceBooking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Source', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('DateBooked', models.DateTimeField(verbose_name=b'Date booked')),
                ('Purpose', models.CharField(max_length=200)),
                ('Day', models.IntegerField()),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day', models.IntegerField()),
                ('Time', models.TimeField()),
                ('Availability', models.BooleanField()),
                ('Count', models.IntegerField()),
            ],
        ),
    ]
