# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0017_auto_20150712_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='name',
            field=models.CharField(max_length=45, default='my_actuator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=45, default='my_sensor'),
            preserve_default=False,
        ),
    ]
