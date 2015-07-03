# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0009_sensordata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActuatorData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('actuator', models.ForeignKey(to='devices.Actuator')),
            ],
        ),
    ]
