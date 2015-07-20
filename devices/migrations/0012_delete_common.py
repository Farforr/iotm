# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_auto_20150703_1817'),
    ]

    operations = [
        migrations.DeleteModel(
            name='common',
        ),
    ]
