# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0004_auto_20160526_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='jobs',
            field=models.ForeignKey(related_name='desc', to='emplois.Job'),
        ),
    ]
