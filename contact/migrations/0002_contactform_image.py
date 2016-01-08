# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
