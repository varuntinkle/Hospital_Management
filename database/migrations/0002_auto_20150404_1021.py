# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
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
                ('appoint_no', models.IntegerField(unique=True)),
                ('done', models.BooleanField(default=False)),
                ('outsider', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=1, choices=[(b'0', b'Waiting'), (b'1', b'Pending'), (b'2', b'Completed')])),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('speciality', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('patients_visited', models.TextField()),
                ('schedule', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('rating', models.CharField(max_length=1, choices=[(b'1', b'poor'), (b'2', b'Average'), (b'3', b'good'), (b'4', b'very good'), (b'5', b'excellent')])),
                ('doctor', models.ForeignKey(to='database.Doctor')),
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
                ('prsc_required', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('patient_history', models.TextField(blank=True)),
                ('patient_test', models.TextField(blank=True)),
                ('outsider', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.CharField(max_length=256)),
                ('symptoms', models.TextField(blank=True)),
                ('prescription_time', models.DateTimeField(blank=True)),
                ('next_visit', models.IntegerField()),
                ('doctor', models.ForeignKey(to='database.Doctor')),
                ('medicine', models.ManyToManyField(to='database.Medicine')),
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
        migrations.DeleteModel(
            name='login',
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(to='database.Registration'),
        ),
        migrations.AddField(
            model_name='followup',
            name='patient',
            field=models.ForeignKey(to='database.Registration'),
        ),
        migrations.AddField(
            model_name='crequest',
            name='doctor',
            field=models.ForeignKey(to='database.Doctor'),
        ),
        migrations.AddField(
            model_name='crequest',
            name='reg_no',
            field=models.ForeignKey(blank=True, to='database.Registration', null=True),
        ),
    ]
