# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0018_auto_20150712_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='name',
            field=models.SlugField(max_length=45),
        ),
        migrations.AlterField(
            model_name='actuatortype',
            name='name',
            field=models.SlugField(max_length=45),
        ),
        migrations.AlterField(
            model_name='network',
            name='name',
            field=models.SlugField(max_length=45),
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.SlugField(max_length=45),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.SlugField(max_length=45),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='name',
            field=models.SlugField(max_length=45),
        ),
    ]
