# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20160106_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='topic',
        ),
    ]
