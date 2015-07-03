# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_sensortype'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='model',
            field=models.ForeignKey(to='devices.SensorType', default=0),
            preserve_default=False,
        ),
    ]
