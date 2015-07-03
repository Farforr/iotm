# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_actuator'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('manufacturer', models.CharField(max_length=45)),
                ('units', models.CharField(max_length=10)),
            ],
        ),
    ]
