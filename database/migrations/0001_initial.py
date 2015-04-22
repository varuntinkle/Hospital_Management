# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('Day', models.CharField(max_length=9)),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day', models.CharField(max_length=9)),
                ('Time', models.TimeField()),
                ('Availability', models.BooleanField()),
                ('Count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=140)),
                ('category', models.CharField(max_length=10, choices=[(b'1', b'poor'), (b'2', b'Average'), (b'3', b'good'), (b'4', b'very good'), (b'5', b'excellent')])),
                ('subject', models.CharField(max_length=140)),
                ('complaint', models.TextField(blank=True)),
                ('complaint_date', models.DateTimeField()),
                ('doc_pat', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('problem', models.CharField(max_length=140)),
                ('request_date', models.DateTimeField()),
                ('appoint_date', models.DateTimeField()),
                ('appoint_no', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
                ('outsider', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=1, choices=[(b'0', b'Waiting'), (b'1', b'Pending'), (b'2', b'Completed')])),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('patients_visited', models.TextField()),
                ('schedule', models.TextField()),
                ('image', models.FileField(upload_to=b'./', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('salt', models.TextField(blank=True)),
                ('mg', models.IntegerField()),
                ('price', models.FloatField()),
                ('disease', models.TextField(blank=True)),
                ('misc', models.TextField(blank=True)),
                ('prsc_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('reg_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('height', models.CharField(max_length=100)),
                ('weight', models.IntegerField(blank=True)),
                ('patient_history', models.TextField(blank=True)),
                ('patient_test', models.TextField(blank=True)),
                ('image', models.FileField(upload_to=b'./', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.CharField(max_length=256)),
                ('medicine', models.TextField(verbose_name=b'Medicine')),
                ('symptoms', models.TextField(blank=True)),
                ('prescription_time', models.DateTimeField(blank=True)),
                ('next_visit', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('image', models.FileField(upload_to=b'./', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('prescription', models.OneToOneField(primary_key=True, serialize=False, to='database.Prescription')),
                ('is_filled', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=1, choices=[(b'1', b'poor'), (b'2', b'Average'), (b'3', b'good'), (b'4', b'very good'), (b'5', b'excellent')])),
                ('doctor', models.ForeignKey(to='database.Doctor')),
                ('patient', models.ForeignKey(to='database.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(to='database.Doctor'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='reg_no',
            field=models.ForeignKey(to='database.Patient'),
        ),
        migrations.AddField(
            model_name='crequest',
            name='doctor',
            field=models.ForeignKey(to='database.Doctor'),
        ),
        migrations.AddField(
            model_name='crequest',
            name='reg_no',
            field=models.ForeignKey(blank=True, to='database.Patient', null=True),
        ),
    ]
