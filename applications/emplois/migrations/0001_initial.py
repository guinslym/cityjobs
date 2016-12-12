# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('KNOWLEDGE', models.TextField(null=True, blank=True)),
                ('LANGUAGE_CERTIFICATES', models.TextField(null=True, blank=True)),
                ('EDUCATIONANDEXP', models.TextField(null=True, blank=True)),
                ('COMPANY_DESC', models.TextField(null=True, blank=True)),
                ('POSTDATE', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('JOBURL', models.URLField(max_length=250, null=True, blank=True)),
                ('EXPIRYDATE', models.DateField(null=True, blank=True)),
                ('SALARYMAX', models.CharField(max_length=40, null=True, blank=True)),
                ('SALARYMIN', models.CharField(max_length=40, null=True, blank=True)),
                ('SALARYTYPE', models.CharField(max_length=20, null=True, blank=True)),
                ('NAME', models.CharField(max_length=40, null=True, blank=True)),
                ('language', models.CharField(max_length=2, choices=[('FR', 'Francais'), ('EN', 'English')], default='EN')),
                ('POSITION', models.CharField(max_length=150, null=True, blank=True)),
                ('JOBREF', models.CharField(max_length=30, null=True, blank=True, unique=True)),
                ('JOB_SUMMARY', models.TextField(null=True, blank=True)),
                ('POSTDATE', models.DateTimeField(null=True, blank=True)),
                ('slug', models.CharField(max_length=200)),
                ('tweeted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='jobs',
            field=models.ForeignKey(to='emplois.Job'),
        ),
    ]
