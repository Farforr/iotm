# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0013_auto_20150703_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='createdd',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 0, 3, 25, 168901, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='last_modifiedd',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 0, 3, 38, 208982, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
