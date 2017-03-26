# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0005_auto_20170326_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='jobs',
            field=models.ForeignKey(to='emplois.Job'),
        ),
    ]
