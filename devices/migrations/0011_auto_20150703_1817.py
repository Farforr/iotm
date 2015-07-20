# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0010_actuatordata'),
    ]

    operations = [
        migrations.CreateModel(
            name='common',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='network',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 4, 1, 17, 14, 595774, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 17, 23, 923719, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
