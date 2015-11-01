# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20151029_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='details',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
    ]
