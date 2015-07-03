# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_actuatortype'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='model',
            field=models.ForeignKey(default=0, to='devices.ActuatorType'),
            preserve_default=False,
        ),
    ]
