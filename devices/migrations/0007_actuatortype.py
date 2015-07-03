# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_sensor_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActuatorType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=45)),
                ('manufacturer', models.CharField(max_length=45)),
            ],
        ),
    ]
