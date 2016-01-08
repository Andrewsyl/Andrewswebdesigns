# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
