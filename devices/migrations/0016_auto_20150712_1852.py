# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0015_auto_20150712_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='actuator',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='actuatordata',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='actuatordata',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='actuatortype',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='actuatortype',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='network',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='network',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='node',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='node',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='last_modified',
            field=models.DateTimeField(verbose_name='created'),
        ),
    ]
