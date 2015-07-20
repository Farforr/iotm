# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_delete_common'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 26, 735527, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuator',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 33, 687460, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuatordata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 37, 583460, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuatordata',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 41, 631477, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuatortype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 44, 775444, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuatortype',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 47, 695379, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 50, 767420, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 53, 759372, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 37, 57, 143330, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 38, 0, 351465, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 38, 4, 223414, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensordata',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 38, 9, 911386, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensortype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 38, 18, 463346, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensortype',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 38, 22, 447351, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
